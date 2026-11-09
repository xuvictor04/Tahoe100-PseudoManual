---
drug: "Budesonide"
type: "drug"
salt_base: "Budesonide"
targets: "NR3C1"
moa_fine: "Glucocorticoid receptor agonist"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 566
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Budesonide

*Glucocorticoid receptor agonist (activator/agonist) · targets: NR3C1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 531 / 411 / 566; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.56 / 0.33.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:G2 | 231 / 300 | — | -0.13 | +0.6/+0.9/+0.7 | — |
| 0.5 µM | [[Plate 11]]:G2 | 261 / 150 | — | -0.31 | -0.1/-0.4/-1.0 | — |
| 5 µM | [[Plate 12]]:G2 | 189 / 377 | — | -0.17 | +0.4/-1.8/-1.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (231 genes, none with an alert; 12 shown): [[FKBP5]] 9.99× (z +34.7, 33/41 lines), [[KLF9]] 2.76× (z +17.0, 33/43 lines), [[TSC22D3]] 5.61× (z +14.5, 30/36 lines), [[IRAK3]] 3.51× (z +13.7, 12/12 lines), [[CCND3]] 2.52× (z +12.6, 31/47 lines), [[PID1]] 2.28× (z +11.6, 22/26 lines), [[NNMT]] 3.29× (z +10.9, 20/24 lines), [[MAOA]] 2.20× (z +10.8, 16/33 lines), [[DNER]] 2.06× (z +9.4, 14/16 lines), [[TMTC1]] 1.74× (z +8.6, 13/23 lines), [[FGD4]] 1.51× (z +8.5, 20/38 lines), [[B4GALT1]] 1.38× (z +8.3, 22/45 lines)

**0.5 µM** (261 genes, none with an alert; 12 shown): [[FKBP5]] 11.8× (z +37.2, 35/41 lines), [[KLF9]] 2.75× (z +17.0, 34/43 lines), [[MAOA]] 2.45× (z +12.4, 17/33 lines), [[TSC22D3]] 4.07× (z +11.8, 29/36 lines), [[CCND3]] 2.32× (z +11.4, 29/47 lines), [[PID1]] 2.20× (z +11.1, 21/26 lines), [[NNMT]] 3.33× (z +11.0, 21/24 lines), [[FGD4]] 1.69× (z +10.9, 20/38 lines), [[ABLIM3]] 2.12× (z +10.8, 21/33 lines), [[IRAK3]] 2.60× (z +10.4, 10/12 lines), [[LDLRAD3]] 1.73× (z +10.1, 25/41 lines), [[DNER]] 2.17× (z +10.1, 14/16 lines)

**5 µM** (189 genes, none with an alert; 12 shown): [[FKBP5]] 10.9× (z +36.1, 32/42 lines), [[KLF9]] 2.26× (z +13.7, 29/43 lines), [[CCND3]] 2.47× (z +12.3, 31/47 lines), [[ABLIM3]] 2.20× (z +11.3, 22/33 lines), [[TSC22D3]] 3.68× (z +10.9, 26/37 lines), [[LDLRAD3]] 1.81× (z +10.9, 30/41 lines), [[NNMT]] 3.08× (z +10.3, 20/24 lines), [[MAOA]] 2.09× (z +10.2, 19/34 lines), [[PID1]] 1.97× (z +9.5, 19/26 lines), [[FGD4]] 1.54× (z +9.0, 22/38 lines), [[ADAMTS9]] 1.80× (z +8.5, 20/29 lines), [[ATP1A1]] 1.47× (z +8.0, 31/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (300 genes, none with an alert; 12 shown): [[WNT7B]] 0.516× (z -8.7, 16/28 lines), [[IGFBP3]] 0.428× (z -8.7, 23/28 lines), [[KIAA1217]] 0.628× (z -8.6, 24/38 lines), [[SYNJ2]] 0.681× (z -8.4, 26/44 lines), [[ENSG00000259354]] 0.495× (z -8.0, 27/30 lines), [[HMGN2P46]] 0.463× (z -7.9, 22/30 lines), [[AFF3]] 0.594× (z -7.7, 20/26 lines), [[LUCAT1]] 0.605× (z -7.6, 30/40 lines), [[CDCP1]] 0.642× (z -7.5, 20/32 lines), [[PKIA]] 0.653× (z -7.3, 19/25 lines), [[ADAMTS16]] 0.658× (z -7.0, 18/23 lines), [[ENSG00000239462]] 0.572× (z -7.0, 21/29 lines)

**0.5 µM** (150 genes, none with an alert; 12 shown): [[WNT7B]] 0.526× (z -8.4, 17/28 lines), [[PTHLH]] 0.469× (z -7.6, 19/25 lines), [[ENSG00000259354]] 0.539× (z -7.2, 26/30 lines), [[IGFBP3]] 0.508× (z -6.9, 22/28 lines), [[PKIA]] 0.680× (z -6.7, 18/25 lines), [[SYNJ2]] 0.759× (z -6.0, 25/44 lines), [[SLC4A7]] 0.749× (z -6.0, 30/45 lines), [[FGF5]] 0.592× (z -6.0, 10/18 lines), [[NAV3]] 0.653× (z -6.0, 19/32 lines), [[LIF]] 0.600× (z -6.0, 24/38 lines), [[HMGN2P46]] 0.566× (z -5.8, 22/30 lines), [[FAM107B]] 0.742× (z -5.7, 21/37 lines)

**5 µM** (377 genes, none with an alert; 12 shown): [[WNT7B]] 0.438× (z -10.9, 19/28 lines), [[PTHLH]] 0.374× (z -9.9, 19/27 lines), [[ENSG00000259354]] 0.476× (z -8.7, 27/30 lines), [[IGFBP3]] 0.449× (z -8.2, 23/28 lines), [[KIAA1217]] 0.650× (z -7.9, 22/38 lines), [[HMGN2P46]] 0.487× (z -7.4, 23/30 lines), [[LUCAT1]] 0.617× (z -7.3, 31/40 lines), [[CD44]] 0.695× (z -7.2, 25/33 lines), [[AFF3]] 0.621× (z -7.1, 17/26 lines), [[SYNJ2]] 0.725× (z -7.0, 24/44 lines), [[TMEM158]] 0.340× (z -6.7, 27/29 lines), [[GBP4]] 0.491× (z -6.7, 24/28 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 098]] (+5.4), [[Module 104]] (+3.4), [[Module 106]] (+3.4) | [[Module 224]] (-2.2), [[Module 112]] (-2.2), [[Module 184]] (-2.0) |
| 0.5 µM | [[Module 098]] (+6.0), [[Module 104]] (+3.8), [[Module 097]] (+3.5) | [[Module 112]] (-2.5), [[Module 224]] (-2.1) |
| 5 µM | [[Module 098]] (+4.6), [[Module 097]] (+3.3), [[Module 106]] (+2.6) | [[Module 112]] (-3.5), [[Module 068]] (-2.9), [[Module 048]] (-2.8) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[HOP62 (line)]] (2.00), [[H4 (line)]] (1.89), [[Hs 766T (line)]] (1.82), [[NCI-H1792 (line)]] (1.71) · weakest: [[SW480 (line)]] (0.292), [[LS 180 (line)]] (0.341), [[A-427 (line)]] (0.369) |
| 0.5 µM | — | [[HOP62 (line)]] (2.06), [[H4 (line)]] (2.02), [[Hs 766T (line)]] (2.02), [[NCI-H1792 (line)]] (1.89) · weakest: [[SW1417 (line)]] (0.196), [[COLO 205 (line)]] (0.231), [[SW480 (line)]] (0.238) |
| 5 µM | — | [[H4 (line)]] (2.30), [[HOP62 (line)]] (2.11), [[NCI-H1792 (line)]] (1.91), [[HS-578T (line)]] (1.83) · weakest: [[SW480 (line)]] (0.232), [[COLO 205 (line)]] (0.305), [[LS 180 (line)]] (0.369) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Dexamethasone (drug)]] (+0.85, Glucocorticoid receptor agonist); [[Econazole (drug)]] (+0.80, unclear); [[Citalopram (hydrobromide) (drug)]] (+0.76, unclear); [[Phenylephrine (hydrochloride) (drug)]] (+0.66, Adrenoceptor agonist); [[Triamcinolone (drug)]] (+0.64, Glucocorticoid receptor agonist); [[Betamethasone dipropionate (drug)]] (+0.57, Glucocorticoid receptor agonist); [[Clobetasol propionate (drug)]] (+0.56, unclear); [[Quinestrol (drug)]] (+0.53, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

None: no gene was found to set how the cells fare under it.

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 250 arrows, 250 of them with an alert ⚠; grade A 0, B 250, C 0. Shown: the 15 strongest; 235 more arrows (235 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[NR3C1]] | [[ENSG00000243797]] | moves it that way too | B | NR3C1 activity lowers ENSG00000243797's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 1.7% of all compounds | 0.014 | ⚠ off-target possible; 3 compounds |
| [[NR3C1]] | [[OLFM2]] | moves it that way too | B | NR3C1 activity lowers OLFM2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 1.7% of all compounds | 0.014 | ⚠ off-target possible; 3 compounds |
| [[NR3C1]] | [[SQSTM1]] | moves it that way too | B | NR3C1 activity lowers SQSTM1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 1.7% of all compounds | 0.014 | ⚠ off-target possible; 3 compounds |
| [[NR3C1]] | [[C15orf48]] | moves it that way too | B | NR3C1 activity lowers C15orf48's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.0% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[NR3C1]] | [[GATM]] | moves it that way too | B | NR3C1 activity lowers GATM's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.0% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[NR3C1]] | [[MT2A]] | moves it that way too | B | NR3C1 activity raises MT2A's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.0% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[NR3C1]] | [[TNS2]] | moves it that way too | B | NR3C1 activity raises TNS2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.0% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[NR3C1]] | [[ABI3BP]] | moves it that way too | B | NR3C1 activity lowers ABI3BP's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.2% of all compounds | 0.020 | ⚠ off-target possible; 3 compounds |
| [[NR3C1]] | [[CA8]] | moves it that way too | B | NR3C1 activity lowers CA8's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.2% of all compounds | 0.020 | ⚠ off-target possible; 3 compounds |
| [[NR3C1]] | [[DPF3]] | moves it that way too | B | NR3C1 activity lowers DPF3's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.2% of all compounds | 0.020 | ⚠ off-target possible; 3 compounds |
| [[NR3C1]] | [[ADAMTS1]] | moves it that way too | B | NR3C1 activity lowers ADAMTS1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |
| [[NR3C1]] | [[CACNA1A]] | moves it that way too | B | NR3C1 activity lowers CACNA1A's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |
| [[NR3C1]] | [[CHPT1]] | moves it that way too | B | NR3C1 activity raises CHPT1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |
| [[NR3C1]] | [[COL22A1]] | moves it that way too | B | NR3C1 activity lowers COL22A1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |
| [[NR3C1]] | [[OSGIN1]] | moves it that way too | B | NR3C1 activity lowers OSGIN1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |

## Data

- `tables/drugs.parquet` — drug == "Budesonide"
- `tables/drugdoses.parquet` — dd in 218, 219, 220
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

---
drug: "Betamethasone dipropionate"
type: "drug"
salt_base: "Betamethasone dipropionate"
targets: "NR3C1"
moa_fine: "Glucocorticoid receptor agonist"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 472
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Betamethasone dipropionate

*Glucocorticoid receptor agonist (activator/agonist) · targets: NR3C1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 430 / 466 / 472; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.63 / 0.61.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:E12 | 187 / 243 | — | -0.55 | +0.2/-0.3/-0.6 | — |
| 0.5 µM | [[Plate 08]]:E12 | 260 / 206 | — | -0.75 | +0.3/-0.3/+0.6 | — |
| 5 µM | [[Plate 09]]:E12 | 174 / 298 | — | +0.43 | +2.6/-0.6/+1.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (187 genes, none with an alert; 12 shown): [[FKBP5]] 10.4× (z +32.6, 33/41 lines), [[KLF9]] 2.59× (z +14.8, 31/42 lines), [[MAOA]] 2.38× (z +11.1, 18/30 lines), [[ITGA10]] 3.42× (z +10.6, 20/32 lines), [[PID1]] 2.25× (z +10.5, 20/25 lines), [[NNMT]] 3.45× (z +10.5, 18/22 lines), [[CCND3]] 2.25× (z +10.2, 30/46 lines), [[TSC22D3]] 3.50× (z +9.7, 26/34 lines), [[IRAK3]] 2.60× (z +9.6, 11/12 lines), [[ATP1A1]] 1.61× (z +9.1, 29/47 lines), [[ABLIM3]] 1.92× (z +8.6, 21/32 lines), [[ADPRHL1]] 2.10× (z +8.2, 22/41 lines)

**0.5 µM** (260 genes, none with an alert; 12 shown): [[FKBP5]] 10.5× (z +35.5, 33/41 lines), [[KLF9]] 2.53× (z +15.6, 31/42 lines), [[CCND3]] 2.64× (z +13.2, 32/46 lines), [[TSC22D3]] 4.60× (z +12.8, 26/35 lines), [[MAOA]] 2.41× (z +12.1, 19/33 lines), [[PID1]] 2.29× (z +11.6, 21/26 lines), [[NNMT]] 3.06× (z +10.2, 16/23 lines), [[ITGA10]] 2.85× (z +9.7, 26/36 lines), [[ADPRHL1]] 2.22× (z +9.5, 24/46 lines), [[IRAK3]] 2.38× (z +9.5, 10/12 lines), [[B3GNT5]] 1.73× (z +9.1, 24/40 lines), [[ABLIM3]] 1.95× (z +8.9, 22/33 lines)

**5 µM** (174 genes, none with an alert; 12 shown): [[FKBP5]] 9.65× (z +32.9, 33/41 lines), [[KLF9]] 2.58× (z +15.3, 33/43 lines), [[TSC22D3]] 5.22× (z +13.3, 30/36 lines), [[CCND3]] 2.52× (z +12.1, 32/46 lines), [[PID1]] 2.21× (z +10.7, 21/26 lines), [[IRAK3]] 2.50× (z +9.6, 10/12 lines), [[NNMT]] 2.95× (z +9.5, 19/24 lines), [[ADPRHL1]] 2.11× (z +8.6, 25/45 lines), [[ATP1A1]] 1.54× (z +8.5, 34/49 lines), [[ITGA10]] 2.50× (z +8.2, 23/35 lines), [[SGPP2]] 1.67× (z +8.0, 7/16 lines), [[DNER]] 1.91× (z +8.0, 14/17 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (243 genes, none with an alert; 12 shown): [[HMGN2P46]] 0.409× (z -8.5, 23/28 lines), [[ADAMTS16]] 0.581× (z -8.4, 17/22 lines), [[WNT7B]] 0.512× (z -8.1, 17/26 lines), [[AFF3]] 0.565× (z -7.9, 17/25 lines), [[ENSG00000259354]] 0.484× (z -7.9, 25/29 lines), [[FAM107B]] 0.677× (z -7.7, 23/36 lines), [[SYNJ2]] 0.690× (z -7.5, 27/43 lines), [[PKIA]] 0.638× (z -7.2, 17/25 lines), [[LINC00944]] 0.611× (z -7.0, 16/27 lines), [[LIF]] 0.553× (z -6.4, 22/37 lines), [[KCNMA1]] 0.707× (z -6.2, 15/21 lines), [[ADAMTSL1]] 0.581× (z -6.0, 13/25 lines)

**0.5 µM** (206 genes, none with an alert; 12 shown): [[AFF3]] 0.555× (z -8.7, 18/26 lines), [[FAM107B]] 0.667× (z -8.7, 23/37 lines), [[HMGN2P46]] 0.434× (z -8.6, 23/30 lines), [[WNT7B]] 0.530× (z -8.3, 16/27 lines), [[ENSG00000259354]] 0.506× (z -8.0, 27/30 lines), [[ADAMTS16]] 0.633× (z -7.7, 19/23 lines), [[PKIA]] 0.659× (z -7.2, 16/25 lines), [[SYNJ2]] 0.721× (z -7.2, 26/44 lines), [[KIAA1217]] 0.684× (z -7.0, 22/38 lines), [[TMEM200A]] 0.552× (z -6.8, 13/18 lines), [[ENSG00000239462]] 0.580× (z -6.8, 18/28 lines), [[TNFRSF9]] 0.509× (z -6.7, 12/25 lines)

**5 µM** (298 genes, none with an alert; 12 shown): [[ADAMTS16]] 0.620× (z -7.7, 19/23 lines), [[AFF3]] 0.586× (z -7.6, 19/26 lines), [[ENSG00000259354]] 0.520× (z -7.3, 27/31 lines), [[LUCAT1]] 0.604× (z -7.3, 31/41 lines), [[LIF]] 0.546× (z -6.8, 25/38 lines), [[ANTXR2]] 0.582× (z -6.6, 29/39 lines), [[IGFBP3]] 0.513× (z -6.6, 24/29 lines), [[WNT7B]] 0.595× (z -6.5, 18/27 lines), [[KIAA1217]] 0.693× (z -6.5, 26/39 lines), [[PLA2G4C]] 0.645× (z -6.4, 22/45 lines), [[HMGN2P46]] 0.530× (z -6.2, 22/30 lines), [[ITGB1-DT]] 0.612× (z -6.2, 21/26 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 098]] (+5.0), [[Module 104]] (+3.4), [[Module 097]] (+3.2) | [[Module 112]] (-3.4), [[Module 081]] (-2.3), [[Module 224]] (-2.2) |
| 0.5 µM | [[Module 098]] (+5.5), [[Module 104]] (+3.8), [[Module 139]] (+3.4) | [[Module 112]] (-2.9), [[Module 224]] (-2.4), [[Module 235]] (-2.1) |
| 5 µM | [[Module 098]] (+4.8), [[Module 139]] (+3.2), [[Module 106]] (+3.1) | [[Module 112]] (-2.4), [[Module 228]] (-2.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[HOP62 (line)]] (2.06), [[H4 (line)]] (2.02), [[Hs 766T (line)]] (1.87), [[NCI-H1573 (line)]] (1.85) · weakest: [[SW480 (line)]] (0.187), [[SW1417 (line)]] (0.215), [[HEC-1-A (line)]] (0.324) |
| 0.5 µM | — | [[H4 (line)]] (2.05), [[HOP62 (line)]] (2.04), [[Hs 766T (line)]] (1.94), [[NCI-H1573 (line)]] (1.78) · weakest: [[SW480 (line)]] (0.178), [[SW1417 (line)]] (0.219), [[C-33 A (line)]] (0.275) |
| 5 µM | — | [[HOP62 (line)]] (2.10), [[H4 (line)]] (2.05), [[Hs 766T (line)]] (1.97), [[NCI-H1573 (line)]] (1.83) · weakest: [[SW480 (line)]] (0.283), [[SW1417 (line)]] (0.337), [[KATO III (line)]] (0.338) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Citalopram (hydrobromide) (drug)]] (+0.81, unclear); [[Phenylephrine (hydrochloride) (drug)]] (+0.76, Adrenoceptor agonist); [[Triamcinolone (drug)]] (+0.68, Glucocorticoid receptor agonist); [[Dexamethasone (drug)]] (+0.68, Glucocorticoid receptor agonist); [[Econazole (drug)]] (+0.66, unclear); [[Budesonide (drug)]] (+0.57, Glucocorticoid receptor agonist); [[Clobetasol propionate (drug)]] (+0.57, unclear); [[Medroxyprogesterone acetate (drug)]] (+0.56, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 24 arrows, 24 of them with an alert ⚠; grade A 0, B 12, C 12. Shown: the 15 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000259354]], [[HMGN2P46]] | 5 µM | B | ENSG00000259354, HMGN2P46 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express ENSG00000259354, HMGN2P46 (18) vs lines expressing them (30) | the lines without ENSG00000259354, HMGN2P46: 0.80× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: C15orf48, IL1R1, STAC; co-absent genes |
| [[GPR39]] | 5 µM | B | GPR39 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express GPR39 (11) vs lines expressing it (37) | the lines without GPR39: 0.81× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[FER1L4]] | 5 µM | B | FER1L4 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express FER1L4 (7) vs lines expressing it (41) | the lines without FER1L4: 0.88× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, STEAP2, OSR2; maybe low, not absent |
| [[PTGS2]] | 5 µM | B | PTGS2 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express PTGS2 (27) vs lines expressing it (21) | the lines without PTGS2: 0.80× the cells of the other lines | 0.074 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[NLGN4X]] | 5 µM | B | NLGN4X activity lowers the cells' numbers under Betamethasone dipropionate 5 µM (makes them more sensitive) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 1.06× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| [[LACC1]] | 5 µM | B | LACC1 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express LACC1 (6) vs lines expressing it (42) | the lines without LACC1: 0.74× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: CCDC122, IL1RAP, NABP1 |
| [[BASP1]] | 5 µM | B | BASP1 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express BASP1 (24) vs lines expressing it (24) | the lines without BASP1: 0.77× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: S1PR3, VEGFC, SRGN |
| [[SLFN5]] | 5 µM | B | SLFN5 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 0.80× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[RAB32]] | 5 µM | B | RAB32 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express RAB32 (7) vs lines expressing it (41) | the lines without RAB32: 0.78× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: PTPRH, INPP4B, ENSG00000285155 |
| [[STAC]] | 5 µM | B | STAC activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express STAC (25) vs lines expressing it (23) | the lines without STAC: 0.79× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[ITGA1]] | 5 µM | B | ITGA1 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express ITGA1 (18) vs lines expressing it (30) | the lines without ITGA1: 0.83× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[CGAS]] | 5 µM | B | CGAS activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express CGAS (17) vs lines expressing it (31) | the lines without CGAS: 0.83× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP |
| [[RARG]] | 5 µM | C | RARG activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 0.70× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| [[LGI4]] | 5 µM | C | LGI4 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express LGI4 (5) vs lines expressing it (43) | the lines without LGI4: 0.75× the cells of the other lines | 0.039 | ⚠ tissue-confounded; across organs; also absent: SLC25A43, FXYD5, NMI; maybe low, not absent |
| [[ACCS]] | 5 µM | C | ACCS activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 0.74× the cells of the other lines | 0.042 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |

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

- `tables/drugs.parquet` — drug == "Betamethasone dipropionate"
- `tables/drugdoses.parquet` — dd in 185, 186, 187
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

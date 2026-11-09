---
drug: "Dexamethasone"
type: "drug"
salt_base: "Dexamethasone"
targets: "NR3C1"
moa_fine: "Glucocorticoid receptor agonist"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 579
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Dexamethasone

*Glucocorticoid receptor agonist (activator/agonist) · targets: NR3C1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 374 / 579 / 448; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.76 / 0.78.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:D9 | 105 / 269 | — | -0.17 | +1.5/+0.2/-0.3 | — |
| 0.5 µM | [[Plate 11]]:D9 | 118 / 461 | — | +0.26 | +1.2/-0.3/-0.7 | — |
| 5 µM | [[Plate 12]]:D9 | 122 / 326 | — | -0.28 | +2.0/+1.0/+0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (105 genes, none with an alert; 12 shown): [[FKBP5]] 9.98× (z +34.7, 29/41 lines), [[KLF9]] 2.13× (z +12.7, 30/43 lines), [[CCND3]] 2.25× (z +11.0, 30/46 lines), [[ABLIM3]] 2.13× (z +10.8, 23/33 lines), [[LDLRAD3]] 1.73× (z +10.1, 29/41 lines), [[MAOA]] 2.07× (z +10.0, 17/33 lines), [[NNMT]] 2.79× (z +9.4, 17/23 lines), [[TSC22D3]] 2.96× (z +9.1, 26/37 lines), [[PID1]] 1.85× (z +8.6, 21/26 lines), [[ITGA10]] 2.46× (z +8.3, 24/36 lines), [[FGD4]] 1.47× (z +8.1, 21/38 lines), [[ADAMTS9]] 1.69× (z +7.6, 19/29 lines)

**0.5 µM** (118 genes, none with an alert; 12 shown): [[FKBP5]] 11.5× (z +36.9, 32/41 lines), [[KLF9]] 2.35× (z +14.3, 30/43 lines), [[ABLIM3]] 2.31× (z +12.0, 23/33 lines), [[LDLRAD3]] 1.90× (z +11.8, 26/41 lines), [[CCND3]] 2.14× (z +10.4, 28/46 lines), [[TSC22D3]] 3.14× (z +9.6, 25/37 lines), [[FGD4]] 1.58× (z +9.5, 20/38 lines), [[PID1]] 1.90× (z +9.0, 20/26 lines), [[NNMT]] 2.65× (z +8.9, 16/23 lines), [[ATP1A1]] 1.51× (z +8.5, 29/48 lines), [[ADAMTS9]] 1.78× (z +8.4, 19/29 lines), [[B3GNT5]] 1.65× (z +8.2, 25/41 lines)

**5 µM** (122 genes, none with an alert; 12 shown): [[FKBP5]] 9.92× (z +34.6, 30/41 lines), [[KLF9]] 2.37× (z +14.5, 31/43 lines), [[MAOA]] 2.55× (z +12.9, 19/34 lines), [[CCND3]] 2.26× (z +11.1, 30/46 lines), [[ABLIM3]] 2.17× (z +11.1, 22/33 lines), [[TSC22D3]] 3.09× (z +9.4, 25/37 lines), [[ATP1A1]] 1.56× (z +9.1, 32/48 lines), [[NNMT]] 2.65× (z +8.9, 17/23 lines), [[LDLRAD3]] 1.55× (z +8.1, 23/41 lines), [[PID1]] 1.78× (z +8.1, 20/26 lines), [[JPH2]] 1.92× (z +7.6, 18/29 lines), [[B3GNT5]] 1.58× (z +7.6, 23/41 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (269 genes, 3 with an alert ⚠; 14 shown): [[FAM107B]] ⚠ 0.665× (z -8.7, 23/37 lines; position correction uncertain), [[ADAMTS16]] 0.622× (z -8.0, 19/23 lines), [[WNT7B]] 0.561× (z -7.6, 17/27 lines), [[ENSG00000259354]] 0.518× (z -7.4, 25/30 lines), [[LIF]] ⚠ 0.533× (z -7.4, 30/38 lines; position correction uncertain), [[MARCHF4]] 0.551× (z -7.2, 11/19 lines), [[MAP7]] 0.774× (z -7.2, 7/27 lines), [[KIAA1217]] 0.683× (z -7.0, 21/38 lines), [[PTHLH]] 0.503× (z -6.9, 17/26 lines), [[FRMD5]] 0.692× (z -6.8, 17/38 lines), [[KCNMA1]] 0.702× (z -6.8, 13/22 lines), [[CD44]] 0.737× (z -6.0, 23/33 lines), [[HMGN2P46]] 0.555× (z -6.0, 21/30 lines), [[FGF5]] 0.601× (z -5.9, 7/18 lines)

**0.5 µM** (461 genes, 3 with an alert ⚠; 13 shown): [[FAM107B]] ⚠ 0.618× (z -9.2, 28/37 lines; position correction uncertain), [[ENSG00000259354]] 0.476× (z -8.7, 24/30 lines), [[SYNJ2]] 0.679× (z -8.5, 24/44 lines), [[PKIA]] 0.623× (z -8.2, 17/26 lines), [[ADAMTS16]] 0.631× (z -7.7, 15/23 lines), [[FRMD5]] 0.666× (z -7.5, 19/38 lines), [[MRPS6]] 0.685× (z -7.5, 27/47 lines), [[PTHLH]] 0.485× (z -7.3, 17/26 lines), [[LUCAT1]] 0.621× (z -7.2, 32/40 lines), [[RASGRP3]] 0.559× (z -7.0, 19/31 lines), [[GALNT5]] 0.603× (z -7.0, 8/21 lines), [[IGFBP3]] 0.506× (z -7.0, 22/28 lines), [[PTGS2]] 0.556× (z -6.9, 11/21 lines)

**5 µM** (326 genes, 3 with an alert ⚠; 13 shown): [[ADAMTS16]] 0.579× (z -9.2, 17/23 lines), [[ENSG00000259354]] 0.465× (z -9.0, 26/30 lines), [[MAP7]] 0.744× (z -8.3, 9/27 lines), [[FAM107B]] ⚠ 0.681× (z -8.2, 25/37 lines; position correction uncertain), [[HMGN2P46]] 0.478× (z -7.6, 22/30 lines), [[KIAA1217]] 0.668× (z -7.4, 24/38 lines), [[WNT7B]] 0.570× (z -7.4, 14/27 lines), [[LUCAT1]] 0.637× (z -6.8, 29/40 lines), [[AFF3]] 0.632× (z -6.8, 17/26 lines), [[SYNJ2]] 0.733× (z -6.8, 27/44 lines), [[KCNMA1]] 0.706× (z -6.7, 17/22 lines), [[FRMD5]] 0.699× (z -6.6, 17/38 lines), [[IGFBP3]] 0.528× (z -6.5, 22/28 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 098]] (+4.4), [[Module 097]] (+2.9), [[Module 113]] (+2.3) | [[Module 112]] (-3.2), [[Module 224]] (-2.2), [[Module 081]] (-2.1) |
| 0.5 µM | [[Module 098]] (+4.4), [[Module 097]] (+3.3), [[Module 217]] (+2.3) | [[Module 112]] (-3.6), [[Module 081]] (-2.6), [[Module 235]] (-2.6) |
| 5 µM | [[Module 098]] (+4.5), [[Module 097]] (+2.9), [[Module 139]] (+2.5) | [[Module 224]] (-3.1), [[Module 112]] (-2.8), [[Module 235]] (-2.6) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[H4 (line)]] (2.41), [[HOP62 (line)]] (2.15), [[Hs 766T (line)]] (2.05), [[NCI-H1573 (line)]] (2.00) · weakest: [[SW480 (line)]] (0.145), [[COLO 205 (line)]] (0.253), [[LS 180 (line)]] (0.255) |
| 0.5 µM | [[Hs 766T (line)]] (-3.4) | [[H4 (line)]] (2.07), [[HOP62 (line)]] (1.92), [[NCI-H1792 (line)]] (1.86), [[NCI-H1573 (line)]] (1.73) · weakest: [[LS 180 (line)]] (0.442), [[SW480 (line)]] (0.454), [[A-427 (line)]] (0.475) |
| 5 µM | — | [[H4 (line)]] (2.32), [[HOP62 (line)]] (2.20), [[NCI-H1792 (line)]] (2.07), [[Hs 766T (line)]] (1.93) · weakest: [[SW1417 (line)]] (0.281), [[SW480 (line)]] (0.287), [[LS 180 (line)]] (0.315) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Econazole (drug)]] (+0.86, unclear); [[Budesonide (drug)]] (+0.85, Glucocorticoid receptor agonist); [[Phenylephrine (hydrochloride) (drug)]] (+0.78, Adrenoceptor agonist); [[Betamethasone dipropionate (drug)]] (+0.68, Glucocorticoid receptor agonist); [[Citalopram (hydrobromide) (drug)]] (+0.66, unclear); [[Quinestrol (drug)]] (+0.66, unclear); [[Edoxaban (tosylate monohydrate) (drug)]] (+0.62, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Triamcinolone (drug)]] (+0.62, Glucocorticoid receptor agonist); [[Asciminib (drug)]] (+0.54, Other TK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[CD44]] | 0.5 µM | B | CD44 activity lowers the cells' numbers under Dexamethasone 0.5 µM (makes them more sensitive) | lines that do not express CD44 (15) vs lines expressing it (33) | the lines without CD44: 1.19× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[MMP1]] | 0.5 µM | B | MMP1 activity lowers the cells' numbers under Dexamethasone 0.5 µM (makes them more sensitive) | lines that do not express MMP1 (26) vs lines expressing it (22) | the lines without MMP1: 1.17× the cells of the other lines | 0.041 | ⚠ within organs, on part of the lines; also absent: SIRLNT, ENSG00000280241, AR |
| [[SIRLNT]] | 0.5 µM | B | SIRLNT activity lowers the cells' numbers under Dexamethasone 0.5 µM (makes them more sensitive) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 1.21× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[CXCL3]] | 0.5 µM | B | CXCL3 activity lowers the cells' numbers under Dexamethasone 0.5 µM (makes them more sensitive) | lines that do not express CXCL3 (14) vs lines expressing it (34) | the lines without CXCL3: 1.20× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[KIF1A]] | 0.5 µM | B | KIF1A activity raises the cells' numbers under Dexamethasone 0.5 µM (protects the cells) | lines that do not express KIF1A (34) vs lines expressing it (14) | the lines without KIF1A: 0.87× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[PRSS23]] | 0.5 µM | B | PRSS23 activity lowers the cells' numbers under Dexamethasone 0.5 µM (makes them more sensitive) | lines that do not express PRSS23 (13) vs lines expressing it (35) | the lines without PRSS23: 1.22× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[LINC02575]] | 0.5 µM | B | LINC02575 activity raises the cells' numbers under Dexamethasone 0.5 µM (protects the cells) | lines that do not express LINC02575 (32) vs lines expressing it (16) | the lines without LINC02575: 0.87× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000289309, LINC01205, MSRB3-AS1 |

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

- `tables/drugs.parquet` — drug == "Dexamethasone"
- `tables/drugdoses.parquet` — dd in 344, 345, 346
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

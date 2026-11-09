---
drug: "Phenylephrine (hydrochloride)"
type: "drug"
salt_base: "Phenylephrine"
targets: "ADRA1A, ADRA1B, ADRA1D"
moa_fine: "Adrenoceptor agonist"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 294
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Phenylephrine (hydrochloride)

*Adrenoceptor agonist (activator/agonist) · targets: ADRA1A, ADRA1B, ADRA1D · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 18 / 294; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.32 / 0.22.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:B6 | 0 / 3 | — | +0.06 | +0.2/+0.2/+0.4 | — |
| 0.5 µM | [[Plate 11]]:B6 | 4 / 14 | — | +0.63 | -1.1/-1.0/-1.1 | — |
| 5 µM | [[Plate 12]]:B6 | 134 / 160 | — | -0.24 | +1.6/+0.6/-0.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (4 genes, none with an alert): [[SNRNP35]] 1.24× (z +3.6, 5/47 lines), [[ZNF557]] 1.24× (z +3.4, 5/47 lines), [[P2RX4]] 1.24× (z +3.2, 7/47 lines), [[ZNF786]] 1.25× (z +2.9, 5/47 lines)

**5 µM** (134 genes, none with an alert; 12 shown): [[FKBP5]] 7.94× (z +31.3, 29/41 lines), [[CCND3]] 2.78× (z +13.9, 32/47 lines), [[KLF9]] 2.13× (z +12.7, 31/43 lines), [[NNMT]] 3.45× (z +11.3, 20/24 lines), [[ABLIM3]] 1.88× (z +9.1, 22/33 lines), [[ADAMTS9]] 1.82× (z +8.7, 19/29 lines), [[B3GNT5]] 1.62× (z +8.0, 25/41 lines), [[PID1]] 1.76× (z +8.0, 20/26 lines), [[TSC22D3]] 2.54× (z +7.8, 24/37 lines), [[IRAK3]] 2.02× (z +7.7, 10/12 lines), [[JPH2]] 1.89× (z +7.5, 18/29 lines), [[SAA1]] 4.73× (z +7.0, 15/19 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[GAL3ST2]] 0.550× (z -3.3, 7/38 lines), [[LINC02245]] 0.823× (z -3.2, 6/48 lines), [[MYADM-AS1]] 0.718× (z -3.1, 5/40 lines)

**0.5 µM** (14 genes, none with an alert; 12 shown): [[CCDC157]] 0.670× (z -4.0, 11/45 lines), [[TYR]] 0.458× (z -3.9, 0/3 lines), [[ANKRD20A11P]] 0.659× (z -3.8, 1/17 lines), [[ENSG00000290514]] 0.513× (z -3.6, 3/15 lines), [[ANXA1]] 0.696× (z -3.6, 23/39 lines), [[TPTE]] 0.760× (z -3.6, 0/12 lines), [[FOSB]] 0.443× (z -3.6, 41/47 lines), [[CFAP210]] 0.435× (z -3.6, 18/46 lines), [[KIF9]] 0.626× (z -3.4, 13/47 lines), [[ANKRD7]] 0.764× (z -3.3, 2/35 lines), [[ZNF474]] 0.675× (z -3.3, 4/38 lines), [[LINC01812]] 0.562× (z -3.3, 0/10 lines)

**5 µM** (160 genes, none with an alert; 12 shown): [[AFF3]] 0.597× (z -7.7, 17/26 lines), [[ENSG00000259354]] 0.554× (z -6.9, 21/30 lines), [[ADAMTS16]] 0.674× (z -6.6, 18/23 lines), [[WNT7B]] 0.607× (z -6.6, 17/27 lines), [[PKIA]] 0.689× (z -6.4, 17/26 lines), [[FAM107B]] 0.748× (z -6.2, 21/37 lines), [[TRAF1]] 0.587× (z -6.2, 24/36 lines), [[KCNMA1]] 0.737× (z -5.9, 14/22 lines), [[HMGN2P46]] 0.577× (z -5.6, 18/30 lines), [[KIAA1217]] 0.736× (z -5.6, 21/38 lines), [[PTHLH]] 0.577× (z -5.5, 14/26 lines), [[NAV3]] 0.676× (z -5.5, 18/32 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 170]] (+2.6) | — |
| 5 µM | [[Module 098]] (+4.5), [[Module 104]] (+2.7), [[Module 139]] (+2.5) | [[Module 112]] (-2.7), [[Module 179]] (-2.4) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[NCI-H1573 (line)]] (2.16), [[H4 (line)]] (2.15), [[HOP62 (line)]] (1.96), [[A549 (line)]] (1.96) · weakest: [[RKO (line)]] (0.166), [[KATO III (line)]] (0.255), [[SW480 (line)]] (0.272) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Econazole (drug)]] (+0.90, unclear); [[Dexamethasone (drug)]] (+0.78, Glucocorticoid receptor agonist); [[Betamethasone dipropionate (drug)]] (+0.76, Glucocorticoid receptor agonist); [[Citalopram (hydrobromide) (drug)]] (+0.74, unclear); [[Clobetasol propionate (drug)]] (+0.70, unclear); [[Budesonide (drug)]] (+0.66, Glucocorticoid receptor agonist); [[Edoxaban (tosylate monohydrate) (drug)]] (+0.65, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Quinestrol (drug)]] (+0.63, unclear); [[Triamcinolone (drug)]] (+0.60, Glucocorticoid receptor agonist)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 30 arrows, 30 of them with an alert ⚠; grade A 0, B 27, C 3. Shown: the 15 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ALDH3B1]] | 0.5 µM | B | ALDH3B1 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 1.26× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[CXCL3]] | 0.5 µM | B | CXCL3 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express CXCL3 (14) vs lines expressing it (34) | the lines without CXCL3: 1.20× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[FBXW10B]] | 0.5 µM | B | FBXW10B activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express FBXW10B (11) vs lines expressing it (37) | the lines without FBXW10B: 1.18× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[ENSG00000251537]] | 0.5 µM | B | ENSG00000251537 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000251537 (9) vs lines expressing it (39) | the lines without ENSG00000251537: 1.24× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: FBXW10B, PCED1B, NHS; maybe low, not absent |
| [[SIRLNT]] | 0.5 µM | B | SIRLNT activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 1.19× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[TGFBR2]] | 0.5 µM | B | TGFBR2 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express TGFBR2 (7) vs lines expressing it (41) | the lines without TGFBR2: 1.27× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[BMP2]] | 0.5 µM | B | BMP2 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express BMP2 (20) vs lines expressing it (28) | the lines without BMP2: 1.22× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[ANTXR2]] | 0.5 µM | B | ANTXR2 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ANTXR2 (10) vs lines expressing it (38) | the lines without ANTXR2: 1.24× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: RIN2, LINC01291, ST3GAL1; maybe low, not absent |
| [[CD44]] | 0.5 µM | B | CD44 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express CD44 (15) vs lines expressing it (33) | the lines without CD44: 1.19× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[CA13]] | 0.5 µM | B | CA13 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express CA13 (9) vs lines expressing it (39) | the lines without CA13: 1.22× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: CA3, PLSCR2, TRIB1; maybe low, not absent |
| [[TLR1]] | 0.5 µM | B | TLR1 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express TLR1 (15) vs lines expressing it (33) | the lines without TLR1: 1.19× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[IFI16]] | 0.5 µM | B | IFI16 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express IFI16 (18) vs lines expressing it (30) | the lines without IFI16: 1.18× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: MMP14, IL1A, MAF |
| [[IL15]] | 0.5 µM | B | IL15 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 1.25× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[DUSP5]] | 0.5 µM | B | DUSP5 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express DUSP5 (7) vs lines expressing it (41) | the lines without DUSP5: 1.22× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[ZHX2]] | 0.5 µM | B | ZHX2 activity lowers the cells' numbers under Phenylephrine (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ZHX2 (7) vs lines expressing it (41) | the lines without ZHX2: 1.22× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Phenylephrine (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 806, 807, 808
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

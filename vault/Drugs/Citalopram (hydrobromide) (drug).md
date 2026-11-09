---
drug: "Citalopram (hydrobromide)"
type: "drug"
salt_base: "Citalopram"
targets: "SLC6A4"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 207
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Citalopram (hydrobromide)

*unclear (inhibitor/antagonist) · targets: SLC6A4 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 207 / 27 / 1; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.13 / 0.42.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:F1 | 124 / 83 | — | +0.88 | +1.8/-0.2/-0.6 | — |
| 0.5 µM | [[Plate 11]]:F1 | 25 / 2 | — | -0.87 | -0.9/-1.3/-0.7 | — |
| 5 µM | [[Plate 12]]:F1 | 1 / 0 | — | +0.09 | +0.1/-0.5/-0.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (124 genes, none with an alert; 12 shown): [[FKBP5]] 6.28× (z +27.7, 35/42 lines), [[KLF9]] 2.24× (z +13.6, 31/43 lines), [[CCND3]] 2.50× (z +12.5, 33/47 lines), [[TSC22D3]] 3.46× (z +10.4, 28/37 lines), [[NNMT]] 3.01× (z +10.1, 23/24 lines), [[TBC1D8]] 1.59× (z +8.2, 33/44 lines), [[PID1]] 1.79× (z +8.1, 20/27 lines), [[FGD4]] 1.46× (z +7.9, 21/40 lines), [[MAOA]] 1.74× (z +7.6, 14/34 lines), [[SNAI2]] 2.27× (z +7.5, 16/25 lines), [[IRAK3]] 1.95× (z +7.3, 10/12 lines), [[ABLIM3]] 1.65× (z +7.1, 22/35 lines)

**0.5 µM** (25 genes, none with an alert; 12 shown): [[LINC01518]] 1.67× (z +4.5, 0/11 lines), [[ENSG00000286034]] 1.66× (z +4.4, 0/17 lines), [[SNED1-AS1]] 1.40× (z +4.0, 5/40 lines), [[EBF2]] 1.59× (z +4.0, 1/15 lines), [[ENSG00000259543]] 1.45× (z +3.8, 5/42 lines), [[LINC02977]] 1.36× (z +3.8, 1/33 lines), [[MCEE]] 1.31× (z +3.7, 15/48 lines), [[RNF17]] 1.74× (z +3.6, 0/4 lines), [[HEPHL1]] 1.90× (z +3.6, 0/1 lines), [[LINC02363]] 1.52× (z +3.6, 3/30 lines), [[AFF2]] 1.44× (z +3.5, 1/20 lines), [[ENSG00000291061]] 1.50× (z +3.5, 0/19 lines)

**5 µM** (1 gene, none with an alert): [[CCDC40]] 1.35× (z +3.3, 10/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (83 genes, none with an alert; 12 shown): [[WNT7B]] 0.646× (z -5.7, 17/28 lines), [[ADAMTS16]] 0.726× (z -5.4, 16/23 lines), [[PKIA]] 0.741× (z -5.2, 15/26 lines), [[PTHLH]] 0.601× (z -5.1, 14/28 lines), [[BMP2]] 0.677× (z -5.0, 16/29 lines), [[AFF3]] 0.718× (z -4.9, 16/28 lines), [[RASGRP3]] 0.667× (z -4.9, 15/31 lines), [[NAV3]] 0.706× (z -4.9, 17/34 lines), [[ENSG00000239462]] 0.680× (z -4.8, 16/30 lines), [[ENSG00000259354]] 0.656× (z -4.7, 21/32 lines), [[HMGN2P46]] 0.631× (z -4.7, 15/30 lines), [[KIAA1217]] 0.785× (z -4.4, 21/40 lines)

**0.5 µM** (2 genes, none with an alert): [[ABCF2]] 0.797× (z -3.4, 15/47 lines), [[ASPM]] 0.826× (z -2.7, 7/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 098]] (+3.9), [[Module 097]] (+2.7), [[Module 106]] (+2.6) | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[NCI-H1573 (line)]] (2.26), [[HOP62 (line)]] (2.15), [[H4 (line)]] (2.10), [[A549 (line)]] (1.99) · weakest: [[SW480 (line)]] (0.286), [[RKO (line)]] (0.351), [[SW1417 (line)]] (0.354) |
| 0.5 µM | [[LS 180 (line)]] (-3.2) | [[SW 1088 (line)]] (2.08), [[AsPC-1 (line)]] (1.97), [[SW48 (line)]] (1.73), [[SW 1271 (line)]] (1.58) · weakest: [[NCI-H23 (line)]] (-0.113), [[NCI-H1792 (line)]] (-0.0332), [[HOP62 (line)]] (0.0540) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Betamethasone dipropionate (drug)]] (+0.81, Glucocorticoid receptor agonist); [[Budesonide (drug)]] (+0.76, Glucocorticoid receptor agonist); [[Phenylephrine (hydrochloride) (drug)]] (+0.74, Adrenoceptor agonist); [[Econazole (drug)]] (+0.73, unclear); [[Clobetasol propionate (drug)]] (+0.70, unclear); [[Dexamethasone (drug)]] (+0.66, Glucocorticoid receptor agonist); [[Triamcinolone (drug)]] (+0.64, Glucocorticoid receptor agonist); [[Quinestrol (drug)]] (+0.45, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 26 arrows, 26 of them with an alert ⚠; grade A 0, B 7, C 19. Shown: the 15 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.79× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[SPOCK1]] | 0.05 µM | B | SPOCK1 activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.76× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[KCNMA1]] | 0.05 µM | B | KCNMA1 activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.77× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[ENSG00000259200]] | 0.05 µM | B | ENSG00000259200 activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express ENSG00000259200 (18) vs lines expressing it (30) | the lines without ENSG00000259200: 0.83× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, CSGALNACT1, ENSG00000232692; maybe low, not absent |
| [[ADAM12]] | 0.05 µM | B | ADAM12 activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 0.77× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| [[SLFN5]] | 0.05 µM | B | SLFN5 activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 0.77× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[STAC]] | 0.05 µM | B | STAC activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express STAC (25) vs lines expressing it (23) | the lines without STAC: 0.80× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11 |
| [[TBILA]] | 0.05 µM | C | TBILA activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.73× the cells of the other lines | 0.027 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| [[ZC3HAV1L]] | 0.05 µM | C | ZC3HAV1L activity lowers the cells' numbers under Citalopram (hydrobromide) 0.05 µM (makes them more sensitive) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 1.35× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| [[PLS3]] | 0.05 µM | C | PLS3 activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express PLS3 (4) vs lines expressing it (44) | the lines without PLS3: 0.72× the cells of the other lines | 0.031 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |
| [[PWWP2B]] | 0.05 µM | C | PWWP2B activity lowers the cells' numbers under Citalopram (hydrobromide) 0.05 µM (makes them more sensitive) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 1.46× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| [[PSMB8]] | 0.05 µM | C | PSMB8 activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.73× the cells of the other lines | 0.056 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| [[CEBPD]], [[GCA]] | 0.05 µM | C | CEBPD, GCA activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.70× the cells of the other lines | 0.056 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| [[FIGN]] | 0.05 µM | C | FIGN activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 0.83× the cells of the other lines | 0.056 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[PHF11]] | 0.05 µM | C | PHF11 activity raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 0.71× the cells of the other lines | 0.071 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Citalopram (hydrobromide)"
- `tables/drugdoses.parquet` — dd in 269, 270, 271
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

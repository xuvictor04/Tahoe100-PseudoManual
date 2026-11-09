---
drug: "Alpelisib"
type: "drug"
salt_base: "Alpelisib"
targets: "PIK3CA"
moa_fine: "PI3K/AKT inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 182
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Alpelisib

*PI3K/AKT inhibitor (inhibitor/antagonist) · targets: PIK3CA · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 2 / 182; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.21 / -0.06.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:A10 | 2 / 0 | — | -0.35 | +0.3/+0.3/+0.0 | — |
| 0.5 µM | [[Plate 02]]:A10 | 2 / 0 | — | +0.11 | +0.4/-0.9/-1.8 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:A10 | 108 / 74 | — | -0.20 | -1.4/-0.9/-0.5 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[ENSG00000239486]] 1.39× (z +3.4, 6/41 lines), [[PALM]] 1.30× (z +3.1, 4/26 lines)

**0.5 µM** (2 genes, none with an alert): [[MBNL3]] 1.49× (z +3.1, 2/31 lines), [[WWOX]] 1.38× (z +3.0, 18/43 lines)

**5 µM** (108 genes, none with an alert; 12 shown): [[ERBB3]] 1.78× (z +4.5, 13/20 lines), [[SELENOP]] 2.59× (z +4.4, 9/18 lines), [[RASSF6]] 2.11× (z +4.3, 7/20 lines), [[HS3ST5]] 2.50× (z +4.3, 1/12 lines), [[SMOC2]] 2.96× (z +4.2, 2/11 lines), [[C6orf89]] 1.36× (z +4.2, 10/47 lines), [[OLFML2A]] 2.05× (z +4.1, 4/24 lines), [[GBP2]] 2.07× (z +4.0, 16/34 lines), [[CP]] 2.43× (z +4.0, 8/9 lines), [[GNPAT]] 1.37× (z +4.0, 14/46 lines), [[CEP68]] 1.46× (z +3.9, 8/46 lines), [[SEMA3D]] 1.81× (z +3.9, 2/14 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (74 genes, none with an alert; 12 shown): [[MCTP1]] 0.511× (z -4.8, 18/35 lines), [[ETV5]] 0.509× (z -4.8, 21/47 lines), [[IPPK]] 0.551× (z -4.8, 20/47 lines), [[SPRY4-AS1]] 0.421× (z -4.7, 26/44 lines), [[ZFPM2-AS1]] 0.581× (z -4.5, 16/31 lines), [[PPP2R1A]] 0.750× (z -4.0, 21/47 lines), [[WDR62]] 0.606× (z -3.9, 16/42 lines), [[SLC35F2]] 0.699× (z -3.8, 15/43 lines), [[TM4SF19]] 0.522× (z -3.8, 11/27 lines), [[MIR4435-2HG]] 0.660× (z -3.8, 19/44 lines), [[ODF2]] 0.698× (z -3.7, 16/47 lines), [[PRAG1]] 0.747× (z -3.6, 13/31 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 200]] (+2.0) | — |
| 5 µM | [[Module 059]] (+2.1) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[HCT15 (line)]] (-6.2), [[NCI-H460 (line)]] (-5.1), [[CHP-212 (line)]] (-5.0), [[NCI-H23 (line)]] (-4.8), [[H4 (line)]] (-4.8) | [[AsPC-1 (line)]] (1.69), [[NCI-H23 (line)]] (1.43), [[HEC-1-A (line)]] (1.34), [[MIA PaCa-2 (line)]] (1.34) · weakest: [[C32 (line)]] (0.439), [[RPMI-7951 (line)]] (0.464), [[SW48 (line)]] (0.518) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Capmatinib (drug)]] (+0.79, EGFR/ERBB inhibitor); [[XRK3F2 (drug)]] (+0.76, unclear); [[Trametinib (DMSO_TF solvate) (drug)]] (+0.76, MEK inhibitor); [[IQ 1 (drug)]] (+0.76, unclear); [[AZD-7648 (drug)]] (+0.75, DNA synthesis/repair inhibitor); [[Binimetinib (drug)]] (+0.75, MEK inhibitor); [[Elimusertib hydrochloride (drug)]] (+0.72, unclear); [[Trametinib (drug)]] (+0.66, MEK inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Cobimetinib (drug)]] (+0.64, MEK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PDE7B]] | 5 µM | B | PDE7B activity lowers the cells' numbers under Alpelisib 5 µM (makes them more sensitive) | lines that do not express PDE7B (26) vs lines expressing it (22) | the lines without PDE7B: 1.31× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: ZMAT4, ANGPTL2, LUM; maybe low, not absent |
| [[ENSG00000249141]] | 5 µM | B | ENSG00000249141 activity lowers the cells' numbers under Alpelisib 5 µM (makes them more sensitive) | lines that do not express ENSG00000249141 (6) vs lines expressing it (42) | the lines without ENSG00000249141: 1.60× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, GGT1, LARGE1; maybe low, not absent |
| [[ENSG00000285458]] | 5 µM | C | ENSG00000285458 activity raises the cells' numbers under Alpelisib 5 µM (protects the cells) | lines that do not express ENSG00000285458 (5) vs lines expressing it (43) | the lines without ENSG00000285458: 0.61× the cells of the other lines | 0.082 | ⚠ tissue-confounded; across organs; also absent: TBILA, GCA, RILP; maybe low, not absent |
| [[TRIM72]] | 5 µM | C | TRIM72 activity lowers the cells' numbers under Alpelisib 5 µM (makes them more sensitive) | lines that do not express TRIM72 (4) vs lines expressing it (44) | the lines without TRIM72: 1.71× the cells of the other lines | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 20 arrows, 20 of them with an alert ⚠; grade A 0, B 20, C 0. Shown: the 15 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[PIK3CA]] | [[KLF3]] | moves it that way too | B | PIK3CA activity lowers KLF3's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 1.4% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[PIK3CA]] | [[SUV39H2]] | moves it that way too | B | PIK3CA activity raises SUV39H2's level | compounds that target PIK3CA: 3 of 4 lower it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[PIK3CA]] | [[TCERG1]] | moves it that way too | B | PIK3CA activity raises TCERG1's level | compounds that target PIK3CA: 3 of 4 lower it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[PIK3CA]] | [[CP]] | moves it that way too | B | PIK3CA activity lowers CP's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[PIK3CA]] | [[CUTALP]] | moves it that way too | B | PIK3CA activity lowers CUTALP's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[PIK3CA]] | [[TRAF3]] | moves it that way too | B | PIK3CA activity raises TRAF3's level | compounds that target PIK3CA: 3 of 4 lower it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[PIK3CA]] | [[ELAVL1]] | moves it that way too | B | PIK3CA activity raises ELAVL1's level | compounds that target PIK3CA: 2 of 4 lower it (Alpelisib, Bimiralisib) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds |
| [[PIK3CA]] | [[RSRC1]] | does not move it that way (the class's other compounds do) | B | PIK3CA activity lowers RSRC1's level | compounds that target PIK3CA: 2 of 4 raise it (Bimiralisib, GSK1059615) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets |
| [[PIK3CA]] | [[ACER3]] | moves it that way too | B | PIK3CA activity raises ACER3's level | compounds that target PIK3CA: 3 of 4 lower it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[PIK3CA]] | [[RXRB]] | moves it that way too | B | PIK3CA activity lowers RXRB's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[PIK3CA]] | [[TNFSF10]] | moves it that way too | B | PIK3CA activity lowers TNFSF10's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[PIK3CA]] | [[E2F3]] | moves it that way too | B | PIK3CA activity raises E2F3's level | compounds that target PIK3CA: 3 of 4 lower it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[PIK3CA]] | [[PDLIM1]] | moves it that way too | B | PIK3CA activity lowers PDLIM1's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[PIK3CA]] | [[ABHD4]] | moves it that way too | B | PIK3CA activity lowers ABHD4's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[PIK3CA]] | [[CEP68]] | moves it that way too | B | PIK3CA activity lowers CEP68's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |

## Data

- `tables/drugs.parquet` — drug == "Alpelisib"
- `tables/drugdoses.parquet` — dd in 81, 82, 83
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

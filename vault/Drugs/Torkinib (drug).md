---
drug: "Torkinib"
type: "drug"
salt_base: "Torkinib"
targets: "MTOR, PDGFRA, PRKDC, PIK3CD, PIK3CG, PIK3CA, PIK3CB, HCK, SRC, KDR, ABL1, EPHB4, EGFR"
moa_fine: "MTOR inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 19
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Torkinib

*MTOR inhibitor (inhibitor/antagonist) · targets: MTOR, PDGFRA, PRKDC, PIK3CD, PIK3CG, PIK3CA, PIK3CB, HCK, SRC, KDR, ABL1, EPHB4, EGFR · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 6 / 0 / 19; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.11 / -0.02.
> Flags by dose: - / noisy plate (z scaled) / toxic; noisy plate (z scaled). ⚠ 5 µM: toxic (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:F11 | 5 / 1 | — | -0.17 | -0.6/-1.4/-1.2 | — |
| 0.5 µM | [[Plate 02]]:F11 | 0 / 0 | — | +0.47 | +0.4/+0.1/+0.2 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:F11 | 15 / 4 | — | -1.17 | +1.2/+1.4/+0.8 | ⚠ toxic · noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[ENSG00000273149]] 1.61× (z +3.3, 7/43 lines), [[ABCA15P]] 1.27× (z +3.0, 1/44 lines), [[LSMEM1]] 1.58× (z +2.9, 6/47 lines), [[ENSG00000232754]] 1.30× (z +2.8, 2/43 lines), [[MTUS2]] 1.28× (z +2.8, 0/44 lines)

**5 µM** (15 genes, 15 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[ENSG00000285471]] ⚠ 1.92× (z +3.4, 0/13 lines), [[SLC52A3]] ⚠ 1.91× (z +3.4, 0/15 lines), [[TDRD9]] ⚠ 2.03× (z +3.3, 0/4 lines), [[SORCS2]] ⚠ 1.64× (z +3.2, 0/17 lines), [[SLIT3]] ⚠ 1.53× (z +3.1, 0/14 lines), [[MRPS18A]] ⚠ 1.37× (z +3.1, 4/39 lines), [[PAX6]] ⚠ 1.76× (z +3.1, 1/14 lines), [[IDH3A]] ⚠ 1.37× (z +3.1, 3/44 lines), [[TSPAN17]] ⚠ 1.41× (z +3.1, 3/36 lines), [[LIN28B]] ⚠ 1.49× (z +3.0, 0/12 lines), [[ARRDC1]] ⚠ 1.54× (z +3.0, 5/30 lines), [[CDKN3]] ⚠ 1.81× (z +3.0, 11/42 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[OLFM1]] 0.670× (z -3.5, 5/19 lines)

**5 µM** (4 genes, 4 with an alert ⚠; the drug-dose carries ⚠ toxic): [[ZNF470]] ⚠ 0.720× (z -3.2, 7/25 lines), [[GFOD2]] ⚠ 0.765× (z -3.1, 9/44 lines), [[FERMT2]] ⚠ 0.763× (z -2.9, 10/37 lines), [[ENSG00000290890]] ⚠ 0.696× (z -2.9, 12/44 lines)

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
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[J82 (line)]] (-4.2), [[A-172 (line)]] (-3.7), [[A498 (line)]] (-3.1) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: toxic. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[AZD2858 (drug)]] (+0.83, GSK3 inhibitor, ⚠ vector dose flagged: toxic); [[Dorzolamide (hydrochloride) (drug)]] (+0.71, unclear); [[Docetaxel (drug)]] (+0.68, Microtubule inhibitor, ⚠ vector dose flagged: transcription drop; cell-cycle shift); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] (+0.68, Glucose transporter inhibitor); [[XRK3F2 (drug)]] (+0.65, unclear); [[LY-2584702 (tosylate salt) (drug)]] (+0.64, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[BI-78D3 (drug)]] (+0.63, Other MAPK inhibitor); [[Imiquimod (hydrochloride) (drug)]] (+0.62, unclear, ⚠ vector dose flagged: toxic); [[Canagliflozin (hemihydrate) (drug)]] (+0.61, Glucose transporter inhibitor); [[Carbamazepine (drug)]] (+0.59, HDAC inhibitor); [[Hydroxyfasudil (drug)]] (+0.58, unclear); [[9-ING-41 (drug)]] (+0.57, GSK3 inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 33 arrows, 33 of them with an alert ⚠; grade A 0, B 29, C 4. Shown: the 15 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[FAAH2]] | 5 µM | B | FAAH2 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express FAAH2 (26) vs lines expressing it (22) | the lines without FAAH2: 0.76× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[ELF3]] | 5 µM | B | ELF3 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express ELF3 (23) vs lines expressing it (25) | the lines without ELF3: 0.82× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[LRRC61]] | 5 µM | B | LRRC61 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express LRRC61 (16) vs lines expressing it (32) | the lines without LRRC61: 0.82× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: ACTR3C, ARHGEF5, ENPP4 |
| [[GOLT1A]] | 5 µM | B | GOLT1A activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express GOLT1A (24) vs lines expressing it (24) | the lines without GOLT1A: 0.80× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent |
| [[VAMP8]] | 5 µM | B | VAMP8 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express VAMP8 (14) vs lines expressing it (34) | the lines without VAMP8: 0.85× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EVPL; maybe low, not absent |
| [[DUSP4]] | 5 µM | B | DUSP4 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express DUSP4 (15) vs lines expressing it (33) | the lines without DUSP4: 0.82× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[FOXA1]] | 5 µM | B | FOXA1 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express FOXA1 (22) vs lines expressing it (26) | the lines without FOXA1: 0.78× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL |
| [[LINC01348]] | 5 µM | B | LINC01348 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express LINC01348 (10) vs lines expressing it (38) | the lines without LINC01348: 0.81× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ARHGAP42, RIPK4, ABCC3; maybe low, not absent |
| [[ENSG00000288656]] | 5 µM | B | ENSG00000288656 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express ENSG00000288656 (20) vs lines expressing it (28) | the lines without ENSG00000288656: 0.81× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: MYO5C, MANSC1, EVPL |
| [[ACTR3C]] | 5 µM | B | ACTR3C activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express ACTR3C (15) vs lines expressing it (33) | the lines without ACTR3C: 0.81× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[ENSG00000227486]] | 5 µM | B | ENSG00000227486 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express ENSG00000227486 (19) vs lines expressing it (29) | the lines without ENSG00000227486: 0.80× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: KLF8, LNX1, MCTP2; maybe low, not absent |
| [[ABCC3]] | 5 µM | B | ABCC3 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express ABCC3 (16) vs lines expressing it (32) | the lines without ABCC3: 0.87× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[ANGPTL4]] | 5 µM | B | ANGPTL4 activity lowers the cells' numbers under Torkinib 5 µM (makes them more sensitive) | lines that do not express ANGPTL4 (13) vs lines expressing it (35) | the lines without ANGPTL4: 1.35× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: CLDN14-AS1, LGALS1, EBI3 |
| [[SMPDL3B]] | 5 µM | B | SMPDL3B activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express SMPDL3B (23) vs lines expressing it (25) | the lines without SMPDL3B: 0.77× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[AHR]] | 5 µM | B | AHR activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 0.90× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 199 arrows, 199 of them with an alert ⚠; grade A 0, B 199, C 0. Shown: the 15 strongest; 184 more arrows (184 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[MTOR]] | [[INSR]] | does not move it that way (the class's other compounds do) | B | MTOR activity lowers INSR's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[FKBP14]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises FKBP14's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 4.2% of all compounds | 0.005 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[WASHC2C]] | does not move it that way (the class's other compounds do) | B | MTOR activity lowers WASHC2C's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[TSPAN13]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises TSPAN13's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 2.8% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[MCM8]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises MCM8's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.6% of all compounds | 0.007 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[WDR19]] | does not move it that way (the class's other compounds do) | B | MTOR activity lowers WDR19's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 5.6% of all compounds | 0.007 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[CENPN]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises CENPN's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.1% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[DTL]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises DTL's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 6.2% of all compounds | 0.008 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[WDR62]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises WDR62's level | compounds that target MTOR: 6 of 8 lower it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 6.2% of all compounds | 0.008 | ⚠ off-target possible; 6 compounds; artifact flags |
| [[MTOR]] | [[MARS1]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises MARS1's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds |
| [[MTOR]] | [[SMAP2]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises SMAP2's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[ERICH1]] | does not move it that way (the class's other compounds do) | B | MTOR activity lowers ERICH1's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.6% of all compounds | 0.010 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[FBXO32]] | does not move it that way (the class's other compounds do) | B | MTOR activity lowers FBXO32's level | compounds that target MTOR: 6 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 75% of the class's compounds vs 7.3% of all compounds | 0.013 | ⚠ off-target possible; 6 compounds |
| [[MTOR]] | [[PDIA3]] | does not move it that way (the class's other compounds do) | B | MTOR activity raises PDIA3's level | compounds that target MTOR: 5 of 8 lower it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.9% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[MTOR]] | [[YPEL1]] | does not move it that way (the class's other compounds do) | B | MTOR activity lowers YPEL1's level | compounds that target MTOR: 5 of 8 raise it (Bimiralisib, GSK1059615, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 3.9% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Torkinib"
- `tables/drugdoses.parquet` — dd in 1030, 1031, 1032
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

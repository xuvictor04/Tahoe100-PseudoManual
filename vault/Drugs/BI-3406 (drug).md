---
drug: "BI-3406"
type: "drug"
salt_base: "BI-3406"
targets: "KRAS, SOS1"
moa_fine: "RAS inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 132
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# BI-3406

*RAS inhibitor (inhibitor/antagonist) · targets: KRAS, SOS1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 5 / 132 / 127; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.32 / 0.77.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:B10 | 4 / 1 | — | +0.15 | -0.9/-0.8/-0.4 | — |
| 0.5 µM | [[Plate 02]]:B10 | 43 / 89 | — | +0.55 | -1.8/-1.0/-1.0 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:B10 | 44 / 83 | — | +0.86 | -1.6/-1.0/-1.0 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[OLFML2A]] 1.37× (z +3.2, 5/27 lines), [[SF3B4]] 1.46× (z +3.0, 15/47 lines), [[CFB]] 1.44× (z +3.0, 8/28 lines), [[NEK5]] 1.29× (z +3.0, 0/41 lines)

**0.5 µM** (43 genes, none with an alert; 12 shown): [[CLIP1]] 1.23× (z +4.7, 23/49 lines), [[CFB]] 2.05× (z +4.6, 16/28 lines), [[GBP2]] 1.72× (z +4.5, 16/36 lines), [[DUSP16]] 1.32× (z +4.3, 23/47 lines), [[KRAS]] 1.26× (z +4.0, 22/49 lines), [[LURAP1L]] 1.49× (z +3.9, 13/36 lines), [[MAP2]] 1.64× (z +3.8, 13/34 lines), [[RHOB]] 1.59× (z +3.7, 25/48 lines), [[TCTA]] 1.47× (z +3.7, 6/48 lines), [[LINC02057]] 1.66× (z +3.5, 15/23 lines), [[PGM2L1]] 1.24× (z +3.4, 16/45 lines), [[GABARAPL1]] 1.40× (z +3.4, 14/46 lines)

**5 µM** (44 genes, none with an alert; 12 shown): [[DUSP16]] 1.47× (z +4.4, 21/46 lines), [[GBP2]] 2.18× (z +4.3, 15/35 lines), [[KRAS]] 1.38× (z +4.0, 20/48 lines), [[CLIP1]] 1.37× (z +4.0, 19/48 lines), [[PALLD]] 1.51× (z +3.7, 16/37 lines), [[CFB]] 2.47× (z +3.7, 15/27 lines), [[STK38]] 1.24× (z +3.6, 11/48 lines), [[PLAGL1]] 1.42× (z +3.6, 8/26 lines), [[PHLDB2]] 1.51× (z +3.5, 17/37 lines), [[ARID5B]] 1.56× (z +3.5, 15/42 lines), [[RHOB]] 1.83× (z +3.5, 22/47 lines), [[NEAT1]] 1.43× (z +3.5, 27/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[SPRED2]] 0.823× (z -2.7, 19/49 lines)

**0.5 µM** (89 genes, none with an alert; 12 shown): [[ETV5]] 0.577× (z -7.2, 30/49 lines), [[SPRY4]] 0.460× (z -7.2, 33/49 lines), [[ETV4]] 0.523× (z -6.5, 27/46 lines), [[ETV1]] 0.468× (z -6.5, 22/37 lines), [[PRAG1]] 0.731× (z -5.4, 15/33 lines), [[EGR1]] 0.393× (z -5.1, 36/47 lines), [[ZFPM2-AS1]] 0.671× (z -5.1, 18/33 lines), [[NT5E]] 0.554× (z -5.1, 24/35 lines), [[ELK3]] 0.659× (z -5.0, 22/45 lines), [[ITGB5]] 0.675× (z -4.9, 30/47 lines), [[FOSL1]] 0.477× (z -4.9, 33/44 lines), [[SPRY4-AS1]] 0.518× (z -4.8, 31/46 lines)

**5 µM** (83 genes, none with an alert; 12 shown): [[ETV5]] 0.292× (z -8.8, 30/48 lines), [[ETV1]] 0.218× (z -7.6, 24/37 lines), [[SPRY4-AS1]] 0.254× (z -7.4, 32/45 lines), [[ZFPM2-AS1]] 0.477× (z -6.1, 24/32 lines), [[SPRY4]] 0.235× (z -6.1, 30/48 lines), [[CCND1]] 0.446× (z -5.9, 30/41 lines), [[EGR1]] 0.167× (z -5.9, 37/46 lines), [[MYEOV]] 0.396× (z -5.5, 20/29 lines), [[NT5E]] 0.345× (z -5.5, 24/34 lines), [[DUSP6]] 0.190× (z -5.4, 33/44 lines), [[ETV4]] 0.325× (z -5.0, 23/44 lines), [[FOSL1]] 0.381× (z -5.0, 33/43 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Module 174]] (-2.3), [[Module 092]] (-2.3) |
| 5 µM | — | [[Module 174]] (-2.4), [[Module 092]] (-2.3) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[NCI-H1792 (line)]] (-6.4), [[SK-MEL-2 (line)]] (-4.2), [[CHP-212 (line)]] (-3.7) | [[NCI-H23 (line)]] (1.50), [[AsPC-1 (line)]] (1.46), [[HOP62 (line)]] (1.42), [[Hs 766T (line)]] (1.38) · weakest: [[SW48 (line)]] (0.221), [[C32 (line)]] (0.248), [[RKO (line)]] (0.284) |
| 5 µM | [[NCI-H1792 (line)]] (-8.6), [[SK-MEL-2 (line)]] (-6.0), [[CHP-212 (line)]] (-5.1), [[NCI-H23 (line)]] (-4.8), [[SW 900 (line)]] (-3.8) | [[NCI-H23 (line)]] (1.55), [[NCI-H460 (line)]] (1.50), [[NCI-H1573 (line)]] (1.46), [[AsPC-1 (line)]] (1.46) · weakest: [[C32 (line)]] (0.00169), [[COLO 205 (line)]] (0.0415), [[RKO (line)]] (0.137) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[RMC-6236 (drug)]] (+0.88, RAS inhibitor); [[Trametinib (drug)]] (+0.88, MEK inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Bimiralisib (drug)]] (+0.85, PI3K/AKT inhibitor); [[Binimetinib (drug)]] (+0.80, MEK inhibitor); [[Trametinib (DMSO_TF solvate) (drug)]] (+0.77, MEK inhibitor); [[Elimusertib hydrochloride (drug)]] (+0.74, unclear); [[Cobimetinib (drug)]] (+0.70, MEK inhibitor); [[Alpelisib (drug)]] (+0.61, PI3K/AKT inhibitor); [[Perindopril (erbumine) (drug)]] (+0.59, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000232884]] | 5 µM | B | ENSG00000232884 activity raises the cells' numbers under BI-3406 5 µM (protects the cells) | lines that do not express ENSG00000232884 (12) vs lines expressing it (36) | the lines without ENSG00000232884: 0.82× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, NRIP1, ATXN1; maybe low, not absent |
| [[ENSG00000232884]] | 0.5 µM | B | ENSG00000232884 activity raises the cells' numbers under BI-3406 0.5 µM (protects the cells) | lines that do not express ENSG00000232884 (12) vs lines expressing it (36) | the lines without ENSG00000232884: 0.84× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, NRIP1, ATXN1; maybe low, not absent |
| [[LINC02575]] | 0.5 µM | B | LINC02575 activity lowers the cells' numbers under BI-3406 0.5 µM (makes them more sensitive) | lines that do not express LINC02575 (32) vs lines expressing it (16) | the lines without LINC02575: 1.25× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000289309, LINC01205, MSRB3-AS1 |
| [[STX1A]] | 5 µM | C | STX1A activity raises the cells' numbers under BI-3406 5 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.60× the cells of the other lines | 0.040 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| [[RILP]] | 5 µM | C | RILP activity raises the cells' numbers under BI-3406 5 µM (protects the cells) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 0.60× the cells of the other lines | 0.041 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| [[PLEKHN1]] | 5 µM | C | PLEKHN1 activity raises the cells' numbers under BI-3406 5 µM (protects the cells) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 0.57× the cells of the other lines | 0.068 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| [[STX1A]] | 0.5 µM | C | STX1A activity raises the cells' numbers under BI-3406 0.5 µM (protects the cells) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 0.74× the cells of the other lines | 0.094 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[KRAS]] | [[MFSD2A]] | moves it that way too | B | KRAS activity raises MFSD2A's level | compounds that target KRAS: 3 of 4 lower it (BI-3406, Lonafarnib, RMC-6236) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

## Data

- `tables/drugs.parquet` — drug == "BI-3406"
- `tables/drugdoses.parquet` — dd in 132, 133, 134
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

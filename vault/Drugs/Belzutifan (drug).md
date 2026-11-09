---
drug: "Belzutifan"
type: "drug"
salt_base: "Belzutifan"
targets: "EPAS1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.5", "5"]
best_dose: "5"
max_sig_genes: 843
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Belzutifan

*unclear (inhibitor/antagonist) · targets: EPAS1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.5 µM / 5 µM): 0 / 843; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.19.
> Flags by dose: noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.5 µM | [[Plate 02]]:F4 | 0 / 0 | — | -0.29 | -0.0/+0.4/+0.2 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:F4 | 370 / 473 | — | -0.59 | -3.1/-2.1/+1.2 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (370 genes, none with an alert; 12 shown): [[ENSG00000229618]] 2.02× (z +5.9, 5/15 lines), [[ENSG00000232884]] 2.98× (z +5.9, 5/20 lines), [[ENSG00000239462]] 2.21× (z +5.0, 16/27 lines), [[CHMP3]] 1.38× (z +4.9, 21/47 lines), [[M6PR]] 1.61× (z +4.9, 25/46 lines), [[LINC02458]] 2.99× (z +4.9, 10/34 lines), [[ZNF92]] 1.59× (z +4.8, 13/45 lines), [[PELO-AS1]] 2.20× (z +4.7, 7/32 lines), [[ENSG00000257062]] 1.96× (z +4.7, 7/17 lines), [[HDAC9]] 1.61× (z +4.7, 24/38 lines), [[THUMPD3]] 1.44× (z +4.6, 16/45 lines), [[VARS1]] 2.22× (z +4.6, 28/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (473 genes, none with an alert; 12 shown): [[JMY]] 0.273× (z -10.9, 44/45 lines), [[RPS6KA5]] 0.424× (z -9.8, 40/47 lines), [[TFDP2]] 0.554× (z -9.5, 42/47 lines), [[KLHL24]] 0.366× (z -8.1, 44/47 lines), [[YPEL2]] 0.409× (z -7.9, 31/42 lines), [[CCDC28A]] 0.426× (z -7.7, 32/45 lines), [[PDCD4]] 0.523× (z -7.4, 39/47 lines), [[MTURN]] 0.405× (z -7.4, 34/42 lines), [[GARRE1]] 0.530× (z -7.3, 36/47 lines), [[RB1CC1]] 0.567× (z -7.3, 46/47 lines), [[TCP11L2]] 0.325× (z -7.1, 40/45 lines), [[HDAC5]] 0.427× (z -7.1, 38/46 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.5 µM | — | — |
| 5 µM | [[Module 001]] (+2.2), [[Module 064]] (+2.1), [[Module 229]] (+2.1) | [[Module 225]] (-4.0), [[Module 069]] (-3.2), [[Module 145]] (-3.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.5 µM | — | — |
| 5 µM | [[HCT15 (line)]] (-4.6), [[RPMI-7951 (line)]] (-4.5), [[HOP62 (line)]] (-3.3), [[SW 1271 (line)]] (-3.2) | [[SW 900 (line)]] (1.25), [[AsPC-1 (line)]] (1.25), [[A498 (line)]] (1.20), [[Hs 766T (line)]] (1.13) · weakest: [[SHP-77 (line)]] (0.636), [[C-33 A (line)]] (0.640), [[SK-MEL-2 (line)]] (0.656) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[EX229 (drug)]] (+0.62, unclear); [[TAK-733 (drug)]] (+0.59, MEK inhibitor); [[c-Kit-IN-1 (drug)]] (+0.59, Multi-TK inhibitor); [[Bestatin (drug)]] (+0.56, unclear, ⚠ only 3 significant genes); [[Abemaciclib (drug)]] (+0.55, CDK inhibitor); [[Sapanisertib (drug)]] (+0.54, MTOR inhibitor); [[Nafamostat (mesylate) (drug)]] (+0.46, unclear, ⚠ only 3 significant genes); [[BI-78D3 (drug)]] (+0.46, Other MAPK inhibitor); [[venetoclax (drug)]] (+0.43, unclear); [[Oxaprozin (drug)]] (+0.42, Cyclooxygenase inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 43 arrows, 43 of them with an alert ⚠; grade A 0, B 6, C 37. Shown: the 15 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[IL15]] | 5 µM | B | IL15 activity lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 1.49× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[KRT16]] | 5 µM | B | KRT16 activity lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | lines that do not express KRT16 (27) vs lines expressing it (21) | the lines without KRT16: 1.34× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[ALDH3B1]] | 5 µM | B | ALDH3B1 activity lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 1.42× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[ATXN1]] | 5 µM | B | ATXN1 activity lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | lines that do not express ATXN1 (6) vs lines expressing it (42) | the lines without ATXN1: 1.55× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |
| [[ENSG00000232884]] | 5 µM | B | ENSG00000232884 activity lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | lines that do not express ENSG00000232884 (12) vs lines expressing it (36) | the lines without ENSG00000232884: 1.43× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, NRIP1, ATXN1; maybe low, not absent |
| [[F3]] | 5 µM | B | F3 activity lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | lines that do not express F3 (24) vs lines expressing it (24) | the lines without F3: 1.30× the cells of the other lines | 0.0997 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[ENSG00000256029]] | 5 µM | C | ENSG00000256029 activity lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | lines that do not express ENSG00000256029 (4) vs lines expressing it (44) | the lines without ENSG00000256029: 1.48× the cells of the other lines | 0.082 | ⚠ few lines (4 vs 46); across organs; also absent: ERRFI1, FXYD5, CAV2; maybe low, not absent |
| [[ENSG00000289130]] | 5 µM | C | ENSG00000289130's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | ENSG00000289130's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.75 | 0.162 over the table, 0.004 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[PPP1R32]] | 5 µM | C | PPP1R32's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | PPP1R32's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.268 over the table, 0.018 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ENSG00000287086]] | 5 µM | C | ENSG00000287086's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | ENSG00000287086's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.023 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[CMYA5]] | 5 µM | C | CMYA5's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | CMYA5's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.287 over the table, 0.023 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ENSG00000255139]] | 5 µM | C | ENSG00000255139's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | ENSG00000255139's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.67 | 0.325 over the table, 0.028 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[PGLS-DT]] | 5 µM | C | PGLS-DT's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | PGLS-DT's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.360 over the table, 0.036 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[KBTBD3]] | 5 µM | C | KBTBD3's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | KBTBD3's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.361 over the table, 0.036 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[LINC00159]] | 5 µM | C | LINC00159's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | LINC00159's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.365 over the table, 0.036 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Belzutifan"
- `tables/drugdoses.parquet` — dd in 153, 154
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

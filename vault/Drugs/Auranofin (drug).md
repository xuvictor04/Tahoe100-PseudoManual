---
drug: "Auranofin"
type: "drug"
salt_base: "Auranofin"
targets: "TXNRD1, TXNRD2"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 8581
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Auranofin

*unclear (inhibitor/antagonist) · targets: TXNRD1, TXNRD2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 9 / 140 / 8581; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.34 / 0.30.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:C6 | 7 / 2 | — | -0.21 | -0.8/-0.4/+0.6 | — |
| 0.5 µM | [[Plate 11]]:C6 | 55 / 85 | — | +0.13 | -0.8/+0.3/+1.8 | — |
| 5 µM | [[Plate 12]]:C6 | 5,419 / 3,162 | — | -0.94 | -3.7/-3.8/+10.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (7 genes, none with an alert): [[ATN1]] 1.24× (z +3.8, 25/48 lines), [[DPM2]] 1.25× (z +3.6, 6/47 lines), [[SORBS3]] 1.25× (z +3.5, 9/45 lines), [[RPL6]] 1.35× (z +3.3, 28/48 lines), [[FAM219B]] 1.23× (z +3.1, 9/47 lines), [[EIF3C]] 1.27× (z +2.8, 3/47 lines), [[IRGQ]] 1.24× (z +2.7, 4/47 lines)

**0.5 µM** (55 genes, none with an alert; 12 shown): [[HMOX1]] 6.20× (z +17.2, 36/37 lines), [[GCLM]] 2.47× (z +12.8, 43/46 lines), [[PIR]] 1.74× (z +8.7, 26/38 lines), [[TXNRD1]] 1.59× (z +7.3, 37/47 lines), [[SLC7A11]] 1.79× (z +7.1, 34/42 lines), [[ME1]] 1.44× (z +6.4, 25/37 lines), [[NMRAL2P]] 1.90× (z +6.1, 16/29 lines), [[NQO1]] 1.75× (z +5.5, 32/43 lines), [[GCLC]] 1.34× (z +5.3, 27/44 lines), [[FBXO30]] 1.47× (z +5.0, 26/46 lines), [[TM4SF19]] 1.41× (z +4.7, 13/28 lines), [[LINC01564]] 1.74× (z +4.6, 12/22 lines)

**5 µM** (5419 genes, none with an alert; 12 shown): [[BAG3]] 13.1× (z +46.0, 48/48 lines), [[SNAP23]] 5.04× (z +43.8, 48/48 lines), [[HMOX1]] 103× (z +43.6, 38/38 lines), [[LINC00624]] 18.3× (z +42.0, 45/45 lines), [[DNAJB1]] 21.6× (z +41.2, 48/48 lines), [[DNAJA4]] 17.5× (z +41.2, 25/25 lines), [[HSPA1B]] 77.1× (z +38.7, 48/48 lines), [[RUNDC3B]] 19.8× (z +37.8, 35/35 lines), [[CUBN]] 11.8× (z +36.4, 25/26 lines), [[HSPH1]] 32.2× (z +36.0, 48/48 lines), [[ENSG00000229618]] 9.44× (z +35.8, 14/16 lines), [[ENSG00000227240]] 10.1× (z +33.6, 34/35 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[METTL25]] 0.819× (z -2.9, 10/47 lines), [[BTBD8]] 0.787× (z -2.6, 9/45 lines)

**0.5 µM** (85 genes, none with an alert; 12 shown): [[ZNF347]] 0.737× (z -4.6, 7/28 lines), [[ACADSB]] 0.806× (z -4.5, 16/48 lines), [[ENSG00000269237]] 0.721× (z -4.4, 12/39 lines), [[PLA2G4A]] 0.790× (z -4.1, 6/26 lines), [[IL7]] 0.764× (z -4.0, 15/40 lines), [[ARHGAP28]] 0.707× (z -3.9, 6/23 lines), [[CEP120]] 0.816× (z -3.9, 20/48 lines), [[MYB]] 0.674× (z -3.8, 7/23 lines), [[GNAO1]] 0.757× (z -3.8, 5/24 lines), [[ENSG00000290888]] 0.747× (z -3.8, 7/25 lines), [[AGMO]] 0.682× (z -3.8, 6/17 lines), [[NMNAT3]] 0.772× (z -3.7, 10/30 lines)

**5 µM** (3162 genes, none with an alert; 12 shown): [[PTPRA]] 0.465× (z -33.7, 47/48 lines), [[EXOC6]] 0.442× (z -22.0, 42/46 lines), [[NEK3]] 0.325× (z -21.8, 38/44 lines), [[UNK]] 0.417× (z -20.3, 46/48 lines), [[PTPN2]] 0.536× (z -20.2, 47/48 lines), [[DCAF6]] 0.455× (z -19.7, 47/48 lines), [[FCHSD2]] 0.494× (z -19.7, 45/47 lines), [[NFYC]] 0.465× (z -19.6, 41/48 lines), [[MAP2K5]] 0.402× (z -19.2, 44/48 lines), [[STX8]] 0.430× (z -19.1, 43/48 lines), [[TANC1]] 0.452× (z -19.1, 45/48 lines), [[CNTRL]] 0.472× (z -19.0, 45/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 117]] (+2.6), [[Module 060]] (+2.3) | — |
| 5 µM | [[Module 060]] (+24.8), [[Module 191]] (+17.9), [[Module 026]] (+14.8) | [[Module 170]] (-10.1), [[Module 065]] (-9.5), [[Module 234]] (-9.4) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[BT-474 (line)]] (2.16), [[HT-29 (line)]] (1.74), [[HCT15 (line)]] (1.55), [[SW 1271 (line)]] (1.34) · weakest: [[NCI-H1573 (line)]] (0.294), [[NCI-H2030 (line)]] (0.348), [[A549 (line)]] (0.443) |
| 5 µM | [[NCI-H23 (line)]] (-7.4), [[RPMI-7951 (line)]] (-4.8), [[MIA PaCa-2 (line)]] (-4.1), [[SK-MEL-2 (line)]] (-3.1) | [[C32 (line)]] (1.50), [[HT-29 (line)]] (1.46), [[A-172 (line)]] (1.37), [[HOP62 (line)]] (1.34) · weakest: [[A549 (line)]] (0.333), [[NCI-H1573 (line)]] (0.417), [[HepG2_C3A (line)]] (0.483) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Infigratinib (drug)]] (+0.59, Other TK inhibitor); [[Nafamostat (mesylate) (drug)]] (+0.46, unclear, ⚠ only 3 significant genes); [[Pimozide (drug)]] (+0.46, unclear); [[Proglumide (drug)]] (+0.41, unclear); [[Bestatin (drug)]] (+0.41, unclear, ⚠ only 3 significant genes); [[Lactate (calcium) (drug)]] (+0.41, unclear); [[Mitoxantrone (dihydrochloride) (drug)]] (+0.40, DNA synthesis/repair inhibitor); [[Belzutifan (drug)]] (+0.36, unclear); [[Orlistat (drug)]] (+0.35, unclear); [[Filgotinib (drug)]] (+0.35, JAK/STAT inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PLD1]] | 5 µM | B | PLD1 activity raises the cells' numbers under Auranofin 5 µM (protects the cells) | lines that do not express PLD1 (7) vs lines expressing it (41) | the lines without PLD1: 0.71× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[HBEGF]] | 5 µM | C | HBEGF activity raises the cells' numbers under Auranofin 5 µM (protects the cells) | lines that do not express HBEGF (3) vs lines expressing it (45) | the lines without HBEGF: 0.59× the cells of the other lines | 0.025 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| [[RRM2]] | 5 µM | C | RRM2 activity lowers the cells' numbers under Auranofin 5 µM (makes them more sensitive) | lines that do not express RRM2 (3) vs lines expressing it (45) | the lines without RRM2: 1.64× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: CLSPN, E2F8, TCF19; maybe low, not absent |
| [[ELF4]] | 5 µM | C | ELF4 activity raises the cells' numbers under Auranofin 5 µM (protects the cells) | lines that do not express ELF4 (3) vs lines expressing it (45) | the lines without ELF4: 0.63× the cells of the other lines | 0.064 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, SP100; maybe low, not absent |
| [[SESTD1]] | 5 µM | C | SESTD1 activity raises the cells' numbers under Auranofin 5 µM (protects the cells) | lines that do not express SESTD1 (4) vs lines expressing it (44) | the lines without SESTD1: 0.66× the cells of the other lines | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SCML1, LHFPL2, TBXAS1; maybe low, not absent |
| [[CYB561]] | 5 µM | C | CYB561 activity lowers the cells' numbers under Auranofin 5 µM (makes them more sensitive) | lines that do not express CYB561 (3) vs lines expressing it (45) | the lines without CYB561: 1.66× the cells of the other lines | 0.066 | ⚠ few lines (3 vs 47); across organs; also absent: MATN1-AS1, E2F8, PBX4; maybe low, not absent |
| [[NCAPH]] | 5 µM | C | NCAPH's natural level lowers the cells' numbers under Auranofin 5 µM (makes them more sensitive) | NCAPH's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.268 over the table, 0.045 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Auranofin"
- `tables/drugdoses.parquet` — dd in 123, 124, 125
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

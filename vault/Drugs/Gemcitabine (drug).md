---
drug: "Gemcitabine"
type: "drug"
salt_base: "Gemcitabine"
targets: ""
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 85
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Gemcitabine

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 85 / 62 / 34; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.46 / 0.54.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:A7, [[Plate 01]]:G9 | 28 / 57 | 0.318 | +0.43 | +3.3/-2.2/+1.0 | — |
| 0.5 µM | [[Plate 02]]:A7, [[Plate 02]]:G9 | 44 / 18 | 0.216 | -0.37 | +2.5/-1.0/+0.6 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:A7, [[Plate 03]]:G9 | 31 / 3 | 0.342 | -0.18 | +2.9/+0.6/+0.9 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (28 genes, none with an alert; 12 shown): [[TPRA1]] 1.40× (z +7.2, 26/48 lines), [[CYP1B1]] 2.07× (z +6.7, 19/19 lines), [[TIPARP]] 1.50× (z +6.6, 38/47 lines), [[ALDH1A3]] 1.40× (z +5.8, 20/28 lines), [[MIR181A1HG]] 1.32× (z +5.6, 30/41 lines), [[CYP1B1-AS1]] 1.60× (z +5.5, 22/33 lines), [[RMDN2-AS1]] 1.75× (z +5.4, 16/29 lines), [[CCNE2]] 1.38× (z +5.4, 16/47 lines), [[E2F7]] 1.34× (z +5.1, 23/43 lines), [[AHRR]] 1.29× (z +4.8, 19/45 lines), [[TP73]] 1.29× (z +4.3, 5/32 lines), [[DTL]] 1.25× (z +4.2, 15/48 lines)

**0.5 µM** (44 genes, none with an alert; 12 shown): [[E2F7]] 1.34× (z +5.4, 24/43 lines), [[TMA7]] 1.57× (z +4.2, 40/48 lines), [[EREG]] 1.35× (z +4.1, 9/22 lines), [[TPRA1]] 1.28× (z +3.9, 11/48 lines), [[CYP1B1]] 2.22× (z +3.7, 13/19 lines), [[POLG2]] 1.27× (z +3.7, 19/48 lines), [[UNC13A]] 1.34× (z +3.7, 3/19 lines), [[PXK]] 1.21× (z +3.6, 12/46 lines), [[UNC5A]] 1.47× (z +3.5, 1/26 lines), [[ENSG00000234261]] 1.35× (z +3.5, 0/19 lines), [[ENSG00000285635]] 1.28× (z +3.5, 5/35 lines), [[DTL]] 1.27× (z +3.4, 12/48 lines)

**5 µM** (31 genes, none with an alert; 12 shown): [[CYP1B1]] 2.90× (z +5.1, 17/19 lines), [[ALDH1A3]] 1.71× (z +5.1, 16/28 lines), [[E2F7]] 1.47× (z +4.5, 15/43 lines), [[PLA2G4A]] 1.38× (z +4.2, 2/26 lines), [[TIPARP]] 1.52× (z +3.8, 32/47 lines), [[MIR181A1HG]] 1.40× (z +3.7, 18/41 lines), [[XRCC3]] 1.45× (z +3.6, 1/42 lines), [[RMDN2-AS1]] 1.94× (z +3.5, 5/22 lines), [[CCNE2]] 1.47× (z +3.5, 5/43 lines), [[CYP1B1-AS1]] 1.71× (z +3.5, 6/29 lines), [[POLA2]] 1.36× (z +3.5, 0/46 lines), [[AHRR]] 1.32× (z +3.4, 12/45 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (57 genes, none with an alert; 12 shown): [[PLK1]] 0.682× (z -6.7, 27/48 lines), [[PIF1]] 0.671× (z -6.7, 26/47 lines), [[H1-5]] 0.446× (z -5.8, 28/37 lines), [[ASPM]] 0.737× (z -5.8, 35/47 lines), [[CCNB1]] 0.722× (z -5.5, 31/47 lines), [[KIF20A]] 0.689× (z -5.4, 26/47 lines), [[H2BC9]] 0.464× (z -5.1, 18/30 lines), [[KNSTRN]] 0.791× (z -5.1, 14/48 lines), [[H1-3]] 0.526× (z -4.8, 22/36 lines), [[DEPDC1]] 0.747× (z -4.8, 29/46 lines), [[DHRS2]] 0.593× (z -4.8, 15/34 lines), [[H2BC8]] 0.502× (z -4.8, 21/34 lines)

**0.5 µM** (18 genes, none with an alert; 12 shown): [[PLK1]] 0.710× (z -4.5, 20/48 lines), [[PIF1]] 0.724× (z -4.1, 16/47 lines), [[CCNB1]] 0.731× (z -4.0, 23/47 lines), [[CCNG1]] 0.808× (z -3.8, 20/48 lines), [[CDC20]] 0.688× (z -3.6, 23/45 lines), [[DDX56]] 0.825× (z -3.5, 11/48 lines), [[P2RY11]] 0.767× (z -3.5, 12/48 lines), [[RRAGA]] 0.742× (z -3.4, 13/47 lines), [[AURKA]] 0.781× (z -3.4, 18/48 lines), [[ASPM]] 0.755× (z -3.3, 21/47 lines), [[ENSG00000258101]] 0.748× (z -3.3, 3/46 lines), [[H1-3]] 0.618× (z -3.2, 16/36 lines)

**5 µM** (3 genes, none with an alert): [[DCBLD1]] 0.806× (z -3.1, 7/47 lines), [[ARFGEF3]] 0.822× (z -2.8, 13/42 lines), [[PIF1]] 0.755× (z -2.6, 6/44 lines)

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
| 0.05 µM | — | [[H4 (line)]] (1.56), [[A-427 (line)]] (1.47), [[HOP62 (line)]] (1.41), [[LS 180 (line)]] (1.38) · weakest: [[AsPC-1 (line)]] (0.507), [[HepG2_C3A (line)]] (0.590), [[NCI-H2347 (line)]] (0.615) |
| 0.5 µM | — | [[SW 1088 (line)]] (1.44), [[HOP62 (line)]] (1.33), [[CFPAC-1 (line)]] (1.26), [[LS 180 (line)]] (1.22) · weakest: [[COLO 205 (line)]] (0.545), [[NCI-H661 (line)]] (0.590), [[A-427 (line)]] (0.672) |
| 5 µM | [[NCI-H460 (line)]] (-3.2), [[RKO (line)]] (-3.1) | [[BT-474 (line)]] (1.38), [[LS 180 (line)]] (1.36), [[HCT15 (line)]] (1.31), [[H4 (line)]] (1.24) · weakest: [[SW 1271 (line)]] (0.176), [[SHP-77 (line)]] (0.631), [[Hs 766T (line)]] (0.643) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 6 next most similar without an alert.*

- [[Cytarabine (drug)]] (+0.57, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Irinotecan (drug)]] (+0.50, DNA synthesis/repair inhibitor); [[Anastrozole (drug)]] (+0.48, unclear, ⚠ only 5 significant genes); [[Hexylresorcinol (drug)]] (+0.46, unclear); [[Cytarabine (hydrochloride) (drug)]] (+0.44, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Capivasertib (drug)]] (+0.44, PI3K/AKT inhibitor, ⚠ only 5 significant genes); [[AT7519 (drug)]] (+0.44, CDK inhibitor, ⚠ only 6 significant genes); [[Zileuton (drug)]] (+0.43, unclear, ⚠ only 4 significant genes); [[Irinotecan (hydrochloride) (drug)]] (+0.43, DNA synthesis/repair inhibitor); [[NVP-BHG712 (drug)]] (+0.42, unclear); [[Menadione (drug)]] (+0.41, unclear); [[Goserelin (acetate) (drug)]] (+0.39, unclear); [[Tomivosertib (drug)]] (+0.39, Protein synthesis inhibitor); [[Trimetrexate (drug)]] (+0.36, DNA synthesis/repair inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MTMR7]] | 5 µM | B | MTMR7 activity lowers the cells' numbers under Gemcitabine 5 µM (makes them more sensitive) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 1.19× the cells of the other lines | 0.022 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[TMEM92]] | 5 µM | B | TMEM92 activity raises the cells' numbers under Gemcitabine 5 µM (protects the cells) | lines that do not express TMEM92 (22) vs lines expressing it (26) | the lines without TMEM92: 0.83× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[INPP4B]] | 5 µM | B | INPP4B activity raises the cells' numbers under Gemcitabine 5 µM (protects the cells) | lines that do not express INPP4B (10) vs lines expressing it (38) | the lines without INPP4B: 0.82× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[DUSP23]] | 5 µM | B | DUSP23 activity raises the cells' numbers under Gemcitabine 5 µM (protects the cells) | lines that do not express DUSP23 (14) vs lines expressing it (34) | the lines without DUSP23: 0.85× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: HLA-F, SH2D4A, RARRES1 |
| [[HERC2P10]] | 5 µM | B | HERC2P10 activity lowers the cells' numbers under Gemcitabine 5 µM (makes them more sensitive) | lines that do not express HERC2P10 (14) vs lines expressing it (34) | the lines without HERC2P10: 1.16× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: TENM3, SHANK1, TENM3-AS1; maybe low, not absent |
| [[FASTKD5]] | 5 µM | C | FASTKD5's natural level lowers the cells' numbers under Gemcitabine 5 µM (makes them more sensitive) | FASTKD5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.268 over the table, 0.025 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[OMA1]] | 5 µM | C | OMA1's natural level raises the cells' numbers under Gemcitabine 5 µM (protects the cells) | OMA1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.69 | 0.268 over the table, 0.025 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Gemcitabine"
- `tables/drugdoses.parquet` — dd in 501, 502, 503
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

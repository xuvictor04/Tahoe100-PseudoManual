---
drug: "TAK-901"
type: "drug"
salt_base: "TAK-901"
targets: "AURKB"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 8188
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# TAK-901

*unclear (inhibitor/antagonist) · targets: AURKB · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1712 / 151 / 8188; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.05 / 0.27.
> Flags by dose: - / low cells (technical?); plate-row cell shift; noisy plate (z scaled) / plate-row cell shift; cell-cycle shift; composition shift; noisy plate (z scaled). ⚠ 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:D5 | 1,003 / 709 | — | -0.50 | -0.6/-1.1/+0.7 | — |
| 0.5 µM | [[Plate 02]]:D5 | 119 / 32 | — | -1.20 | +0.3/+0.3/+2.2 | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:D5 | 3,986 / 4,202 | — | +0.93 | +2.8/+3.7/+8.0 | ⚠ cell-cycle shift · plate-row cell shift; composition shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1003 genes, none with an alert; 12 shown): [[ENSG00000235609]] 1.99× (z +12.2, 35/39 lines), [[ENSG00000232884]] 2.78× (z +9.9, 21/30 lines), [[STYK1]] 1.77× (z +9.0, 16/27 lines), [[LINC01031]] 2.24× (z +8.9, 37/46 lines), [[METTL16]] 1.50× (z +8.9, 31/47 lines), [[CALCRL]] 2.60× (z +8.8, 20/27 lines), [[MGC4859]] 2.48× (z +8.5, 17/38 lines), [[LINC00616]] 3.05× (z +8.1, 22/35 lines), [[ENSG00000289130]] 2.39× (z +8.0, 23/43 lines), [[ENSG00000254180]] 1.94× (z +8.0, 27/45 lines), [[CMYA5]] 2.06× (z +7.9, 27/45 lines), [[CFAP161]] 2.88× (z +7.9, 34/40 lines)

**0.5 µM** (119 genes, none with an alert; 12 shown): [[TNFAIP3]] 2.90× (z +8.4, 33/45 lines), [[NUAK2]] 2.14× (z +7.1, 23/38 lines), [[NFKBIA]] 2.49× (z +6.3, 41/47 lines), [[KLF10]] 1.72× (z +5.9, 32/48 lines), [[ENSG00000265554]] 3.86× (z +5.3, 1/4 lines), [[ENSG00000289130]] 2.15× (z +5.3, 16/42 lines), [[ENSG00000285534]] 1.94× (z +5.2, 7/17 lines), [[ZNF35]] 1.49× (z +4.5, 11/43 lines), [[PPAN]] 1.53× (z +4.5, 17/47 lines), [[CDC123]] 1.29× (z +4.4, 17/48 lines), [[ITPRIP]] 1.44× (z +4.3, 10/38 lines), [[PDE4B]] 1.48× (z +4.2, 5/24 lines)

**5 µM** (3986 genes, 268 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[PPP4R2]] 7.41× (z +31.1, 49/49 lines; cell-cycle shift (explains ~2% here)), [[VTA1]] 4.64× (z +29.7, 48/49 lines; cell-cycle shift (explains ~0% here)), [[PRCC]] 10.1× (z +29.2, 48/49 lines; cell-cycle shift (explains ~0% here)), [[PPP4R3A]] 6.64× (z +28.9, 49/49 lines; cell-cycle shift (explains ~2% here)), [[CSNK1A1]] 4.04× (z +27.6, 48/49 lines; cell-cycle shift (explains ~4% here)), [[CBLL1]] 9.05× (z +27.4, 48/49 lines; cell-cycle shift (explains ~1% here)), [[PPP6C]] 6.02× (z +26.8, 48/49 lines; cell-cycle shift (explains ~1% here)), [[VIRMA]] 6.23× (z +26.5, 48/49 lines; cell-cycle shift (explains ~0% here)), [[KLF10]] 28.3× (z +26.4, 49/49 lines; cell-cycle shift (explains ~8% here)), [[PUM1]] 6.60× (z +25.7, 49/49 lines; cell-cycle shift (explains ~0% here)), [[RRN3]] 11.2× (z +25.7, 48/48 lines; cell-cycle shift (explains ~5% here)), [[TAB2]] 7.03× (z +25.6, 48/49 lines; cell-cycle shift (explains ~0% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (709 genes, none with an alert; 12 shown): [[ZC3H6]] 0.648× (z -9.0, 33/47 lines), [[HLA-E]] 0.525× (z -9.0, 38/46 lines), [[KDELR3]] 0.534× (z -8.4, 33/44 lines), [[FAM114A1]] 0.658× (z -8.2, 35/45 lines), [[ENSG00000253100]] 0.405× (z -8.0, 21/35 lines), [[TTC3]] 0.757× (z -7.4, 36/47 lines), [[KCTD17]] 0.432× (z -7.3, 23/43 lines), [[PRKRA]] 0.701× (z -7.2, 37/47 lines), [[PI4K2B]] 0.739× (z -7.1, 25/47 lines), [[RBL2]] 0.745× (z -7.0, 26/47 lines), [[ACTR1B]] 0.600× (z -7.0, 27/47 lines), [[TSPAN31]] 0.628× (z -7.0, 21/45 lines)

**0.5 µM** (32 genes, none with an alert; 12 shown): [[MIRLET7BHG]] 0.698× (z -3.7, 16/47 lines), [[ENSG00000291178]] 0.771× (z -3.7, 14/48 lines), [[ENSG00000214265]] 0.724× (z -3.7, 15/34 lines), [[EPN2]] 0.815× (z -3.7, 22/48 lines), [[PRKCZ]] 0.763× (z -3.5, 11/38 lines), [[ANGEL2]] 0.713× (z -3.5, 17/48 lines), [[PLEKHA1]] 0.818× (z -3.4, 6/47 lines), [[POLR2J3-1]] 0.645× (z -3.3, 8/42 lines), [[ZFYVE27]] 0.770× (z -3.3, 12/48 lines), [[SENP2]] 0.816× (z -3.3, 13/48 lines), [[HSPA12A]] 0.813× (z -3.2, 6/44 lines), [[NEAT1]] 0.784× (z -3.2, 27/47 lines)

**5 µM** (4202 genes, 484 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[MIB1]] 0.345× (z -19.3, 49/49 lines; cell-cycle shift (explains ~0% here)), [[EXOC6]] 0.254× (z -19.3, 44/47 lines; cell-cycle shift (explains ~2% here)), [[KATNBL1]] 0.224× (z -19.1, 47/49 lines; cell-cycle shift (explains ~0% here)), [[NLN]] 0.306× (z -18.4, 45/49 lines; cell-cycle shift (explains ~5% here)), [[SLC25A43]] 0.189× (z -18.3, 40/44 lines; cell-cycle shift (explains ~7% here)), [[FAM114A1]] 0.200× (z -17.6, 46/47 lines; cell-cycle shift (explains ~12% here)), [[EFCAB11]] 0.172× (z -17.1, 48/48 lines; cell-cycle shift (explains ~2% here)), [[PTPRA]] 0.484× (z -16.7, 40/49 lines; cell-cycle shift (explains ~6% here)), [[DNAAF9]] 0.208× (z -16.6, 35/37 lines; cell-cycle shift (explains ~13% here)), [[LIMS1]] 0.451× (z -16.5, 38/49 lines; cell-cycle shift (explains ~3% here)), [[NBEAL1]] 0.284× (z -16.5, 47/49 lines; cell-cycle shift (explains ~8% here)), [[CMC1]] 0.318× (z -16.4, 43/49 lines; cell-cycle shift (explains ~9% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 137]] (+4.1), [[Module 005]] (+3.6), [[Module 194]] (+3.4) | [[Module 030]] (-2.9), [[Module 208]] (-2.9), [[Module 041]] (-2.8) |
| 0.5 µM | — | — |
| 5 µM | [[Module 095]] (+10.8), [[Module 118]] (+10.2), [[Module 051]] (+10.1) | [[Module 184]] (-10.2), [[Module 002]] (-7.9), [[Module 146]] (-7.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[LOX-IMVI (line)]] (-5.8), [[SW48 (line)]] (-4.1) | [[A-172 (line)]] (1.68), [[Panc 03.27 (line)]] (1.51), [[NCI-H2347 (line)]] (1.48), [[SW1417 (line)]] (1.33) · weakest: [[SHP-77 (line)]] (0.378), [[NCI-H1792 (line)]] (0.586), [[HCT15 (line)]] (0.639) |
| 0.5 µM | — | [[Hs 766T (line)]] (1.38), [[CHP-212 (line)]] (1.35), [[A-172 (line)]] (1.33), [[HOP62 (line)]] (1.31) · weakest: [[KATO III (line)]] (0.603), [[SHP-77 (line)]] (0.629), [[NCI-H1792 (line)]] (0.638) |
| 5 µM | [[NCI-H23 (line)]] (-15.7), [[HT-29 (line)]] (-13.5), [[A-427 (line)]] (-11.9), [[SK-MEL-2 (line)]] (-10.8), [[SW 900 (line)]] (-10.0) | [[COLO 205 (line)]] (1.22), [[MIA PaCa-2 (line)]] (1.20), [[NCI-H1573 (line)]] (1.17), [[Panc 03.27 (line)]] (1.17) · weakest: [[NCI-H2122 (line)]] (0.570), [[C32 (line)]] (0.744), [[NCI-H661 (line)]] (0.788) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[PH-797804 (drug)]] (+0.91, Other MAPK inhibitor); [[Lonafarnib (drug)]] (+0.36, RAS inhibitor, ⚠ vector dose flagged: toxic); [[Sonidegib (drug)]] (+0.30, Sonic inhibitor); [[Darinaparsin (drug)]] (+0.27, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Sulfatinib (drug)]] (+0.26, Multi-TK inhibitor); [[Omeprazole (drug)]] (+0.24, unclear); [[Glasdegib (drug)]] (+0.24, Sonic inhibitor, ⚠ only 4 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Pralsetinib (drug)]] (+0.24, Other TK inhibitor); [[BI-78D3 (drug)]] (+0.23, Other MAPK inhibitor); [[Carbamazepine (drug)]] (+0.23, HDAC inhibitor); [[ERK5-IN-2 (drug)]] (+0.22, Other MAPK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[FAM13A]] | 0.05 µM | B | FAM13A activity raises the cells' numbers under TAK-901 0.05 µM (protects the cells) | lines that do not express FAM13A (6) vs lines expressing it (42) | the lines without FAM13A: 0.69× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[SCAT1]] | 0.05 µM | B | SCAT1 activity raises the cells' numbers under TAK-901 0.05 µM (protects the cells) | lines that do not express SCAT1 (16) vs lines expressing it (32) | the lines without SCAT1: 0.84× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[SH3TC1]] | 0.05 µM | B | SH3TC1 activity raises the cells' numbers under TAK-901 0.05 µM (protects the cells) | lines that do not express SH3TC1 (10) vs lines expressing it (38) | the lines without SH3TC1: 0.78× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[APOL3]] | 0.05 µM | B | APOL3 activity raises the cells' numbers under TAK-901 0.05 µM (protects the cells) | lines that do not express APOL3 (14) vs lines expressing it (34) | the lines without APOL3: 0.80× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[STON2]] | 0.05 µM | B | STON2 activity raises the cells' numbers under TAK-901 0.05 µM (protects the cells) | lines that do not express STON2 (19) vs lines expressing it (29) | the lines without STON2: 0.83× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[ENSG00000253227]] | 0.05 µM | B | ENSG00000253227 activity raises the cells' numbers under TAK-901 0.05 µM (protects the cells) | lines that do not express ENSG00000253227 (18) vs lines expressing it (30) | the lines without ENSG00000253227: 0.83× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: COL16A1, SERPINE2, SLCO2B1; maybe low, not absent |
| [[SLC2A9]] | 0.05 µM | B | SLC2A9 activity raises the cells' numbers under TAK-901 0.05 µM (protects the cells) | lines that do not express SLC2A9 (6) vs lines expressing it (42) | the lines without SLC2A9: 0.84× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[TFF1]] | 0.05 µM | B | TFF1 activity raises the cells' numbers under TAK-901 0.05 µM (protects the cells) | lines that do not express TFF1 (31) vs lines expressing it (17) | the lines without TFF1: 0.83× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC |
| [[MGST2]] | 5 µM | B | MGST2 activity raises the cells' numbers under TAK-901 5 µM (protects the cells) | lines that do not express MGST2 (10) vs lines expressing it (38) | the lines without MGST2: 0.49× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| [[DIRC3]] | 0.05 µM | B | DIRC3 activity raises the cells' numbers under TAK-901 0.05 µM (protects the cells) | lines that do not express DIRC3 (19) vs lines expressing it (29) | the lines without DIRC3: 0.84× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: CD200, MSC, TNS1; maybe low, not absent |
| [[MANSC1]] | 0.05 µM | B | MANSC1 activity raises the cells' numbers under TAK-901 0.05 µM (protects the cells) | lines that do not express MANSC1 (16) vs lines expressing it (32) | the lines without MANSC1: 0.88× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: ENSG00000288656, MYO5C, EVPL; maybe low, not absent |
| [[PRRG1]] | 0.05 µM | C | PRRG1 activity raises the cells' numbers under TAK-901 0.05 µM (protects the cells) | lines that do not express PRRG1 (3) vs lines expressing it (45) | the lines without PRRG1: 0.70× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "TAK-901"
- `tables/drugdoses.parquet` — dd in 976, 977, 978
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

---
drug: "palbociclib"
type: "drug"
salt_base: "palbociclib"
targets: "CDK4, CDK6"
moa_fine: "CDK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 281
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# palbociclib

*CDK inhibitor (inhibitor/antagonist) · targets: CDK4, CDK6 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 80 / 281 / 147; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.30 / -0.10.
> Flags by dose: - / cell-cycle shift; noisy plate (z scaled) / noisy plate (z scaled). ⚠ 0.5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:A12 | 41 / 39 | — | -0.53 | -1.0/-0.6/+2.3 | — |
| 0.5 µM | [[Plate 02]]:A12 | 35 / 246 | — | +0.07 | -5.9/-4.1/-1.2 | ⚠ cell-cycle shift · noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:A12 | 18 / 129 | — | +0.02 | -3.9/-2.5/+0.5 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (41 genes, none with an alert; 12 shown): [[SERPINE1]] 1.53× (z +4.0, 18/21 lines), [[TNIP3]] 1.56× (z +4.0, 1/13 lines), [[VPS16]] 1.28× (z +3.9, 7/47 lines), [[HSPA4]] 1.23× (z +3.8, 23/48 lines), [[LINC01819]] 1.73× (z +3.8, 0/12 lines), [[HCG20]] 1.45× (z +3.6, 5/41 lines), [[TIMM22]] 1.31× (z +3.6, 8/45 lines), [[PNPLA4]] 1.57× (z +3.5, 3/35 lines), [[ENSG00000273489]] 1.47× (z +3.5, 3/29 lines), [[ENSG00000275016]] 1.74× (z +3.4, 0/3 lines), [[THY1]] 1.78× (z +3.3, 2/9 lines), [[FUNDC1]] 1.34× (z +3.3, 10/45 lines)

**0.5 µM** (35 genes, 18 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 18 shown): [[ARHGAP12]] 1.30× (z +4.0, 29/48 lines; cell-cycle shift (explains ~6% here)), [[IGF2BP2]] ⚠ 1.21× (z +4.0, 18/45 lines; cell-cycle shift, explains ~31% of this change), [[ZNF292]] ⚠ 1.29× (z +3.9, 32/48 lines; cell-cycle shift, explains ~29% of this change), [[KDM7A]] ⚠ 1.43× (z +3.8, 29/47 lines; cell-cycle shift, explains ~30% of this change), [[FYN]] 1.26× (z +3.7, 18/40 lines; cell-cycle shift (explains ~1% here)), [[ESYT2]] ⚠ 1.37× (z +3.6, 35/48 lines; cell-cycle shift, explains ~31% of this change), [[MLF1]] 1.81× (z +3.5, 25/43 lines; cell-cycle shift (explains ~0% here)), [[PTCH1]] 1.37× (z +3.5, 4/46 lines; cell-cycle shift (explains ~7% here)), [[SLCO5A1]] 1.39× (z +3.4, 3/41 lines; cell-cycle shift (explains ~0% here)), [[SLC9A7]] 1.28× (z +3.4, 11/47 lines; cell-cycle shift (explains ~0% here)), [[FAM13A]] ⚠ 1.41× (z +3.4, 24/42 lines; cell-cycle shift, explains ~38% of this change), [[PARP8]] ⚠ 1.26× (z +3.4, 16/42 lines; cell-cycle shift, explains ~28% of this change), [[HERC3]] 1.52× (z +3.4, 26/46 lines; cell-cycle shift (explains ~8% here)), [[EOGT]] 1.31× (z +3.3, 4/47 lines; cell-cycle shift (explains ~12% here)), [[FAM107B]] 1.24× (z +3.3, 13/37 lines; cell-cycle shift (explains ~0% here)), [[RFX2]] 1.47× (z +3.2, 15/47 lines; cell-cycle shift (explains ~0% here)), [[KDM5B]] 1.24× (z +3.1, 25/48 lines; cell-cycle shift (explains ~0% here)), [[FEM1C]] 1.44× (z +3.1, 24/48 lines; cell-cycle shift (explains ~8% here))

**5 µM** (18 genes, none with an alert; 12 shown): [[IFIT2]] 2.24× (z +3.5, 10/39 lines), [[DMD]] 1.41× (z +3.3, 3/26 lines), [[AGPAT1]] 1.61× (z +3.3, 5/46 lines), [[GBP1]] 1.95× (z +3.2, 12/31 lines), [[APOL6]] 1.42× (z +3.2, 10/41 lines), [[PLAAT4]] 2.19× (z +3.1, 4/21 lines), [[IFI35]] 1.86× (z +3.1, 7/39 lines), [[SNAP23]] 1.24× (z +3.0, 7/47 lines), [[PROM1]] 1.71× (z +3.0, 2/11 lines), [[ETFRF1]] 1.43× (z +3.0, 3/44 lines), [[LINC01186]] 1.51× (z +2.9, 0/30 lines), [[TRIM22]] 1.81× (z +2.9, 4/30 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (39 genes, none with an alert; 12 shown): [[DIAPH3]] 0.768× (z -5.3, 29/45 lines), [[CIT]] 0.769× (z -4.1, 25/47 lines), [[POLQ]] 0.757× (z -4.0, 18/46 lines), [[PLK4]] 0.764× (z -4.0, 13/48 lines), [[ENSG00000291201]] 0.707× (z -4.0, 14/44 lines), [[RFC3]] 0.812× (z -3.9, 20/47 lines), [[NEIL3]] 0.705× (z -3.7, 17/45 lines), [[ENSG00000272840]] 0.730× (z -3.6, 10/31 lines), [[POLE]] 0.778× (z -3.6, 15/48 lines), [[ENSG00000254692]] 0.808× (z -3.6, 7/46 lines), [[ENSG00000197332]] 0.786× (z -3.6, 9/42 lines), [[ZNF71]] 0.755× (z -3.6, 8/31 lines)

**0.5 µM** (246 genes, 225 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 23 shown): [[DIAPH3]] ⚠ 0.550× (z -9.1, 33/45 lines; cell-cycle shift, explains ~45% of this change), [[SPC25]] ⚠ 0.464× (z -8.0, 35/47 lines; cell-cycle shift, explains ~47% of this change), [[EXO1]] ⚠ 0.448× (z -7.0, 30/46 lines; cell-cycle shift, explains ~61% of this change), [[FANCD2]] ⚠ 0.583× (z -7.0, 29/47 lines; cell-cycle shift, explains ~47% of this change), [[MIR924HG]] ⚠ 0.457× (z -6.9, 29/40 lines; cell-cycle shift, explains ~36% of this change), [[CENPK]] ⚠ 0.577× (z -6.9, 30/46 lines; cell-cycle shift, explains ~53% of this change), [[WDR76]] ⚠ 0.536× (z -6.5, 25/46 lines; cell-cycle shift, explains ~72% of this change), [[BLM]] ⚠ 0.592× (z -6.5, 30/46 lines; cell-cycle shift, explains ~74% of this change), [[ENSG00000229983]] 0.330× (z -6.4, 24/42 lines; cell-cycle shift (explains ~17% here)), [[ATAD5]] ⚠ 0.610× (z -6.4, 30/48 lines; cell-cycle shift, explains ~62% of this change), [[CLSPN]] ⚠ 0.377× (z -6.3, 34/44 lines; cell-cycle shift, explains ~69% of this change), [[FAM111B]] ⚠ 0.362× (z -6.3, 27/37 lines; cell-cycle shift, explains ~73% of this change), [[ENSG00000227598]] 0.621× (z -5.3, 21/48 lines; cell-cycle shift (explains ~25% here)), [[GPR19]] 0.483× (z -5.1, 12/41 lines; cell-cycle shift (explains ~22% here)), [[ENSG00000287022]] 0.385× (z -4.3, 22/44 lines; cell-cycle shift (explains ~17% here)), [[ZNF519]] 0.702× (z -4.1, 11/46 lines; cell-cycle shift (explains ~20% here)), [[DCLRE1C]] 0.783× (z -3.8, 11/48 lines; cell-cycle shift (explains ~2% here)), [[DDX11-AS1]] 0.608× (z -3.8, 9/45 lines; cell-cycle shift (explains ~5% here)), [[C10orf88B]] 0.629× (z -3.7, 11/37 lines; cell-cycle shift (explains ~23% here)), [[HELLPAR]] 0.661× (z -3.4, 17/48 lines; cell-cycle shift (explains ~21% here)), [[UPF3A]] 0.786× (z -3.4, 5/48 lines; cell-cycle shift (explains ~10% here)), [[BRME1]] 0.612× (z -3.2, 3/40 lines; cell-cycle shift (explains ~10% here)), [[CSTF3-DT]] 0.654× (z -3.2, 7/45 lines; cell-cycle shift (explains ~23% here))

**5 µM** (129 genes, none with an alert; 12 shown): [[DIAPH3]] 0.493× (z -7.9, 35/45 lines), [[BLM]] 0.498× (z -6.4, 24/45 lines), [[MELK]] 0.483× (z -6.0, 26/44 lines), [[CDC45]] 0.443× (z -5.4, 19/41 lines), [[NCAPG2]] 0.575× (z -5.1, 33/47 lines), [[EXO1]] 0.472× (z -5.1, 22/44 lines), [[E2F7]] 0.546× (z -5.1, 20/43 lines), [[NSD2]] 0.711× (z -5.1, 25/48 lines), [[POLQ]] 0.540× (z -4.9, 26/45 lines), [[WDHD1]] 0.629× (z -4.8, 17/47 lines), [[ZGRF1]] 0.640× (z -4.7, 15/47 lines), [[CIT]] 0.585× (z -4.7, 26/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Module 006]] (-3.3), [[Module 091]] (-2.3), [[Module 022]] (-2.3) |
| 5 µM | — | [[Module 006]] (-2.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1271 (line)]] (1.43), [[SW 1088 (line)]] (1.42), [[H4 (line)]] (1.27), [[MIA PaCa-2 (line)]] (1.17) · weakest: [[CFPAC-1 (line)]] (0.407), [[NCI-H1792 (line)]] (0.492), [[SK-MEL-2 (line)]] (0.503) |
| 0.5 µM | — | [[COLO 205 (line)]] (1.76), [[KATO III (line)]] (1.73), [[HT-29 (line)]] (1.62), [[LS 180 (line)]] (1.58) · weakest: [[J82 (line)]] (0.0909), [[C-33 A (line)]] (0.130), [[SHP-77 (line)]] (0.173) |
| 5 µM | [[CHP-212 (line)]] (-4.7), [[MIA PaCa-2 (line)]] (-3.5) | [[KATO III (line)]] (1.85), [[SW480 (line)]] (1.78), [[A-427 (line)]] (1.65), [[H4 (line)]] (1.47) · weakest: [[J82 (line)]] (0.216), [[C-33 A (line)]] (0.276), [[SHP-77 (line)]] (0.284) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Cloxacillin (sodium) (drug)]] (+0.61, unclear); [[Lapatinib ditosylate (drug)]] (+0.61, EGFR/ERBB inhibitor, ⚠ only 9 significant genes); [[Ranolazine (drug)]] (+0.54, unclear); [[Pravastatin (sodium) (drug)]] (+0.49, unclear); [[Artesunate (drug)]] (+0.47, JAK/STAT inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Daidzin (drug)]] (+0.46, unclear, ⚠ only 3 significant genes); [[Goserelin (acetate) (drug)]] (+0.45, unclear); [[Terfenadine (drug)]] (+0.45, unclear); [[Clopidogrel (drug)]] (+0.45, unclear); [[Captopril (drug)]] (+0.44, unclear); [[Dimethyl fumarate (drug)]] (+0.43, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[STEAP1]] | 5 µM | B | STEAP1 activity raises the cells' numbers under palbociclib 5 µM (protects the cells) | lines that do not express STEAP1 (11) vs lines expressing it (37) | the lines without STEAP1: 0.81× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: STEAP2-AS1, STEAP2 |
| [[TRPS1]] | 5 µM | B | TRPS1 activity raises the cells' numbers under palbociclib 5 µM (protects the cells) | lines that do not express TRPS1 (14) vs lines expressing it (34) | the lines without TRPS1: 0.87× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, FBXO32, PRDM1 |
| [[DUSP23]] | 5 µM | B | DUSP23 activity raises the cells' numbers under palbociclib 5 µM (protects the cells) | lines that do not express DUSP23 (14) vs lines expressing it (34) | the lines without DUSP23: 0.80× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: HLA-F, SH2D4A, RARRES1 |
| [[SDC3]] | 5 µM | C | SDC3 activity raises the cells' numbers under palbociclib 5 µM (protects the cells) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 0.69× the cells of the other lines | 0.022 | ⚠ few lines (4 vs 46); across organs |
| [[DDX1]] | 5 µM | C | DDX1's natural level lowers the cells' numbers under palbociclib 5 µM (makes them more sensitive) | DDX1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.268 over the table, 0.024 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ENSG00000234185]] | 5 µM | C | ENSG00000234185's natural level lowers the cells' numbers under palbociclib 5 µM (makes them more sensitive) | ENSG00000234185's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.268 over the table, 0.024 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[MLLT1]] | 5 µM | C | MLLT1's natural level lowers the cells' numbers under palbociclib 5 µM (makes them more sensitive) | MLLT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.361 over the table, 0.070 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[DOCK6]] | 5 µM | C | DOCK6's natural level lowers the cells' numbers under palbociclib 5 µM (makes them more sensitive) | DOCK6's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.361 over the table, 0.070 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "palbociclib"
- `tables/drugdoses.parquet` — dd in 1120, 1121, 1122
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

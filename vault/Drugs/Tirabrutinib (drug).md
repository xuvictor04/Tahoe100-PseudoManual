---
drug: "Tirabrutinib"
type: "drug"
salt_base: "Tirabrutinib"
targets: "BTK"
moa_fine: "Other TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 50
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Tirabrutinib

*Other TK inhibitor (inhibitor/antagonist) · targets: BTK · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 17 / 50 / 4; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.12 / 0.09.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:C9 | 0 / 17 | — | +0.62 | -0.5/-1.0/-1.4 | — |
| 0.5 µM | [[Plate 08]]:C9 | 13 / 37 | — | +0.38 | +0.1/-0.4/-1.8 | — |
| 5 µM | [[Plate 09]]:C9 | 1 / 3 | — | +0.78 | -1.0/+0.1/-0.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (13 genes, none with an alert; 12 shown): [[ST3GAL1]] 1.24× (z +4.3, 15/37 lines), [[FHL2]] 1.21× (z +3.5, 20/44 lines), [[TMEM45A]] 1.31× (z +3.4, 12/35 lines), [[NR2F2-AS1]] 1.32× (z +3.2, 19/40 lines), [[SYTL3]] 1.22× (z +3.2, 9/39 lines), [[EDA]] 1.22× (z +3.1, 4/35 lines), [[WWOX]] 1.28× (z +3.1, 22/43 lines), [[ENSG00000239498]] 1.35× (z +3.1, 4/27 lines), [[ENC1]] 1.37× (z +3.1, 16/43 lines), [[TIAM1]] 1.20× (z +3.0, 5/37 lines), [[ENSG00000284879]] 1.27× (z +2.9, 6/45 lines), [[CYTOR]] 1.24× (z +2.8, 18/46 lines)

**5 µM** (1 gene, none with an alert): [[DHRS3]] 1.22× (z +3.2, 10/35 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (17 genes, none with an alert; 12 shown): [[UTY]] 0.772× (z -4.1, 0/17 lines), [[LINC02864]] 0.715× (z -4.0, 0/12 lines), [[ENSG00000287069]] 0.678× (z -3.8, 1/7 lines), [[PROM1]] 0.718× (z -3.7, 0/11 lines), [[MIR493HG]] 0.457× (z -3.6, 1/11 lines), [[THOC3]] 0.768× (z -3.6, 7/48 lines), [[AJAP1]] 0.614× (z -3.5, 0/7 lines), [[LINC02476]] 0.698× (z -3.5, 0/8 lines), [[BAALC]] 0.631× (z -3.4, 1/13 lines), [[PTPRO]] 0.729× (z -3.4, 6/44 lines), [[EDAR]] 0.670× (z -3.3, 0/12 lines), [[LINC01611]] 0.711× (z -3.2, 0/13 lines)

**0.5 µM** (37 genes, none with an alert; 12 shown): [[RAB21]] 0.791× (z -4.7, 26/48 lines), [[LINC02680]] 0.649× (z -3.9, 27/48 lines), [[TDG]] 0.828× (z -3.8, 13/48 lines), [[LRRFIP2]] 0.827× (z -3.7, 23/48 lines), [[BAG4]] 0.815× (z -3.7, 14/48 lines), [[RCHY1]] 0.776× (z -3.6, 14/48 lines), [[RHEBL1]] 0.619× (z -3.5, 13/46 lines), [[C16orf87]] 0.755× (z -3.5, 16/48 lines), [[HSPA5]] 0.677× (z -3.5, 37/48 lines), [[IARS1]] 0.801× (z -3.5, 26/48 lines), [[GOLGA4]] 0.807× (z -3.4, 27/48 lines), [[PSMD14]] 0.790× (z -3.4, 27/48 lines)

**5 µM** (3 genes, none with an alert): [[PDC-AS1]] 0.673× (z -4.4, 19/48 lines), [[RHOH]] 0.692× (z -3.2, 4/22 lines), [[SMCO2]] 0.705× (z -3.1, 2/36 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 048]] (-2.3) |
| 0.5 µM | — | [[Module 182]] (-2.6) |
| 5 µM | [[Module 207]] (+2.0) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[HEC-1-A (line)]] (-3.5) | [[SW 1088 (line)]] (1.80), [[LS 180 (line)]] (1.42), [[NCI-H1792 (line)]] (1.38), [[HOP62 (line)]] (1.33) · weakest: [[BT-474 (line)]] (-0.0547), [[AN3 CA (line)]] (0.156), [[SHP-77 (line)]] (0.270) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Diphenhydramine (drug)]] (+0.93, unclear); [[Apalutamide (drug)]] (+0.89, Androgen receptor antagonist); [[Esmolol (hydrochloride) (drug)]] (+0.89, unclear); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.81, unclear); [[Estrone sulfate (potassium) (drug)]] (+0.80, unclear); [[Mifepristone (drug)]] (+0.79, unclear); [[Busulfan (drug)]] (+0.78, DNA synthesis/repair inhibitor); [[Larotrectinib (drug)]] (+0.76, Other TK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 25 arrows, 25 of them with an alert ⚠; grade A 0, B 19, C 6. Shown: the 15 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ANKRD22]] | 0.5 µM | B | ANKRD22 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express ANKRD22 (34) vs lines expressing it (14) | the lines without ANKRD22: 1.19× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[TMEM30B]] | 0.5 µM | B | TMEM30B activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express TMEM30B (35) vs lines expressing it (13) | the lines without TMEM30B: 1.18× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[COL17A1]] | 0.5 µM | B | COL17A1 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express COL17A1 (34) vs lines expressing it (14) | the lines without COL17A1: 1.18× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[ATP2C2]] | 0.5 µM | B | ATP2C2 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express ATP2C2 (32) vs lines expressing it (16) | the lines without ATP2C2: 1.23× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[SERPINB5]] | 0.5 µM | B | SERPINB5 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express SERPINB5 (34) vs lines expressing it (14) | the lines without SERPINB5: 1.19× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[SLC5A1]] | 0.5 µM | B | SLC5A1 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express SLC5A1 (36) vs lines expressing it (12) | the lines without SLC5A1: 1.19× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[LINC02257]] | 0.5 µM | B | LINC02257 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express LINC02257 (15) vs lines expressing it (33) | the lines without LINC02257: 1.11× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: CTSS, PAG1, ZNF365; maybe low, not absent |
| [[ENSG00000262302]] | 0.5 µM | B | ENSG00000262302 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000262302 (29) vs lines expressing it (19) | the lines without ENSG00000262302: 1.22× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: CLDN7, ESRP1, ATP2C2; maybe low, not absent |
| [[CLIC5]] | 0.5 µM | B | CLIC5 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express CLIC5 (37) vs lines expressing it (11) | the lines without CLIC5: 1.21× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[VIPR1]] | 0.5 µM | B | VIPR1 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express VIPR1 (24) vs lines expressing it (24) | the lines without VIPR1: 1.20× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| [[MEIS3]] | 0.5 µM | B | MEIS3 activity raises the cells' numbers under Tirabrutinib 0.5 µM (protects the cells) | lines that do not express MEIS3 (12) vs lines expressing it (36) | the lines without MEIS3: 0.91× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: PARVG, HECW2, RFLNB |
| [[DAPP1]] | 0.5 µM | B | DAPP1 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express DAPP1 (39) vs lines expressing it (9) | the lines without DAPP1: 1.17× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[VWA2]] | 0.5 µM | B | VWA2 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express VWA2 (36) vs lines expressing it (12) | the lines without VWA2: 1.21× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC01559, SLC5A1, SKAP1 |
| [[KRT16]] | 0.5 µM | B | KRT16 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express KRT16 (27) vs lines expressing it (21) | the lines without KRT16: 1.16× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[DPP4]] | 0.5 µM | B | DPP4 activity lowers the cells' numbers under Tirabrutinib 0.5 µM (makes them more sensitive) | lines that do not express DPP4 (29) vs lines expressing it (19) | the lines without DPP4: 1.17× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Tirabrutinib"
- `tables/drugdoses.parquet` — dd in 1006, 1007, 1008
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

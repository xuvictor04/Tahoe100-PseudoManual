---
drug: "Tirabrutinib (hydrochloride)"
type: "drug"
salt_base: "Tirabrutinib"
targets: "BTK"
moa_fine: "Other TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 98
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Tirabrutinib (hydrochloride)

*Other TK inhibitor (inhibitor/antagonist) · targets: BTK · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 12 / 98 / 10; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.03 / 0.24.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:B3 | 3 / 9 | — | +0.68 | +0.6/+1.7/+1.0 | — |
| 0.5 µM | [[Plate 11]]:B3 | 32 / 66 | — | +0.44 | -2.4/-0.9/-3.1 | — |
| 5 µM | [[Plate 12]]:B3 | 4 / 6 | — | +0.11 | +0.0/+0.5/+0.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[ARID3A]] 1.32× (z +3.5, 36/49 lines), [[ENSG00000285827]] 1.23× (z +3.3, 12/49 lines), [[CFAP210]] 1.80× (z +3.2, 9/46 lines)

**0.5 µM** (32 genes, 1 with an alert ⚠; 13 shown): [[DHRS3]] ⚠ 1.38× (z +5.3, 28/35 lines; position correction uncertain), [[ZNF791]] 1.29× (z +4.4, 27/48 lines), [[TMUB2]] 1.27× (z +4.4, 7/47 lines), [[RAP2B]] 1.25× (z +4.1, 16/45 lines), [[NADK2]] 1.25× (z +3.8, 12/48 lines), [[UBE2Q2P1]] 1.30× (z +3.8, 8/46 lines), [[VPS54]] 1.20× (z +3.7, 23/48 lines), [[CLMN]] 1.22× (z +3.6, 17/41 lines), [[FBXO8]] 1.29× (z +3.6, 7/48 lines), [[PNMA2]] 1.27× (z +3.6, 7/31 lines), [[ZNF776]] 1.32× (z +3.5, 3/48 lines), [[TRIM32]] 1.34× (z +3.5, 8/47 lines), [[ATG16L2]] 1.23× (z +3.4, 5/48 lines)

**5 µM** (4 genes, 1 with an alert ⚠): [[DHRS3]] ⚠ 1.43× (z +5.9, 30/35 lines; position correction uncertain), [[ZNF791]] 1.25× (z +3.9, 23/48 lines), [[ARID3A]] 1.31× (z +3.4, 26/48 lines), [[TCTA]] 1.22× (z +2.6, 2/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (9 genes, none with an alert): [[AOC2]] 0.609× (z -4.4, 8/45 lines), [[ENSG00000254979]] 0.633× (z -4.0, 5/24 lines), [[SRSF1]] 0.759× (z -3.7, 37/49 lines), [[ENSG00000291171]] 0.760× (z -3.5, 15/48 lines), [[LINC01798]] 0.634× (z -3.5, 6/30 lines), [[ENSG00000286563]] 0.669× (z -3.5, 9/46 lines), [[TXNDC5]] 0.757× (z -3.3, 24/48 lines), [[PIGL]] 0.817× (z -3.3, 12/48 lines), [[SLC25A19]] 0.797× (z -3.2, 6/47 lines)

**0.5 µM** (66 genes, 1 with an alert ⚠; 12 shown): [[LINC02934]] 0.604× (z -4.7, 19/40 lines), [[SNHG1]] 0.615× (z -4.7, 35/48 lines), [[PACC1]] 0.772× (z -4.5, 10/47 lines), [[SRSF1]] 0.719× (z -4.4, 36/48 lines), [[PDC-AS1]] 0.682× (z -4.2, 17/48 lines), [[COLEC12]] 0.636× (z -4.1, 2/20 lines), [[RBM27]] 0.813× (z -4.1, 25/48 lines), [[LUC7L3]] 0.800× (z -4.1, 32/48 lines), [[DDX46]] 0.823× (z -4.0, 28/48 lines), [[CXCL3]] 0.522× (z -3.9, 20/34 lines), [[RBM17]] 0.809× (z -3.9, 24/48 lines), [[AOC2]] 0.646× (z -3.9, 9/46 lines)

**5 µM** (6 genes, none with an alert): [[CREB5]] 0.754× (z -5.0, 22/33 lines), [[TARDBP]] 0.802× (z -4.1, 28/48 lines), [[KBTBD8]] 0.654× (z -3.9, 6/41 lines), [[TXNDC5]] 0.735× (z -3.7, 33/48 lines), [[PTDSS1]] 0.817× (z -3.5, 10/48 lines), [[SRSF1]] 0.789× (z -3.2, 30/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 170]] (+2.6) | [[Module 043]] (-2.1) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[SW 1271 (line)]] (1.40), [[RPMI-7951 (line)]] (1.39), [[SW 1088 (line)]] (1.33), [[SNU-423 (line)]] (1.32) · weakest: [[SHP-77 (line)]] (0.493), [[HepG2_C3A (line)]] (0.590), [[AN3 CA (line)]] (0.644) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[LB-100 (drug)]] (+0.58, unclear, ⚠ only 5 significant genes); [[Delamanid (drug)]] (+0.57, unclear, ⚠ only 6 significant genes); [[Lucanthone (drug)]] (+0.56, unclear); [[Rutin (trihydrate) (drug)]] (+0.56, unclear); [[Relugolix (drug)]] (+0.53, unclear, ⚠ only 5 significant genes); [[Lumateperone (tosylate) (drug)]] (+0.51, unclear, ⚠ only 9 significant genes); [[Posaconazole (drug)]] (+0.51, unclear); [[Daidzin (drug)]] (+0.51, unclear, ⚠ only 3 significant genes); [[Pexidartinib (hydrochloride) (drug)]] (+0.50, Multi-TK inhibitor); [[Asciminib (drug)]] (+0.47, Other TK inhibitor); [[Sinomenine (drug)]] (+0.46, unclear); [[Fenofibrate (drug)]] (+0.43, unclear); [[Quinestrol (drug)]] (+0.43, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 38 arrows, 38 of them with an alert ⚠; grade A 0, B 22, C 16. Shown: the 15 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SRPX]] | 0.05 µM | B | SRPX activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express SRPX (22) vs lines expressing it (26) | the lines without SRPX: 0.85× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[HTRA1]] | 0.05 µM | B | HTRA1 activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express HTRA1 (19) vs lines expressing it (29) | the lines without HTRA1: 0.84× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| [[KCNMA1]] | 0.05 µM | B | KCNMA1 activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.83× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[MYH14]] | 0.05 µM | B | MYH14 activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 1.21× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[PRSS23]] | 0.5 µM | B | PRSS23 activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express PRSS23 (13) vs lines expressing it (35) | the lines without PRSS23: 1.36× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[DNAH11]] | 0.5 µM | B | DNAH11 activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express DNAH11 (23) vs lines expressing it (25) | the lines without DNAH11: 1.20× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[SYTL2]] | 0.5 µM | B | SYTL2 activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SYTL2 (7) vs lines expressing it (41) | the lines without SYTL2: 1.23× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: ATXN1, SAMSN1, IFIT2; maybe low, not absent |
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[CXCL3]] | 0.5 µM | B | CXCL3 activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express CXCL3 (14) vs lines expressing it (34) | the lines without CXCL3: 1.35× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[LINC02257]] | 0.5 µM | B | LINC02257 activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express LINC02257 (15) vs lines expressing it (33) | the lines without LINC02257: 1.25× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: CTSS, PAG1, ZNF365; maybe low, not absent |
| [[PTPRG]] | 0.05 µM | B | PTPRG activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express PTPRG (8) vs lines expressing it (40) | the lines without PTPRG: 0.83× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines |
| [[PCED1B]] | 0.5 µM | B | PCED1B activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express PCED1B (11) vs lines expressing it (37) | the lines without PCED1B: 1.39× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[ZNF860]] | 0.05 µM | B | ZNF860 activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express ZNF860 (16) vs lines expressing it (32) | the lines without ZNF860: 1.16× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[SIRLNT]] | 0.05 µM | B | SIRLNT activity raises the cells' numbers under Tirabrutinib (hydrochloride) 0.05 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.83× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[PTGR1]] | 0.5 µM | B | PTGR1 activity lowers the cells' numbers under Tirabrutinib (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express PTGR1 (8) vs lines expressing it (40) | the lines without PTGR1: 1.42× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: ANXA2, ZNF717 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Tirabrutinib (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 1009, 1010, 1011
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

---
drug: "ERK5-IN-2"
type: "drug"
salt_base: "ERK5-IN-2"
targets: "MAPK7"
moa_fine: "Other MAPK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 149
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# ERK5-IN-2

*Other MAPK inhibitor (inhibitor/antagonist) · targets: MAPK7 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 7 / 149; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.29 / -0.40.
> Flags by dose: - / low cells (technical?); plate-row cell shift; noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:D3 | 2 / 0 | — | +0.01 | +0.0/-0.3/-0.1 | — |
| 0.5 µM | [[Plate 02]]:D3 | 5 / 2 | — | -1.40 | +0.4/+0.8/+1.6 | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:D3 | 120 / 29 | — | +1.44 | -0.5/+0.0/-0.9 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[MOK]] 1.25× (z +3.0, 7/48 lines), [[HSPE1-MOB4]] 1.57× (z +2.8, 3/43 lines)

**0.5 µM** (5 genes, none with an alert): [[SUPT7L]] 1.26× (z +3.4, 6/47 lines), [[LRRK2]] 1.58× (z +3.1, 0/20 lines), [[THUMPD3]] 1.20× (z +3.0, 4/47 lines), [[LINC01518]] 1.56× (z +2.8, 0/11 lines), [[IKZF3]] 1.41× (z +2.7, 0/15 lines)

**5 µM** (120 genes, none with an alert; 12 shown): [[MGC4859]] 3.80× (z +6.9, 16/38 lines), [[ENSG00000232884]] 2.96× (z +5.8, 16/32 lines), [[LINC01031]] 2.17× (z +5.2, 21/47 lines), [[ENSG00000272980]] 2.13× (z +5.1, 11/46 lines), [[STYK1]] 1.76× (z +4.9, 10/28 lines), [[CMYA5]] 2.22× (z +4.9, 18/46 lines), [[STPG4]] 2.27× (z +4.6, 23/46 lines), [[C1QTNF7-AS1]] 1.58× (z +4.6, 17/46 lines), [[TMEM161B-DT]] 1.54× (z +4.4, 27/49 lines), [[NUP210L]] 1.92× (z +4.3, 6/48 lines), [[PRPF3]] 1.70× (z +4.3, 29/49 lines), [[BAALC-AS1]] 2.07× (z +4.3, 13/45 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (2 genes, none with an alert): [[TRMT2B]] 0.782× (z -3.0, 6/47 lines), [[CA5BP1]] 0.781× (z -3.0, 6/46 lines)

**5 µM** (29 genes, none with an alert; 12 shown): [[HLA-E]] 0.603× (z -3.9, 28/48 lines), [[MAP1B]] 0.690× (z -3.8, 18/33 lines), [[MAP4]] 0.809× (z -3.7, 15/48 lines), [[SLC25A29]] 0.654× (z -3.6, 13/48 lines), [[HLA-F]] 0.570× (z -3.4, 11/38 lines), [[DNASE1L1]] 0.552× (z -3.4, 16/48 lines), [[MFHAS1]] 0.794× (z -3.4, 4/49 lines), [[MEGF6]] 0.631× (z -3.4, 3/37 lines), [[PFN2]] 0.608× (z -3.3, 17/44 lines), [[BOK]] 0.549× (z -3.3, 3/41 lines), [[PRKRA]] 0.744× (z -3.3, 9/49 lines), [[GALNT12]] 0.598× (z -3.3, 9/38 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 179]] (+2.1) | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 179]] (+2.5) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[A-172 (line)]] (-3.9), [[PANC-1 (line)]] (-3.2) | — |
| 5 µM | [[LOX-IMVI (line)]] (-4.7), [[A-427 (line)]] (-4.1) | [[Panc 03.27 (line)]] (1.44), [[HEC-1-A (line)]] (1.41), [[BT-474 (line)]] (1.40), [[HOP62 (line)]] (1.39) · weakest: [[SHP-77 (line)]] (0.418), [[CHP-212 (line)]] (0.424), [[NCI-H2122 (line)]] (0.453) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Paclitaxel (drug)]] (+0.64, Microtubule inhibitor, ⚠ only 3 significant genes); [[Pentagastrin (drug)]] (+0.63, unclear, ⚠ only 9 significant genes); [[Anethole trithione (drug)]] (+0.58, unclear); [[Dabrafenib (drug)]] (+0.55, RAF inhibitor); [[Benproperine (phosphate) (drug)]] (+0.53, unclear); [[Fenofibrate (drug)]] (+0.52, unclear); [[Cinacalcet (drug)]] (+0.49, unclear, ⚠ only 8 significant genes); [[Rutin (trihydrate) (drug)]] (+0.49, unclear); [[MK-8353 (drug)]] (+0.48, Other MAPK inhibitor); [[Tucatinib (drug)]] (+0.47, EGFR/ERBB inhibitor); [[Volasertib (drug)]] (+0.47, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 94 arrows, 94 of them with an alert ⚠; grade A 0, B 16, C 78. Shown: the 15 strongest; 79 more arrows (79 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[APOL3]] | 5 µM | B | APOL3 activity raises the cells' numbers under ERK5-IN-2 5 µM (protects the cells) | lines that do not express APOL3 (14) vs lines expressing it (34) | the lines without APOL3: 0.77× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[PLXNA2]] | 5 µM | B | PLXNA2 activity raises the cells' numbers under ERK5-IN-2 5 µM (protects the cells) | lines that do not express PLXNA2 (15) vs lines expressing it (33) | the lines without PLXNA2: 0.81× the cells of the other lines | 0.074 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[PIP5K1B]] | 0.5 µM | B | PIP5K1B activity raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | lines that do not express PIP5K1B (33) vs lines expressing it (15) | the lines without PIP5K1B: 0.83× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B |
| [[GJC1]] | 0.5 µM | B | GJC1 activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express GJC1 (13) vs lines expressing it (35) | the lines without GJC1: 1.21× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000267405, FHOD3, RIMKLB |
| [[MGC32805]] | 0.5 µM | B | MGC32805 activity raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | lines that do not express MGC32805 (32) vs lines expressing it (16) | the lines without MGC32805: 0.85× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: CEACAM5, ST18, PRR15L; maybe low, not absent |
| [[CACNG7]] | 0.5 µM | B | CACNG7 activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express CACNG7 (21) vs lines expressing it (27) | the lines without CACNG7: 1.21× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[DPP10]] | 0.5 µM | B | DPP10 activity raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | lines that do not express DPP10 (40) vs lines expressing it (8) | the lines without DPP10: 0.87× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent |
| [[SLC6A16]] | 0.5 µM | B | SLC6A16 activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express SLC6A16 (11) vs lines expressing it (37) | the lines without SLC6A16: 1.16× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, TEAD2, ZNF71; maybe low, not absent |
| [[RASGEF1B]] | 5 µM | B | RASGEF1B activity raises the cells' numbers under ERK5-IN-2 5 µM (protects the cells) | lines that do not express RASGEF1B (10) vs lines expressing it (38) | the lines without RASGEF1B: 0.75× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[TREM1]] | 5 µM | B | TREM1 activity raises the cells' numbers under ERK5-IN-2 5 µM (protects the cells) | lines that do not express TREM1 (25) vs lines expressing it (23) | the lines without TREM1: 0.85× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[DUSP10]] | 5 µM | B | DUSP10 activity raises the cells' numbers under ERK5-IN-2 5 µM (protects the cells) | lines that do not express DUSP10 (11) vs lines expressing it (37) | the lines without DUSP10: 0.80× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[ADGRD1]] | 0.5 µM | B | ADGRD1 activity raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | lines that do not express ADGRD1 (37) vs lines expressing it (11) | the lines without ADGRD1: 0.87× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, SLC15A5 |
| [[CAV2]], [[ENSG00000237813]] | 0.5 µM | B | CAV2, ENSG00000237813 activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express CAV2, ENSG00000237813 (8) vs lines expressing them (40) | the lines without CAV2, ENSG00000237813: 1.34× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: PLAUR, LRRK1, HRH1; maybe low, not absent; co-absent genes |
| [[ENSG00000285155]] | 0.5 µM | B | ENSG00000285155 activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000285155 (5) vs lines expressing it (43) | the lines without ENSG00000285155: 1.28× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A, TGFBR2, EP300; also absent: RBMS1, TBC1D9, TCEA2 |
| [[APOL6]] | 5 µM | B | APOL6 activity raises the cells' numbers under ERK5-IN-2 5 µM (protects the cells) | lines that do not express APOL6 (6) vs lines expressing it (42) | the lines without APOL6: 0.69× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "ERK5-IN-2"
- `tables/drugdoses.parquet` — dd in 386, 387, 388
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

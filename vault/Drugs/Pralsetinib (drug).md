---
drug: "Pralsetinib"
type: "drug"
salt_base: "Pralsetinib"
targets: "RET"
moa_fine: "Other TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 806
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Pralsetinib

*Other TK inhibitor (inhibitor/antagonist) · targets: RET · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 22 / 1 / 806; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.32 / 0.08.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:F6 | 22 / 0 | — | -0.05 | -0.2/+0.1/+0.3 | — |
| 0.5 µM | [[Plate 02]]:F6 | 1 / 0 | — | -0.48 | +0.1/+0.5/-0.2 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:F6 | 378 / 428 | — | -0.87 | +1.6/+0.2/+2.0 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (22 genes, none with an alert; 12 shown): [[FAM83B]] 1.29× (z +4.8, 1/19 lines), [[GLIPR1]] 1.40× (z +3.5, 4/28 lines), [[DLGAP1]] 1.23× (z +3.5, 4/42 lines), [[KIF5C]] 1.26× (z +3.5, 6/48 lines), [[LTO1]] 1.23× (z +3.4, 3/48 lines), [[ENSG00000266602]] 1.42× (z +3.4, 0/12 lines), [[CLDN10]] 1.58× (z +3.4, 0/33 lines), [[ENSG00000257869]] 1.41× (z +3.3, 0/12 lines), [[PPP1R9A-AS1]] 1.33× (z +3.3, 2/44 lines), [[ENSG00000285822]] 1.40× (z +3.3, 0/9 lines), [[TMEM266]] 1.34× (z +3.2, 1/42 lines), [[ZKSCAN7-AS1]] 1.35× (z +3.2, 3/47 lines)

**0.5 µM** (1 gene, none with an alert): [[RAB38]] 1.33× (z +2.8, 1/25 lines)

**5 µM** (378 genes, none with an alert; 12 shown): [[LTV1]] 1.76× (z +5.1, 26/48 lines), [[UTP25]] 1.52× (z +5.1, 20/46 lines), [[METTL1]] 2.11× (z +5.0, 6/32 lines), [[BOP1]] 2.41× (z +5.0, 17/37 lines), [[PINX1]] 1.69× (z +5.0, 11/44 lines), [[RIOX2]] 1.67× (z +4.9, 16/44 lines), [[INTS12]] 1.48× (z +4.9, 11/46 lines), [[UTP14A]] 1.68× (z +4.8, 25/47 lines), [[MRPL42]] 1.44× (z +4.8, 18/48 lines), [[SPG21]] 1.48× (z +4.8, 17/48 lines), [[MYBBP1A]] 1.84× (z +4.7, 16/44 lines), [[DHX33]] 1.49× (z +4.5, 9/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (428 genes, none with an alert; 12 shown): [[TXNIP]] 0.266× (z -9.0, 34/38 lines), [[ARRDC4]] 0.461× (z -6.3, 24/39 lines), [[LINC01031]] 0.418× (z -5.8, 26/42 lines), [[INTS6L]] 0.509× (z -5.3, 24/37 lines), [[TICAM2]] 0.532× (z -5.2, 21/47 lines), [[ASH1L]] 0.766× (z -5.2, 32/49 lines), [[TVP23C]] 0.637× (z -5.2, 28/47 lines), [[DCAF6]] 0.675× (z -5.1, 36/49 lines), [[ZDBF2]] 0.639× (z -5.1, 20/34 lines), [[ZNF404]] 0.550× (z -5.0, 15/30 lines), [[INTS6]] 0.533× (z -5.0, 38/49 lines), [[SLC2A1-DT]] 0.569× (z -5.0, 20/42 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 001]] (+2.8), [[Module 004]] (+2.3) | [[Module 179]] (-3.3), [[Module 207]] (-2.6), [[Module 234]] (-2.5) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[HCT15 (line)]] (1.35), [[SNU-1 (line)]] (1.35), [[RKO (line)]] (1.25), [[SW 1088 (line)]] (1.20) · weakest: [[NCI-H2122 (line)]] (-0.181), [[SK-MEL-2 (line)]] (-0.0695), [[SNU-423 (line)]] (0.207) |
| 0.5 µM | — | — |
| 5 µM | [[PANC-1 (line)]] (-5.5), [[NCI-H23 (line)]] (-5.4), [[NCI-H2030 (line)]] (-5.0), [[NCI-H1573 (line)]] (-4.5), [[MIA PaCa-2 (line)]] (-3.7) | [[SNU-423 (line)]] (1.44), [[NCI-H1792 (line)]] (1.43), [[C32 (line)]] (1.40), [[NCI-H1573 (line)]] (1.40) · weakest: [[SW1417 (line)]] (0.404), [[AN3 CA (line)]] (0.541), [[HepG2_C3A (line)]] (0.607) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Belumosudil (drug)]] (+0.80, unclear); [[Sonidegib (drug)]] (+0.63, Sonic inhibitor); [[Temuterkib (drug)]] (+0.50, Other MAPK inhibitor, ⚠ only 3 significant genes); [[Berbamine (drug)]] (+0.48, unclear); [[Adenine (drug)]] (+0.47, unclear); [[Lidocaine (hydrochloride) (drug)]] (+0.47, unclear); [[Benztropine (mesylate) (drug)]] (+0.45, unclear); [[Ataluren (drug)]] (+0.45, unclear, ⚠ only 7 significant genes); [[Retinoic acid (drug)]] (+0.43, Retinoic receptor agonist); [[Vitamin K4 (drug)]] (+0.42, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 38 arrows, 38 of them with an alert ⚠; grade A 0, B 33, C 5. Shown: the 15 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ATP1B1]] | 0.05 µM | B | ATP1B1 activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 1.29× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[ENSG00000251537]] | 0.05 µM | B | ENSG00000251537 activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000251537 (9) vs lines expressing it (39) | the lines without ENSG00000251537: 1.22× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: FBXW10B, PCED1B, NHS; maybe low, not absent |
| [[PYROXD2]] | 0.05 µM | B | PYROXD2 activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express PYROXD2 (7) vs lines expressing it (41) | the lines without PYROXD2: 1.31× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| [[DUSP10]] | 0.05 µM | B | DUSP10 activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express DUSP10 (11) vs lines expressing it (37) | the lines without DUSP10: 1.18× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[HIPK2]] | 0.05 µM | B | HIPK2 activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express HIPK2 (5) vs lines expressing it (43) | the lines without HIPK2: 1.36× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[FBXW10B]] | 0.05 µM | B | FBXW10B activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express FBXW10B (11) vs lines expressing it (37) | the lines without FBXW10B: 1.19× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[SNTG1]] | 5 µM | B | SNTG1 activity raises the cells' numbers under Pralsetinib 5 µM (protects the cells) | lines that do not express SNTG1 (38) vs lines expressing it (10) | the lines without SNTG1: 0.64× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[MSRB3-AS1]] | 0.05 µM | B | MSRB3-AS1 activity raises the cells' numbers under Pralsetinib 0.05 µM (protects the cells) | lines that do not express MSRB3-AS1 (42) vs lines expressing it (6) | the lines without MSRB3-AS1: 0.70× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2 |
| [[LGALS3BP]] | 0.05 µM | B | LGALS3BP activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 1.38× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[SLC2A9]] | 0.05 µM | B | SLC2A9 activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express SLC2A9 (6) vs lines expressing it (42) | the lines without SLC2A9: 1.34× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[IL15]] | 0.05 µM | B | IL15 activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 1.31× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[IRX2]] | 5 µM | B | IRX2 activity raises the cells' numbers under Pralsetinib 5 µM (protects the cells) | lines that do not express IRX2 (30) vs lines expressing it (18) | the lines without IRX2: 0.86× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000251652, NRK, HEPHL1 |
| [[ENPP2]] | 5 µM | B | ENPP2 activity raises the cells' numbers under Pralsetinib 5 µM (protects the cells) | lines that do not express ENPP2 (26) vs lines expressing it (22) | the lines without ENPP2: 0.71× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC16A6, ITGA4, SNTG1; maybe low, not absent |
| [[AQP3]] | 0.05 µM | B | AQP3 activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express AQP3 (19) vs lines expressing it (29) | the lines without AQP3: 1.23× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[ENSG00000286533]] | 0.05 µM | B | ENSG00000286533 activity lowers the cells' numbers under Pralsetinib 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000286533 (5) vs lines expressing it (43) | the lines without ENSG00000286533: 1.31× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: HIPK2, ZMIZ1, LGALS3BP; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Pralsetinib"
- `tables/drugdoses.parquet` — dd in 836, 837, 838
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

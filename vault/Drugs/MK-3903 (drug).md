---
drug: "MK-3903"
type: "drug"
salt_base: "MK-3903"
targets: "PRKAA1"
moa_fine: "unclear"
moa_broad: "activator/agonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 56
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# MK-3903

*unclear (activator/agonist) · targets: PRKAA1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 1 / 56; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.16 / 0.09.
> Flags by dose: - / plate-row cell shift; noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:E8 | 1 / 0 | — | -0.23 | -0.4/-0.5/-0.7 | — |
| 0.5 µM | [[Plate 02]]:E8 | 1 / 0 | — | -0.85 | +0.5/+1.1/+0.5 | plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:E8 | 39 / 17 | — | -0.22 | -1.5/-1.3/-1.8 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ZNF365]] 1.30× (z +2.8, 1/22 lines)

**0.5 µM** (1 gene, none with an alert): [[ZNF331]] 1.23× (z +3.0, 4/33 lines)

**5 µM** (39 genes, none with an alert; 12 shown): [[PKD1L2]] 2.19× (z +4.1, 6/25 lines), [[INSR]] 1.48× (z +3.8, 20/45 lines), [[FOXN3]] 1.36× (z +3.8, 11/46 lines), [[DHRSX]] 1.34× (z +3.7, 15/47 lines), [[ARHGEF28]] 1.54× (z +3.6, 18/42 lines), [[PKIG]] 1.36× (z +3.6, 8/42 lines), [[MEGF6]] 1.60× (z +3.4, 6/34 lines), [[ANKRD42-DT]] 1.40× (z +3.4, 4/46 lines), [[SLC49A4]] 1.43× (z +3.4, 11/48 lines), [[HDAC5]] 1.48× (z +3.3, 12/48 lines), [[SYT14]] 1.60× (z +3.3, 2/19 lines), [[TGFB2]] 1.46× (z +3.3, 4/32 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (17 genes, none with an alert; 12 shown): [[EFNB2]] 0.549× (z -4.0, 22/33 lines), [[EGR1]] 0.296× (z -4.0, 33/46 lines), [[LPIN1]] 0.739× (z -3.6, 11/48 lines), [[DHCR24]] 0.605× (z -3.4, 15/43 lines), [[FOSL1]] 0.520× (z -3.4, 26/43 lines), [[HOMER1]] 0.595× (z -3.3, 14/47 lines), [[LDLR]] 0.633× (z -3.3, 20/46 lines), [[ASPH]] 0.714× (z -3.3, 21/43 lines), [[EHD4]] 0.756× (z -3.1, 11/48 lines), [[EHD1]] 0.671× (z -3.0, 13/48 lines), [[PGK1]] 0.735× (z -3.0, 29/48 lines), [[RTN4]] 0.791× (z -3.0, 15/48 lines)

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
| 0.05 µM | [[LOX-IMVI (line)]] (-3.6), [[J82 (line)]] (-3.2) | — |
| 0.5 µM | — | — |
| 5 µM | [[COLO 205 (line)]] (-4.8), [[LoVo (line)]] (-3.8) | [[Hs 766T (line)]] (1.35), [[LS 180 (line)]] (1.34), [[AsPC-1 (line)]] (1.26), [[H4 (line)]] (1.25) · weakest: [[NCI-H23 (line)]] (0.514), [[hTERT-HPNE (line)]] (0.530), [[SNU-1 (line)]] (0.536) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Resveratrol (drug)]] (+0.78, unclear); [[AZD-8055 (drug)]] (+0.73, MTOR inhibitor); [[Temsirolimus (drug)]] (+0.72, MTOR inhibitor); [[Rapamycin (drug)]] (+0.72, MTOR inhibitor); [[AZD1390 (drug)]] (+0.66, unclear); [[IQ 1 (drug)]] (+0.63, unclear); [[ULK-101 (drug)]] (+0.63, unclear); [[Sunitinib (drug)]] (+0.58, Multi-TK inhibitor, ⚠ vector dose flagged: toxic); [[Bimiralisib (drug)]] (+0.55, PI3K/AKT inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 63 arrows, 63 of them with an alert ⚠; grade A 0, B 46, C 17. Shown: the 15 strongest; 48 more arrows (48 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[LGALS3BP]] | 0.05 µM | B | LGALS3BP activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 0.78× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[GPRC5D-AS1]] | 0.05 µM | B | GPRC5D-AS1 activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (43) | the lines without GPRC5D-AS1: 0.73× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| [[AHR]] | 0.05 µM | B | AHR activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 0.87× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[IL15]] | 0.05 µM | B | IL15 activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 0.83× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[ARHGAP30]] | 0.05 µM | B | ARHGAP30 activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express ARHGAP30 (22) vs lines expressing it (26) | the lines without ARHGAP30: 0.86× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[FBXW10B]] | 0.05 µM | B | FBXW10B activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express FBXW10B (11) vs lines expressing it (37) | the lines without FBXW10B: 0.90× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[RAB27B]] | 0.05 µM | B | RAB27B activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express RAB27B (15) vs lines expressing it (33) | the lines without RAB27B: 0.88× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[LTBR]] | 0.05 µM | B | LTBR activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express LTBR (8) vs lines expressing it (40) | the lines without LTBR: 0.90× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[INAVA]], [[MROH3P]] | 0.05 µM | B | INAVA, MROH3P activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express INAVA, MROH3P (29) vs lines expressing them (19) | the lines without INAVA, MROH3P: 0.85× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[NIPAL1]] | 0.05 µM | B | NIPAL1 activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express NIPAL1 (5) vs lines expressing it (43) | the lines without NIPAL1: 0.85× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC18B1, AHR, RALGPS2; maybe low, not absent |
| [[ENSG00000286533]] | 0.05 µM | B | ENSG00000286533 activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express ENSG00000286533 (5) vs lines expressing it (43) | the lines without ENSG00000286533: 0.81× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: HIPK2, ZMIZ1, LGALS3BP; maybe low, not absent |
| [[C1orf116]], [[IRF6]] | 0.05 µM | B | C1orf116, IRF6 activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (17) | the lines without C1orf116, IRF6: 0.85× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |
| [[RASGEF1B]] | 0.05 µM | B | RASGEF1B activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express RASGEF1B (10) vs lines expressing it (38) | the lines without RASGEF1B: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[ENSG00000283321]] | 0.05 µM | B | ENSG00000283321 activity raises the cells' numbers under MK-3903 0.05 µM (protects the cells) | lines that do not express ENSG00000283321 (7) vs lines expressing it (41) | the lines without ENSG00000283321: 0.89× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: AHR, PSMB8, CXCL2 |
| [[LINC00589]] | 5 µM | B | LINC00589 activity lowers the cells' numbers under MK-3903 5 µM (makes them more sensitive) | lines that do not express LINC00589 (28) vs lines expressing it (20) | the lines without LINC00589: 1.24× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00520, ENSG00000267881, TSPAN8 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "MK-3903"
- `tables/drugdoses.parquet` — dd in 642, 643, 644
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

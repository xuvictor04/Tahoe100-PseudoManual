---
drug: "Mifepristone"
type: "drug"
salt_base: "Mifepristone"
targets: "NR3C1, PGR"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 64
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Mifepristone

*unclear (inhibitor/antagonist) · targets: NR3C1, PGR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 18 / 64 / 30; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.35 / 0.08.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:H5 | 16 / 2 | — | -0.20 | +0.2/+0.4/+1.4 | — |
| 0.5 µM | [[Plate 08]]:H5 | 31 / 33 | — | +0.17 | +1.0/+0.8/+0.7 | — |
| 5 µM | [[Plate 09]]:H5 | 27 / 3 | — | +0.08 | -1.2/+1.0/+0.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (16 genes, none with an alert; 12 shown): [[CPT1A]] 1.41× (z +6.1, 26/46 lines), [[PLIN2]] 2.11× (z +6.0, 28/31 lines), [[PDK4]] 1.79× (z +4.9, 17/23 lines), [[NTAN1]] 1.27× (z +4.0, 11/46 lines), [[HAUS6]] 1.22× (z +3.9, 11/47 lines), [[ETFDH]] 1.22× (z +3.8, 15/47 lines), [[CES1]] 1.77× (z +3.5, 0/4 lines), [[ENSG00000280241]] 1.56× (z +3.3, 4/12 lines), [[LRRN3]] 1.42× (z +3.2, 1/32 lines), [[ENSG00000289418]] 1.90× (z +3.2, 4/8 lines), [[PSMD8]] 1.30× (z +3.1, 25/47 lines), [[MYL6]] 1.36× (z +3.0, 31/47 lines)

**0.5 µM** (31 genes, none with an alert; 12 shown): [[CPT1A]] 1.72× (z +10.5, 43/46 lines), [[PDK4]] 2.71× (z +9.1, 19/23 lines), [[PLIN2]] 2.74× (z +8.7, 29/31 lines), [[ACAA2]] 1.44× (z +4.8, 25/47 lines), [[LPCAT3]] 1.28× (z +4.7, 17/48 lines), [[HAUS6]] 1.25× (z +4.7, 22/48 lines), [[ABCC3]] 1.39× (z +4.6, 21/32 lines), [[ECH1]] 1.55× (z +4.2, 30/47 lines), [[HS6ST2]] 1.25× (z +4.0, 1/20 lines), [[SYK]] 1.33× (z +3.9, 12/18 lines), [[LINC01204]] 1.59× (z +3.9, 8/25 lines), [[KLF10]] 1.29× (z +3.9, 26/48 lines)

**5 µM** (27 genes, none with an alert; 12 shown): [[CPT1A]] 1.63× (z +9.0, 39/46 lines), [[PLIN2]] 2.79× (z +8.5, 26/31 lines), [[PDK4]] 2.48× (z +7.9, 18/23 lines), [[CAT]] 1.44× (z +5.5, 25/47 lines), [[DENND4C]] 1.26× (z +5.0, 28/48 lines), [[ACAA2]] 1.47× (z +4.9, 26/47 lines), [[HAUS6]] 1.25× (z +4.6, 19/48 lines), [[SLC25A20]] 1.45× (z +4.4, 7/42 lines), [[ETFDH]] 1.23× (z +4.2, 16/48 lines), [[LPCAT3]] 1.25× (z +4.0, 14/47 lines), [[KLF10]] 1.30× (z +3.8, 24/48 lines), [[TRIB3]] 1.31× (z +3.7, 12/44 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[PRRT2]] 0.639× (z -3.9, 7/27 lines), [[TAPBP]] 0.833× (z -2.8, 17/47 lines)

**0.5 µM** (33 genes, none with an alert; 12 shown): [[HSF2]] 0.751× (z -3.8, 14/47 lines), [[SPATA5L1]] 0.783× (z -3.8, 11/48 lines), [[ELOVL7]] 0.758× (z -3.7, 14/36 lines), [[LRRFIP2]] 0.830× (z -3.6, 22/48 lines), [[TAPT1]] 0.792× (z -3.5, 15/48 lines), [[SRP54-AS1]] 0.742× (z -3.4, 22/48 lines), [[FHIP2A]] 0.769× (z -3.4, 20/48 lines), [[USP3]] 0.743× (z -3.4, 30/48 lines), [[KDM1A]] 0.803× (z -3.4, 23/48 lines), [[AKTIP]] 0.803× (z -3.3, 5/47 lines), [[C5orf34]] 0.822× (z -3.3, 5/47 lines), [[ZNF592]] 0.818× (z -3.3, 15/48 lines)

**5 µM** (3 genes, none with an alert): [[RHCE]] 0.705× (z -3.3, 8/42 lines), [[ENSG00000272305]] 0.793× (z -3.2, 6/46 lines), [[STING1]] 0.716× (z -3.1, 6/30 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Module 179]] (-3.7), [[Module 171]] (-2.3), [[Module 065]] (-2.3) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[SNU-423 (line)]] (1.51), [[AsPC-1 (line)]] (1.44), [[HT-29 (line)]] (1.40), [[HS-578T (line)]] (1.36) · weakest: [[C32 (line)]] (0.363), [[NCI-H23 (line)]] (0.371), [[AN3 CA (line)]] (0.399) |
| 5 µM | — | [[KATO III (line)]] (1.82), [[Panc 03.27 (line)]] (1.72), [[HS-578T (line)]] (1.59), [[LS 180 (line)]] (1.58) · weakest: [[C-33 A (line)]] (0.134), [[HEC-1-A (line)]] (0.301), [[SW 1088 (line)]] (0.375) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Apalutamide (drug)]] (+0.93, Androgen receptor antagonist); [[Estrone sulfate (potassium) (drug)]] (+0.83, unclear); [[Proglumide (drug)]] (+0.82, unclear); [[Esmolol (hydrochloride) (drug)]] (+0.80, unclear); [[L-Eflornithine (monohydrochloride) (drug)]] (+0.79, unclear); [[Diphenhydramine (drug)]] (+0.79, unclear); [[Tirabrutinib (drug)]] (+0.79, Other TK inhibitor); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.71, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 71 arrows, 71 of them with an alert ⚠; grade A 0, B 62, C 9. Shown: the 15 strongest; 56 more arrows (56 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ST14]] | 0.5 µM | B | ST14 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express ST14 (32) vs lines expressing it (16) | the lines without ST14: 1.26× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[ANKRD22]] | 0.5 µM | B | ANKRD22 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express ANKRD22 (34) vs lines expressing it (14) | the lines without ANKRD22: 1.26× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[OVOL1]], [[TMPRSS4]] | 0.5 µM | B | OVOL1, TMPRSS4 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express OVOL1, TMPRSS4 (33) vs lines expressing them (15) | the lines without OVOL1, TMPRSS4: 1.26× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: GRHL2, ST14, TMEM30B; co-absent genes |
| [[C1orf116]], [[IRF6]] | 0.5 µM | B | C1orf116, IRF6 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (17) | the lines without C1orf116, IRF6: 1.25× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |
| [[KDF1]] | 0.5 µM | B | KDF1 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express KDF1 (30) vs lines expressing it (18) | the lines without KDF1: 1.22× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[KCNH8]] | 0.5 µM | B | KCNH8 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express KCNH8 (32) vs lines expressing it (16) | the lines without KCNH8: 1.21× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SLC5A1, VWA2, ANKRD22 |
| [[CCDC80]] | 0.5 µM | B | CCDC80 activity raises the cells' numbers under Mifepristone 0.5 µM (protects the cells) | lines that do not express CCDC80 (21) vs lines expressing it (27) | the lines without CCDC80: 0.84× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| [[RASEF]] | 0.5 µM | B | RASEF activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express RASEF (20) vs lines expressing it (28) | the lines without RASEF: 1.17× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[GRHL2]], [[LINC02967]] | 0.5 µM | B | GRHL2, LINC02967 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express GRHL2, LINC02967 (34) vs lines expressing them (14) | the lines without GRHL2, LINC02967: 1.25× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent genes |
| [[KLK10]] | 0.5 µM | B | KLK10 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express KLK10 (34) vs lines expressing it (14) | the lines without KLK10: 1.25× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[CLDN7]] | 0.5 µM | B | CLDN7 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express CLDN7 (30) vs lines expressing it (18) | the lines without CLDN7: 1.24× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[ERBB3]] | 0.5 µM | B | ERBB3 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express ERBB3 (27) vs lines expressing it (21) | the lines without ERBB3: 1.22× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[ESRP1]] | 0.5 µM | B | ESRP1 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express ESRP1 (31) vs lines expressing it (17) | the lines without ESRP1: 1.25× the cells of the other lines | 0.035 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[TMEM125]] | 0.5 µM | B | TMEM125 activity lowers the cells' numbers under Mifepristone 0.5 µM (makes them more sensitive) | lines that do not express TMEM125 (33) vs lines expressing it (15) | the lines without TMEM125: 1.25× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[HEG1]] | 0.5 µM | B | HEG1 activity raises the cells' numbers under Mifepristone 0.5 µM (protects the cells) | lines that do not express HEG1 (11) vs lines expressing it (37) | the lines without HEG1: 0.80× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: CCDC88A, STARD9, RECK |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Mifepristone"
- `tables/drugdoses.parquet` — dd in 684, 685, 686
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

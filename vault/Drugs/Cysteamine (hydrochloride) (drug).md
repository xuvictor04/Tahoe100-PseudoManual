---
drug: "Cysteamine (hydrochloride)"
type: "drug"
salt_base: "Cysteamine"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 16
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Cysteamine (hydrochloride)

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 16 / 2; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.17 / 0.05.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:A6 | 0 / 2 | — | -0.01 | +0.2/+0.6/+0.7 | — |
| 0.5 µM | [[Plate 05]]:A6 | 13 / 3 | — | -0.72 | -0.9/-0.7/-0.2 | — |
| 5 µM | [[Plate 14]]:A6 | 1 / 1 | 0.706 | +0.30 | +1.3/+1.2/-0.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (13 genes, none with an alert; 12 shown): [[LSM6]] 1.35× (z +4.4, 17/46 lines), [[ENSG00000273014]] 1.44× (z +3.8, 8/27 lines), [[TSBP1-AS1]] 1.30× (z +3.6, 1/34 lines), [[CLDN18]] 1.53× (z +3.4, 0/23 lines), [[BTN2A3P]] 1.35× (z +3.2, 5/36 lines), [[MIR325HG]] 1.54× (z +3.1, 1/12 lines), [[SLCO6A1]] 1.63× (z +3.1, 1/10 lines), [[RBM24]] 1.46× (z +3.1, 3/18 lines), [[ENSG00000224322]] 1.42× (z +3.0, 0/6 lines), [[DTX4]] 1.22× (z +3.0, 2/37 lines), [[ENSG00000267022]] 1.37× (z +2.9, 4/28 lines), [[ENSG00000260710]] 1.43× (z +2.9, 0/14 lines)

**5 µM** (1 gene, none with an alert): [[CREB5]] 1.20× (z +4.5, 15/34 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[GUSBP18]] 0.820× (z -3.3, 10/48 lines), [[ELFN2]] 0.765× (z -2.9, 3/28 lines)

**0.5 µM** (3 genes, none with an alert): [[GUSBP18]] 0.829× (z -3.1, 13/48 lines), [[ENSG00000271204]] 0.826× (z -3.1, 11/43 lines), [[C14orf132]] 0.818× (z -2.9, 6/27 lines)

**5 µM** (1 gene, none with an alert): [[MATN1-AS1]] 0.814× (z -3.1, 4/42 lines)

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
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[RKO (line)]] (-3.5), [[LOX-IMVI (line)]] (-3.0) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 6 next most similar without an alert.*

- [[Rimonabant (Hydrochloride) (drug)]] (+0.61, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Sunitinib (drug)]] (+0.61, Multi-TK inhibitor, ⚠ vector dose flagged: toxic); [[Macitentan (drug)]] (+0.61, unclear, ⚠ only 5 significant genes); [[Fostamatinib (disodium hexahydrate) (drug)]] (+0.58, Other TK inhibitor, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Ataluren (drug)]] (+0.58, unclear, ⚠ only 7 significant genes); [[Lidocaine (hydrochloride) (drug)]] (+0.57, unclear); [[Imiquimod (hydrochloride) (drug)]] (+0.57, unclear, ⚠ vector dose flagged: toxic); [[Orlistat (drug)]] (+0.56, unclear); [[Cabozantinib (S-malate) (drug)]] (+0.55, Multi-TK inhibitor); [[Isocorydine (drug)]] (+0.51, unclear); [[Drospirenone (drug)]] (+0.50, unclear); [[Ponatinib (drug)]] (+0.48, Multi-TK inhibitor); [[Menadione (drug)]] (+0.48, unclear); [[Pasireotide (acetate) (drug)]] (+0.48, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 137 arrows, 137 of them with an alert ⚠; grade A 0, B 134, C 3. Shown: the 15 strongest; 122 more arrows (122 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[LGALS3BP]] | 5 µM | B | LGALS3BP activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 0.84× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[ATP1B1]] | 5 µM | B | ATP1B1 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 0.85× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[IL15]] | 5 µM | B | IL15 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 0.87× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[RNF39]] | 5 µM | B | RNF39 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express RNF39 (30) vs lines expressing it (18) | the lines without RNF39: 0.87× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[ENSG00000251584]] | 5 µM | B | ENSG00000251584 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express ENSG00000251584 (28) vs lines expressing it (20) | the lines without ENSG00000251584: 0.88× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: HPGD, HNF1A-AS1, ENSG00000267881 |
| [[MPZL3]] | 5 µM | B | MPZL3 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express MPZL3 (25) vs lines expressing it (23) | the lines without MPZL3: 0.88× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[C1orf116]], [[IRF6]] | 5 µM | B | C1orf116, IRF6 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (17) | the lines without C1orf116, IRF6: 0.88× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |
| [[TNNT2]] | 5 µM | B | TNNT2 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express TNNT2 (29) vs lines expressing it (19) | the lines without TNNT2: 0.88× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[ELF3]] | 5 µM | B | ELF3 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express ELF3 (23) vs lines expressing it (25) | the lines without ELF3: 0.89× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[MPZL2]] | 5 µM | B | MPZL2 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express MPZL2 (29) vs lines expressing it (19) | the lines without MPZL2: 0.89× the cells of the other lines | 0.027 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[GALNT3]] | 5 µM | B | GALNT3 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express GALNT3 (30) vs lines expressing it (18) | the lines without GALNT3: 0.90× the cells of the other lines | 0.030 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[AQP3]] | 5 µM | B | AQP3 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express AQP3 (19) vs lines expressing it (29) | the lines without AQP3: 0.88× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[LGALS3]] | 5 µM | B | LGALS3 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express LGALS3 (11) vs lines expressing it (37) | the lines without LGALS3: 0.88× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[PRR15]] | 5 µM | B | PRR15 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express PRR15 (28) vs lines expressing it (20) | the lines without PRR15: 0.89× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[ATXN1]] | 5 µM | B | ATXN1 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express ATXN1 (6) vs lines expressing it (42) | the lines without ATXN1: 0.86× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Cysteamine (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 299, 300, 301
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

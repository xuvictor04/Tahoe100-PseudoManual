---
drug: "Pemetrexed"
type: "drug"
salt_base: "Pemetrexed"
targets: "TYMS, DHFR, GART"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 23
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Pemetrexed

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: TYMS, DHFR, GART · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 23 / 9; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.00 / 0.09.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:F8 | 0 / 1 | — | +0.18 | +0.3/+0.0/+0.2 | — |
| 0.5 µM | [[Plate 08]]:F8 | 3 / 20 | — | -0.68 | -0.6/-1.4/-1.4 | — |
| 5 µM | [[Plate 09]]:F8 | 4 / 5 | — | -0.90 | +0.4/+0.3/-0.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (3 genes, none with an alert): [[FAM219B]] 1.25× (z +3.4, 3/47 lines), [[MCOLN2]] 1.27× (z +3.3, 4/29 lines), [[NSUN5P1]] 1.38× (z +3.2, 3/41 lines)

**5 µM** (4 genes, none with an alert): [[KCNQ2]] 1.40× (z +3.0, 1/12 lines), [[CDR2L]] 1.24× (z +3.0, 3/41 lines), [[PLEKHS1]] 1.46× (z +2.9, 1/15 lines), [[SUSD4]] 1.41× (z +2.8, 3/17 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENSG00000289318]] 0.642× (z -3.8, 8/32 lines)

**0.5 µM** (20 genes, none with an alert; 12 shown): [[ADAM15]] 0.706× (z -4.8, 20/47 lines), [[CNOT7]] 0.803× (z -4.4, 26/47 lines), [[PPP1R11]] 0.756× (z -4.4, 27/47 lines), [[HIKESHI]] 0.792× (z -3.9, 15/47 lines), [[PPP6R1]] 0.815× (z -3.9, 21/47 lines), [[LINC00654]] 0.633× (z -3.7, 12/42 lines), [[CCDC127]] 0.771× (z -3.7, 9/47 lines), [[MAP3K11]] 0.800× (z -3.7, 14/47 lines), [[MUC17]] 0.587× (z -3.7, 0/4 lines), [[SPCS2]] 0.792× (z -3.5, 23/47 lines), [[ARHGEF34P]] 0.788× (z -3.3, 2/28 lines), [[HNRNPA1]] 0.791× (z -3.3, 28/47 lines)

**5 µM** (5 genes, none with an alert): [[ENSG00000291107]] 0.626× (z -4.6, 5/27 lines), [[GPR137C]] 0.721× (z -3.7, 11/43 lines), [[ATP8B4]] 0.673× (z -3.4, 6/28 lines), [[DVL2]] 0.817× (z -3.4, 6/46 lines), [[SOCS2-AS1]] 0.749× (z -3.3, 4/25 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Module 048]] (-2.2) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[HOP62 (line)]] (-4.8), [[SNU-423 (line)]] (-4.1), [[HS-578T (line)]] (-4.1), [[A498 (line)]] (-4.0), [[NCI-H2030 (line)]] (-3.8) | [[Hs 766T (line)]] (1.93), [[AN3 CA (line)]] (1.91), [[H4 (line)]] (1.59), [[LoVo (line)]] (1.48) · weakest: [[A498 (line)]] (0.364), [[SW1417 (line)]] (0.500), [[SNU-423 (line)]] (0.523) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Lopinavir (drug)]] (+0.83, unclear); [[Fluvoxamine (drug)]] (+0.67, unclear); [[Mozavaptan (drug)]] (+0.67, unclear); [[Gallic acid (drug)]] (+0.67, Cyclooxygenase inhibitor); [[Clonidine (hydrochloride) (drug)]] (+0.64, Adrenoceptor agonist, ⚠ only 4 significant genes); [[Ferulic acid (drug)]] (+0.60, Other TK inhibitor); [[Temuterkib (drug)]] (+0.57, Other MAPK inhibitor, ⚠ only 3 significant genes); [[Adenine (drug)]] (+0.56, unclear); [[Ropivacaine (hydrochloride monohydrate) (drug)]] (+0.52, unclear); [[Fusidic acid (drug)]] (+0.51, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 31 arrows, 31 of them with an alert ⚠; grade A 0, B 20, C 11. Shown: the 15 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[STK26]] | 5 µM | B | STK26 activity raises the cells' numbers under Pemetrexed 5 µM (protects the cells) | lines that do not express STK26 (5) vs lines expressing it (43) | the lines without STK26: 0.74× the cells of the other lines | 0.027 | ⚠ across organs; maybe low, not absent |
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity lowers the cells' numbers under Pemetrexed 5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.27× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[BMPER]] | 5 µM | B | BMPER activity lowers the cells' numbers under Pemetrexed 5 µM (makes them more sensitive) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 1.23× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Pemetrexed 5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.22× the cells of the other lines | 0.044 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[EPCAM]] | 5 µM | B | EPCAM activity raises the cells' numbers under Pemetrexed 5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.82× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[KCNMA1]] | 5 µM | B | KCNMA1 activity lowers the cells' numbers under Pemetrexed 5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.24× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[C10orf90]] | 5 µM | B | C10orf90 activity lowers the cells' numbers under Pemetrexed 5 µM (makes them more sensitive) | lines that do not express C10orf90 (35) vs lines expressing it (13) | the lines without C10orf90: 1.26× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GRIN2A, LINC01242, ADGRG7; maybe low, not absent |
| [[CLDN3]] | 5 µM | B | CLDN3 activity raises the cells' numbers under Pemetrexed 5 µM (protects the cells) | lines that do not express CLDN3 (28) vs lines expressing it (20) | the lines without CLDN3: 0.82× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[RNF125]] | 5 µM | B | RNF125 activity raises the cells' numbers under Pemetrexed 5 µM (protects the cells) | lines that do not express RNF125 (9) vs lines expressing it (39) | the lines without RNF125: 0.74× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SAMD10, TMTC2; maybe low, not absent |
| [[AOX1]] | 5 µM | B | AOX1 activity lowers the cells' numbers under Pemetrexed 5 µM (makes them more sensitive) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 1.24× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[ERBB3]] | 5 µM | B | ERBB3 activity raises the cells' numbers under Pemetrexed 5 µM (protects the cells) | lines that do not express ERBB3 (27) vs lines expressing it (21) | the lines without ERBB3: 0.82× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[SMPDL3B]] | 5 µM | B | SMPDL3B activity raises the cells' numbers under Pemetrexed 5 µM (protects the cells) | lines that do not express SMPDL3B (23) vs lines expressing it (25) | the lines without SMPDL3B: 0.83× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[ENSG00000230615]] | 5 µM | B | ENSG00000230615 activity lowers the cells' numbers under Pemetrexed 5 µM (makes them more sensitive) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 1.22× the cells of the other lines | 0.085 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[CNRIP1]] | 5 µM | B | CNRIP1 activity lowers the cells' numbers under Pemetrexed 5 µM (makes them more sensitive) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 1.15× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| [[MSRB3]] | 5 µM | B | MSRB3 activity lowers the cells' numbers under Pemetrexed 5 µM (makes them more sensitive) | lines that do not express MSRB3 (20) vs lines expressing it (28) | the lines without MSRB3: 1.18× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Pemetrexed"
- `tables/drugdoses.parquet` — dd in 780, 781, 782
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

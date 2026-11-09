---
drug: "Imiquimod (hydrochloride)"
type: "drug"
salt_base: "Imiquimod"
targets: "TLR7"
moa_fine: "unclear"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 827
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Imiquimod (hydrochloride)

*unclear (activator/agonist) · targets: TLR7 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 18 / 1 / 827; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.41 / -0.11.
> Flags by dose: - / - / toxic. ⚠ 5 µM: toxic (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:B10 | 8 / 10 | — | -0.02 | -0.1/-0.8/-0.0 | — |
| 0.5 µM | [[Plate 11]]:B10 | 0 / 1 | — | +0.63 | +0.5/-0.1/-0.0 | — |
| 5 µM | [[Plate 12]]:B10 | 778 / 49 | — | -1.67 | +0.4/+0.5/+2.4 | ⚠ toxic |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (8 genes, none with an alert): [[SHKBP1]] 1.23× (z +3.8, 8/47 lines), [[TBL3]] 1.30× (z +3.7, 6/46 lines), [[RNF44]] 1.30× (z +3.5, 9/47 lines), [[RHOT2]] 1.34× (z +3.3, 12/47 lines), [[SCARA3]] 1.34× (z +3.2, 5/26 lines), [[CTU2]] 1.43× (z +3.1, 2/44 lines), [[SF3B4]] 1.43× (z +3.1, 18/46 lines), [[KLHL21]] 1.31× (z +3.1, 8/47 lines)

**5 µM** (778 genes, 778 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[GDPD4]] ⚠ 2.28× (z +5.9, 2/8 lines), [[LINC00879]] ⚠ 2.41× (z +5.8, 0/2 lines), [[ZNF677]] ⚠ 2.78× (z +5.6, 1/5 lines), [[BNC1]] ⚠ 2.41× (z +5.5, 0/7 lines), [[EPHX4]] ⚠ 1.97× (z +5.5, 3/16 lines), [[ENSG00000268119]] ⚠ 1.83× (z +5.4, 2/10 lines), [[TRIM58]] ⚠ 1.95× (z +5.4, 2/17 lines), [[LNCOG]] ⚠ 2.20× (z +5.3, 0/9 lines), [[ENSG00000224322]] ⚠ 1.83× (z +5.3, 0/6 lines), [[KLK7]] ⚠ 2.91× (z +5.3, 1/8 lines), [[AEBP1]] ⚠ 2.42× (z +5.2, 1/7 lines), [[DDIT4L]] ⚠ 2.49× (z +5.2, 0/8 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (10 genes, none with an alert): [[GPC6]] 0.811× (z -3.9, 2/22 lines), [[MAGI2]] 0.769× (z -3.8, 1/18 lines), [[PCDH17]] 0.627× (z -3.8, 0/17 lines), [[ADGRL3]] 0.757× (z -3.6, 3/22 lines), [[UTY]] 0.815× (z -3.5, 0/17 lines), [[ADGRB3]] 0.729× (z -3.4, 1/19 lines), [[TENM2]] 0.772× (z -3.4, 1/15 lines), [[SMOC1]] 0.741× (z -3.2, 0/14 lines), [[MACC1]] 0.771× (z -3.1, 0/16 lines), [[COL5A2]] 0.779× (z -3.0, 0/19 lines)

**0.5 µM** (1 gene, none with an alert): [[MIB2]] 0.758× (z -3.5, 5/48 lines)

**5 µM** (49 genes, 49 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[OCLN]] ⚠ 0.724× (z -4.1, 18/29 lines), [[ENSG00000228541]] ⚠ 0.771× (z -4.0, 11/44 lines), [[MC1R]] ⚠ 0.699× (z -3.9, 15/41 lines), [[ZNF468]] ⚠ 0.705× (z -3.8, 13/38 lines), [[SMCR8]] ⚠ 0.776× (z -3.7, 20/47 lines), [[HRH1]] ⚠ 0.823× (z -3.5, 11/38 lines), [[ZNF655]] ⚠ 0.767× (z -3.5, 23/41 lines), [[TOR1AIP1]] ⚠ 0.824× (z -3.5, 17/48 lines), [[LOXL1]] ⚠ 0.764× (z -3.4, 6/22 lines), [[EXT1]] ⚠ 0.832× (z -3.4, 22/45 lines), [[TINF2]] ⚠ 0.785× (z -3.4, 15/43 lines), [[PTPRB]] ⚠ 0.765× (z -3.3, 6/25 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 179]] (+2.0) | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 048]] (+2.7), [[Module 054]] (+2.6), [[Module 182]] (+2.4) | [[Module 230]] (-2.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[SNU-423 (line)]] (-3.3) | [[SW 1271 (line)]] (2.19), [[HepG2_C3A (line)]] (1.86), [[NCI-H661 (line)]] (1.80), [[SW 1088 (line)]] (1.78) · weakest: [[SW480 (line)]] (0.357), [[SHP-77 (line)]] (0.471), [[NCI-H1573 (line)]] (0.563) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: toxic. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Fingolimod (hydrochloride) (drug)]] (+0.79, unclear, ⚠ vector dose flagged: toxic); [[Darolutamide (drug)]] (+0.77, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Erythromycin (drug)]] (+0.75, unclear); [[Bendamustine (drug)]] (+0.74, DNA synthesis/repair inhibitor); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] (+0.74, Glucose transporter inhibitor); [[Sunitinib (drug)]] (+0.73, Multi-TK inhibitor, ⚠ vector dose flagged: toxic); [[Methylprednisolone succinate (drug)]] (+0.73, Glucocorticoid receptor agonist); [[Decitabine (drug)]] (+0.72, DNA methyltransferase inhibitor); [[Bicalutamide (drug)]] (+0.71, Androgen receptor antagonist); [[Saquinavir (drug)]] (+0.70, unclear); [[Docetaxel (Trihydrate) (drug)]] (+0.69, Microtubule inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 35 arrows, 35 of them with an alert ⚠; grade A 0, B 24, C 11. Shown: the 15 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[AOX1]] | 5 µM | B | AOX1 activity lowers the cells' numbers under Imiquimod (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 1.27× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Imiquimod (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.25× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity lowers the cells' numbers under Imiquimod (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.23× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[MBNL3]] | 5 µM | B | MBNL3 activity raises the cells' numbers under Imiquimod (hydrochloride) 5 µM (protects the cells) | lines that do not express MBNL3 (16) vs lines expressing it (32) | the lines without MBNL3: 0.83× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: EPHA1, ERBB3, MYO1D |
| [[PAMR1]] | 5 µM | B | PAMR1 activity lowers the cells' numbers under Imiquimod (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express PAMR1 (28) vs lines expressing it (20) | the lines without PAMR1: 1.14× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent |
| [[NLGN4X]] | 0.05 µM | B | NLGN4X activity raises the cells' numbers under Imiquimod (hydrochloride) 0.05 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.95× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| [[LINC02058]] | 5 µM | B | LINC02058 activity raises the cells' numbers under Imiquimod (hydrochloride) 5 µM (protects the cells) | lines that do not express LINC02058 (34) vs lines expressing it (14) | the lines without LINC02058: 0.81× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC02253, ENSG00000260573, ST18; maybe low, not absent |
| [[EPCAM]] | 5 µM | B | EPCAM activity raises the cells' numbers under Imiquimod (hydrochloride) 5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.85× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[DNAH11]] | 0.05 µM | B | DNAH11 activity lowers the cells' numbers under Imiquimod (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express DNAH11 (23) vs lines expressing it (25) | the lines without DNAH11: 1.21× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1 |
| [[SMPDL3B]] | 5 µM | B | SMPDL3B activity raises the cells' numbers under Imiquimod (hydrochloride) 5 µM (protects the cells) | lines that do not express SMPDL3B (23) vs lines expressing it (25) | the lines without SMPDL3B: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[MYH14]] | 0.05 µM | B | MYH14 activity raises the cells' numbers under Imiquimod (hydrochloride) 0.05 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.81× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[HSD11B2]] | 5 µM | B | HSD11B2 activity raises the cells' numbers under Imiquimod (hydrochloride) 5 µM (protects the cells) | lines that do not express HSD11B2 (16) vs lines expressing it (32) | the lines without HSD11B2: 0.82× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[KCNMA1]] | 5 µM | B | KCNMA1 activity lowers the cells' numbers under Imiquimod (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.19× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[ADAM12]] | 5 µM | B | ADAM12 activity lowers the cells' numbers under Imiquimod (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 1.19× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| [[PRSS23]] | 0.05 µM | B | PRSS23 activity lowers the cells' numbers under Imiquimod (hydrochloride) 0.05 µM (makes them more sensitive) | lines that do not express PRSS23 (13) vs lines expressing it (35) | the lines without PRSS23: 1.29× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Imiquimod (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 546, 547, 548
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

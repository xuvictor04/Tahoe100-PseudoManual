---
drug: "Pasireotide (acetate)"
type: "drug"
salt_base: "Pasireotide"
targets: "SSTR1, SSTR2, SSTR3, SSTR5"
moa_fine: "unclear"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 74
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Pasireotide (acetate)

*unclear (activator/agonist) · targets: SSTR1, SSTR2, SSTR3, SSTR5 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 6 / 15 / 74; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.24 / 0.62.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:A8 | 1 / 5 | — | +0.21 | +2.5/+1.7/+2.2 | — |
| 0.5 µM | [[Plate 05]]:A8 | 7 / 8 | — | +0.02 | +0.4/+0.1/+1.4 | — |
| 5 µM | [[Plate 14]]:A8 | 18 / 56 | 0.872 | +0.16 | +0.2/+1.1/+2.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[MOCS3]] 1.33× (z +2.8, 0/44 lines)

**0.5 µM** (7 genes, none with an alert): [[SENP3]] 1.30× (z +4.5, 18/48 lines), [[RYR2]] 1.57× (z +4.5, 15/47 lines), [[FUNDC2]] 1.40× (z +4.3, 22/47 lines), [[NSUN5P1]] 1.46× (z +3.7, 6/39 lines), [[MRPS35]] 1.21× (z +3.6, 22/49 lines), [[EIF3A]] 1.22× (z +3.2, 27/49 lines), [[WBP11]] 1.20× (z +2.8, 17/49 lines)

**5 µM** (18 genes, none with an alert; 12 shown): [[RNF126]] 1.24× (z +3.9, 13/48 lines), [[ZNF706]] 1.21× (z +3.8, 24/49 lines), [[SSR3]] 1.20× (z +3.7, 21/49 lines), [[RPL6]] 1.28× (z +3.7, 30/49 lines), [[CCNB2]] 1.21× (z +3.5, 10/48 lines), [[GCSH]] 1.26× (z +3.4, 4/46 lines), [[ENSG00000287856]] 1.21× (z +3.3, 2/47 lines), [[C16orf87]] 1.21× (z +3.3, 17/48 lines), [[SRPRB]] 1.20× (z +3.3, 14/48 lines), [[ENY2]] 1.22× (z +3.2, 29/49 lines), [[FAM72A]] 1.31× (z +3.2, 7/44 lines), [[TBC1D22A-DT]] 1.39× (z +3.1, 12/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[NCKIPSD]] 0.802× (z -3.5, 7/48 lines), [[ZNF160]] 0.830× (z -3.4, 22/44 lines), [[SYT7]] 0.816× (z -3.1, 1/39 lines), [[PTPRH]] 0.825× (z -3.0, 8/42 lines), [[ENSG00000253100]] 0.745× (z -2.7, 7/35 lines)

**0.5 µM** (8 genes, none with an alert): [[THSD7B]] 0.707× (z -3.5, 3/39 lines), [[ENSG00000285953]] 0.782× (z -3.1, 9/48 lines), [[THUMPD3-AS1]] 0.832× (z -3.0, 15/49 lines), [[TET1]] 0.831× (z -3.0, 6/36 lines), [[KIAA0040]] 0.809× (z -2.9, 6/24 lines), [[PRELID2]] 0.818× (z -2.7, 22/48 lines), [[TRIM9]] 0.831× (z -2.7, 3/32 lines), [[ENSG00000251314]] 0.805× (z -2.7, 5/38 lines)

**5 µM** (56 genes, none with an alert; 12 shown): [[POT1-AS1]] 0.754× (z -4.3, 14/45 lines), [[PLD1]] 0.814× (z -4.2, 28/42 lines), [[ENSG00000251314]] 0.802× (z -3.9, 22/39 lines), [[KLHL3]] 0.777× (z -3.7, 10/35 lines), [[LINC01876]] 0.825× (z -3.7, 17/25 lines), [[MAML2]] 0.830× (z -3.5, 19/41 lines), [[LRMDA]] 0.832× (z -3.5, 18/28 lines), [[CALCRL]] 0.776× (z -3.5, 2/28 lines), [[SLC38A4-AS1]] 0.773× (z -3.5, 36/48 lines), [[DIRC3]] 0.808× (z -3.5, 12/30 lines), [[RGS17]] 0.833× (z -3.5, 13/34 lines), [[MAPK10]] 0.792× (z -3.4, 9/36 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 043]] (+2.2), [[Module 171]] (+2.2), [[Module 030]] (+2.1) | [[Module 200]] (-3.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[SW 1271 (line)]] (1.60), [[RPMI-7951 (line)]] (1.27), [[HCT15 (line)]] (1.22), [[Panc 03.27 (line)]] (1.21) · weakest: [[AsPC-1 (line)]] (0.493), [[NCI-H2122 (line)]] (0.522), [[HepG2_C3A (line)]] (0.583) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Terfenadine (drug)]] (+0.64, unclear); [[Lipoic acid (drug)]] (+0.62, unclear, ⚠ only 6 significant genes); [[Tetracycline (hydrochloride) (drug)]] (+0.62, unclear, ⚠ only 6 significant genes); [[Menadione (drug)]] (+0.61, unclear); [[Eplerenone (drug)]] (+0.56, unclear, ⚠ only 4 significant genes); [[Tomivosertib (drug)]] (+0.54, Protein synthesis inhibitor); [[Docetaxel (Trihydrate) (drug)]] (+0.53, Microtubule inhibitor); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.53, unclear); [[Erythromycin (drug)]] (+0.52, unclear); [[Entecavir (monohydrate) (drug)]] (+0.51, unclear); [[Aprepitant (drug)]] (+0.50, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 18 arrows, 18 of them with an alert ⚠; grade A 0, B 17, C 1. Shown: the 15 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MSRB3]] | 5 µM | B | MSRB3 activity lowers the cells' numbers under Pasireotide (acetate) 5 µM (makes them more sensitive) | lines that do not express MSRB3 (20) vs lines expressing it (28) | the lines without MSRB3: 1.11× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[LAMA1]] | 5 µM | B | LAMA1 activity lowers the cells' numbers under Pasireotide (acetate) 5 µM (makes them more sensitive) | lines that do not express LAMA1 (31) vs lines expressing it (17) | the lines without LAMA1: 1.15× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1 |
| [[EHF]] | 5 µM | B | EHF activity raises the cells' numbers under Pasireotide (acetate) 5 µM (protects the cells) | lines that do not express EHF (27) vs lines expressing it (21) | the lines without EHF: 0.89× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[DPP4]] | 5 µM | B | DPP4 activity raises the cells' numbers under Pasireotide (acetate) 5 µM (protects the cells) | lines that do not express DPP4 (29) vs lines expressing it (19) | the lines without DPP4: 0.93× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[GJB3]] | 5 µM | B | GJB3 activity raises the cells' numbers under Pasireotide (acetate) 5 µM (protects the cells) | lines that do not express GJB3 (31) vs lines expressing it (17) | the lines without GJB3: 0.87× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[RASEF]] | 5 µM | B | RASEF activity raises the cells' numbers under Pasireotide (acetate) 5 µM (protects the cells) | lines that do not express RASEF (20) vs lines expressing it (28) | the lines without RASEF: 0.92× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[ENSG00000287778]] | 5 µM | B | ENSG00000287778 activity raises the cells' numbers under Pasireotide (acetate) 5 µM (protects the cells) | lines that do not express ENSG00000287778 (27) vs lines expressing it (21) | the lines without ENSG00000287778: 0.89× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: HS3ST1, LIPH, KLK10 |
| [[C1orf116]], [[IRF6]] | 5 µM | B | C1orf116, IRF6 activity raises the cells' numbers under Pasireotide (acetate) 5 µM (protects the cells) | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (17) | the lines without C1orf116, IRF6: 0.88× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |
| [[TMEM125]] | 5 µM | B | TMEM125 activity raises the cells' numbers under Pasireotide (acetate) 5 µM (protects the cells) | lines that do not express TMEM125 (33) vs lines expressing it (15) | the lines without TMEM125: 0.88× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[TSPAN15]] | 5 µM | B | TSPAN15 activity raises the cells' numbers under Pasireotide (acetate) 5 µM (protects the cells) | lines that do not express TSPAN15 (15) vs lines expressing it (33) | the lines without TSPAN15: 0.90× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |
| [[HENMT1]] | 5 µM | B | HENMT1 activity raises the cells' numbers under Pasireotide (acetate) 5 µM (protects the cells) | lines that do not express HENMT1 (17) vs lines expressing it (31) | the lines without HENMT1: 0.91× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |
| [[DCLK2]] | 5 µM | B | DCLK2 activity lowers the cells' numbers under Pasireotide (acetate) 5 µM (makes them more sensitive) | lines that do not express DCLK2 (17) vs lines expressing it (31) | the lines without DCLK2: 1.10× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[LEF1-AS1]] | 5 µM | B | LEF1-AS1 activity lowers the cells' numbers under Pasireotide (acetate) 5 µM (makes them more sensitive) | lines that do not express LEF1-AS1 (33) vs lines expressing it (15) | the lines without LEF1-AS1: 1.10× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL19A1, ENSG00000226043, DCT; maybe low, not absent |
| [[PCDH1]] | 5 µM | B | PCDH1 activity raises the cells' numbers under Pasireotide (acetate) 5 µM (protects the cells) | lines that do not express PCDH1 (20) vs lines expressing it (28) | the lines without PCDH1: 0.92× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[SKAP1]] | 5 µM | B | SKAP1 activity raises the cells' numbers under Pasireotide (acetate) 5 µM (protects the cells) | lines that do not express SKAP1 (34) vs lines expressing it (14) | the lines without SKAP1: 0.87× the cells of the other lines | 0.097 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Pasireotide (acetate)"
- `tables/drugdoses.parquet` — dd in 777, 778, 779
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

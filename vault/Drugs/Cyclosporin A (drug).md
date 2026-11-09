---
drug: "Cyclosporin A"
type: "drug"
salt_base: "Cyclosporin A"
targets: "PPP3CA, PPP3CB, PPP3CC"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 42
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Cyclosporin A

*unclear (inhibitor/antagonist) · targets: PPP3CA, PPP3CB, PPP3CC · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 30 / 22 / 42; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.52 / 0.45.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:F7 | 11 / 19 | — | +0.70 | +0.8/+1.3/+1.5 | — |
| 0.5 µM | [[Plate 11]]:F7 | 16 / 6 | — | -0.32 | -0.3/+0.2/+0.8 | — |
| 5 µM | [[Plate 12]]:F7 | 24 / 18 | — | -0.00 | -1.9/-0.3/+0.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (11 genes, none with an alert): [[CFAP210]] 2.04× (z +3.9, 21/46 lines), [[FOSB]] 2.33× (z +3.6, 41/48 lines), [[ATP1B1]] 1.25× (z +3.5, 19/41 lines), [[MARCKS]] 1.38× (z +3.4, 30/39 lines), [[KLF4]] 1.40× (z +3.3, 11/42 lines), [[KIF9]] 1.44× (z +3.2, 11/47 lines), [[MMP1]] 1.60× (z +3.1, 6/23 lines), [[MLF1]] 1.45× (z +3.1, 24/43 lines), [[LGALS3]] 1.27× (z +3.1, 20/38 lines), [[OSR2]] 1.61× (z +3.1, 2/41 lines), [[TRIM72]] 1.96× (z +3.0, 6/41 lines)

**0.5 µM** (16 genes, none with an alert; 12 shown): [[PODXL]] 1.27× (z +4.0, 15/24 lines), [[FLII]] 1.20× (z +3.6, 16/48 lines), [[KRT23]] 1.62× (z +3.5, 3/8 lines), [[TNFSF15]] 1.42× (z +3.5, 7/17 lines), [[DYSF]] 1.28× (z +3.3, 3/32 lines), [[TOB1]] 1.23× (z +3.3, 15/48 lines), [[MSANTD3-TMEFF1]] 1.26× (z +3.2, 5/45 lines), [[RFX5]] 1.29× (z +3.2, 5/44 lines), [[ENSG00000228033]] 1.32× (z +3.1, 6/22 lines), [[MUC5AC]] 1.85× (z +3.1, 5/9 lines), [[DBN1]] 1.29× (z +3.0, 11/45 lines), [[GEMIN7-AS1]] 1.32× (z +3.0, 3/42 lines)

**5 µM** (24 genes, none with an alert; 12 shown): [[CPT1A]] 1.28× (z +4.8, 18/46 lines), [[BAIAP2L1]] 1.20× (z +3.9, 15/40 lines), [[FDPS]] 1.34× (z +3.7, 29/48 lines), [[LAMC2]] 1.31× (z +3.7, 13/21 lines), [[TRIB3]] 1.29× (z +3.6, 12/44 lines), [[CYP51A1]] 1.25× (z +3.5, 22/47 lines), [[SPCS2]] 1.25× (z +3.5, 25/48 lines), [[VEGFA]] 1.26× (z +3.5, 25/46 lines), [[FDFT1]] 1.29× (z +3.5, 18/47 lines), [[RNF114]] 1.25× (z +3.4, 26/48 lines), [[CEBPG]] 1.26× (z +3.4, 14/48 lines), [[SCD]] 1.27× (z +3.4, 25/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (19 genes, none with an alert; 12 shown): [[STARD7-AS1]] 0.721× (z -4.5, 8/48 lines), [[ZNG1E]] 0.801× (z -3.8, 10/48 lines), [[CELF5]] 0.708× (z -3.4, 1/44 lines), [[PRKG1-AS1]] 0.708× (z -3.4, 3/31 lines), [[TMEM175]] 0.743× (z -3.4, 8/47 lines), [[MIOS]] 0.825× (z -3.3, 12/48 lines), [[ZNF16]] 0.797× (z -3.3, 11/48 lines), [[ACSF3]] 0.792× (z -3.3, 12/48 lines), [[ZNF2]] 0.824× (z -3.3, 3/47 lines), [[ZNF251]] 0.831× (z -3.2, 17/48 lines), [[ALG5]] 0.833× (z -3.2, 8/48 lines), [[ZNF767P-1]] 0.803× (z -3.2, 19/49 lines)

**0.5 µM** (6 genes, none with an alert): [[SCFD2]] 0.792× (z -3.6, 20/48 lines), [[ALG14]] 0.827× (z -3.4, 10/46 lines), [[ZNF181]] 0.775× (z -3.3, 8/42 lines), [[ENSG00000285572]] 0.696× (z -3.1, 8/31 lines), [[ENSG00000288710]] 0.732× (z -3.1, 11/41 lines), [[LINC02026]] 0.685× (z -2.9, 5/25 lines)

**5 µM** (18 genes, none with an alert; 12 shown): [[SCFD2]] 0.640× (z -6.9, 36/48 lines), [[LINC02937]] 0.670× (z -4.0, 19/47 lines), [[METTL13]] 0.829× (z -3.9, 7/47 lines), [[MPC1]] 0.820× (z -3.8, 9/48 lines), [[ENSG00000270571]] 0.590× (z -3.7, 8/40 lines), [[FAM222A-AS1]] 0.697× (z -3.6, 8/41 lines), [[PYGO2]] 0.771× (z -3.3, 15/47 lines), [[ENSG00000249476]] 0.630× (z -3.3, 20/47 lines), [[GABPB1-AS1]] 0.809× (z -3.2, 11/46 lines), [[SUGCT]] 0.811× (z -3.1, 10/44 lines), [[PUS10]] 0.826× (z -3.1, 4/47 lines), [[MAP2K6]] 0.714× (z -3.0, 4/26 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 170]] (-2.2) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[C-33 A (line)]] (-3.4), [[SK-MEL-2 (line)]] (-3.2) | [[NCI-H2030 (line)]] (1.32), [[C32 (line)]] (1.27), [[NCI-H661 (line)]] (1.27), [[COLO 205 (line)]] (1.24) · weakest: [[NCI-H2122 (line)]] (0.143), [[RKO (line)]] (0.449), [[A-172 (line)]] (0.493) |
| 0.5 µM | — | [[H4 (line)]] (1.73), [[AN3 CA (line)]] (1.65), [[Panc 03.27 (line)]] (1.63), [[NCI-H1573 (line)]] (1.39) · weakest: [[C32 (line)]] (-0.314), [[C-33 A (line)]] (-0.0800), [[SNU-1 (line)]] (0.0394) |
| 5 µM | — | [[COLO 205 (line)]] (1.42), [[A549 (line)]] (1.35), [[MIA PaCa-2 (line)]] (1.35), [[NCI-H2030 (line)]] (1.35) · weakest: [[SNU-1 (line)]] (0.370), [[NCI-H661 (line)]] (0.538), [[NCI-H23 (line)]] (0.566) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 6 next most similar without an alert.*

- [[Neratinib (drug)]] (+0.53, EGFR/ERBB inhibitor); [[Sunitinib (drug)]] (+0.48, Multi-TK inhibitor, ⚠ vector dose flagged: toxic); [[Pitavastatin (Calcium) (drug)]] (+0.48, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Fingolimod (hydrochloride) (drug)]] (+0.46, unclear, ⚠ vector dose flagged: toxic); [[Docetaxel (Trihydrate) (drug)]] (+0.45, Microtubule inhibitor); [[Plicamycin (drug)]] (+0.45, unclear, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Dexmedetomidine (drug)]] (+0.44, Adrenoceptor agonist, ⚠ only 9 significant genes); [[Artesunate (drug)]] (+0.44, JAK/STAT inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.44, unclear); [[Adagrasib (drug)]] (+0.43, RAS inhibitor); [[Decitabine (drug)]] (+0.42, DNA methyltransferase inhibitor); [[Saquinavir (drug)]] (+0.42, unclear); [[Terfenadine (drug)]] (+0.40, unclear); [[Aprepitant (drug)]] (+0.40, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 20 arrows, 20 of them with an alert ⚠; grade A 0, B 10, C 10. Shown: the 15 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PRSS23]] | 0.05 µM | B | PRSS23 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express PRSS23 (13) vs lines expressing it (35) | the lines without PRSS23: 0.75× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.81× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[CD44]] | 0.05 µM | B | CD44 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express CD44 (15) vs lines expressing it (33) | the lines without CD44: 0.77× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[SPOCK1]] | 0.05 µM | B | SPOCK1 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.79× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[KCNMA1]] | 0.05 µM | B | KCNMA1 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.79× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[PTGR1]] | 0.05 µM | B | PTGR1 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express PTGR1 (8) vs lines expressing it (40) | the lines without PTGR1: 0.80× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: ANXA2, ZNF717 |
| [[SIRLNT]] | 0.05 µM | B | SIRLNT activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.76× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[LINC02057]] | 0.05 µM | B | LINC02057 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express LINC02057 (25) vs lines expressing it (23) | the lines without LINC02057: 0.79× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[ALDH3B1]] | 0.05 µM | B | ALDH3B1 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.75× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[ENSG00000259200]] | 0.05 µM | B | ENSG00000259200 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express ENSG00000259200 (18) vs lines expressing it (30) | the lines without ENSG00000259200: 0.81× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, CSGALNACT1, ENSG00000232692; maybe low, not absent |
| [[TBILA]] | 0.05 µM | C | TBILA activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.70× the cells of the other lines | 0.021 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| [[ISG20]] | 0.05 µM | C | ISG20 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 0.68× the cells of the other lines | 0.025 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| [[PSMB8]] | 0.05 µM | C | PSMB8 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.69× the cells of the other lines | 0.033 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] | 0.05 µM | C | ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.66× the cells of the other lines | 0.033 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| [[CEBPD]], [[GCA]] | 0.05 µM | C | CEBPD, GCA activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.66× the cells of the other lines | 0.038 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Cyclosporin A"
- `tables/drugdoses.parquet` — dd in 296, 297, 298
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

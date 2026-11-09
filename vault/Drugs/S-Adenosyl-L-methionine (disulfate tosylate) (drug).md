---
drug: "S-Adenosyl-L-methionine (disulfate tosylate)"
type: "drug"
salt_base: "S-Adenosyl-L-methionine"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 106
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# S-Adenosyl-L-methionine (disulfate tosylate)

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 56 / 25 / 106; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.35 / 0.52.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:C11 | 11 / 45 | — | -0.01 | +0.1/+1.1/+0.3 | — |
| 0.5 µM | [[Plate 05]]:C11 | 2 / 23 | — | +0.65 | +0.7/+1.4/-0.4 | — |
| 5 µM | [[Plate 14]]:C11 | 38 / 68 | 0.868 | +0.17 | -0.7/+1.0/-0.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (11 genes, none with an alert): [[GNL2]] 1.31× (z +3.8, 35/48 lines), [[NANS]] 1.27× (z +3.6, 24/48 lines), [[SDE2]] 1.24× (z +3.2, 14/48 lines), [[COQ10B]] 1.26× (z +3.1, 24/48 lines), [[HIVEP3]] 1.21× (z +3.1, 13/41 lines), [[TRIM3]] 1.29× (z +3.1, 7/48 lines), [[HEXIM1]] 1.24× (z +3.0, 15/48 lines), [[ENSG00000288632]] 1.28× (z +2.9, 7/48 lines), [[NOLC1]] 1.25× (z +2.9, 19/48 lines), [[TAF13]] 1.25× (z +2.8, 12/48 lines), [[HSPH1]] 1.28× (z +2.6, 12/48 lines)

**0.5 µM** (2 genes, none with an alert): [[ENSG00000289318]] 1.41× (z +3.6, 6/35 lines), [[HIVEP3]] 1.24× (z +3.4, 19/41 lines)

**5 µM** (38 genes, none with an alert; 12 shown): [[MED26]] 1.32× (z +4.5, 38/49 lines), [[GNL2]] 1.23× (z +4.3, 34/49 lines), [[ARG2]] 1.33× (z +4.2, 18/44 lines), [[POFUT2]] 1.22× (z +4.1, 23/48 lines), [[RRP12]] 1.33× (z +4.1, 34/49 lines), [[LGMN]] 1.23× (z +4.1, 22/48 lines), [[BLZF1]] 1.21× (z +4.1, 21/49 lines), [[NOLC1]] 1.25× (z +4.0, 40/49 lines), [[SMIM41]] 1.52× (z +3.9, 15/45 lines), [[COQ10B]] 1.23× (z +3.9, 28/49 lines), [[ENSG00000259052]] 1.31× (z +3.7, 3/44 lines), [[UBE2S]] 1.32× (z +3.7, 20/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (45 genes, none with an alert; 12 shown): [[FAM86HP]] 0.613× (z -4.0, 10/39 lines), [[C12orf60]] 0.710× (z -4.0, 14/45 lines), [[RHCE]] 0.677× (z -3.9, 11/44 lines), [[CHODL]] 0.618× (z -3.9, 8/38 lines), [[ADGRL3]] 0.746× (z -3.8, 6/23 lines), [[ZNF701]] 0.814× (z -3.7, 5/42 lines), [[ZNF540]] 0.741× (z -3.7, 3/41 lines), [[RFX3-DT]] 0.726× (z -3.7, 20/45 lines), [[RHOU]] 0.684× (z -3.7, 5/35 lines), [[UNC79]] 0.705× (z -3.7, 8/44 lines), [[ENSG00000232732]] 0.669× (z -3.7, 10/37 lines), [[UFL1-AS1]] 0.669× (z -3.7, 17/46 lines)

**0.5 µM** (23 genes, none with an alert; 12 shown): [[DSC3]] 0.626× (z -5.0, 3/17 lines), [[NLRP2]] 0.709× (z -4.1, 0/15 lines), [[GPR158]] 0.802× (z -4.1, 6/26 lines), [[KBTBD12]] 0.547× (z -4.0, 2/12 lines), [[RAD52]] 0.812× (z -3.9, 12/48 lines), [[LRRN1]] 0.622× (z -3.9, 1/16 lines), [[ENSG00000236283]] 0.702× (z -3.8, 4/34 lines), [[ADGRF4]] 0.634× (z -3.7, 1/23 lines), [[RHOB]] 0.718× (z -3.7, 27/47 lines), [[LINC02967]] 0.538× (z -3.7, 3/12 lines), [[ENSG00000286046]] 0.624× (z -3.6, 3/35 lines), [[FOSL2]] 0.815× (z -3.5, 15/48 lines)

**5 µM** (68 genes, none with an alert; 12 shown): [[UBE2Q1]] 0.792× (z -4.9, 27/48 lines), [[ENSG00000286787]] 0.693× (z -4.5, 23/47 lines), [[RHOU]] 0.724× (z -4.4, 16/37 lines), [[ENSG00000229618]] 0.823× (z -4.4, 2/17 lines), [[CASC9]] 0.800× (z -4.4, 10/27 lines), [[RERG]] 0.700× (z -4.1, 7/23 lines), [[THBS4]] 0.714× (z -4.1, 15/41 lines), [[ZNF19]] 0.765× (z -4.0, 14/46 lines), [[AJUBA-DT]] 0.715× (z -4.0, 13/43 lines), [[ENSG00000289956]] 0.808× (z -4.0, 13/40 lines), [[UFL1-AS1]] 0.735× (z -4.0, 20/47 lines), [[ZBED5-AS1]] 0.746× (z -4.0, 9/45 lines)

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
| 0.05 µM | — | [[COLO 205 (line)]] (1.56), [[SW48 (line)]] (1.50), [[SW 1088 (line)]] (1.46), [[hTERT-HPNE (line)]] (1.45) · weakest: [[CHP-212 (line)]] (0.424), [[SW 1271 (line)]] (0.551), [[A-427 (line)]] (0.717) |
| 0.5 µM | [[Hs 766T (line)]] (-6.4) | [[MIA PaCa-2 (line)]] (1.88), [[H4 (line)]] (1.76), [[SW 1088 (line)]] (1.50), [[C32 (line)]] (1.45) · weakest: [[LS 180 (line)]] (0.440), [[KATO III (line)]] (0.464), [[Hs 766T (line)]] (0.468) |
| 5 µM | — | [[C32 (line)]] (1.34), [[hTERT-HPNE (line)]] (1.30), [[MIA PaCa-2 (line)]] (1.30), [[RKO (line)]] (1.30) · weakest: [[NCI-H2122 (line)]] (6.1e-04), [[BT-474 (line)]] (0.608), [[HepG2_C3A (line)]] (0.696) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[ML264 (drug)]] (+0.70, unclear, ⚠ only 5 significant genes); [[Ranolazine (drug)]] (+0.64, unclear); [[Sacubitril_Valsartan (drug)]] (+0.60, unclear, ⚠ only 1 significant gene); [[Allopurinol (drug)]] (+0.57, unclear); [[Cloxacillin (sodium) (drug)]] (+0.55, unclear); [[Artemether (drug)]] (+0.54, unclear, ⚠ only 7 significant genes); [[Lapatinib ditosylate (drug)]] (+0.53, EGFR/ERBB inhibitor, ⚠ only 9 significant genes); [[Rucaparib (phosphate) (drug)]] (+0.52, DNA synthesis/repair inhibitor, ⚠ only 5 significant genes); [[Mebendazole (drug)]] (+0.51, Microtubule inhibitor); [[Clopidogrel (drug)]] (+0.49, unclear); [[Goserelin (acetate) (drug)]] (+0.46, unclear); [[Volasertib (drug)]] (+0.46, unclear); [[Quinidine (15% dihydroquinidine) (drug)]] (+0.45, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 16 arrows, 16 of them with an alert ⚠; grade A 0, B 14, C 2. Shown: the 15 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[RAB27B]] | 5 µM | B | RAB27B activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 5 µM (protects the cells) | lines that do not express RAB27B (15) vs lines expressing it (33) | the lines without RAB27B: 0.88× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3 |
| [[ALDH3B1]] | 5 µM | B | ALDH3B1 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 5 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.84× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[RNF103-CHMP3]] | 0.5 µM | B | RNF103-CHMP3 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 0.5 µM (protects the cells) | lines that do not express RNF103-CHMP3 (5) vs lines expressing it (43) | the lines without RNF103-CHMP3: 0.77× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: TMEM144, YBX3, DTX4; maybe low, not absent |
| [[ENSG00000289526]] | 5 µM | B | ENSG00000289526 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 5 µM (protects the cells) | lines that do not express ENSG00000289526 (18) vs lines expressing it (30) | the lines without ENSG00000289526: 0.92× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; co-occurs with BRCA2; also absent: TLR6, TMEM158, NALCN; maybe low, not absent |
| [[GPRC5D-AS1]] | 5 µM | B | GPRC5D-AS1 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 5 µM (protects the cells) | lines that do not express GPRC5D-AS1 (5) vs lines expressing it (43) | the lines without GPRC5D-AS1: 0.80× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: S100A6, LGALS3BP, NMI; maybe low, not absent |
| [[FAS]] | 0.5 µM | B | FAS activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 0.5 µM (protects the cells) | lines that do not express FAS (8) vs lines expressing it (40) | the lines without FAS: 0.89× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| [[TLR1]] | 5 µM | B | TLR1 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 5 µM (protects the cells) | lines that do not express TLR1 (15) vs lines expressing it (33) | the lines without TLR1: 0.88× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[SH3GL3]] | 0.5 µM | B | SH3GL3 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 0.5 µM (protects the cells) | lines that do not express SH3GL3 (21) vs lines expressing it (27) | the lines without SH3GL3: 0.91× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: S1PR3, SPANXA2-OT1, SALL1 |
| [[IL15]] | 5 µM | B | IL15 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 5 µM (protects the cells) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 0.83× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[ZHX2]] | 5 µM | B | ZHX2 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 5 µM (protects the cells) | lines that do not express ZHX2 (7) vs lines expressing it (41) | the lines without ZHX2: 0.84× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[ZNF341-AS1]] | 5 µM | B | ZNF341-AS1 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 5 µM (protects the cells) | lines that do not express ZNF341-AS1 (7) vs lines expressing it (41) | the lines without ZNF341-AS1: 0.85× the cells of the other lines | 0.097 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[NMRAL2P]] | 5 µM | B | NMRAL2P activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 5 µM (protects the cells) | lines that do not express NMRAL2P (18) vs lines expressing it (30) | the lines without NMRAL2P: 0.89× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[TGFBR2]] | 5 µM | B | TGFBR2 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 5 µM (protects the cells) | lines that do not express TGFBR2 (7) vs lines expressing it (41) | the lines without TGFBR2: 0.81× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[PI3]] | 5 µM | B | PI3 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 5 µM (protects the cells) | lines that do not express PI3 (27) vs lines expressing it (21) | the lines without PI3: 0.91× the cells of the other lines | 0.0997 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A |
| [[ZDHHC1]] | 0.5 µM | C | ZDHHC1 activity raises the cells' numbers under S-Adenosyl-L-methionine (disulfate tosylate) 0.5 µM (protects the cells) | lines that do not express ZDHHC1 (4) vs lines expressing it (44) | the lines without ZDHHC1: 0.78× the cells of the other lines | 0.030 | ⚠ few lines (4 vs 46); across organs; also absent: PDE4C, KIF5A |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "S-Adenosyl-L-methionine (disulfate tosylate)"
- `tables/drugdoses.parquet` — dd in 923, 924, 925
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

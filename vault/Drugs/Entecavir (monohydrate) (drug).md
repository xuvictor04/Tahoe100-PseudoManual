---
drug: "Entecavir (monohydrate)"
type: "drug"
salt_base: "Entecavir"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 32
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Entecavir (monohydrate)

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 6 / 32 / 30; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.04 / -0.18.
> Flags by dose: - / - / plate-row cell shift.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:A4 | 0 / 6 | — | -0.10 | +0.2/-0.0/+0.3 | — |
| 0.5 µM | [[Plate 08]]:A4 | 16 / 16 | — | +0.91 | +1.5/+1.3/+1.5 | — |
| 5 µM | [[Plate 09]]:A4 | 11 / 19 | — | +1.22 | +2.0/-0.4/-2.3 | plate-row cell shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (16 genes, none with an alert; 12 shown): [[UBE2Q2P2]] 1.23× (z +3.8, 21/49 lines), [[RPS10-NUDT3]] 1.57× (z +3.7, 11/47 lines), [[SPATA5L1]] 1.27× (z +3.7, 8/48 lines), [[PPTC7]] 1.25× (z +3.3, 20/49 lines), [[SUPV3L1]] 1.27× (z +3.2, 17/48 lines), [[PMS2P3]] 1.48× (z +3.2, 3/46 lines), [[RPS3A]] 1.27× (z +3.1, 15/48 lines), [[STRAP]] 1.22× (z +3.1, 20/49 lines), [[CD83]] 1.43× (z +3.0, 12/44 lines), [[KCTD6]] 1.29× (z +3.0, 1/47 lines), [[PPAT]] 1.21× (z +3.0, 10/48 lines), [[PSMC6]] 1.22× (z +3.0, 11/49 lines)

**5 µM** (11 genes, none with an alert): [[NPIPB14P]] 1.48× (z +5.7, 27/48 lines), [[UBE2Q2P2]] 1.29× (z +4.6, 28/48 lines), [[ENSG00000291228]] 1.36× (z +3.8, 20/48 lines), [[GYS1]] 1.24× (z +3.6, 24/48 lines), [[BRIP1]] 1.32× (z +3.6, 20/47 lines), [[ENSG00000290835]] 1.23× (z +3.5, 11/48 lines), [[DDB2]] 1.23× (z +3.5, 11/46 lines), [[MCF2L]] 1.29× (z +3.4, 8/33 lines), [[CEP250]] 1.22× (z +3.4, 25/48 lines), [[ZNF608]] 1.28× (z +3.2, 11/36 lines), [[RNF150]] 1.26× (z +3.0, 5/32 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (6 genes, none with an alert): [[SUOX]] 0.698× (z -4.3, 16/42 lines), [[ZNF35]] 0.792× (z -3.5, 6/44 lines), [[PET100]] 0.664× (z -3.5, 12/42 lines), [[GTF2IP4]] 0.732× (z -3.3, 7/38 lines), [[CHKB]] 0.783× (z -3.2, 9/47 lines), [[BORCS7-ASMT]] 0.780× (z -3.1, 11/46 lines)

**0.5 µM** (16 genes, none with an alert; 12 shown): [[CSTF2T]] 0.713× (z -3.8, 12/45 lines), [[SEPTIN5]] 0.687× (z -3.5, 8/36 lines), [[ELFN2]] 0.725× (z -3.5, 4/28 lines), [[RAB11B-AS1]] 0.742× (z -3.3, 3/46 lines), [[MYOM3]] 0.693× (z -3.3, 3/20 lines), [[TBX18]] 0.783× (z -3.2, 2/21 lines), [[ENSG00000235337]] 0.692× (z -3.2, 0/22 lines), [[CARD6]] 0.723× (z -3.2, 4/30 lines), [[SRD5A3]] 0.779× (z -3.2, 4/46 lines), [[TRIM65]] 0.805× (z -3.0, 13/48 lines), [[VILL]] 0.720× (z -3.0, 4/29 lines), [[AARS2]] 0.830× (z -3.0, 6/48 lines)

**5 µM** (19 genes, none with an alert; 12 shown): [[DPH3]] 0.742× (z -4.4, 11/48 lines), [[YOD1]] 0.748× (z -4.1, 20/46 lines), [[GNPTG]] 0.787× (z -4.0, 11/48 lines), [[PSMD6]] 0.764× (z -3.9, 19/48 lines), [[CRB3]] 0.533× (z -3.8, 1/19 lines), [[CCNB1IP1]] 0.785× (z -3.6, 15/48 lines), [[BAG1]] 0.831× (z -3.5, 6/48 lines), [[NIP7]] 0.751× (z -3.5, 7/47 lines), [[EIF4E]] 0.791× (z -3.4, 21/48 lines), [[HNRNPAB]] 0.730× (z -3.4, 24/48 lines), [[PSMC6]] 0.803× (z -3.4, 20/48 lines), [[CMTM6]] 0.817× (z -3.3, 15/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 182]] (+2.5), [[Module 207]] (+2.1) | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[NCI-H1792 (line)]] (1.80), [[NCI-H1573 (line)]] (1.60), [[C32 (line)]] (1.47), [[HS-578T (line)]] (1.47) · weakest: [[NCI-H2122 (line)]] (-0.188), [[BT-474 (line)]] (0.167), [[SNU-1 (line)]] (0.540) |
| 5 µM | — | [[NCI-H1792 (line)]] (1.48), [[NCI-H460 (line)]] (1.43), [[LOX-IMVI (line)]] (1.41), [[RPMI-7951 (line)]] (1.39) · weakest: [[KATO III (line)]] (0.435), [[LoVo (line)]] (0.438), [[HepG2_C3A (line)]] (0.498) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[Tetracycline (hydrochloride) (drug)]] (+0.77, unclear, ⚠ only 6 significant genes); [[Quinidine (15% dihydroquinidine) (drug)]] (+0.69, unclear); [[Tomivosertib (drug)]] (+0.64, Protein synthesis inhibitor); [[Ivabradine (hydrochloride) (drug)]] (+0.60, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Tolcapone (drug)]] (+0.56, unclear, ⚠ only 6 significant genes); [[Rucaparib (phosphate) (drug)]] (+0.55, DNA synthesis/repair inhibitor, ⚠ only 5 significant genes); [[Ranolazine (drug)]] (+0.54, unclear); [[Altretamine (drug)]] (+0.54, DNA synthesis/repair inhibitor, ⚠ only 1 significant gene); [[Piroxicam (drug)]] (+0.53, Cyclooxygenase inhibitor); [[Pravastatin (sodium) (drug)]] (+0.53, unclear); [[Trimetrexate (drug)]] (+0.52, DNA synthesis/repair inhibitor); [[Pasireotide (acetate) (drug)]] (+0.51, unclear); [[Terfenadine (drug)]] (+0.51, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 60 arrows, 60 of them with an alert ⚠; grade A 0, B 54, C 6. Shown: the 15 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[COL17A1]] | 5 µM | B | COL17A1 activity lowers the cells' numbers under Entecavir (monohydrate) 5 µM (makes them more sensitive) | lines that do not express COL17A1 (34) vs lines expressing it (14) | the lines without COL17A1: 1.27× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[EHF]] | 5 µM | B | EHF activity lowers the cells' numbers under Entecavir (monohydrate) 5 µM (makes them more sensitive) | lines that do not express EHF (27) vs lines expressing it (21) | the lines without EHF: 1.21× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3 |
| [[ALDH3B1]] | 0.5 µM | B | ALDH3B1 activity raises the cells' numbers under Entecavir (monohydrate) 0.5 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.74× the cells of the other lines | 0.049 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[ENSG00000230647]] | 0.5 µM | B | ENSG00000230647 activity raises the cells' numbers under Entecavir (monohydrate) 0.5 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.81× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[ITGB6]] | 5 µM | B | ITGB6 activity lowers the cells' numbers under Entecavir (monohydrate) 5 µM (makes them more sensitive) | lines that do not express ITGB6 (32) vs lines expressing it (16) | the lines without ITGB6: 1.22× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[ARHGEF6]] | 5 µM | B | ARHGEF6 activity raises the cells' numbers under Entecavir (monohydrate) 5 µM (protects the cells) | lines that do not express ARHGEF6 (20) vs lines expressing it (28) | the lines without ARHGEF6: 0.84× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[ESRP1]] | 5 µM | B | ESRP1 activity lowers the cells' numbers under Entecavir (monohydrate) 5 µM (makes them more sensitive) | lines that do not express ESRP1 (31) vs lines expressing it (17) | the lines without ESRP1: 1.24× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[ATP2C2]] | 5 µM | B | ATP2C2 activity lowers the cells' numbers under Entecavir (monohydrate) 5 µM (makes them more sensitive) | lines that do not express ATP2C2 (32) vs lines expressing it (16) | the lines without ATP2C2: 1.23× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[TMPRSS2]] | 5 µM | B | TMPRSS2 activity lowers the cells' numbers under Entecavir (monohydrate) 5 µM (makes them more sensitive) | lines that do not express TMPRSS2 (35) vs lines expressing it (13) | the lines without TMPRSS2: 1.27× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[HRH1]] | 0.5 µM | B | HRH1 activity raises the cells' numbers under Entecavir (monohydrate) 0.5 µM (protects the cells) | lines that do not express HRH1 (10) vs lines expressing it (38) | the lines without HRH1: 0.73× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[DAPP1]] | 5 µM | B | DAPP1 activity lowers the cells' numbers under Entecavir (monohydrate) 5 µM (makes them more sensitive) | lines that do not express DAPP1 (39) vs lines expressing it (9) | the lines without DAPP1: 1.25× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B |
| [[DNAJA4]] | 5 µM | B | DNAJA4 activity lowers the cells' numbers under Entecavir (monohydrate) 5 µM (makes them more sensitive) | lines that do not express DNAJA4 (22) vs lines expressing it (26) | the lines without DNAJA4: 1.24× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: COL17A1, ENSG00000262302, KIAA0040 |
| [[BMPER]] | 5 µM | B | BMPER activity raises the cells' numbers under Entecavir (monohydrate) 5 µM (protects the cells) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 0.83× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[KCNMA1]] | 0.5 µM | B | KCNMA1 activity raises the cells' numbers under Entecavir (monohydrate) 0.5 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.78× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[GXYLT2]] | 5 µM | B | GXYLT2 activity raises the cells' numbers under Entecavir (monohydrate) 5 µM (protects the cells) | lines that do not express GXYLT2 (11) vs lines expressing it (37) | the lines without GXYLT2: 0.80× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Entecavir (monohydrate)"
- `tables/drugdoses.parquet` — dd in 409, 410, 411
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

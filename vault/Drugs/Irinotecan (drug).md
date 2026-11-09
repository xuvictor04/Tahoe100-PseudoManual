---
drug: "Irinotecan"
type: "drug"
salt_base: "Irinotecan"
targets: "TOP1"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 53
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Irinotecan

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: TOP1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 30 / 53; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.20 / -0.22.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:A8 | 1 / 0 | — | +0.31 | +1.1/+0.7/+1.4 | — |
| 0.5 µM | [[Plate 02]]:A8 | 26 / 4 | — | -0.12 | +2.2/-0.3/-1.0 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:A8 | 13 / 40 | — | +1.11 | +3.3/+0.5/+0.9 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[BOP1]] 1.32× (z +2.8, 1/47 lines)

**0.5 µM** (26 genes, none with an alert; 12 shown): [[DIAPH3]] 1.29× (z +3.9, 20/45 lines), [[MMS22L]] 1.39× (z +3.8, 16/48 lines), [[MIR924HG]] 1.50× (z +3.6, 17/40 lines), [[BRIP1]] 1.45× (z +3.6, 19/47 lines), [[RFC3]] 1.28× (z +3.5, 17/47 lines), [[MELK]] 1.36× (z +3.5, 14/45 lines), [[DTL]] 1.42× (z +3.5, 11/48 lines), [[POLQ]] 1.37× (z +3.4, 17/46 lines), [[KIF24]] 1.35× (z +3.3, 6/47 lines), [[DERA]] 1.30× (z +3.3, 10/48 lines), [[SRBD1]] 1.26× (z +3.3, 17/48 lines), [[VRK1]] 1.26× (z +3.3, 13/48 lines)

**5 µM** (13 genes, none with an alert; 12 shown): [[PCNA]] 1.82× (z +3.2, 14/46 lines), [[XRCC3]] 1.58× (z +3.1, 1/45 lines), [[EXO1]] 1.56× (z +3.0, 6/46 lines), [[E2F7]] 1.41× (z +2.9, 6/43 lines), [[CENPU]] 1.61× (z +2.9, 12/48 lines), [[BLM]] 1.37× (z +2.8, 10/46 lines), [[ATAD5]] 1.34× (z +2.8, 10/48 lines), [[CCNE2]] 1.53× (z +2.8, 7/45 lines), [[WDHD1]] 1.30× (z +2.7, 5/48 lines), [[ATAD2]] 1.35× (z +2.7, 10/49 lines), [[GINS4]] 1.47× (z +2.7, 8/46 lines), [[NETO2]] 1.30× (z +2.7, 2/37 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (4 genes, none with an alert): [[EIF2B4]] 0.765× (z -3.7, 5/48 lines), [[PHAX]] 0.735× (z -3.3, 17/48 lines), [[SLC50A1]] 0.743× (z -3.0, 7/48 lines), [[HLA-E]] 0.753× (z -3.0, 28/47 lines)

**5 µM** (40 genes, none with an alert; 12 shown): [[FHIT]] 0.475× (z -4.9, 39/44 lines), [[ENSG00000223727]] 0.398× (z -4.8, 20/41 lines), [[C1QTNF7-AS1]] 0.621× (z -4.8, 19/47 lines), [[LINC02935]] 0.502× (z -4.3, 11/43 lines), [[DIAPH2]] 0.669× (z -4.2, 30/43 lines), [[ENSG00000289986]] 0.536× (z -4.1, 7/43 lines), [[WWOX]] 0.552× (z -4.0, 34/45 lines), [[LRGUK]] 0.454× (z -3.9, 15/46 lines), [[NAV2]] 0.655× (z -3.7, 17/33 lines), [[MAP4]] 0.811× (z -3.7, 19/49 lines), [[ENSG00000226965]] 0.622× (z -3.7, 14/38 lines), [[ENSG00000285713]] 0.648× (z -3.6, 7/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 006]] (+2.2) | — |
| 5 µM | — | [[Module 200]] (-2.3) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[A-172 (line)]] (-3.4), [[NCI-H661 (line)]] (-3.3), [[LOX-IMVI (line)]] (-3.1) | [[Hs 766T (line)]] (1.90), [[MIA PaCa-2 (line)]] (1.82), [[HOP62 (line)]] (1.73), [[SW 1088 (line)]] (1.67) · weakest: [[CHP-212 (line)]] (-0.297), [[NCI-H661 (line)]] (0.266), [[SHP-77 (line)]] (0.363) |
| 5 µM | — | [[MIA PaCa-2 (line)]] (1.68), [[SNU-1 (line)]] (1.49), [[SW 1088 (line)]] (1.44), [[HOP62 (line)]] (1.37) · weakest: [[NCI-H596 (line)]] (0.357), [[SHP-77 (line)]] (0.417), [[AsPC-1 (line)]] (0.502) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Irinotecan (hydrochloride) (drug)]] (+0.71, DNA synthesis/repair inhibitor); [[Cytarabine (hydrochloride) (drug)]] (+0.59, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Cytarabine (drug)]] (+0.55, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Gemcitabine (drug)]] (+0.50, DNA synthesis/repair inhibitor); [[Topotecan (hydrochloride) (drug)]] (+0.50, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: toxic; cell-cycle shift); [[Amsacrine (drug)]] (+0.42, DNA synthesis/repair inhibitor); [[Plicamycin (drug)]] (+0.42, unclear, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Pemigatinib (drug)]] (+0.37, Other TK inhibitor); [[Vilanterol (drug)]] (+0.31, Adrenoceptor agonist); [[Minodronic acid (drug)]] (+0.31, unclear); [[Methotrexate (drug)]] (+0.29, DNA synthesis/repair inhibitor); [[Pimitespib (drug)]] (+0.28, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 44 arrows, 44 of them with an alert ⚠; grade A 0, B 36, C 8. Shown: the 15 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[AHR]] | 0.5 µM | B | AHR activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 0.74× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[ENSG00000258919]] | 0.5 µM | B | ENSG00000258919 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express ENSG00000258919 (23) vs lines expressing it (25) | the lines without ENSG00000258919: 0.76× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC02320, ENSG00000266088, DIO3OS |
| [[LINC02320]] | 0.5 µM | B | LINC02320 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express LINC02320 (19) vs lines expressing it (29) | the lines without LINC02320: 0.77× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[RASGEF1B]] | 0.5 µM | B | RASGEF1B activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express RASGEF1B (10) vs lines expressing it (38) | the lines without RASGEF1B: 0.76× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[SLC2A9]] | 0.5 µM | B | SLC2A9 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express SLC2A9 (6) vs lines expressing it (42) | the lines without SLC2A9: 0.71× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[TBC1D8]] | 0.5 µM | B | TBC1D8 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express TBC1D8 (6) vs lines expressing it (42) | the lines without TBC1D8: 0.76× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[SCAT1]] | 0.5 µM | B | SCAT1 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express SCAT1 (16) vs lines expressing it (32) | the lines without SCAT1: 0.79× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[AQP3]] | 0.5 µM | B | AQP3 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express AQP3 (19) vs lines expressing it (29) | the lines without AQP3: 0.78× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[KPNA7]] | 0.5 µM | B | KPNA7 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express KPNA7 (10) vs lines expressing it (38) | the lines without KPNA7: 0.78× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[ATP1B1]] | 0.5 µM | B | ATP1B1 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 0.75× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[FER1L6]] | 0.5 µM | B | FER1L6 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express FER1L6 (7) vs lines expressing it (41) | the lines without FER1L6: 0.75× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000228566, LINC00298, GNA14; maybe low, not absent |
| [[TGFA]] | 0.5 µM | B | TGFA activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express TGFA (17) vs lines expressing it (31) | the lines without TGFA: 0.77× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[PRR15]] | 0.5 µM | B | PRR15 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express PRR15 (28) vs lines expressing it (20) | the lines without PRR15: 0.76× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |
| [[LGALS3BP]] | 0.5 µM | B | LGALS3BP activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 0.72× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[ENSG00000283321]] | 0.5 µM | B | ENSG00000283321 activity raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | lines that do not express ENSG00000283321 (7) vs lines expressing it (41) | the lines without ENSG00000283321: 0.80× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: AHR, PSMB8, CXCL2 |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 98 arrows, 98 of them with an alert ⚠; grade A 0, B 98, C 0. Shown: the 15 strongest; 83 more arrows (83 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[TOP1]] | [[SRBD1]] | moves it that way too | B | TOP1 activity lowers SRBD1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 1.4% of all compounds | 0.010 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[ENSG00000227240]] | moves it that way too | B | TOP1 activity raises ENSG00000227240's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 2.0% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[ENSG00000229618]] | moves it that way too | B | TOP1 activity raises ENSG00000229618's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[ENSG00000267053]] | moves it that way too | B | TOP1 activity lowers ENSG00000267053's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[MND1]] | moves it that way too | B | TOP1 activity lowers MND1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[LINC03041]] | moves it that way too | B | TOP1 activity raises LINC03041's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[TAF4]] | moves it that way too | B | TOP1 activity lowers TAF4's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.4% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[CENPO]] | moves it that way too | B | TOP1 activity lowers CENPO's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[MELK]] | moves it that way too | B | TOP1 activity lowers MELK's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[POLQ]] | moves it that way too | B | TOP1 activity lowers POLQ's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[RFC3]] | moves it that way too | B | TOP1 activity lowers RFC3's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[TBC1D31]] | moves it that way too | B | TOP1 activity lowers TBC1D31's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[SEMA6A-AS1]] | moves it that way too | B | TOP1 activity raises SEMA6A-AS1's level | compounds that target TOP1: 2 of 3 lower it (Irinotecan, Topotecan) | 67% of the class's compounds vs 0.6% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP1]] | [[DNA2]] | moves it that way too | B | TOP1 activity lowers DNA2's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP1]] | [[FANCI]] | moves it that way too | B | TOP1 activity lowers FANCI's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Irinotecan"
- `tables/drugdoses.parquet` — dd in 561, 562, 563
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

---
drug: "Irinotecan (hydrochloride)"
type: "drug"
salt_base: "Irinotecan"
targets: "TOP1"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 137
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Irinotecan (hydrochloride)

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: TOP1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 13 / 35 / 137; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.33 / 0.41.
> Flags by dose: - / - / plate-row cell shift.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:A12 | 12 / 1 | — | -0.42 | -0.3/-0.8/-1.0 | — |
| 0.5 µM | [[Plate 08]]:A12 | 11 / 24 | — | +0.45 | +0.7/+0.9/-0.7 | — |
| 5 µM | [[Plate 09]]:A12 | 47 / 90 | — | +0.70 | +3.4/+0.8/-0.6 | plate-row cell shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (12 genes, none with an alert): [[ENSG00000289293]] 1.68× (z +4.5, 11/44 lines), [[ENSG00000254536]] 1.46× (z +4.0, 4/33 lines), [[AMZ1]] 1.27× (z +3.6, 0/45 lines), [[ENSG00000278996]] 1.86× (z +3.5, 16/45 lines), [[RPSAP52]] 1.36× (z +3.2, 6/25 lines), [[ENSG00000267053]] 1.37× (z +3.2, 3/36 lines), [[ENSG00000268870]] 1.29× (z +3.1, 3/41 lines), [[IDI2-AS1]] 1.43× (z +3.0, 11/45 lines), [[ZNF347]] 1.24× (z +3.0, 3/27 lines), [[CORO2B]] 1.36× (z +3.0, 5/34 lines), [[ADAM32]] 1.25× (z +2.8, 10/45 lines), [[RRAGC-DT]] 1.27× (z +2.7, 7/48 lines)

**0.5 µM** (11 genes, none with an alert): [[SLCO5A1]] 1.32× (z +4.0, 6/42 lines), [[DNAJC5]] 1.21× (z +3.6, 20/48 lines), [[TAF4]] 1.22× (z +3.6, 15/48 lines), [[PTPRJ]] 1.21× (z +3.4, 20/46 lines), [[CRYBB2P1-1]] 1.21× (z +3.3, 9/44 lines), [[GAS2L3]] 1.20× (z +3.2, 7/48 lines), [[ABTB2]] 1.24× (z +3.1, 18/41 lines), [[PICALM]] 1.20× (z +3.1, 22/48 lines), [[MED6]] 1.21× (z +3.1, 11/48 lines), [[ARL8B]] 1.23× (z +2.9, 20/48 lines), [[STAM]] 1.23× (z +2.9, 17/48 lines)

**5 µM** (47 genes, none with an alert; 12 shown): [[GINS4]] 1.45× (z +4.8, 15/47 lines), [[DNA2]] 1.29× (z +4.6, 18/48 lines), [[E2F7]] 1.29× (z +4.5, 17/43 lines), [[DTL]] 1.39× (z +4.5, 19/48 lines), [[EXO1]] 1.42× (z +4.4, 17/46 lines), [[FANCB]] 1.26× (z +4.3, 20/48 lines), [[WDHD1]] 1.25× (z +4.3, 15/48 lines), [[FANCI]] 1.31× (z +4.3, 27/48 lines), [[ATAD5]] 1.26× (z +4.1, 16/48 lines), [[BLM]] 1.26× (z +3.9, 15/45 lines), [[POLA2]] 1.25× (z +3.8, 13/47 lines), [[NTN1]] 1.25× (z +3.8, 12/30 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENPP4]] 0.828× (z -2.8, 5/30 lines)

**0.5 µM** (24 genes, none with an alert; 12 shown): [[POLDIP2]] 0.723× (z -5.2, 28/48 lines), [[RAD17]] 0.832× (z -4.4, 13/48 lines), [[PLA2G12B]] 0.509× (z -4.2, 17/45 lines), [[PEG3]] 0.573× (z -3.9, 0/7 lines), [[PAGR1]] 0.748× (z -3.9, 13/48 lines), [[GJB1]] 0.500× (z -3.9, 0/10 lines), [[PDGFRB]] 0.683× (z -3.5, 0/12 lines), [[USP9Y]] 0.812× (z -3.4, 0/18 lines), [[ENSG00000242021]] 0.768× (z -3.4, 1/18 lines), [[NELFE]] 0.786× (z -3.4, 15/48 lines), [[SLC9A3R2]] 0.687× (z -3.2, 12/45 lines), [[ENSG00000286863]] 0.806× (z -3.2, 1/25 lines)

**5 µM** (90 genes, none with an alert; 12 shown): [[ENSG00000223727]] 0.485× (z -7.0, 29/40 lines), [[ENSG00000226965]] 0.620× (z -6.8, 19/37 lines), [[FHIT]] 0.610× (z -5.9, 40/42 lines), [[KAZN]] 0.768× (z -5.9, 22/43 lines), [[POU5F1B]] 0.571× (z -5.8, 15/33 lines), [[ENSG00000227240]] 0.663× (z -5.7, 19/35 lines), [[C1QTNF7-AS1]] 0.736× (z -5.5, 22/45 lines), [[DIAPH2]] 0.760× (z -5.2, 29/41 lines), [[BCAS3]] 0.745× (z -5.1, 40/48 lines), [[ENSG00000286540]] 0.674× (z -4.9, 15/25 lines), [[WWOX]] 0.674× (z -4.9, 34/43 lines), [[CCSER1]] 0.729× (z -4.9, 21/28 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Module 064]] (-2.3) |
| 5 µM | — | [[Module 200]] (-2.9) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[SW 1271 (line)]] (1.89), [[HCT15 (line)]] (1.60), [[hTERT-HPNE (line)]] (1.59), [[AsPC-1 (line)]] (1.57) · weakest: [[KATO III (line)]] (0.486), [[AN3 CA (line)]] (0.546), [[HepG2_C3A (line)]] (0.585) |
| 5 µM | — | [[COLO 205 (line)]] (1.44), [[NCI-H2030 (line)]] (1.37), [[H4 (line)]] (1.33), [[HOP62 (line)]] (1.31) · weakest: [[NCI-H1792 (line)]] (0.512), [[AsPC-1 (line)]] (0.537), [[CHP-212 (line)]] (0.555) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[Irinotecan (drug)]] (+0.71, DNA synthesis/repair inhibitor); [[Cytarabine (drug)]] (+0.53, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Cytarabine (hydrochloride) (drug)]] (+0.45, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Methotrexate (drug)]] (+0.44, DNA synthesis/repair inhibitor); [[Delamanid (drug)]] (+0.44, unclear, ⚠ only 6 significant genes); [[Gemcitabine (drug)]] (+0.43, DNA synthesis/repair inhibitor); [[Topotecan (hydrochloride) (drug)]] (+0.32, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: toxic; cell-cycle shift); [[Raltitrexed (drug)]] (+0.31, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Hexylresorcinol (drug)]] (+0.31, unclear); [[Trimetrexate (drug)]] (+0.31, DNA synthesis/repair inhibitor); [[Vilanterol (drug)]] (+0.27, Adrenoceptor agonist); [[Quinestrol (drug)]] (+0.26, unclear); [[Ranolazine (drug)]] (+0.25, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 27 arrows, 27 of them with an alert ⚠; grade A 0, B 23, C 4. Shown: the 15 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.81× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[ALDH3B1]] | 0.5 µM | B | ALDH3B1 activity raises the cells' numbers under Irinotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.82× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[SRPX]] | 5 µM | B | SRPX activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express SRPX (22) vs lines expressing it (26) | the lines without SRPX: 0.85× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[HTRA1]] | 5 µM | B | HTRA1 activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express HTRA1 (19) vs lines expressing it (29) | the lines without HTRA1: 0.88× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| [[TEX41]] | 5 µM | B | TEX41 activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express TEX41 (29) vs lines expressing it (19) | the lines without TEX41: 0.83× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000280241, ADAM12 |
| [[RSPO3]] | 0.5 µM | B | RSPO3 activity raises the cells' numbers under Irinotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.81× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[ME3]] | 5 µM | B | ME3 activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express ME3 (13) vs lines expressing it (35) | the lines without ME3: 0.93× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: PLAAT3 |
| [[KCNMA1]] | 5 µM | B | KCNMA1 activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.84× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[CCL5]] | 5 µM | B | CCL5 activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express CCL5 (22) vs lines expressing it (26) | the lines without CCL5: 0.85× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| [[ENSG00000251537]] | 0.5 µM | B | ENSG00000251537 activity raises the cells' numbers under Irinotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ENSG00000251537 (9) vs lines expressing it (39) | the lines without ENSG00000251537: 0.85× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: FBXW10B, PCED1B, NHS; maybe low, not absent |
| [[ADAM12]] | 0.5 µM | B | ADAM12 activity raises the cells' numbers under Irinotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 0.86× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| [[CNRIP1]] | 0.5 µM | B | CNRIP1 activity raises the cells' numbers under Irinotecan (hydrochloride) 0.5 µM (protects the cells) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 0.88× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| [[SSPN]] | 5 µM | B | SSPN activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express SSPN (15) vs lines expressing it (33) | the lines without SSPN: 0.85× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| [[EPCAM]] | 5 µM | B | EPCAM activity lowers the cells' numbers under Irinotecan (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 1.15× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[SRGN]] | 5 µM | B | SRGN activity raises the cells' numbers under Irinotecan (hydrochloride) 5 µM (protects the cells) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 0.81× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |

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

- `tables/drugs.parquet` — drug == "Irinotecan (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 564, 565, 566
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

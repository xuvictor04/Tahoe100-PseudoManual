---
drug: "Docetaxel (Trihydrate)"
type: "drug"
salt_base: "Docetaxel"
targets: "TUBB1, TUBB3, TUBB4B, TUBB4A, TUBB2A, TUBB2B"
moa_fine: "Microtubule inhibitor"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 829
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Docetaxel (Trihydrate)

*Microtubule inhibitor (unclear) · targets: TUBB1, TUBB3, TUBB4B, TUBB4A, TUBB2A, TUBB2B · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 28 / 829 / 44; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.59 / 0.27.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:H1 | 19 / 9 | — | -0.32 | -1.3/-0.6/+0.8 | — |
| 0.5 µM | [[Plate 08]]:H1 | 700 / 129 | — | -0.44 | -0.7/+0.7/+1.7 | — |
| 5 µM | [[Plate 09]]:H1 | 27 / 17 | — | +0.02 | -1.6/-0.3/+0.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (19 genes, none with an alert; 12 shown): [[TUBB2A]] 1.88× (z +5.0, 31/46 lines), [[TUBA4A]] 1.87× (z +4.9, 24/33 lines), [[FAM149A]] 1.34× (z +3.7, 3/22 lines), [[ING4]] 1.22× (z +3.4, 3/47 lines), [[TUBA1B]] 1.58× (z +3.3, 30/47 lines), [[ENSG00000290846]] 1.29× (z +3.3, 9/46 lines), [[SYT16]] 1.50× (z +3.3, 6/34 lines), [[ENSG00000246090]] 1.37× (z +3.3, 4/44 lines), [[TUBA1A]] 1.39× (z +3.2, 17/38 lines), [[HHLA2]] 1.56× (z +3.1, 0/10 lines), [[UNC119B]] 1.25× (z +3.1, 7/46 lines), [[ENSG00000281883]] 1.50× (z +3.1, 3/27 lines)

**0.5 µM** (700 genes, none with an alert; 12 shown): [[MAL2]] 1.58× (z +8.3, 1/17 lines), [[CDH1]] 1.63× (z +7.4, 0/17 lines), [[TUBA4A]] 2.27× (z +7.1, 29/35 lines), [[ZFY]] 1.64× (z +6.7, 0/19 lines), [[PRKY]] 1.61× (z +6.6, 0/17 lines), [[GALNT3]] 1.52× (z +6.6, 0/18 lines), [[TUBB2A]] 2.15× (z +6.6, 39/48 lines), [[WNK3]] 1.50× (z +6.3, 1/18 lines), [[ESRP1]] 1.60× (z +6.2, 0/17 lines), [[SGPP2]] 1.46× (z +6.2, 0/16 lines), [[SLCO1B3]] 1.40× (z +6.2, 0/20 lines), [[GRHL2]] 1.47× (z +5.7, 0/14 lines)

**5 µM** (27 genes, none with an alert; 12 shown): [[TUBA4A]] 1.83× (z +5.0, 27/35 lines), [[TUBA1A]] 1.60× (z +4.7, 22/38 lines), [[TUBB2A]] 1.64× (z +4.1, 29/48 lines), [[ENSG00000288573]] 1.55× (z +3.9, 8/41 lines), [[LINC00944]] 1.28× (z +3.6, 6/28 lines), [[ENSG00000289156]] 1.39× (z +3.6, 5/44 lines), [[TUBB4B]] 1.59× (z +3.5, 37/48 lines), [[BACH2]] 1.22× (z +3.5, 5/41 lines), [[ENSG00000237596]] 1.38× (z +3.5, 6/33 lines), [[ENSG00000236453]] 1.45× (z +3.4, 6/24 lines), [[PPP1R1C]] 1.29× (z +3.2, 3/34 lines), [[DPYS]] 1.64× (z +3.2, 8/27 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (9 genes, none with an alert): [[TMEM161A]] 0.822× (z -3.3, 6/45 lines), [[BMS1P1-1]] 0.777× (z -3.3, 7/43 lines), [[TGFBRAP1]] 0.830× (z -3.1, 13/47 lines), [[CCN2]] 0.700× (z -3.0, 11/29 lines), [[CCN1]] 0.764× (z -2.8, 18/41 lines), [[ITGA3]] 0.827× (z -2.7, 12/38 lines), [[WEE1]] 0.832× (z -2.6, 11/47 lines), [[MAML2]] 0.811× (z -2.6, 17/40 lines), [[COL13A1]] 0.750× (z -2.6, 9/35 lines)

**0.5 µM** (129 genes, none with an alert; 12 shown): [[NDFIP2]] 0.825× (z -4.4, 20/47 lines), [[DMXL2]] 0.741× (z -4.2, 32/45 lines), [[RAB23]] 0.780× (z -4.2, 12/45 lines), [[FHL2]] 0.797× (z -4.1, 22/44 lines), [[CDK6]] 0.816× (z -4.0, 20/44 lines), [[PRR16]] 0.728× (z -4.0, 15/24 lines), [[PLCB4]] 0.822× (z -4.0, 15/35 lines), [[CCN2]] 0.605× (z -4.0, 16/30 lines), [[CD44]] 0.818× (z -3.9, 20/33 lines), [[CCN1]] 0.703× (z -3.9, 24/41 lines), [[SRGAP1]] 0.808× (z -3.9, 24/46 lines), [[ENSG00000259755]] 0.755× (z -3.9, 13/42 lines)

**5 µM** (17 genes, none with an alert; 12 shown): [[ENSG00000259316]] 0.622× (z -5.3, 12/45 lines), [[GTPBP3]] 0.768× (z -3.9, 6/47 lines), [[CCN2]] 0.646× (z -3.8, 14/30 lines), [[LINC01029]] 0.517× (z -3.5, 1/6 lines), [[ABHD14B]] 0.772× (z -3.4, 9/46 lines), [[GSTA4]] 0.759× (z -3.3, 5/42 lines), [[UNC119B]] 0.795× (z -3.3, 5/47 lines), [[MAP3K14]] 0.788× (z -3.3, 19/48 lines), [[ENSG00000268173]] 0.705× (z -3.2, 12/47 lines), [[ITGA3]] 0.810× (z -3.1, 17/38 lines), [[RAB40B]] 0.814× (z -3.1, 7/45 lines), [[IGFBP3]] 0.732× (z -3.0, 18/28 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 059]] (+3.1), [[Module 024]] (+2.5), [[Module 012]] (+2.5) | [[Module 025]] (-2.8), [[Module 200]] (-2.4), [[Module 029]] (-2.4) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1271 (line)]] (1.77), [[RKO (line)]] (1.62), [[C32 (line)]] (1.41), [[NCI-H460 (line)]] (1.38) · weakest: [[NCI-H661 (line)]] (0.150), [[HepG2_C3A (line)]] (0.319), [[AsPC-1 (line)]] (0.402) |
| 0.5 µM | [[H4 (line)]] (-3.5) | [[RKO (line)]] (1.39), [[HOP62 (line)]] (1.11), [[H4 (line)]] (1.11), [[MIA PaCa-2 (line)]] (1.08) · weakest: [[SHP-77 (line)]] (0.574), [[BT-474 (line)]] (0.604), [[SK-MEL-2 (line)]] (0.620) |
| 5 µM | [[H4 (line)]] (-5.0), [[NCI-H23 (line)]] (-3.0) | [[RKO (line)]] (1.95), [[HOP62 (line)]] (1.38), [[NCI-H460 (line)]] (1.34), [[NCI-H1792 (line)]] (1.32) · weakest: [[SHP-77 (line)]] (0.392), [[HepG2_C3A (line)]] (0.480), [[SK-MEL-2 (line)]] (0.521) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Tranilast (drug)]] (+0.89, unclear, ⚠ only 6 significant genes); [[Methylprednisolone succinate (drug)]] (+0.84, Glucocorticoid receptor agonist); [[Darolutamide (drug)]] (+0.80, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Decitabine (drug)]] (+0.80, DNA methyltransferase inhibitor); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.79, unclear); [[Nimesulide (drug)]] (+0.74, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Fingolimod (hydrochloride) (drug)]] (+0.74, unclear, ⚠ vector dose flagged: toxic); [[Bimatoprost (drug)]] (+0.74, unclear); [[Ipatasertib (drug)]] (+0.72, PI3K/AKT inhibitor); [[Bicalutamide (drug)]] (+0.71, Androgen receptor antagonist); [[Almonertinib (hydrochloride) (drug)]] (+0.71, EGFR/ERBB inhibitor); [[Bendamustine (drug)]] (+0.71, DNA synthesis/repair inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 27 arrows, 27 of them with an alert ⚠; grade A 0, B 22, C 5. Shown: the 15 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[EDN1]] | 5 µM | B | EDN1 activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express EDN1 (27) vs lines expressing it (21) | the lines without EDN1: 0.81× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: P2RY2, S100A14, CBLC |
| [[FMN2]] | 5 µM | B | FMN2 activity lowers the cells' numbers under Docetaxel (Trihydrate) 5 µM (makes them more sensitive) | lines that do not express FMN2 (26) vs lines expressing it (22) | the lines without FMN2: 1.25× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, TRPC4, HECW2; maybe low, not absent |
| [[HUNK]] | 0.5 µM | B | HUNK activity lowers the cells' numbers under Docetaxel (Trihydrate) 0.5 µM (makes them more sensitive) | lines that do not express HUNK (21) vs lines expressing it (27) | the lines without HUNK: 1.16× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: SLC7A2, VAV3, NRXN3 |
| [[VIPR1]] | 5 µM | B | VIPR1 activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express VIPR1 (24) vs lines expressing it (24) | the lines without VIPR1: 0.80× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, ENSG00000262302 |
| [[TRIM29]] | 5 µM | B | TRIM29 activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express TRIM29 (28) vs lines expressing it (20) | the lines without TRIM29: 0.82× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[GAP43]] | 5 µM | B | GAP43 activity lowers the cells' numbers under Docetaxel (Trihydrate) 5 µM (makes them more sensitive) | lines that do not express GAP43 (22) vs lines expressing it (26) | the lines without GAP43: 1.21× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent |
| [[MST1R]] | 5 µM | B | MST1R activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express MST1R (24) vs lines expressing it (24) | the lines without MST1R: 0.80× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SLC52A3, SPINT1, MAP7 |
| [[STYK1]] | 5 µM | B | STYK1 activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express STYK1 (20) vs lines expressing it (28) | the lines without STYK1: 0.84× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[ITGB4]] | 5 µM | B | ITGB4 activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express ITGB4 (25) vs lines expressing it (23) | the lines without ITGB4: 0.80× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[PLEKHO1]] | 5 µM | B | PLEKHO1 activity lowers the cells' numbers under Docetaxel (Trihydrate) 5 µM (makes them more sensitive) | lines that do not express PLEKHO1 (13) vs lines expressing it (35) | the lines without PLEKHO1: 1.24× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| [[EPS8L2]] | 5 µM | B | EPS8L2 activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express EPS8L2 (19) vs lines expressing it (29) | the lines without EPS8L2: 0.83× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: KRT80, ITGB4, C19orf33; maybe low, not absent |
| [[AKR1E2]] | 0.5 µM | B | AKR1E2 activity raises the cells' numbers under Docetaxel (Trihydrate) 0.5 µM (protects the cells) | lines that do not express AKR1E2 (19) vs lines expressing it (29) | the lines without AKR1E2: 0.87× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: FLNC, AFAP1L1, CACNA2D1 |
| [[PCDH1]] | 5 µM | B | PCDH1 activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express PCDH1 (20) vs lines expressing it (28) | the lines without PCDH1: 0.84× the cells of the other lines | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[C1orf116]], [[IRF6]] | 5 µM | B | C1orf116, IRF6 activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (17) | the lines without C1orf116, IRF6: 0.81× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |
| [[C19orf33]] | 5 µM | B | C19orf33 activity raises the cells' numbers under Docetaxel (Trihydrate) 5 µM (protects the cells) | lines that do not express C19orf33 (19) vs lines expressing it (29) | the lines without C19orf33: 0.81× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: KRT80, MISP, AREG |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, [[TUBB4B]] | [[SGSH]] | moves it that way too | B | TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B activity raises SGSH's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 lower it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, [[TUBB4B]] | [[MZT1]] | moves it that way too | B | TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B activity lowers MZT1's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 raise it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, [[TUBB4B]] | [[ENSG00000287352]] | moves it that way too | B | TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B activity lowers ENSG00000287352's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 raise it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| TUBB1, [[TUBB2A]], [[TUBB3]], TUBB4A, [[TUBB4B]] | [[RAB28]] | moves it that way too | B | TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B activity raises RAB28's level | compounds that target TUBB1, TUBB2A, TUBB3, TUBB4A, TUBB4B: 2 of 2 lower it (Docetaxel, Mebendazole) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

## Data

- `tables/drugs.parquet` — drug == "Docetaxel (Trihydrate)"
- `tables/drugdoses.parquet` — dd in 371, 372, 373
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

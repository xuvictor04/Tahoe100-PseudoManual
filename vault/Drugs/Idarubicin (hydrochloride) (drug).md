---
drug: "Idarubicin (hydrochloride)"
type: "drug"
salt_base: "Idarubicin"
targets: "TOP2A"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 11472
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Idarubicin (hydrochloride)

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: TOP2A · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 33 / 3579 / 11472; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.27 / 0.68.
> Flags by dose: - / cell-cycle shift / cell-cycle shift. ⚠ 0.5 µM: cell-cycle shift; 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:C12 | 16 / 17 | — | +0.05 | +2.7/+0.1/+0.9 | — |
| 0.5 µM | [[Plate 05]]:C12 | 2,636 / 943 | — | +0.21 | +1.4/-4.3/+1.0 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 14]]:C12 | 8,040 / 3,432 | 0.991 | -0.82 | +8.1/-0.8/+1.0 | ⚠ cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (16 genes, none with an alert; 12 shown): [[PTCHD4]] 1.51× (z +4.3, 12/15 lines), [[CDC6]] 1.37× (z +4.3, 15/48 lines), [[PURPL]] 1.34× (z +4.0, 13/23 lines), [[DNA2]] 1.24× (z +3.9, 10/48 lines), [[EDA2R]] 1.38× (z +3.4, 9/19 lines), [[AEN]] 1.32× (z +3.4, 14/47 lines), [[ACTA2]] 1.37× (z +3.3, 13/36 lines), [[POLH]] 1.22× (z +3.2, 18/47 lines), [[TMEM132B]] 1.31× (z +3.1, 5/40 lines), [[PIK3R3]] 1.30× (z +3.0, 16/46 lines), [[ADAMTS7]] 1.35× (z +3.0, 5/26 lines), [[SHCBP1]] 1.22× (z +3.0, 13/47 lines)

**0.5 µM** (2636 genes, 613 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[CCDC26]] 7.19× (z +26.2, 41/42 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000289084]] 3.79× (z +18.2, 35/43 lines; cell-cycle shift (explains ~3% here)), [[ENSG00000228566]] 4.75× (z +17.5, 33/40 lines; cell-cycle shift (explains ~0% here)), [[ENSG00000248752]] 4.51× (z +17.3, 37/43 lines; cell-cycle shift (explains ~1% here)), [[ENSG00000290551]] 4.60× (z +16.2, 36/41 lines; cell-cycle shift (explains ~0% here)), [[GALNTL6]] 4.73× (z +15.9, 33/40 lines; cell-cycle shift (explains ~1% here)), [[ENSG00000231918]] 5.22× (z +15.9, 36/41 lines; cell-cycle shift (explains ~0% here)), [[GRID2]] 4.79× (z +15.8, 33/39 lines; cell-cycle shift (explains ~2% here)), [[HPSE2]] 5.16× (z +15.7, 37/40 lines; cell-cycle shift (explains ~0% here)), [[LAMA2]] 2.95× (z +15.5, 24/37 lines; cell-cycle shift (explains ~2% here)), [[ENSG00000288714]] 4.76× (z +15.3, 37/42 lines; cell-cycle shift (explains ~0% here)), [[LINC02006]] 4.89× (z +15.0, 32/40 lines; cell-cycle shift (explains ~0% here))

**5 µM** (8040 genes, 732 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[ENSG00000289156]] 29.5× (z +54.3, 38/38 lines; cell-cycle shift (explains ~0% here)), [[SERINC5]] 3.52× (z +53.5, 44/48 lines; cell-cycle shift (explains ~0% here)), [[ALG11]] 3.41× (z +50.8, 49/49 lines; cell-cycle shift (explains ~2% here)), [[CCNT2-AS1]] 11.3× (z +49.2, 40/40 lines; cell-cycle shift (explains ~2% here)), [[EPHA4]] 10.8× (z +49.1, 29/29 lines; cell-cycle shift (explains ~6% here)), [[DPF3]] 14.0× (z +48.5, 28/29 lines; cell-cycle shift (explains ~7% here)), [[SIAH2-AS1]] 42.3× (z +47.0, 31/31 lines; cell-cycle shift (explains ~0% here)), [[FRAS1]] 4.69× (z +46.9, 24/26 lines; cell-cycle shift (explains ~1% here)), [[ENSG00000287292]] 26.2× (z +45.6, 30/30 lines; cell-cycle shift (explains ~0% here)), [[BHLHE40-AS1]] 7.16× (z +45.4, 43/43 lines; cell-cycle shift (explains ~0% here)), [[CCDC26]] 11.1× (z +45.0, 40/41 lines; cell-cycle shift (explains ~1% here)), [[ENSG00000228541]] 7.54× (z +44.3, 39/41 lines; cell-cycle shift (explains ~2% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (17 genes, none with an alert; 12 shown): [[BNC2]] 0.770× (z -4.1, 10/27 lines), [[SRCIN1]] 0.727× (z -4.1, 10/38 lines), [[DIXDC1]] 0.832× (z -3.7, 15/48 lines), [[BCL11A]] 0.776× (z -3.7, 10/28 lines), [[LINC03041]] 0.698× (z -3.6, 9/25 lines), [[PIF1]] 0.758× (z -3.5, 13/46 lines), [[KIF20A]] 0.729× (z -3.4, 20/47 lines), [[FAM13A-AS1]] 0.737× (z -3.4, 13/46 lines), [[DHRS2]] 0.625× (z -3.2, 13/33 lines), [[FZD4]] 0.767× (z -3.1, 6/38 lines), [[FOXP4-AS1]] 0.788× (z -3.0, 3/41 lines), [[HERC3]] 0.772× (z -3.0, 20/46 lines)

**0.5 µM** (943 genes, 309 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 15 shown): [[DIAPH3]] 0.562× (z -12.3, 35/45 lines; cell-cycle shift (explains ~11% here)), [[ENSG00000235609]] 0.531× (z -11.8, 31/40 lines; cell-cycle shift (explains ~24% here)), [[ENSG00000284906]] ⚠ 0.619× (z -10.4, 35/48 lines; cell-cycle shift, explains ~27% of this change), [[KIF4A]] ⚠ 0.569× (z -9.8, 38/47 lines; cell-cycle shift, explains ~44% of this change), [[PLXND1]] 0.566× (z -9.8, 27/40 lines; cell-cycle shift (explains ~0% here)), [[CENPE]] ⚠ 0.578× (z -9.5, 32/48 lines; cell-cycle shift, explains ~56% of this change), [[L1CAM]] 0.504× (z -9.1, 22/26 lines; cell-cycle shift (explains ~8% here)), [[GFPT1]] 0.618× (z -9.1, 42/48 lines; cell-cycle shift (explains ~1% here)), [[CIT]] 0.579× (z -9.1, 33/47 lines; cell-cycle shift (explains ~21% here)), [[ZNF496]] 0.698× (z -8.9, 32/48 lines; cell-cycle shift (explains ~0% here)), [[LRRFIP1]] 0.724× (z -8.9, 38/48 lines; cell-cycle shift (explains ~14% here)), [[DHRSX]] 0.700× (z -8.7, 35/47 lines; cell-cycle shift (explains ~20% here)), [[SH3PXD2B]] 0.660× (z -8.6, 35/46 lines; cell-cycle shift (explains ~0% here)), [[DIAPH2]] 0.648× (z -8.6, 36/41 lines; cell-cycle shift (explains ~0% here)), [[C1QTNF7-AS1]] 0.644× (z -8.5, 30/45 lines; cell-cycle shift (explains ~16% here))

**5 µM** (3432 genes, 560 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[DHRSX]] 0.343× (z -37.0, 47/48 lines; cell-cycle shift (explains ~15% here)), [[TOM1L1]] 0.426× (z -36.8, 45/49 lines; cell-cycle shift (explains ~6% here)), [[FLNB]] 0.275× (z -36.5, 46/46 lines; cell-cycle shift (explains ~2% here)), [[HDAC8]] 0.310× (z -36.3, 49/49 lines; cell-cycle shift (explains ~4% here)), [[SLC25A43]] 0.297× (z -36.0, 43/43 lines; cell-cycle shift (explains ~8% here)), [[GTF2IRD1]] 0.336× (z -35.8, 48/49 lines; cell-cycle shift (explains ~7% here)), [[UBE2E2]] 0.361× (z -35.7, 37/38 lines; cell-cycle shift (explains ~0% here)), [[CAMK2G]] 0.374× (z -35.4, 47/49 lines; cell-cycle shift (explains ~0% here)), [[CSTPP1]] 0.389× (z -34.6, 48/49 lines; cell-cycle shift (explains ~0% here)), [[PAG1]] 0.334× (z -32.9, 34/34 lines; cell-cycle shift (explains ~0% here)), [[GBE1]] 0.251× (z -32.8, 47/47 lines; cell-cycle shift (explains ~10% here)), [[SPIN1]] 0.399× (z -32.6, 46/49 lines; cell-cycle shift (explains ~10% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 165]] (+8.5), [[Module 166]] (+8.1), [[Module 140]] (+7.8) | [[Module 085]] (-4.7), [[Module 077]] (-3.4), [[Module 033]] (-2.8) |
| 5 µM | [[Module 026]] (+27.4), [[Module 165]] (+22.4), [[Module 207]] (+22.4) | [[Module 230]] (-20.6), [[Module 017]] (-18.5), [[Module 085]] (-16.8) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[CHP-212 (line)]] (-4.6) | [[RKO (line)]] (1.71), [[SNU-1 (line)]] (1.58), [[A549 (line)]] (1.56), [[SW48 (line)]] (1.52) · weakest: [[SHP-77 (line)]] (0.347), [[SW 900 (line)]] (0.422), [[SNU-423 (line)]] (0.428) |
| 0.5 µM | [[A549 (line)]] (-6.7), [[CHP-212 (line)]] (-6.6), [[LOX-IMVI (line)]] (-5.1), [[H4 (line)]] (-3.3), [[SW48 (line)]] (-3.0) | [[BT-474 (line)]] (1.63), [[A549 (line)]] (1.59), [[SW48 (line)]] (1.56), [[RKO (line)]] (1.48) · weakest: [[SW 1088 (line)]] (0.103), [[NCI-H1573 (line)]] (0.397), [[COLO 205 (line)]] (0.422) |
| 5 µM | [[A-427 (line)]] (-17.7), [[SK-MEL-2 (line)]] (-14.1), [[RKO (line)]] (-13.9), [[AsPC-1 (line)]] (-12.6), [[NCI-H23 (line)]] (-12.3) | [[A549 (line)]] (1.25), [[RKO (line)]] (1.22), [[AsPC-1 (line)]] (1.13), [[HOP62 (line)]] (1.12) · weakest: [[NCI-H2122 (line)]] (0.458), [[NCI-H661 (line)]] (0.511), [[A-427 (line)]] (0.619) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[Doxorubicin (hydrochloride) (drug)]] (+0.82, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Epirubicin (hydrochloride) (drug)]] (+0.81, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] (+0.68, DNA synthesis/repair inhibitor); [[Pimozide (drug)]] (+0.54, unclear); [[Vemurafenib (drug)]] (+0.51, RAF inhibitor, ⚠ only 1 significant gene); [[olaparib (drug)]] (+0.47, DNA synthesis/repair inhibitor, ⚠ only 3 significant genes); [[Nafamostat (mesylate) (drug)]] (+0.45, unclear, ⚠ only 3 significant genes); [[Pyridoxine (drug)]] (+0.45, unclear); [[Bimatoprost (drug)]] (+0.44, unclear); [[Drospirenone (drug)]] (+0.43, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.43, Glucose transporter inhibitor); [[Oxaprozin (drug)]] (+0.41, Cyclooxygenase inhibitor); [[Bicalutamide (drug)]] (+0.40, Androgen receptor antagonist)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 66 arrows, 66 of them with an alert ⚠; grade A 0, B 36, C 30. Shown: the 15 strongest; 51 more arrows (51 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[LNX1]] | 0.5 µM | B | LNX1 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express LNX1 (20) vs lines expressing it (28) | the lines without LNX1: 0.75× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[SPTLC3]] | 0.05 µM | B | SPTLC3 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 0.79× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[GAL3ST1]] | 5 µM | B | GAL3ST1 activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express GAL3ST1 (5) vs lines expressing it (43) | the lines without GAL3ST1: 0.33× the cells of the other lines | 0.047 | ⚠ within organs, on part of the lines; also absent: ID2, ENSG00000275993; maybe low, not absent |
| [[DNM3]] | 5 µM | B | DNM3 activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express DNM3 (7) vs lines expressing it (41) | the lines without DNM3: 0.42× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: DENND3, TSC22D3; maybe low, not absent |
| [[EPHA1-AS1]] | 5 µM | B | EPHA1-AS1 activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express EPHA1-AS1 (6) vs lines expressing it (42) | the lines without EPHA1-AS1: 0.51× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[SPTLC3]] | 0.5 µM | B | SPTLC3 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 0.73× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[FBXW10B]] | 0.05 µM | B | FBXW10B activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express FBXW10B (11) vs lines expressing it (37) | the lines without FBXW10B: 0.89× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000251537, NHS, BDKRB2; maybe low, not absent |
| [[ENSG00000251537]] | 0.05 µM | B | ENSG00000251537 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express ENSG00000251537 (9) vs lines expressing it (39) | the lines without ENSG00000251537: 0.86× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: FBXW10B, PCED1B, NHS; maybe low, not absent |
| [[CYP27A1]] | 5 µM | B | CYP27A1 activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express CYP27A1 (10) vs lines expressing it (38) | the lines without CYP27A1: 0.55× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: RNF217, ENSG00000224905, ESYT3; maybe low, not absent |
| [[C11orf52]] | 0.5 µM | B | C11orf52 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express C11orf52 (23) vs lines expressing it (25) | the lines without C11orf52: 0.74× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[ENSG00000287188]] | 5 µM | B | ENSG00000287188 activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express ENSG00000287188 (5) vs lines expressing it (43) | the lines without ENSG00000287188: 0.38× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: DDX60, PUDP, DDX60L; maybe low, not absent |
| [[CXCL3]] | 0.05 µM | B | CXCL3 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express CXCL3 (14) vs lines expressing it (34) | the lines without CXCL3: 0.80× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[ENSG00000259354]], [[HMGN2P46]] | 0.05 µM | B | ENSG00000259354, HMGN2P46 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express ENSG00000259354, HMGN2P46 (18) vs lines expressing them (30) | the lines without ENSG00000259354, HMGN2P46: 0.81× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: C15orf48, IL1R1, STAC; co-absent genes |
| [[CDCP1]] | 0.05 µM | B | CDCP1 activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express CDCP1 (16) vs lines expressing it (32) | the lines without CDCP1: 0.82× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[ATXN1]] | 5 µM | B | ATXN1 activity raises the cells' numbers under Idarubicin (hydrochloride) 5 µM (protects the cells) | lines that do not express ATXN1 (6) vs lines expressing it (42) | the lines without ATXN1: 0.50× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 4,166 arrows, 4,166 of them with an alert ⚠; grade A 0, B 4,166, C 0. Shown: the 15 strongest; 4,151 more arrows (4,151 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[TOP2A]] | [[G2E3]] | moves it that way too | B | TOP2A activity raises G2E3's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.5% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[RABL2B]] | moves it that way too | B | TOP2A activity lowers RABL2B's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.8% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[RASSF8-AS1]] | moves it that way too | B | TOP2A activity lowers RASSF8-AS1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 2.8% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ENSG00000285667]] | moves it that way too | B | TOP2A activity lowers ENSG00000285667's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.1% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[LRRIQ3]] | moves it that way too | B | TOP2A activity lowers LRRIQ3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.1% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[BAX]] | moves it that way too | B | TOP2A activity lowers BAX's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[CIBAR1-DT]] | moves it that way too | B | TOP2A activity lowers CIBAR1-DT's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ENSG00000287400]] | moves it that way too | B | TOP2A activity lowers ENSG00000287400's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[MIDEAS]] | moves it that way too | B | TOP2A activity raises MIDEAS's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[TARID]] | moves it that way too | B | TOP2A activity lowers TARID's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ZNF665]] | moves it that way too | B | TOP2A activity lowers ZNF665's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.4% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[AK1]] | moves it that way too | B | TOP2A activity lowers AK1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[CAMKK1]] | moves it that way too | B | TOP2A activity raises CAMKK1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[ENSG00000228566]] | moves it that way too | B | TOP2A activity lowers ENSG00000228566's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | [[FCGBP]] | moves it that way too | B | TOP2A activity lowers FCGBP's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 3.6% of all compounds | 0.004 | ⚠ off-target possible; 5 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Idarubicin (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 540, 541, 542
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

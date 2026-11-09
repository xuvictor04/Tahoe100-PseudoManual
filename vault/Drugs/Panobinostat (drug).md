---
drug: "Panobinostat"
type: "drug"
salt_base: "Panobinostat"
targets: "HDAC1, HDAC2, HDAC3, HDAC6, HDAC8, HDAC10, HDAC11"
moa_fine: "HDAC inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 10622
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Panobinostat

*HDAC inhibitor (inhibitor/antagonist) · targets: HDAC1, HDAC2, HDAC3, HDAC6, HDAC8, HDAC10, HDAC11 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 6637 / 10266 / 10622; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.85 / 0.98.
> Flags by dose: cell-cycle shift / cell-cycle shift / cell-cycle shift. ⚠ 0.05 µM: cell-cycle shift; 0.5 µM: cell-cycle shift; 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:H8 | 4,058 / 2,579 | — | +0.38 | +4.8/+1.8/-0.6 | ⚠ cell-cycle shift |
| 0.5 µM | [[Plate 11]]:H8 | 5,813 / 4,453 | — | +0.18 | +14.0/+2.2/+1.8 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 12]]:H8 | 6,106 / 4,516 | — | -0.37 | +16.5/+2.5/+2.0 | ⚠ cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4058 genes, 620 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[B3GALT1]] 8.41× (z +38.2, 26/27 lines; cell-cycle shift (explains ~4% here)), [[DPF3]] 10.4× (z +30.4, 34/34 lines; cell-cycle shift (explains ~5% here)), [[RGL1]] 4.18× (z +27.7, 41/44 lines; cell-cycle shift (explains ~4% here)), [[SORBS1]] 4.23× (z +27.4, 40/42 lines; cell-cycle shift (explains ~3% here)), [[OTUD7A]] 4.25× (z +26.6, 41/41 lines; cell-cycle shift (explains ~1% here)), [[MEGF9]] 2.78× (z +26.2, 48/48 lines; cell-cycle shift (explains ~4% here)), [[SEMA6A]] 5.20× (z +24.6, 27/29 lines; cell-cycle shift (explains ~0% here)), [[ATP8A1]] 3.83× (z +24.6, 34/35 lines; cell-cycle shift (explains ~0% here)), [[WDR17]] 5.96× (z +23.6, 30/30 lines; cell-cycle shift (explains ~4% here)), [[MED12L]] 4.73× (z +23.3, 27/29 lines; cell-cycle shift (explains ~6% here)), [[MITF]] 3.64× (z +23.2, 34/39 lines; cell-cycle shift (explains ~4% here)), [[MPP7]] 3.45× (z +23.0, 27/28 lines; cell-cycle shift (explains ~0% here))

**0.5 µM** (5813 genes, 1,971 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[B3GALT1]] 12.8× (z +45.7, 26/27 lines; cell-cycle shift (explains ~9% here)), [[RGL1]] 9.89× (z +44.5, 42/44 lines; cell-cycle shift (explains ~9% here)), [[DPF3]] 29.4× (z +43.9, 34/34 lines; cell-cycle shift (explains ~11% here)), [[OTUD7A]] 9.84× (z +42.0, 41/41 lines; cell-cycle shift (explains ~3% here)), [[SORBS1]] 7.52× (z +38.4, 41/42 lines; cell-cycle shift (explains ~6% here)), [[STK4]] 2.77× (z +38.3, 48/48 lines; cell-cycle shift (explains ~11% here)), [[TYW1B]] 8.48× (z +37.8, 48/48 lines; cell-cycle shift (explains ~12% here)), [[EFR3B]] 9.00× (z +36.2, 35/37 lines; cell-cycle shift (explains ~16% here)), [[LINC00624]] 11.8× (z +35.8, 44/47 lines; cell-cycle shift (explains ~4% here)), [[CALN1]] 7.90× (z +35.5, 47/47 lines; cell-cycle shift (explains ~0% here)), [[PTPN1]] 3.88× (z +34.8, 48/48 lines; cell-cycle shift (explains ~16% here)), [[WDR17]] 13.8× (z +34.8, 30/30 lines; cell-cycle shift (explains ~10% here))

**5 µM** (6106 genes, 2,134 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[RGL1]] 16.1× (z +53.9, 43/44 lines; cell-cycle shift (explains ~9% here)), [[B3GALT1]] 15.8× (z +49.6, 25/27 lines; cell-cycle shift (explains ~10% here)), [[DPF3]] 43.3× (z +49.0, 34/34 lines; cell-cycle shift (explains ~12% here)), [[OTUD7A]] 10.6× (z +43.4, 41/41 lines; cell-cycle shift (explains ~3% here)), [[CALN1]] 12.1× (z +42.8, 47/47 lines; cell-cycle shift (explains ~0% here)), [[CRISPLD2]] 33.1× (z +41.7, 36/36 lines; cell-cycle shift (explains ~16% here)), [[TYW1B]] 10.4× (z +41.4, 48/48 lines; cell-cycle shift (explains ~12% here)), [[EFR3B]] 11.7× (z +40.5, 36/37 lines; cell-cycle shift (explains ~17% here)), [[SORBS1]] 8.33× (z +40.3, 41/42 lines; cell-cycle shift (explains ~7% here)), [[LINC00624]] 16.1× (z +40.2, 43/47 lines; cell-cycle shift (explains ~4% here)), [[ENSG00000259124]] 72.6× (z +39.6, 46/46 lines; cell-cycle shift (explains ~1% here)), [[SYT11]] 25.9× (z +38.8, 23/23 lines; cell-cycle shift (explains ~1% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2579 genes, 584 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[DHRSX]] 0.298× (z -29.6, 47/47 lines; cell-cycle shift (explains ~10% here)), [[KAT6B]] 0.338× (z -27.4, 48/48 lines; cell-cycle shift (explains ~7% here)), [[SENP6]] 0.420× (z -25.3, 48/48 lines; cell-cycle shift (explains ~7% here)), [[EFCAB2]] 0.222× (z -25.1, 47/48 lines; cell-cycle shift (explains ~3% here)), [[ZFX]] 0.328× (z -23.9, 48/48 lines; cell-cycle shift (explains ~4% here)), [[CREBBP]] 0.470× (z -22.6, 47/48 lines; cell-cycle shift (explains ~5% here)), [[CUL1]] 0.456× (z -22.4, 46/48 lines; cell-cycle shift (explains ~5% here)), [[PMF1]] 0.380× (z -22.0, 47/48 lines; cell-cycle shift (explains ~3% here)), [[INO80D]] 0.416× (z -21.3, 48/48 lines; cell-cycle shift (explains ~7% here)), [[MAP3K20]] 0.576× (z -19.9, 44/47 lines; cell-cycle shift (explains ~7% here)), [[KMT5B]] 0.529× (z -19.9, 48/48 lines; cell-cycle shift (explains ~12% here)), [[ATP9A]] 0.369× (z -19.1, 43/44 lines; cell-cycle shift (explains ~14% here))

**0.5 µM** (4453 genes, 1,631 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[CUL1]] 0.151× (z -53.9, 48/48 lines; cell-cycle shift (explains ~6% here)), [[SENP6]] 0.175× (z -50.8, 48/48 lines; cell-cycle shift (explains ~10% here)), [[TLK1]] 0.237× (z -45.9, 48/48 lines; cell-cycle shift (explains ~10% here)), [[DHRSX]] 0.158× (z -45.1, 47/47 lines; cell-cycle shift (explains ~20% here)), [[MAP3K20]] 0.289× (z -44.9, 47/47 lines; cell-cycle shift (explains ~10% here)), [[BBX]] 0.278× (z -44.6, 48/48 lines; cell-cycle shift (explains ~12% here)), [[ZFX]] 0.140× (z -42.1, 48/48 lines; cell-cycle shift (explains ~7% here)), [[GNAQ]] 0.254× (z -41.1, 47/47 lines; cell-cycle shift (explains ~7% here)), [[ZNF827]] 0.164× (z -40.1, 44/44 lines; cell-cycle shift (explains ~5% here)), [[ARID1B]] 0.161× (z -39.4, 47/47 lines; cell-cycle shift (explains ~11% here)), [[STAG2]] 0.242× (z -39.1, 48/48 lines; cell-cycle shift (explains ~15% here)), [[UBE2E1]] 0.210× (z -37.7, 47/47 lines; cell-cycle shift (explains ~13% here))

**5 µM** (4516 genes, 1,864 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[CUL1]] 0.137× (z -56.8, 48/48 lines; cell-cycle shift (explains ~7% here)), [[SENP6]] 0.179× (z -50.1, 48/48 lines; cell-cycle shift (explains ~12% here)), [[DHRSX]] 0.147× (z -46.8, 47/47 lines; cell-cycle shift (explains ~22% here)), [[MAP3K20]] 0.292× (z -44.5, 47/47 lines; cell-cycle shift (explains ~12% here)), [[ZFX]] 0.127× (z -44.1, 48/48 lines; cell-cycle shift (explains ~8% here)), [[BBX]] 0.284× (z -43.8, 48/48 lines; cell-cycle shift (explains ~14% here)), [[ZNF827]] 0.149× (z -42.3, 44/44 lines; cell-cycle shift (explains ~6% here)), [[TLK1]] 0.274× (z -41.3, 48/48 lines; cell-cycle shift (explains ~13% here)), [[SPATS2L]] 0.256× (z -40.3, 47/47 lines; cell-cycle shift (explains ~7% here)), [[UBE2E1]] 0.196× (z -39.4, 47/47 lines; cell-cycle shift (explains ~15% here)), [[STAG2]] 0.241× (z -39.3, 48/48 lines; cell-cycle shift (explains ~18% here)), [[GNAQ]] 0.276× (z -38.6, 46/47 lines; cell-cycle shift (explains ~8% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 184]] (+11.4), [[Module 115]] (+10.2), [[Module 077]] (+9.0) | [[Module 095]] (-19.4), [[Module 137]] (-12.9), [[Module 083]] (-11.5) |
| 0.5 µM | [[Module 002]] (+21.8), [[Module 184]] (+19.4), [[Module 085]] (+18.8) | [[Module 095]] (-25.3), [[Module 137]] (-21.0), [[Module 046]] (-19.9) |
| 5 µM | [[Module 002]] (+22.5), [[Module 191]] (+20.5), [[Module 085]] (+19.8) | [[Module 095]] (-29.3), [[Module 137]] (-20.6), [[Module 046]] (-20.3) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[H4 (line)]] (-3.7), [[A-172 (line)]] (-3.4) | [[HOP62 (line)]] (1.32), [[H4 (line)]] (1.29), [[SNU-423 (line)]] (1.25), [[SK-MEL-2 (line)]] (1.22) · weakest: [[SNU-1 (line)]] (0.534), [[AN3 CA (line)]] (0.653), [[SHP-77 (line)]] (0.707) |
| 0.5 µM | [[NCI-H1792 (line)]] (-15.0), [[A-172 (line)]] (-6.3), [[NCI-H23 (line)]] (-5.4), [[LOX-IMVI (line)]] (-4.4), [[COLO 205 (line)]] (-4.1) | [[A549 (line)]] (1.21), [[HOP62 (line)]] (1.16), [[SW480 (line)]] (1.15), [[H4 (line)]] (1.14) · weakest: [[NCI-H661 (line)]] (0.688), [[AN3 CA (line)]] (0.741), [[SW 1271 (line)]] (0.764) |
| 5 µM | [[NCI-H1792 (line)]] (-12.9), [[A-172 (line)]] (-7.2), [[H4 (line)]] (-6.3), [[LOX-IMVI (line)]] (-4.4), [[NCI-H23 (line)]] (-4.0) | [[A549 (line)]] (1.22), [[HOP62 (line)]] (1.16), [[H4 (line)]] (1.15), [[NCI-H460 (line)]] (1.15) · weakest: [[NCI-H661 (line)]] (0.643), [[AN3 CA (line)]] (0.750), [[SW 1088 (line)]] (0.764) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Belinostat (drug)]] (+0.94, HDAC inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Brivudine (drug)]] (+0.55, unclear); [[HI-TOPK-032 (drug)]] (+0.49, unclear); [[Fumaric acid (drug)]] (+0.48, unclear); [[Aprepitant (drug)]] (+0.47, unclear); [[Erythromycin (drug)]] (+0.46, unclear); [[Quinidine (15% dihydroquinidine) (drug)]] (+0.45, unclear); [[AT7519 (drug)]] (+0.44, CDK inhibitor, ⚠ only 6 significant genes); [[Pemigatinib (drug)]] (+0.42, Other TK inhibitor); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] (+0.42, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[GLS2]] | 5 µM | B | GLS2 activity raises the cells' numbers under Panobinostat 5 µM (protects the cells) | lines that do not express GLS2 (14) vs lines expressing it (34) | the lines without GLS2: 0.67× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: SLC9A2, PLS1, NRARP; maybe low, not absent |
| [[IL17RE]] | 5 µM | B | IL17RE activity raises the cells' numbers under Panobinostat 5 µM (protects the cells) | lines that do not express IL17RE (10) vs lines expressing it (38) | the lines without IL17RE: 0.71× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: MCF2L; maybe low, not absent |
| [[REEP1]] | 5 µM | B | REEP1 activity raises the cells' numbers under Panobinostat 5 µM (protects the cells) | lines that do not express REEP1 (10) vs lines expressing it (38) | the lines without REEP1: 0.78× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: SEPTIN3; maybe low, not absent |
| [[PPM1E]] | 0.5 µM | B | PPM1E activity raises the cells' numbers under Panobinostat 0.5 µM (protects the cells) | lines that do not express PPM1E (16) vs lines expressing it (32) | the lines without PPM1E: 0.88× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: ANKRD6, LONRF2, SNRPN; maybe low, not absent |
| [[SCAMP5]] | 5 µM | C | SCAMP5 activity raises the cells' numbers under Panobinostat 5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.58× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| [[TACC2]] | 5 µM | C | TACC2 activity raises the cells' numbers under Panobinostat 5 µM (protects the cells) | lines that do not express TACC2 (3) vs lines expressing it (45) | the lines without TACC2: 0.58× the cells of the other lines | 0.029 | ⚠ few lines (3 vs 47); across organs; also absent: NME3, OSR2, H1-0; maybe low, not absent |
| [[TMEM216]] | 5 µM | C | TMEM216 activity raises the cells' numbers under Panobinostat 5 µM (protects the cells) | lines that do not express TMEM216 (6) vs lines expressing it (42) | the lines without TMEM216: 0.70× the cells of the other lines | 0.097 | ⚠ tissue-confounded; across organs; also absent: H1-0, LPIN3, TACC2 |
| [[LINC03015]] | 0.5 µM | C | LINC03015's natural level lowers the cells' numbers under Panobinostat 0.5 µM (makes them more sensitive) | LINC03015's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.77 | 0.162 over the table, 0.002 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ARID5A]] | 0.5 µM | C | ARID5A's natural level lowers the cells' numbers under Panobinostat 0.5 µM (makes them more sensitive) | ARID5A's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.75 | 0.162 over the table, 0.002 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 2,338 arrows, 2,338 of them with an alert ⚠; grade A 0, B 2,338, C 0. Shown: the 15 strongest; 2,323 more arrows (2,323 of them with an alert ⚠) not shown.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[CDC23]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CDC23's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[CMIP]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CMIP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[CROCCP3]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CROCCP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[CYB561]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises CYB561's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[DNAJC2]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DNAJC2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[ENSG00000288899]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ENSG00000288899's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[FAM78B]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FAM78B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[FBXW9]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises FBXW9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[FMN1]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FMN1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[LRRC51]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises LRRC51's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[MRPS7]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises MRPS7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[NCBP3]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises NCBP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[RAPGEF5]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RAPGEF5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | [[REXO1]] | moves it that way too | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises REXO1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | [[ABRACL]] | moves it that way too | B | HDAC6 activity raises ABRACL's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Panobinostat"
- `tables/drugdoses.parquet` — dd in 774, 775, 776
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

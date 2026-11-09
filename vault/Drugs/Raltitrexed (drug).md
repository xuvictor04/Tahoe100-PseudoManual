---
drug: "Raltitrexed"
type: "drug"
salt_base: "Raltitrexed"
targets: "TYMS"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 142
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Raltitrexed

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: TYMS · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 75 / 142; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.35 / 0.57.
> Flags by dose: - / - / cell-cycle shift. ⚠ 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:A12 | 0 / 0 | — | -0.00 | +0.9/+0.9/+1.0 | — |
| 0.5 µM | [[Plate 05]]:A12 | 59 / 16 | — | -0.73 | +3.9/+1.0/+2.2 | — |
| 5 µM | [[Plate 14]]:A12 | 96 / 46 | 0.878 | +0.40 | +6.0/+2.3/+2.6 | ⚠ cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (59 genes, none with an alert; 12 shown): [[CCNE2]] 1.60× (z +5.9, 18/44 lines), [[DCK]] 1.32× (z +5.1, 24/48 lines), [[ENSG00000259316]] 1.52× (z +4.9, 13/43 lines), [[PDCD10]] 1.22× (z +4.4, 21/48 lines), [[ELP5]] 1.35× (z +4.3, 17/46 lines), [[ENSG00000289293]] 1.58× (z +4.2, 11/45 lines), [[ZNF367]] 1.33× (z +4.2, 7/42 lines), [[PPIL1]] 1.38× (z +4.1, 10/44 lines), [[USP1]] 1.29× (z +4.1, 24/48 lines), [[CENPU]] 1.42× (z +4.0, 25/48 lines), [[DNA2]] 1.24× (z +3.9, 11/47 lines), [[FANCD2]] 1.24× (z +3.8, 20/47 lines)

**5 µM** (96 genes, 95 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 13 shown): [[DTL]] ⚠ 1.45× (z +7.2, 39/48 lines; cell-cycle shift, explains ~74% of this change), [[CCNE2]] ⚠ 1.44× (z +6.5, 19/48 lines; cell-cycle shift, explains ~63% of this change), [[CDC45]] ⚠ 1.41× (z +6.2, 18/45 lines; cell-cycle shift, explains ~81% of this change), [[ATAD2]] ⚠ 1.26× (z +6.1, 24/48 lines; cell-cycle shift, explains ~83% of this change), [[CDC6]] ⚠ 1.35× (z +5.8, 27/48 lines; cell-cycle shift, explains ~73% of this change), [[BLM]] ⚠ 1.26× (z +5.8, 19/46 lines; cell-cycle shift, explains ~89% of this change), [[EXO1]] ⚠ 1.36× (z +5.6, 26/46 lines; cell-cycle shift, explains ~89% of this change), [[POLA2]] ⚠ 1.25× (z +5.5, 17/48 lines; cell-cycle shift, explains ~72% of this change), [[RRM2]] ⚠ 1.39× (z +5.5, 35/46 lines; cell-cycle shift, explains ~75% of this change), [[WDR76]] ⚠ 1.30× (z +5.5, 15/46 lines; cell-cycle shift, explains ~93% of this change), [[MCM10]] ⚠ 1.40× (z +5.4, 22/44 lines; cell-cycle shift, explains ~97% of this change), [[FAM111B]] ⚠ 1.56× (z +5.4, 22/38 lines; cell-cycle shift, explains ~89% of this change), [[AZU1]] 1.38× (z +3.1, 4/43 lines; cell-cycle shift (explains ~13% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (16 genes, none with an alert; 12 shown): [[ENSG00000259723]] 0.744× (z -3.9, 6/26 lines), [[ENSG00000284116]] 0.730× (z -3.9, 12/44 lines), [[LNP1]] 0.751× (z -3.6, 11/40 lines), [[RNF217-AS1]] 0.693× (z -3.6, 12/36 lines), [[HSD17B7]] 0.779× (z -3.5, 12/45 lines), [[APBA3]] 0.762× (z -3.5, 8/44 lines), [[GLUD1P3]] 0.750× (z -3.4, 13/44 lines), [[TMEM9B-AS1]] 0.737× (z -3.3, 16/41 lines), [[MROH7]] 0.708× (z -3.2, 4/25 lines), [[C2orf27A]] 0.832× (z -3.1, 10/43 lines), [[AGRN]] 0.803× (z -3.0, 21/47 lines), [[BORCS7-ASMT]] 0.798× (z -3.0, 12/45 lines)

**5 µM** (46 genes, 42 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 16 shown): [[ENSG00000269237]] ⚠ 0.809× (z -4.0, 6/41 lines; cell-cycle shift, explains ~15% of this change), [[CXCL13]] ⚠ 0.718× (z -3.9, 10/40 lines; cell-cycle shift, explains ~43% of this change), [[LINC00640]] ⚠ 0.787× (z -3.8, 10/45 lines; cell-cycle shift, explains ~21% of this change), [[LINC02649]] ⚠ 0.824× (z -3.8, 18/46 lines; cell-cycle shift, explains ~50% of this change), [[ENSG00000287943]] ⚠ 0.751× (z -3.8, 6/37 lines; cell-cycle shift, explains ~30% of this change), [[SLAIN1]] ⚠ 0.824× (z -3.8, 4/26 lines; cell-cycle shift, explains ~5% of this change), [[TMEM178A]] ⚠ 0.760× (z -3.8, 6/44 lines; cell-cycle shift, explains ~26% of this change), [[SYCP2L]] ⚠ 0.807× (z -3.7, 14/43 lines; cell-cycle shift, explains ~37% of this change), [[SIRT5]] ⚠ 0.825× (z -3.7, 7/48 lines; cell-cycle shift, explains ~47% of this change), [[LINC02641]] ⚠ 0.747× (z -3.6, 8/34 lines; cell-cycle shift, explains ~31% of this change), [[ENSG00000288583]] ⚠ 0.789× (z -3.6, 6/40 lines; cell-cycle shift, explains ~44% of this change), [[ZNF487]] ⚠ 0.823× (z -3.5, 10/48 lines; cell-cycle shift, explains ~32% of this change), [[H1-3]] 0.702× (z -3.4, 15/36 lines; cell-cycle shift (explains ~0% here)), [[H3C12]] 0.769× (z -3.3, 9/48 lines; cell-cycle shift (explains ~0% here)), [[DEPTOR]] 0.815× (z -3.3, 6/42 lines; cell-cycle shift (explains ~0% here)), [[H1-2]] 0.762× (z -3.1, 20/48 lines; cell-cycle shift (explains ~0% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 006]] (+2.1) | — |
| 5 µM | [[Module 006]] (+2.8) | [[Module 170]] (-2.8), [[Module 234]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[HT-29 (line)]] (1.58), [[LS 180 (line)]] (1.54), [[COLO 205 (line)]] (1.42), [[CFPAC-1 (line)]] (1.40) · weakest: [[NCI-H1792 (line)]] (0.0825), [[CHP-212 (line)]] (0.274), [[NCI-H661 (line)]] (0.376) |
| 5 µM | — | [[COLO 205 (line)]] (1.98), [[HT-29 (line)]] (1.95), [[SNU-1 (line)]] (1.68), [[LS 180 (line)]] (1.65) · weakest: [[NCI-H2122 (line)]] (0.147), [[NCI-H1792 (line)]] (0.437), [[NCI-H2347 (line)]] (0.539) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 6 next most similar without an alert.*

- [[Trifluridine (drug)]] (+0.69, DNA synthesis/repair inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Balsalazide (sodium hydrate) (drug)]] (+0.64, JAK/STAT inhibitor, ⚠ only 9 significant genes); [[Oxaliplatin (drug)]] (+0.64, DNA synthesis/repair inhibitor, ⚠ only 7 significant genes); [[Rimonabant (drug)]] (+0.61, unclear, ⚠ only 7 significant genes); [[Megestrol (drug)]] (+0.57, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Retinoic acid (drug)]] (+0.56, Retinoic receptor agonist); [[Temuterkib (drug)]] (+0.53, Other MAPK inhibitor, ⚠ only 3 significant genes); [[Palmatine (chloride) (drug)]] (+0.53, unclear); [[Pyridoxine (hydrochloride) (drug)]] (+0.53, unclear); [[Larotrectinib (drug)]] (+0.50, Other TK inhibitor); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.50, unclear); [[Diammonium Glycyrrhizinate (drug)]] (+0.48, unclear); [[Busulfan (drug)]] (+0.48, DNA synthesis/repair inhibitor); [[Diphenhydramine (drug)]] (+0.46, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MTMR7]] | 0.5 µM | B | MTMR7 activity raises the cells' numbers under Raltitrexed 0.5 µM (protects the cells) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 0.82× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[KCNK6]] | 0.5 µM | B | KCNK6 activity lowers the cells' numbers under Raltitrexed 0.5 µM (makes them more sensitive) | lines that do not express KCNK6 (12) vs lines expressing it (36) | the lines without KCNK6: 1.25× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: ALS2CL, LRRK1, CDCP1 |
| [[INPP4B]] | 0.5 µM | B | INPP4B activity lowers the cells' numbers under Raltitrexed 0.5 µM (makes them more sensitive) | lines that do not express INPP4B (10) vs lines expressing it (38) | the lines without INPP4B: 1.24× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[ENSG00000285458]] | 0.5 µM | C | ENSG00000285458 activity lowers the cells' numbers under Raltitrexed 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000285458 (5) vs lines expressing it (43) | the lines without ENSG00000285458: 1.31× the cells of the other lines | 0.027 | ⚠ tissue-confounded; across organs; also absent: TBILA, GCA, RILP; maybe low, not absent |
| [[RARG]] | 0.5 µM | C | RARG activity lowers the cells' numbers under Raltitrexed 0.5 µM (makes them more sensitive) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 1.36× the cells of the other lines | 0.031 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| [[PLEKHN1]] | 0.5 µM | C | PLEKHN1 activity lowers the cells' numbers under Raltitrexed 0.5 µM (makes them more sensitive) | lines that do not express PLEKHN1 (3) vs lines expressing it (45) | the lines without PLEKHN1: 1.38× the cells of the other lines | 0.035 | ⚠ few lines (3 vs 47); across organs; also absent: SAT1, ARHGAP27, MYH16 |
| [[RILP]] | 0.5 µM | C | RILP activity lowers the cells' numbers under Raltitrexed 0.5 µM (makes them more sensitive) | lines that do not express RILP (3) vs lines expressing it (45) | the lines without RILP: 1.37× the cells of the other lines | 0.040 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KCP, RABGEF1P3; maybe low, not absent |
| [[ACCS]] | 0.5 µM | C | ACCS activity lowers the cells' numbers under Raltitrexed 0.5 µM (makes them more sensitive) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 1.27× the cells of the other lines | 0.075 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |
| [[PICART1]] | 0.5 µM | C | PICART1 activity lowers the cells' numbers under Raltitrexed 0.5 µM (makes them more sensitive) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 1.30× the cells of the other lines | 0.090 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Raltitrexed"
- `tables/drugdoses.parquet` — dd in 869, 870, 871
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

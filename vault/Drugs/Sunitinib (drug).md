---
drug: "Sunitinib"
type: "drug"
salt_base: "Sunitinib"
targets: "KDR, PDGFRB"
moa_fine: "Multi-TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1157
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Sunitinib

*Multi-TK inhibitor (inhibitor/antagonist) · targets: KDR, PDGFRB · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 11 / 4 / 1157; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.28 / 0.33.
> Flags by dose: - / - / toxic. ⚠ 5 µM: toxic (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:C11 | 8 / 3 | — | -0.47 | -0.6/-0.2/+0.5 | — |
| 0.5 µM | [[Plate 11]]:C11 | 3 / 1 | — | +0.04 | +0.4/+0.7/+0.6 | — |
| 5 µM | [[Plate 12]]:C11 | 970 / 187 | — | -1.26 | -3.1/-1.0/+0.3 | ⚠ toxic |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (8 genes, none with an alert): [[ENSG00000284946]] 1.43× (z +3.3, 4/40 lines), [[CAMK1]] 1.28× (z +3.2, 2/35 lines), [[UBE2R2-AS1]] 1.27× (z +3.1, 5/44 lines), [[ENSG00000236924]] 1.24× (z +2.9, 3/37 lines), [[CRISPLD1]] 1.36× (z +2.9, 1/19 lines), [[ENSG00000288612]] 1.37× (z +2.9, 1/38 lines), [[DAAM2]] 1.46× (z +2.9, 0/13 lines), [[RPS10-NUDT3]] 1.38× (z +2.6, 2/45 lines)

**0.5 µM** (3 genes, none with an alert): [[CLPTM1L]] 1.25× (z +3.0, 12/48 lines), [[MCM2]] 1.27× (z +3.0, 5/44 lines), [[BCHE]] 1.29× (z +3.0, 4/13 lines)

**5 µM** (970 genes, 970 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[LGI4]] ⚠ 2.34× (z +7.2, 11/26 lines), [[KLRD1]] ⚠ 2.40× (z +7.0, 28/39 lines), [[ENSG00000269967]] ⚠ 2.13× (z +6.8, 23/40 lines), [[MGC4859]] ⚠ 1.97× (z +6.7, 19/33 lines), [[LINC01208]] ⚠ 1.76× (z +6.6, 19/42 lines), [[MAP7D2]] ⚠ 1.71× (z +6.5, 28/43 lines), [[RPS10-NUDT3]] ⚠ 2.19× (z +6.4, 27/44 lines), [[NPR3]] ⚠ 1.61× (z +6.3, 14/36 lines), [[ENSG00000232884]] ⚠ 1.85× (z +6.3, 7/27 lines), [[LINC01762]] ⚠ 2.27× (z +6.3, 12/22 lines), [[COPG2IT1]] ⚠ 1.83× (z +6.1, 14/27 lines), [[ENSG00000285635]] ⚠ 1.53× (z +5.9, 15/31 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[SOX2-OT]] 0.782× (z -3.3, 12/46 lines), [[UGT1A6]] 0.734× (z -3.3, 0/12 lines), [[PKN2-AS1]] 0.738× (z -3.3, 7/47 lines)

**0.5 µM** (1 gene, none with an alert): [[ALG12]] 0.826× (z -3.5, 7/44 lines)

**5 µM** (187 genes, 187 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[ABTB3]] ⚠ 0.710× (z -6.0, 16/25 lines), [[TENT5A]] ⚠ 0.713× (z -5.9, 25/37 lines), [[ATP2B4]] ⚠ 0.769× (z -5.6, 24/40 lines), [[GMDS]] ⚠ 0.792× (z -5.3, 34/48 lines), [[DAB2]] ⚠ 0.727× (z -5.2, 17/30 lines), [[CREB5]] ⚠ 0.752× (z -5.0, 20/33 lines), [[SORBS1]] ⚠ 0.770× (z -5.0, 21/41 lines), [[KITLG]] ⚠ 0.635× (z -4.9, 22/37 lines), [[CEP83]] ⚠ 0.796× (z -4.9, 23/47 lines), [[MARCHF3]] ⚠ 0.753× (z -4.9, 24/42 lines), [[TAF4B]] ⚠ 0.752× (z -4.9, 27/48 lines), [[ITPR1]] ⚠ 0.773× (z -4.7, 23/33 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 024]] (+3.0), [[Module 054]] (+2.8), [[Module 168]] (+2.4) | [[Module 051]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[hTERT-HPNE (line)]] (-5.0), [[C32 (line)]] (-4.3), [[NCI-H2030 (line)]] (-3.2), [[HEC-1-A (line)]] (-3.2) | [[SW 1088 (line)]] (2.12), [[CHP-212 (line)]] (1.75), [[AN3 CA (line)]] (1.53), [[hTERT-HPNE (line)]] (1.48) · weakest: [[NCI-H1573 (line)]] (0.488), [[CFPAC-1 (line)]] (0.502), [[SK-MEL-2 (line)]] (0.518) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: toxic. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Imiquimod (hydrochloride) (drug)]] (+0.73, unclear, ⚠ vector dose flagged: toxic); [[Docetaxel (Trihydrate) (drug)]] (+0.72, Microtubule inhibitor); [[Methylprednisolone succinate (drug)]] (+0.70, Glucocorticoid receptor agonist); [[Darolutamide (drug)]] (+0.70, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Saquinavir (drug)]] (+0.67, unclear); [[Bicalutamide (drug)]] (+0.65, Androgen receptor antagonist); [[Erythromycin (drug)]] (+0.64, unclear); [[Fingolimod (hydrochloride) (drug)]] (+0.64, unclear, ⚠ vector dose flagged: toxic); [[Ipatasertib (drug)]] (+0.63, PI3K/AKT inhibitor); [[Drospirenone (drug)]] (+0.62, unclear); [[Celecoxib (drug)]] (+0.62, Cyclooxygenase inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[BMPER]] | 5 µM | B | BMPER activity lowers the cells' numbers under Sunitinib 5 µM (makes them more sensitive) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 1.24× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Sunitinib 5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.28× the cells of the other lines | 0.062 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[RSPO3]] | 5 µM | B | RSPO3 activity lowers the cells' numbers under Sunitinib 5 µM (makes them more sensitive) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 1.27× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[CNRIP1]] | 5 µM | B | CNRIP1 activity lowers the cells' numbers under Sunitinib 5 µM (makes them more sensitive) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 1.15× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity lowers the cells' numbers under Sunitinib 5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.23× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[CYB561]] | 5 µM | C | CYB561 activity raises the cells' numbers under Sunitinib 5 µM (protects the cells) | lines that do not express CYB561 (3) vs lines expressing it (45) | the lines without CYB561: 0.62× the cells of the other lines | 0.030 | ⚠ few lines (3 vs 47); across organs; also absent: MATN1-AS1, E2F8, PBX4; maybe low, not absent |
| [[PLEKHH1]] | 5 µM | C | PLEKHH1 activity raises the cells' numbers under Sunitinib 5 µM (protects the cells) | lines that do not express PLEKHH1 (4) vs lines expressing it (44) | the lines without PLEKHH1: 0.70× the cells of the other lines | 0.076 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: BMP8B, E2F8, RIMKLA |
| [[EZR]], [[TMC7]] | 5 µM | C | EZR, TMC7 activity raises the cells' numbers under Sunitinib 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.68× the cells of the other lines | 0.097 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| KDR | [[PPARD]] | moves it that way too | B | KDR activity raises PPARD's level | compounds that target KDR: 5 of 8 lower it (Cabozantinib, Ponatinib, Regorafenib, Sulfatinib, Sunitinib) | 62% of the class's compounds vs 6.2% of all compounds | 0.036 | ⚠ off-target possible; 5 compounds; artifact flags |
| KDR | [[DNAJB6]] | does not move it that way (the class's other compounds do) | B | KDR activity raises DNAJB6's level | compounds that target KDR: 3 of 8 lower it (Cabozantinib, Ponatinib, c-Kit-IN-1) | 38% of the class's compounds vs 1.7% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| KDR | [[DUSP10]] | moves it that way too | B | KDR activity raises DUSP10's level | compounds that target KDR: 4 of 8 lower it (Cabozantinib, Ponatinib, Sunitinib, c-Kit-IN-1) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |
| KDR | [[PGLS-DT]] | moves it that way too | B | KDR activity lowers PGLS-DT's level | compounds that target KDR: 4 of 8 raise it (Cabozantinib, Ponatinib, Sunitinib, c-Kit-IN-1) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Sunitinib"
- `tables/drugdoses.parquet` — dd in 970, 971, 972
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

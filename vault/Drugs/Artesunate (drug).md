---
drug: "Artesunate"
type: "drug"
salt_base: "Artesunate"
targets: ""
moa_fine: "JAK/STAT inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 519
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Artesunate

*JAK/STAT inhibitor (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 39 / 313 / 519; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.15 / 0.68.
> Flags by dose: - / - / cell-cycle shift. ⚠ 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:G12 | 32 / 7 | — | +0.38 | +0.1/-1.0/-1.5 | — |
| 0.5 µM | [[Plate 05]]:G12 | 116 / 197 | — | +0.82 | -2.3/-0.9/-1.0 | — |
| 5 µM | [[Plate 14]]:G12 | 201 / 318 | 0.941 | +0.32 | -6.0/-2.7/-0.9 | ⚠ cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (32 genes, none with an alert; 12 shown): [[CACNA1D]] 1.37× (z +4.9, 15/25 lines), [[ZNF618]] 1.35× (z +3.9, 17/39 lines), [[ARRB1]] 1.23× (z +3.8, 10/47 lines), [[ANK3]] 1.22× (z +3.6, 16/25 lines), [[ADAM22]] 1.25× (z +3.5, 10/36 lines), [[ADAMTS13]] 1.38× (z +3.5, 6/45 lines), [[SNED1]] 1.30× (z +3.5, 10/40 lines), [[ZNF248]] 1.20× (z +3.5, 13/48 lines), [[ENSG00000237356]] 1.32× (z +3.5, 13/42 lines), [[PLPP3]] 1.24× (z +3.5, 6/43 lines), [[SMAD6]] 1.50× (z +3.4, 17/44 lines), [[MINDY4]] 1.30× (z +3.4, 2/43 lines)

**0.5 µM** (116 genes, 1 with an alert ⚠; 13 shown): [[NIBAN1]] 2.18× (z +12.7, 31/37 lines), [[TRIB3]] 2.31× (z +11.7, 41/45 lines), [[SLC7A1]] ⚠ 1.56× (z +10.9, 42/47 lines; position correction uncertain), [[ASNS]] 2.25× (z +10.5, 40/44 lines), [[YARS1]] 1.52× (z +9.1, 43/48 lines), [[AARS1]] 1.75× (z +9.0, 44/48 lines), [[IARS1]] 1.78× (z +8.9, 45/48 lines), [[PSAT1]] 1.97× (z +8.7, 34/40 lines), [[PCK2]] 1.82× (z +8.3, 31/47 lines), [[TCEA1]] 1.55× (z +8.3, 39/48 lines), [[WARS1]] 1.67× (z +8.2, 40/47 lines), [[CARS1]] 1.48× (z +8.0, 43/48 lines), [[GOT1]] 2.02× (z +8.0, 38/48 lines)

**5 µM** (201 genes, 67 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 13 shown): [[TRIB3]] 2.41× (z +16.8, 42/45 lines; cell-cycle shift (explains ~13% here)), [[NIBAN1]] 2.14× (z +16.7, 33/37 lines; cell-cycle shift (explains ~5% here)), [[ASNS]] 2.29× (z +15.2, 41/44 lines; cell-cycle shift (explains ~0% here)), [[SLC7A1]] ⚠ 1.49× (z +13.9, 42/47 lines; position correction uncertain; cell-cycle shift (explains ~5% here)), [[PSAT1]] 2.13× (z +13.7, 37/40 lines; cell-cycle shift (explains ~0% here)), [[PCK2]] 1.98× (z +13.5, 42/47 lines; cell-cycle shift (explains ~7% here)), [[YARS1]] 1.54× (z +13.1, 43/48 lines; cell-cycle shift (explains ~0% here)), [[CARS1]] 1.59× (z +12.9, 45/48 lines; cell-cycle shift (explains ~4% here)), [[AARS1]] 1.79× (z +12.5, 46/48 lines; cell-cycle shift (explains ~11% here)), [[TCEA1]] 1.59× (z +11.6, 43/48 lines; cell-cycle shift (explains ~5% here)), [[ARHGEF2]] 1.68× (z +11.5, 43/47 lines; cell-cycle shift (explains ~14% here)), [[AKNA]] 1.68× (z +11.1, 34/47 lines; cell-cycle shift (explains ~6% here)), [[IARS1]] 1.67× (z +11.1, 46/48 lines; cell-cycle shift (explains ~1% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (7 genes, none with an alert): [[XPOT]] 0.812× (z -4.3, 22/48 lines), [[H4C3]] 0.551× (z -3.6, 39/48 lines), [[CHMP4C]] 0.807× (z -3.4, 13/32 lines), [[PTAFR]] 0.753× (z -3.4, 1/19 lines), [[PHGDH]] 0.784× (z -3.0, 8/43 lines), [[CEBPG]] 0.821× (z -3.0, 14/48 lines), [[SLC31A1]] 0.792× (z -2.9, 19/48 lines)

**0.5 µM** (197 genes, none with an alert; 12 shown): [[PROM1]] 0.618× (z -5.9, 2/11 lines), [[ELAVL2]] 0.628× (z -5.8, 3/14 lines), [[SMOC2]] 0.495× (z -5.2, 3/14 lines), [[UHRF1]] 0.580× (z -5.2, 23/46 lines), [[B3GAT1-DT]] 0.425× (z -5.1, 3/13 lines), [[ENSG00000251652]] 0.608× (z -4.9, 0/11 lines), [[UBE2QL1]] 0.545× (z -4.8, 2/14 lines), [[CHDH]] 0.648× (z -4.8, 5/24 lines), [[GALNT14]] 0.755× (z -4.8, 3/24 lines), [[RASGEF1A]] 0.585× (z -4.7, 4/21 lines), [[MAGEA3-DT]] 0.756× (z -4.7, 1/19 lines), [[POU5F1]] 0.726× (z -4.7, 1/21 lines)

**5 µM** (318 genes, 198 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 22 shown): [[UHRF1]] ⚠ 0.516× (z -8.9, 33/46 lines; cell-cycle shift, explains ~32% of this change), [[FAM111B]] ⚠ 0.517× (z -8.1, 32/38 lines; cell-cycle shift, explains ~59% of this change), [[AP1S3]] ⚠ 0.803× (z -7.3, 22/44 lines; cell-cycle shift, explains ~27% of this change), [[FANCA]] ⚠ 0.705× (z -7.3, 34/48 lines; cell-cycle shift, explains ~56% of this change), [[DHCR24]] 0.677× (z -7.3, 33/44 lines; cell-cycle shift (explains ~22% here)), [[CDC45]] ⚠ 0.683× (z -7.0, 26/45 lines; cell-cycle shift, explains ~71% of this change), [[COBL]] 0.805× (z -6.8, 15/25 lines; cell-cycle shift (explains ~0% here)), [[MCM10]] ⚠ 0.663× (z -6.6, 30/44 lines; cell-cycle shift, explains ~79% of this change), [[CDC7]] ⚠ 0.699× (z -6.5, 26/46 lines; cell-cycle shift, explains ~50% of this change), [[MMS22L]] ⚠ 0.749× (z -6.5, 34/48 lines; cell-cycle shift, explains ~48% of this change), [[GALNT14]] ⚠ 0.766× (z -6.4, 7/24 lines; cell-cycle shift, explains ~19% of this change), [[LMNB1]] ⚠ 0.741× (z -6.4, 29/47 lines; cell-cycle shift, explains ~32% of this change), [[BMP5]] 0.590× (z -6.2, 7/10 lines; cell-cycle shift (explains ~0% here)), [[BCL2]] 0.733× (z -6.2, 16/37 lines; cell-cycle shift (explains ~14% here)), [[LYPD6]] 0.641× (z -6.1, 25/33 lines; cell-cycle shift (explains ~19% here)), [[LRP8]] 0.719× (z -6.0, 30/46 lines; cell-cycle shift (explains ~17% here)), [[DIO2]] 0.652× (z -5.8, 18/34 lines; cell-cycle shift (explains ~0% here)), [[MID1]] 0.781× (z -5.7, 27/42 lines; cell-cycle shift (explains ~6% here)), [[GBX2-AS1]] 0.690× (z -5.7, 20/34 lines; cell-cycle shift (explains ~3% here)), [[TCF4]] 0.781× (z -5.5, 12/23 lines; cell-cycle shift (explains ~0% here)), [[SERTAD4]] 0.607× (z -5.3, 15/32 lines; cell-cycle shift (explains ~14% here)), [[C1GALT1C1]] 0.732× (z -5.3, 23/47 lines; cell-cycle shift (explains ~15% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 063]] (+4.1), [[Module 133]] (+3.7), [[Module 234]] (+2.0) | [[Module 006]] (-2.4), [[Module 177]] (-2.1) |
| 5 µM | [[Module 063]] (+6.5), [[Module 133]] (+6.0), [[Module 041]] (+3.5) | [[Module 006]] (-4.7), [[Module 004]] (-3.2), [[Module 005]] (-2.8) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 900 (line)]] (1.16), [[NCI-H1573 (line)]] (1.15), [[Panc 03.27 (line)]] (1.14), [[H4 (line)]] (1.12) · weakest: [[NCI-H661 (line)]] (0.457), [[AsPC-1 (line)]] (0.591), [[RKO (line)]] (0.617) |
| 0.5 µM | [[NCI-H2347 (line)]] (-3.6) | [[SNU-1 (line)]] (1.59), [[HCT15 (line)]] (1.55), [[SW48 (line)]] (1.46), [[SW 1088 (line)]] (1.43) · weakest: [[NCI-H2347 (line)]] (0.527), [[AsPC-1 (line)]] (0.594), [[CFPAC-1 (line)]] (0.607) |
| 5 µM | — | [[SNU-1 (line)]] (1.75), [[COLO 205 (line)]] (1.72), [[HCT15 (line)]] (1.69), [[LS 180 (line)]] (1.45) · weakest: [[AsPC-1 (line)]] (0.473), [[NCI-H1792 (line)]] (0.530), [[SW 1271 (line)]] (0.561) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Chlorhexidine (diacetate) (drug)]] (+0.63, unclear); [[Tomivosertib (drug)]] (+0.56, Protein synthesis inhibitor); [[Dihydroartemisinin (drug)]] (+0.53, unclear); [[Neratinib (maleate) (drug)]] (+0.53, EGFR/ERBB inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Terfenadine (drug)]] (+0.52, unclear); [[Pravastatin (sodium) (drug)]] (+0.49, unclear); [[Almonertinib (mesylate) (drug)]] (+0.48, EGFR/ERBB inhibitor); [[palbociclib (drug)]] (+0.47, CDK inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Neratinib (drug)]] (+0.46, EGFR/ERBB inhibitor); [[Cloxacillin (sodium) (drug)]] (+0.44, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[LINC00922]] | 0.5 µM | B | LINC00922 activity raises the cells' numbers under Artesunate 0.5 µM (protects the cells) | lines that do not express LINC00922 (9) vs lines expressing it (39) | the lines without LINC00922: 0.82× the cells of the other lines | 0.057 | ⚠ within organs, on part of the lines; also absent: MGC4859, ENSG00000250149, LINC01811; maybe low, not absent |
| [[LINC02306]] | 0.5 µM | B | LINC02306 activity raises the cells' numbers under Artesunate 0.5 µM (protects the cells) | lines that do not express LINC02306 (13) vs lines expressing it (35) | the lines without LINC02306: 0.85× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: KCNMB2, COP1-DT, LINC02398; maybe low, not absent |
| [[ITPRIP]] | 0.5 µM | B | ITPRIP activity raises the cells' numbers under Artesunate 0.5 µM (protects the cells) | lines that do not express ITPRIP (10) vs lines expressing it (38) | the lines without ITPRIP: 0.83× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[MTMR7]] | 0.5 µM | B | MTMR7 activity raises the cells' numbers under Artesunate 0.5 µM (protects the cells) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 0.85× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[SCUBE2]] | 0.5 µM | B | SCUBE2 activity raises the cells' numbers under Artesunate 0.5 µM (protects the cells) | lines that do not express SCUBE2 (7) vs lines expressing it (41) | the lines without SCUBE2: 0.86× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[ODF3B]] | 0.5 µM | B | ODF3B activity lowers the cells' numbers under Artesunate 0.5 µM (makes them more sensitive) | lines that do not express ODF3B (13) vs lines expressing it (35) | the lines without ODF3B: 1.16× the cells of the other lines | 0.097 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[AOX1]] | 0.5 µM | B | AOX1 activity raises the cells' numbers under Artesunate 0.5 µM (protects the cells) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 0.91× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[EZR]], [[TMC7]] | 0.5 µM | C | EZR, TMC7 activity lowers the cells' numbers under Artesunate 0.5 µM (makes them more sensitive) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 1.29× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| [[ENSG00000231731]] | 0.5 µM | C | ENSG00000231731's natural level raises the cells' numbers under Artesunate 0.5 µM (protects the cells) | ENSG00000231731's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.70 | 0.268 over the table, 0.036 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Artesunate"
- `tables/drugdoses.parquet` — dd in 108, 109, 110
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

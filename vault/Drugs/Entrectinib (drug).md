---
drug: "Entrectinib"
type: "drug"
salt_base: "Entrectinib"
targets: "NTRK1, NTRK2, NTRK3, ROS1, ALK"
moa_fine: "Other TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 569
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Entrectinib

*Other TK inhibitor (inhibitor/antagonist) · targets: NTRK1, NTRK2, NTRK3, ROS1, ALK · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 3 / 569; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.39 / 0.05.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:B7 | 0 / 0 | — | +0.10 | -1.0/+0.1/-0.3 | — |
| 0.5 µM | [[Plate 11]]:B7 | 1 / 2 | — | +0.72 | -2.0/-1.0/-1.2 | — |
| 5 µM | [[Plate 12]]:B7 | 437 / 132 | — | -0.82 | -3.3/-0.5/-0.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[MR1]] 1.32× (z +2.8, 1/42 lines)

**5 µM** (437 genes, none with an alert; 12 shown): [[SCD]] 2.48× (z +12.9, 47/48 lines), [[DHCR7]] 2.21× (z +8.1, 38/44 lines), [[LPIN1]] 1.43× (z +8.0, 32/48 lines), [[IDI1]] 1.82× (z +7.9, 39/47 lines), [[DHCR24]] 1.74× (z +7.2, 30/44 lines), [[FASN]] 2.03× (z +7.1, 38/46 lines), [[ACAT2]] 1.60× (z +7.0, 32/47 lines), [[FADS1]] 1.80× (z +6.7, 37/40 lines), [[FDPS]] 1.71× (z +6.7, 39/48 lines), [[CYP51A1]] 1.52× (z +6.5, 36/47 lines), [[FDFT1]] 1.61× (z +6.5, 38/47 lines), [[MVK]] 1.58× (z +6.4, 20/45 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (2 genes, none with an alert): [[ENSG00000250899]] 0.664× (z -3.9, 7/39 lines), [[ANGPTL2]] 0.686× (z -3.1, 3/17 lines)

**5 µM** (132 genes, none with an alert; 12 shown): [[NUP93]] 0.735× (z -5.0, 28/48 lines), [[POLA2]] 0.757× (z -5.0, 17/47 lines), [[WWC1]] 0.830× (z -4.9, 17/35 lines), [[HELLS]] 0.736× (z -4.9, 29/48 lines), [[BMAL2]] 0.711× (z -4.8, 29/41 lines), [[PNPT1]] 0.732× (z -4.8, 33/47 lines), [[POLA1]] 0.733× (z -4.8, 30/48 lines), [[MTBP]] 0.800× (z -4.8, 22/48 lines), [[FANCB]] 0.787× (z -4.8, 17/48 lines), [[MDN1]] 0.807× (z -4.6, 25/48 lines), [[RAD18]] 0.787× (z -4.6, 26/48 lines), [[BLM]] 0.768× (z -4.6, 13/45 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 086]] (+4.9), [[Module 059]] (+3.2), [[Module 223]] (+2.3) | [[Module 006]] (-3.7), [[Module 020]] (-2.3), [[Module 018]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[H4 (line)]] (1.33), [[SW 1271 (line)]] (1.21), [[HOP62 (line)]] (1.20), [[NCI-H661 (line)]] (1.19) · weakest: [[SHP-77 (line)]] (0.479), [[CFPAC-1 (line)]] (0.594), [[NCI-H1573 (line)]] (0.618) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Almonertinib (hydrochloride) (drug)]] (+0.70, EGFR/ERBB inhibitor); [[olaparib (drug)]] (+0.67, DNA synthesis/repair inhibitor, ⚠ only 3 significant genes); [[Nimesulide (drug)]] (+0.61, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Adagrasib (drug)]] (+0.59, RAS inhibitor); [[Ixazomib (drug)]] (+0.59, Proteasome inhibitor); [[Hydroxyfasudil (drug)]] (+0.59, unclear); [[Saquinavir (drug)]] (+0.58, unclear); [[Almonertinib (mesylate) (drug)]] (+0.58, EGFR/ERBB inhibitor); [[Canagliflozin (hemihydrate) (drug)]] (+0.57, Glucose transporter inhibitor); [[9-ING-41 (drug)]] (+0.57, GSK3 inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000256029]] | 5 µM | C | ENSG00000256029 activity lowers the cells' numbers under Entrectinib 5 µM (makes them more sensitive) | lines that do not express ENSG00000256029 (4) vs lines expressing it (44) | the lines without ENSG00000256029: 1.39× the cells of the other lines | 0.004 | ⚠ few lines (4 vs 46); across organs; also absent: ERRFI1, FXYD5, CAV2; maybe low, not absent |
| [[PHF11]] | 5 µM | C | PHF11 activity lowers the cells' numbers under Entrectinib 5 µM (makes them more sensitive) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 1.37× the cells of the other lines | 0.010 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| [[SETD7]] | 5 µM | C | SETD7 activity lowers the cells' numbers under Entrectinib 5 µM (makes them more sensitive) | lines that do not express SETD7 (3) vs lines expressing it (45) | the lines without SETD7: 1.34× the cells of the other lines | 0.036 | ⚠ few lines (3 vs 47); across organs; also absent: MAP3K5, SNHG15; maybe low, not absent |
| [[LRRCC1]], [[OXR1]] | 5 µM | C | LRRCC1, OXR1 activity lowers the cells' numbers under Entrectinib 5 µM (makes them more sensitive) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 1.28× the cells of the other lines | 0.038 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| [[ENSG00000284716]] | 5 µM | C | ENSG00000284716 activity lowers the cells' numbers under Entrectinib 5 µM (makes them more sensitive) | lines that do not express ENSG00000284716 (5) vs lines expressing it (43) | the lines without ENSG00000284716: 1.25× the cells of the other lines | 0.086 | ⚠ tissue-confounded; across organs; also absent: FTH1, TMEM184A, ZFP36; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Entrectinib"
- `tables/drugdoses.parquet` — dd in 412, 413, 414
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

---
drug: "Erdafitinib"
type: "drug"
salt_base: "Erdafitinib"
targets: "FGFR1, FGFR2, FGFR3, FGFR4"
moa_fine: "Other TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "5"]
best_dose: "0.05"
max_sig_genes: 6
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Erdafitinib

*Other TK inhibitor (inhibitor/antagonist) · targets: FGFR1, FGFR2, FGFR3, FGFR4 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 5 µM): 6 / 0; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.16.
> Flags by dose: - / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:A2 | 5 / 1 | — | +0.09 | +1.7/+1.3/+1.7 | — |
| 5 µM | [[Plate 03]]:A2 | 0 / 0 | — | +0.46 | +0.1/+0.2/-0.3 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[ENSG00000255114]] 1.74× (z +3.9, 6/42 lines), [[SF3B4]] 1.52× (z +3.4, 15/47 lines), [[CCT7]] 1.30× (z +3.2, 16/48 lines), [[MRPL9]] 1.24× (z +3.1, 8/48 lines), [[KATNB1]] 1.28× (z +3.1, 4/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENSG00000290399]] 0.767× (z -3.1, 5/35 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 6 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Pemigatinib (drug)]] (+0.74, Other TK inhibitor); [[Minodronic acid (drug)]] (+0.69, unclear); [[Docetaxel (drug)]] (+0.60, Microtubule inhibitor, ⚠ vector dose flagged: transcription drop; cell-cycle shift); [[LB-100 (drug)]] (+0.60, unclear, ⚠ only 5 significant genes); [[Torkinib (drug)]] (+0.60, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Mozavaptan (drug)]] (+0.59, unclear); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] (+0.57, unclear); [[Pimitespib (drug)]] (+0.56, unclear); [[Dimethyl fumarate (drug)]] (+0.55, unclear); [[Sonidegib (drug)]] (+0.54, Sonic inhibitor); [[Aprepitant (drug)]] (+0.52, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 15 arrows, 15 of them with an alert ⚠; grade A 0, B 7, C 8.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[KLRK1-AS1]] | 5 µM | B | KLRK1-AS1 activity raises the cells' numbers under Erdafitinib 5 µM (protects the cells) | lines that do not express KLRK1-AS1 (11) vs lines expressing it (37) | the lines without KLRK1-AS1: 0.96× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| [[ENSG00000281091]] | 5 µM | B | ENSG00000281091 activity lowers the cells' numbers under Erdafitinib 5 µM (makes them more sensitive) | lines that do not express ENSG00000281091 (12) vs lines expressing it (36) | the lines without ENSG00000281091: 1.18× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, TGFB1I1, AKT3 |
| [[PLS1]] | 5 µM | B | PLS1 activity raises the cells' numbers under Erdafitinib 5 µM (protects the cells) | lines that do not express PLS1 (14) vs lines expressing it (34) | the lines without PLS1: 0.85× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| [[NRIR]] | 5 µM | B | NRIR activity raises the cells' numbers under Erdafitinib 5 µM (protects the cells) | lines that do not express NRIR (14) vs lines expressing it (34) | the lines without NRIR: 0.92× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[CACNG7]] | 5 µM | B | CACNG7 activity lowers the cells' numbers under Erdafitinib 5 µM (makes them more sensitive) | lines that do not express CACNG7 (21) vs lines expressing it (27) | the lines without CACNG7: 1.15× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[AXL]] | 5 µM | B | AXL activity lowers the cells' numbers under Erdafitinib 5 µM (makes them more sensitive) | lines that do not express AXL (14) vs lines expressing it (34) | the lines without AXL: 1.19× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2 |
| [[REEP2]] | 5 µM | B | REEP2 activity lowers the cells' numbers under Erdafitinib 5 µM (makes them more sensitive) | lines that do not express REEP2 (12) vs lines expressing it (36) | the lines without REEP2: 1.12× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: DLK2, ENSG00000234405, STARD9; maybe low, not absent |
| [[C2orf74]] | 5 µM | C | C2orf74 activity lowers the cells' numbers under Erdafitinib 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.18× the cells of the other lines | 0.011 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[NR3C1]] | 5 µM | C | NR3C1 activity lowers the cells' numbers under Erdafitinib 5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.18× the cells of the other lines | 0.024 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[SEMA4G]] | 5 µM | C | SEMA4G activity raises the cells' numbers under Erdafitinib 5 µM (protects the cells) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 0.81× the cells of the other lines | 0.025 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| [[LIFR]] | 5 µM | C | LIFR activity lowers the cells' numbers under Erdafitinib 5 µM (makes them more sensitive) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 1.15× the cells of the other lines | 0.056 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| [[SIX1]] | 5 µM | C | SIX1 activity lowers the cells' numbers under Erdafitinib 5 µM (makes them more sensitive) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 1.17× the cells of the other lines | 0.063 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| [[ENSG00000286964]] | 5 µM | C | ENSG00000286964 activity lowers the cells' numbers under Erdafitinib 5 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.16× the cells of the other lines | 0.081 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |
| [[FIGN]] | 5 µM | C | FIGN activity lowers the cells' numbers under Erdafitinib 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.12× the cells of the other lines | 0.085 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[SPART-AS1]] | 5 µM | C | SPART-AS1 activity lowers the cells' numbers under Erdafitinib 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.12× the cells of the other lines | 0.095 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Erdafitinib"
- `tables/drugdoses.parquet` — dd in 421, 422
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

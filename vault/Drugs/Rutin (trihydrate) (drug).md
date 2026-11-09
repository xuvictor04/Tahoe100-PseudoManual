---
drug: "Rutin (trihydrate)"
type: "drug"
salt_base: "Rutin"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 90
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Rutin (trihydrate)

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 90 / 1 / 3; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.27 / 0.04.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:C7 | 0 / 90 | — | +0.97 | +0.4/+0.3/-1.4 | — |
| 0.5 µM | [[Plate 08]]:C7 | 1 / 0 | — | +0.16 | +0.5/+0.4/-0.4 | — |
| 5 µM | [[Plate 09]]:C7 | 2 / 1 | — | -0.07 | -0.9/-0.0/-0.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[H3C12]] 1.37× (z +2.9, 3/47 lines)

**5 µM** (2 genes, none with an alert): [[ZNF732]] 1.76× (z +2.9, 1/6 lines), [[RHOB]] 1.29× (z +2.7, 14/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (90 genes, none with an alert; 12 shown): [[ENSG00000286026]] 0.386× (z -6.2, 1/19 lines), [[MAL2]] 0.706× (z -5.8, 0/17 lines), [[TXLNGY-1]] 0.616× (z -5.3, 0/17 lines), [[UTY]] 0.727× (z -5.0, 0/17 lines), [[SLC44A4]] 0.563× (z -4.7, 0/11 lines), [[MIR3667HG]] 0.618× (z -4.6, 0/9 lines), [[ESRP1]] 0.694× (z -4.4, 0/17 lines), [[ENSG00000250038]] 0.501× (z -4.4, 1/12 lines), [[SLC25A24P1]] 0.516× (z -4.4, 0/8 lines), [[ARHGEF38]] 0.658× (z -4.3, 0/12 lines), [[UGT2B7]] 0.536× (z -4.2, 1/10 lines), [[SOD3]] 0.397× (z -4.2, 1/14 lines)

**5 µM** (1 gene, none with an alert): [[ENSG00000287917]] 0.670× (z -3.6, 10/35 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 177]] (-2.4), [[Module 024]] (-2.3), [[Module 048]] (-2.1) |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 137]] (-2.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[NCI-H1792 (line)]] (-3.5) | [[SW 1271 (line)]] (1.74), [[SW48 (line)]] (1.55), [[SW 1088 (line)]] (1.54), [[CHP-212 (line)]] (1.51) · weakest: [[KATO III (line)]] (0.448), [[SW480 (line)]] (0.496), [[CFPAC-1 (line)]] (0.502) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Lucanthone (drug)]] (+0.90, unclear); [[Fenofibrate (drug)]] (+0.82, unclear); [[Tucatinib (drug)]] (+0.79, EGFR/ERBB inhibitor); [[Anethole trithione (drug)]] (+0.78, unclear); [[MK-8353 (drug)]] (+0.77, Other MAPK inhibitor); [[Methyl aminolevulinate (hydrochloride) (drug)]] (+0.76, unclear, ⚠ only 3 significant genes); [[Benproperine (phosphate) (drug)]] (+0.76, unclear); [[Erlotinib (drug)]] (+0.75, EGFR/ERBB inhibitor); [[Pyridoxine (hydrochloride) (drug)]] (+0.68, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 14 arrows, 14 of them with an alert ⚠; grade A 0, B 7, C 7.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[KLRC4-KLRK1]], [[KLRK1]] | 0.05 µM | B | KLRC4-KLRK1, KLRK1 activity raises the cells' numbers under Rutin (trihydrate) 0.05 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.85× the cells of the other lines | 0.062 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[HENMT1]] | 0.05 µM | B | HENMT1 activity lowers the cells' numbers under Rutin (trihydrate) 0.05 µM (makes them more sensitive) | lines that do not express HENMT1 (17) vs lines expressing it (31) | the lines without HENMT1: 1.19× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748 |
| [[KLRC3]] | 0.05 µM | B | KLRC3 activity raises the cells' numbers under Rutin (trihydrate) 0.05 µM (protects the cells) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 0.85× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| [[IGFBP2]] | 0.05 µM | B | IGFBP2 activity raises the cells' numbers under Rutin (trihydrate) 0.05 µM (protects the cells) | lines that do not express IGFBP2 (16) vs lines expressing it (32) | the lines without IGFBP2: 0.84× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: CBFA2T3, CHRNA7, FSTL4 |
| [[LINC01237]] | 0.05 µM | B | LINC01237 activity raises the cells' numbers under Rutin (trihydrate) 0.05 µM (protects the cells) | lines that do not express LINC01237 (7) vs lines expressing it (41) | the lines without LINC01237: 0.96× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[INPP4B]] | 0.05 µM | B | INPP4B activity lowers the cells' numbers under Rutin (trihydrate) 0.05 µM (makes them more sensitive) | lines that do not express INPP4B (10) vs lines expressing it (38) | the lines without INPP4B: 1.20× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[AKR1E2]] | 0.05 µM | B | AKR1E2 activity lowers the cells' numbers under Rutin (trihydrate) 0.05 µM (makes them more sensitive) | lines that do not express AKR1E2 (19) vs lines expressing it (29) | the lines without AKR1E2: 1.20× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: FLNC, AFAP1L1, CACNA2D1 |
| [[PICART1]] | 0.05 µM | C | PICART1 activity lowers the cells' numbers under Rutin (trihydrate) 0.05 µM (makes them more sensitive) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 1.34× the cells of the other lines | 0.033 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |
| [[ENSG00000291063]] | 0.05 µM | C | ENSG00000291063 activity lowers the cells' numbers under Rutin (trihydrate) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000291063 (5) vs lines expressing it (43) | the lines without ENSG00000291063: 1.27× the cells of the other lines | 0.033 | ⚠ tissue-confounded; across organs; also absent: RNF135, ENSG00000266865, TMEM54; maybe low, not absent |
| [[LGI4]] | 0.05 µM | C | LGI4 activity lowers the cells' numbers under Rutin (trihydrate) 0.05 µM (makes them more sensitive) | lines that do not express LGI4 (5) vs lines expressing it (43) | the lines without LGI4: 1.25× the cells of the other lines | 0.056 | ⚠ tissue-confounded; across organs; also absent: SLC25A43, FXYD5, NMI; maybe low, not absent |
| [[MARVELD1]] | 0.05 µM | C | MARVELD1 activity lowers the cells' numbers under Rutin (trihydrate) 0.05 µM (makes them more sensitive) | lines that do not express MARVELD1 (4) vs lines expressing it (44) | the lines without MARVELD1: 1.28× the cells of the other lines | 0.075 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: LDHB, GSTP1, E2F7 |
| [[RARG]] | 0.05 µM | C | RARG activity lowers the cells' numbers under Rutin (trihydrate) 0.05 µM (makes them more sensitive) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 1.34× the cells of the other lines | 0.096 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| [[ENSG00000231731]] | 0.05 µM | C | ENSG00000231731's natural level raises the cells' numbers under Rutin (trihydrate) 0.05 µM (protects the cells) | ENSG00000231731's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.305 over the table, 0.065 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[SENP3]] | 0.05 µM | C | SENP3's natural level raises the cells' numbers under Rutin (trihydrate) 0.05 µM (protects the cells) | SENP3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.317 over the table, 0.065 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Rutin (trihydrate)"
- `tables/drugdoses.parquet` — dd in 920, 921, 922
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

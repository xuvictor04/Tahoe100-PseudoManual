---
drug: "Brivudine"
type: "drug"
salt_base: "Brivudine"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 4140
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Brivudine

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 201 / 4140; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.14 / 0.59.
> Flags by dose: - / noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:C5 | 2 / 1 | — | +0.06 | +0.7/+0.3/+0.4 | — |
| 0.5 µM | [[Plate 02]]:C5 | 188 / 13 | — | -0.05 | -0.4/-0.5/-0.4 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:C5 | 2,554 / 1,586 | — | +1.14 | +2.5/+0.6/-1.4 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[NLRP3]] 1.52× (z +3.0, 0/19 lines), [[FAH]] 1.22× (z +2.8, 3/46 lines)

**0.5 µM** (188 genes, none with an alert; 12 shown): [[ENSG00000283674]] 1.72× (z +6.7, 18/32 lines), [[CDC14B]] 1.39× (z +5.9, 25/50 lines), [[ARHGAP44]] 1.43× (z +5.8, 12/32 lines), [[ENSG00000255367]] 1.84× (z +5.7, 12/28 lines), [[PLEKHH2]] 1.48× (z +5.6, 11/34 lines), [[MPP7]] 1.52× (z +5.5, 8/28 lines), [[WDR17]] 1.78× (z +5.4, 13/30 lines), [[STRBP]] 1.25× (z +5.2, 18/49 lines), [[NRG2]] 1.60× (z +5.1, 10/33 lines), [[CAMK2G]] 1.32× (z +5.0, 22/49 lines), [[ROR2]] 1.49× (z +5.0, 4/22 lines), [[MAPT]] 1.47× (z +4.9, 13/38 lines)

**5 µM** (2554 genes, none with an alert; 12 shown): [[B3GALT1]] 7.69× (z +19.1, 25/28 lines), [[RGL1]] 6.42× (z +18.9, 42/44 lines), [[MEGF9]] 3.54× (z +16.9, 45/48 lines), [[OTUD7A]] 5.83× (z +16.9, 40/42 lines), [[DPF3]] 11.9× (z +16.8, 31/32 lines), [[ATP8A1]] 4.76× (z +15.0, 32/35 lines), [[SORBS1]] 4.07× (z +14.0, 38/43 lines), [[MITF]] 4.14× (z +13.3, 32/39 lines), [[SESN3]] 4.21× (z +13.1, 25/28 lines), [[PLEKHH2]] 3.47× (z +13.1, 30/34 lines), [[PRKAR2B]] 5.45× (z +13.1, 33/35 lines), [[STRBP]] 2.11× (z +12.8, 43/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[PDK1-AS1]] 0.832× (z -2.9, 4/48 lines)

**0.5 µM** (13 genes, none with an alert; 12 shown): [[EFCAB2]] 0.711× (z -4.1, 16/48 lines), [[KAT6B]] 0.806× (z -3.8, 25/50 lines), [[EIF4G2]] 0.743× (z -3.7, 43/50 lines), [[DIMT1]] 0.807× (z -3.5, 6/48 lines), [[CD164]] 0.833× (z -3.2, 14/50 lines), [[PDK1-AS1]] 0.768× (z -3.1, 10/48 lines), [[PMF1]] 0.824× (z -3.1, 6/48 lines), [[GPRC5D-AS1]] 0.720× (z -3.1, 8/45 lines), [[BRPF3]] 0.755× (z -3.1, 9/48 lines), [[RAB11B]] 0.766× (z -3.1, 7/48 lines), [[ENSG00000248734]] 0.674× (z -2.9, 1/43 lines), [[SLC38A2]] 0.817× (z -2.9, 15/50 lines)

**5 µM** (1586 genes, none with an alert; 12 shown): [[DHRSX]] 0.246× (z -17.9, 48/48 lines), [[EFCAB2]] 0.175× (z -15.2, 46/48 lines), [[KAT6B]] 0.318× (z -15.1, 48/49 lines), [[PMF1]] 0.307× (z -14.0, 40/48 lines), [[TXNDC15]] 0.392× (z -11.8, 39/48 lines), [[XIAP]] 0.496× (z -10.9, 43/49 lines), [[UBE2J1]] 0.459× (z -10.6, 41/49 lines), [[SENP6]] 0.479× (z -10.6, 47/49 lines), [[MAP3K20]] 0.572× (z -10.5, 36/48 lines), [[FBXW4]] 0.350× (z -10.2, 46/49 lines), [[KMT5B]] 0.542× (z -10.0, 44/49 lines), [[RSF1]] 0.598× (z -9.8, 45/49 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 045]] (+2.4), [[Module 146]] (+2.4), [[Module 115]] (+2.4) | [[Module 095]] (-2.9), [[Module 010]] (-2.2), [[Module 137]] (-2.1) |
| 5 µM | [[Module 085]] (+6.0), [[Module 115]] (+5.8), [[Module 077]] (+5.6) | [[Module 095]] (-11.5), [[Module 088]] (-7.3), [[Module 137]] (-7.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[HT-29 (line)]] (1.36), [[NCI-H23 (line)]] (1.32), [[PANC-1 (line)]] (1.28), [[SW 1271 (line)]] (1.25) · weakest: [[NCI-H596 (line)]] (0.169), [[NCI-H661 (line)]] (0.479), [[BT-474 (line)]] (0.585) |
| 5 µM | [[NCI-H23 (line)]] (-8.5), [[SK-MEL-2 (line)]] (-5.5), [[NCI-H1792 (line)]] (-5.0), [[A-427 (line)]] (-4.9), [[LOX-IMVI (line)]] (-4.5) | [[PANC-1 (line)]] (1.20), [[A549 (line)]] (1.19), [[AsPC-1 (line)]] (1.17), [[HOP62 (line)]] (1.17) · weakest: [[NCI-H2122 (line)]] (0.576), [[AN3 CA (line)]] (0.683), [[SNU-1 (line)]] (0.753) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Belinostat (drug)]] (+0.74, HDAC inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Panobinostat (drug)]] (+0.55, HDAC inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Dimethyl fumarate (drug)]] (+0.54, unclear); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] (+0.54, unclear); [[Fumaric acid (drug)]] (+0.49, unclear); [[Pimitespib (drug)]] (+0.49, unclear); [[Tucidinostat (drug)]] (+0.48, HDAC inhibitor); [[Bexarotene (drug)]] (+0.45, Retinoic receptor agonist); [[Radotinib (drug)]] (+0.44, Other TK inhibitor); [[Tomivosertib (drug)]] (+0.42, Protein synthesis inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000253496]] | 5 µM | B | ENSG00000253496 activity raises the cells' numbers under Brivudine 5 µM (protects the cells) | lines that do not express ENSG00000253496 (13) vs lines expressing it (35) | the lines without ENSG00000253496: 0.80× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC01807, TUSC3, HSPA2; maybe low, not absent |
| [[ENSG00000225647]] | 5 µM | B | ENSG00000225647 activity raises the cells' numbers under Brivudine 5 µM (protects the cells) | lines that do not express ENSG00000225647 (10) vs lines expressing it (38) | the lines without ENSG00000225647: 0.75× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: BTBD6, CPA6; maybe low, not absent |
| [[MGST2]] | 5 µM | B | MGST2 activity raises the cells' numbers under Brivudine 5 µM (protects the cells) | lines that do not express MGST2 (10) vs lines expressing it (38) | the lines without MGST2: 0.70× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| [[RASD1]] | 5 µM | B | RASD1 activity raises the cells' numbers under Brivudine 5 µM (protects the cells) | lines that do not express RASD1 (21) vs lines expressing it (27) | the lines without RASD1: 0.78× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Brivudine"
- `tables/drugdoses.parquet` — dd in 215, 216, 217
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

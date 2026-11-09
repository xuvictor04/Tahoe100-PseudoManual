---
drug: "DTP3"
type: "drug"
salt_base: "DTP3"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 25
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# DTP3

*unclear (inhibitor/antagonist) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 15 / 0 / 25; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.40 / -0.19.
> Flags by dose: unreliable plate only / noisy plate (z scaled) / noisy plate (z scaled). ⚠ 0.05 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:A9 | 5 / 10 | — | +0.41 | -1.3/-2.1/-1.3 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 02]]:G4 | 0 / 0 | — | +0.54 | -0.5/-0.7/-0.7 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:G4 | 18 / 7 | — | -0.30 | -0.5/-0.4/+0.2 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, 5 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[VIM-AS1]] ⚠ 1.28× (z +3.6, 6/41 lines), [[ENSG00000286563]] ⚠ 1.49× (z +3.4, 5/47 lines), [[SLC22A13]] ⚠ 1.44× (z +3.4, 6/46 lines), [[PYGM]] ⚠ 1.60× (z +3.1, 8/47 lines), [[C21orf91-OT1]] ⚠ 1.45× (z +3.1, 2/42 lines)

**5 µM** (18 genes, none with an alert; 12 shown): [[ABTB1]] 2.34× (z +4.3, 15/34 lines), [[YPEL3]] 2.70× (z +4.1, 14/35 lines), [[FBXO21]] 1.27× (z +3.6, 10/48 lines), [[CCNDBP1]] 1.63× (z +3.5, 15/45 lines), [[LRP10]] 1.53× (z +3.4, 15/47 lines), [[DPH1]] 1.63× (z +3.4, 5/43 lines), [[ADGRL4]] 2.13× (z +3.3, 3/18 lines), [[SEC14L2]] 1.43× (z +3.2, 7/45 lines), [[WDR45]] 1.44× (z +3.2, 5/41 lines), [[CNNM3]] 1.42× (z +3.1, 3/38 lines), [[BCL10-AS1]] 1.43× (z +3.1, 11/42 lines), [[MAT2B]] 1.46× (z +3.1, 16/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (10 genes, 10 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[OSTC]] ⚠ 0.731× (z -4.8, 40/48 lines), [[HDGFL2]] ⚠ 0.729× (z -4.4, 27/48 lines), [[FAM162A]] ⚠ 0.652× (z -3.9, 43/47 lines), [[TRIM15]] ⚠ 0.637× (z -3.6, 0/14 lines), [[EFHD2]] ⚠ 0.792× (z -3.3, 11/46 lines), [[NR2F2]] ⚠ 0.757× (z -3.2, 21/47 lines), [[IKBIP]] ⚠ 0.801× (z -3.2, 17/44 lines), [[DBN1]] ⚠ 0.770× (z -3.2, 8/45 lines), [[SPINT2]] ⚠ 0.829× (z -3.1, 6/24 lines), [[TMED1]] ⚠ 0.712× (z -3.1, 5/47 lines)

**5 µM** (7 genes, none with an alert): [[XPO1]] 0.727× (z -3.3, 28/48 lines), [[TPST1]] 0.759× (z -3.2, 12/43 lines), [[EGLN3]] 0.776× (z -3.2, 8/48 lines), [[TENT5A]] 0.706× (z -3.2, 10/36 lines), [[CEP85]] 0.727× (z -3.2, 11/45 lines), [[HSPA4L]] 0.702× (z -3.1, 8/44 lines), [[ASCC3]] 0.792× (z -2.9, 15/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 048]] (-2.0) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[H4 (line)]] (-5.2), [[RPMI-7951 (line)]] (-4.1), [[NCI-H1573 (line)]] (-3.6), [[C32 (line)]] (-3.5), [[LoVo (line)]] (-3.2) | [[LS 180 (line)]] (1.76), [[AN3 CA (line)]] (1.34), [[AsPC-1 (line)]] (1.32), [[A498 (line)]] (1.29) · weakest: [[NCI-H661 (line)]] (0.181), [[SNU-1 (line)]] (0.240), [[A-427 (line)]] (0.481) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Temsirolimus (drug)]] (+0.67, MTOR inhibitor); [[9-ING-41 (drug)]] (+0.66, GSK3 inhibitor); [[XRK3F2 (drug)]] (+0.62, unclear); [[AZD1390 (drug)]] (+0.59, unclear); [[Rapamycin (drug)]] (+0.59, MTOR inhibitor); [[Canagliflozin (hemihydrate) (drug)]] (+0.54, Glucose transporter inhibitor); [[Celecoxib (drug)]] (+0.52, Cyclooxygenase inhibitor); [[Nimesulide (drug)]] (+0.49, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[MK-3903 (drug)]] (+0.49, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SLC29A4]] | 5 µM | B | SLC29A4 activity raises the cells' numbers under DTP3 5 µM (protects the cells) | lines that do not express SLC29A4 (6) vs lines expressing it (42) | the lines without SLC29A4: 0.73× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[PLXNA2]] | 5 µM | B | PLXNA2 activity lowers the cells' numbers under DTP3 5 µM (makes them more sensitive) | lines that do not express PLXNA2 (15) vs lines expressing it (33) | the lines without PLXNA2: 1.17× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[ENSG00000264825]] | 5 µM | B | ENSG00000264825 activity lowers the cells' numbers under DTP3 5 µM (makes them more sensitive) | lines that do not express ENSG00000264825 (24) vs lines expressing it (24) | the lines without ENSG00000264825: 1.19× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: GATA6, TFF1, AGR2; maybe low, not absent |
| [[EZR]], [[TMC7]] | 5 µM | C | EZR, TMC7 activity raises the cells' numbers under DTP3 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.61× the cells of the other lines | 0.029 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "DTP3"
- `tables/drugdoses.parquet` — dd in 311, 312, 313
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

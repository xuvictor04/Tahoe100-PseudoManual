---
drug: "Sonidegib"
type: "drug"
salt_base: "Sonidegib"
targets: "SMO"
moa_fine: "Sonic inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 53
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Sonidegib

*Sonic inhibitor (inhibitor/antagonist) · targets: SMO · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 20 / 53 / 7; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.46 / -0.05.
> Flags by dose: unreliable plate only / low cells (technical?); plate-row cell shift; noisy plate (z scaled) / noisy plate (z scaled). ⚠ 0.05 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:A5 | 14 / 6 | — | +0.36 | -1.4/-0.7/-1.8 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 02]]:E6 | 37 / 16 | — | -1.23 | +0.6/+0.9/+2.1 | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:E6 | 7 / 0 | — | -0.99 | -1.2/-0.7/-0.4 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (14 genes, 14 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[ARID5B]] ⚠ 1.27× (z +3.7, 18/42 lines), [[RBKS]] ⚠ 1.30× (z +3.5, 6/41 lines), [[ZNF608]] ⚠ 1.28× (z +3.4, 12/36 lines), [[MX1]] ⚠ 1.36× (z +3.3, 20/29 lines), [[RNF150]] ⚠ 1.28× (z +3.3, 10/32 lines), [[PARP14]] ⚠ 1.29× (z +3.2, 26/45 lines), [[STAT1]] ⚠ 1.24× (z +3.2, 24/48 lines), [[CFB]] ⚠ 1.43× (z +3.2, 12/28 lines), [[TRIM22]] ⚠ 1.36× (z +3.1, 13/30 lines), [[GBP2]] ⚠ 1.22× (z +3.1, 12/35 lines), [[DDX60]] ⚠ 1.32× (z +3.1, 18/42 lines), [[NREP]] ⚠ 1.33× (z +3.0, 14/35 lines)

**0.5 µM** (37 genes, none with an alert; 12 shown): [[CCT7]] 1.51× (z +4.2, 33/48 lines), [[EIF2B1]] 1.29× (z +3.7, 11/48 lines), [[PPIA]] 1.37× (z +3.7, 24/48 lines), [[SUZ12]] 1.21× (z +3.6, 18/48 lines), [[NDUFA9]] 1.25× (z +3.6, 12/48 lines), [[LAPTM4B]] 1.25× (z +3.6, 10/44 lines), [[ALG3]] 1.49× (z +3.4, 7/45 lines), [[DRG2]] 1.32× (z +3.3, 5/47 lines), [[PPIE]] 1.29× (z +3.3, 6/47 lines), [[SRP9]] 1.24× (z +3.3, 16/48 lines), [[TMEM9B]] 1.30× (z +3.3, 5/46 lines), [[PPID]] 1.33× (z +3.2, 12/48 lines)

**5 µM** (7 genes, none with an alert): [[RNF180]] 1.74× (z +3.9, 0/15 lines), [[ENSG00000274561]] 1.91× (z +3.7, 0/12 lines), [[LIN28B]] 1.61× (z +3.6, 0/16 lines), [[HERC2P10]] 1.71× (z +3.1, 0/9 lines), [[ENSG00000282440]] 2.11× (z +3.0, 0/8 lines), [[NIBAN1]] 1.40× (z +2.9, 10/34 lines), [[NIM1K]] 1.50× (z +2.8, 0/25 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (6 genes, 6 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[NUDT15]] ⚠ 0.772× (z -3.3, 1/47 lines), [[UPP1]] ⚠ 0.747× (z -3.0, 16/39 lines), [[CLMP]] ⚠ 0.786× (z -2.8, 7/23 lines), [[TMEM158]] ⚠ 0.638× (z -2.8, 15/29 lines), [[TRIB3]] ⚠ 0.823× (z -2.7, 5/45 lines), [[NLRP3]] ⚠ 0.706× (z -2.7, 7/19 lines)

**0.5 µM** (16 genes, none with an alert; 12 shown): [[MALAT1]] 0.761× (z -3.5, 43/48 lines), [[TVP23C]] 0.806× (z -3.3, 18/46 lines), [[ENSG00000285696]] 0.696× (z -3.3, 7/39 lines), [[GARRE1]] 0.817× (z -3.2, 15/48 lines), [[TEX21P]] 0.693× (z -3.1, 13/45 lines), [[KCNAB2]] 0.805× (z -3.1, 7/43 lines), [[TPT1-AS1]] 0.799× (z -3.1, 18/48 lines), [[SUGT1P4-STRA6LP]] 0.656× (z -3.1, 6/35 lines), [[L3MBTL1]] 0.791× (z -3.0, 8/41 lines), [[CUL9]] 0.755× (z -3.0, 9/47 lines), [[GRAMD4]] 0.802× (z -3.0, 4/46 lines), [[ENSG00000291067]] 0.807× (z -3.0, 7/42 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[H4 (line)]] (2.30), [[A-172 (line)]] (2.06), [[KATO III (line)]] (2.05), [[SW 1088 (line)]] (1.95) · weakest: [[NCI-H661 (line)]] (0.180), [[HEC-1-A (line)]] (0.335), [[BT-474 (line)]] (0.414) |
| 0.5 µM | — | [[HCT15 (line)]] (1.58), [[SW 1271 (line)]] (1.44), [[hTERT-HPNE (line)]] (1.33), [[C32 (line)]] (1.30) · weakest: [[SHP-77 (line)]] (0.396), [[NCI-H661 (line)]] (0.400), [[NCI-H2347 (line)]] (0.474) |
| 5 µM | [[H4 (line)]] (-4.0), [[SW480 (line)]] (-3.3), [[hTERT-HPNE (line)]] (-3.2) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[BI-78D3 (drug)]] (+0.76, Other MAPK inhibitor); [[Pralsetinib (drug)]] (+0.63, Other TK inhibitor); [[LJI308 (drug)]] (+0.60, Other MAPK inhibitor); [[XRK3F2 (drug)]] (+0.57, unclear); [[Furosemide (drug)]] (+0.56, unclear); [[OTS514 (drug)]] (+0.55, Other MAPK inhibitor); [[Erdafitinib (drug)]] (+0.54, Other TK inhibitor, ⚠ only 6 significant genes); [[Torkinib (drug)]] (+0.53, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[DT-061 (drug)]] (+0.53, unclear); [[Canagliflozin (drug)]] (+0.47, Glucose transporter inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ZP3]] | 5 µM | B | ZP3 activity raises the cells' numbers under Sonidegib 5 µM (protects the cells) | lines that do not express ZP3 (11) vs lines expressing it (37) | the lines without ZP3: 0.83× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[EZR]], [[TMC7]] | 5 µM | C | EZR, TMC7 activity raises the cells' numbers under Sonidegib 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.69× the cells of the other lines | 0.027 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |
| [[KIAA1671]] | 5 µM | C | KIAA1671 activity raises the cells' numbers under Sonidegib 5 µM (protects the cells) | lines that do not express KIAA1671 (3) vs lines expressing it (45) | the lines without KIAA1671: 0.71× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: SOX13, FZD5, PDCD6P1; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Sonidegib"
- `tables/drugdoses.parquet` — dd in 961, 962, 963
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

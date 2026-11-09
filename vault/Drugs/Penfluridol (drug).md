---
drug: "Penfluridol"
type: "drug"
salt_base: "Penfluridol"
targets: "DRD2"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 84
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Penfluridol

*unclear (inhibitor/antagonist) · targets: DRD2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 5 / 84; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.01 / 0.21.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:F6 | 0 / 0 | — | -0.04 | -0.4/+0.0/+0.4 | — |
| 0.5 µM | [[Plate 08]]:F6 | 2 / 3 | — | -0.89 | -0.7/-0.4/-0.6 | — |
| 5 µM | [[Plate 09]]:F6 | 58 / 26 | — | -0.66 | -2.3/-1.5/-0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (2 genes, none with an alert): [[ALKBH6]] 1.32× (z +3.1, 3/46 lines), [[GOT1-DT]] 1.38× (z +2.9, 0/42 lines)

**5 µM** (58 genes, none with an alert; 12 shown): [[GULP1]] 1.28× (z +5.0, 25/43 lines), [[KCNG3]] 1.48× (z +4.7, 6/26 lines), [[HDAC9]] 1.27× (z +4.4, 22/38 lines), [[ENSG00000237596]] 1.49× (z +4.3, 9/33 lines), [[BICDL1]] 1.28× (z +4.3, 9/35 lines), [[TMEM135]] 1.30× (z +4.1, 29/47 lines), [[ENSG00000276150]] 1.45× (z +4.0, 6/37 lines), [[HSPBAP1]] 1.30× (z +3.9, 10/47 lines), [[PPARGC1B]] 1.40× (z +3.7, 12/43 lines), [[SAMD12]] 1.24× (z +3.7, 7/28 lines), [[ZFPM2-AS1]] 1.23× (z +3.7, 17/31 lines), [[CRYM]] 1.48× (z +3.7, 12/34 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (3 genes, none with an alert): [[KIF5C]] 0.750× (z -4.6, 17/47 lines), [[PTGER4]] 0.755× (z -3.5, 12/35 lines), [[EPHX3]] 0.688× (z -3.5, 4/43 lines)

**5 µM** (26 genes, none with an alert; 12 shown): [[CHID1]] 0.789× (z -4.4, 9/47 lines), [[BROX]] 0.833× (z -4.2, 16/47 lines), [[PHETA1]] 0.647× (z -3.8, 11/33 lines), [[KIF5C]] 0.791× (z -3.6, 13/47 lines), [[TGOLN2]] 0.821× (z -3.6, 21/47 lines), [[MAP3K6]] 0.715× (z -3.6, 10/43 lines), [[EFEMP2]] 0.683× (z -3.5, 10/40 lines), [[TAX1BP3]] 0.772× (z -3.5, 13/45 lines), [[MAMDC4]] 0.654× (z -3.5, 12/42 lines), [[ZNF185]] 0.783× (z -3.4, 10/33 lines), [[GXYLT2]] 0.797× (z -3.2, 8/36 lines), [[INPP5D]] 0.767× (z -3.1, 8/14 lines)

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
| 0.05 µM | — | — |
| 0.5 µM | [[HOP62 (line)]] (-5.6), [[A498 (line)]] (-4.7), [[SNU-423 (line)]] (-4.2), [[Hs 766T (line)]] (-3.9), [[hTERT-HPNE (line)]] (-3.4) | — |
| 5 µM | — | [[BT-474 (line)]] (1.67), [[AsPC-1 (line)]] (1.50), [[A498 (line)]] (1.41), [[HOP62 (line)]] (1.38) · weakest: [[LS 180 (line)]] (0.361), [[NCI-H2347 (line)]] (0.437), [[LoVo (line)]] (0.475) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Adagrasib (drug)]] (+0.50, RAS inhibitor); [[Benztropine (mesylate) (drug)]] (+0.48, unclear); [[Cepharanthine (drug)]] (+0.40, unclear); [[Vitamin K4 (drug)]] (+0.39, unclear); [[Cysteamine (hydrochloride) (drug)]] (+0.39, unclear); [[Lidocaine (hydrochloride) (drug)]] (+0.37, unclear); [[Rimonabant (Hydrochloride) (drug)]] (+0.36, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Osimertinib (mesylate) (drug)]] (+0.34, EGFR/ERBB inhibitor); [[Doxycycline (monohydrate) (drug)]] (+0.34, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 52 arrows, 52 of them with an alert ⚠; grade A 0, B 39, C 13. Shown: the 15 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[FAAH2]] | 5 µM | B | FAAH2 activity raises the cells' numbers under Penfluridol 5 µM (protects the cells) | lines that do not express FAAH2 (26) vs lines expressing it (22) | the lines without FAAH2: 0.83× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Penfluridol 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.68× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[ENSG00000230615]] | 0.5 µM | B | ENSG00000230615 activity lowers the cells' numbers under Penfluridol 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 1.46× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[KCNMA1]] | 0.5 µM | B | KCNMA1 activity lowers the cells' numbers under Penfluridol 0.5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.46× the cells of the other lines | 0.044 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[ENSG00000230647]] | 0.5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Penfluridol 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.38× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[BNC2]] | 5 µM | B | BNC2 activity lowers the cells' numbers under Penfluridol 5 µM (makes them more sensitive) | lines that do not express BNC2 (21) vs lines expressing it (27) | the lines without BNC2: 1.18× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[EPCAM]] | 0.5 µM | B | EPCAM activity raises the cells' numbers under Penfluridol 0.5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.72× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[CKMT1B]] | 0.5 µM | B | CKMT1B activity raises the cells' numbers under Penfluridol 0.5 µM (protects the cells) | lines that do not express CKMT1B (28) vs lines expressing it (20) | the lines without CKMT1B: 0.75× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| [[ENSG00000197813]] | 5 µM | B | ENSG00000197813 activity lowers the cells' numbers under Penfluridol 5 µM (makes them more sensitive) | lines that do not express ENSG00000197813 (11) vs lines expressing it (37) | the lines without ENSG00000197813: 1.18× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC6A16, TEAD2, SLC2A3; maybe low, not absent |
| [[SRPX]] | 0.5 µM | B | SRPX activity lowers the cells' numbers under Penfluridol 0.5 µM (makes them more sensitive) | lines that do not express SRPX (22) vs lines expressing it (26) | the lines without SRPX: 1.34× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[EID2B]] | 5 µM | B | EID2B activity lowers the cells' numbers under Penfluridol 5 µM (makes them more sensitive) | lines that do not express EID2B (13) vs lines expressing it (35) | the lines without EID2B: 1.19× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |
| [[COL12A1]] | 5 µM | B | COL12A1 activity lowers the cells' numbers under Penfluridol 5 µM (makes them more sensitive) | lines that do not express COL12A1 (23) vs lines expressing it (25) | the lines without COL12A1: 1.23× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: RFTN1, FMN2, KIAA0408 |
| [[SRGN]] | 0.5 µM | B | SRGN activity lowers the cells' numbers under Penfluridol 0.5 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.52× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| [[ENSG00000230479]] | 0.5 µM | B | ENSG00000230479 activity lowers the cells' numbers under Penfluridol 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230479 (13) vs lines expressing it (35) | the lines without ENSG00000230479: 1.39× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: CLDN14-AS1, HRH1, ENSG00000289526; maybe low, not absent |
| [[TEAD2]] | 5 µM | B | TEAD2 activity lowers the cells' numbers under Penfluridol 5 µM (makes them more sensitive) | lines that do not express TEAD2 (9) vs lines expressing it (39) | the lines without TEAD2: 1.18× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, SLC6A16, FBXO17 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Penfluridol"
- `tables/drugdoses.parquet` — dd in 785, 786, 787
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

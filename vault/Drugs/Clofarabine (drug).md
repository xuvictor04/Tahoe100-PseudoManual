---
drug: "Clofarabine"
type: "drug"
salt_base: "Clofarabine"
targets: ""
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 8
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Clofarabine

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 8 / 4 / 1; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.22 / -0.04.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:G8 | 4 / 4 | — | -0.20 | +0.5/+0.4/+0.5 | — |
| 0.5 µM | [[Plate 08]]:G8 | 3 / 1 | — | -0.78 | -0.6/-0.9/-1.3 | — |
| 5 µM | [[Plate 09]]:G8 | 1 / 0 | — | -0.52 | +0.1/+0.5/+0.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[EIF2AK1]] 1.33× (z +4.6, 34/48 lines), [[PLD5]] 1.43× (z +3.3, 3/33 lines), [[BMS1P20]] 1.22× (z +3.1, 8/46 lines), [[LINC02208]] 1.40× (z +2.8, 0/31 lines)

**0.5 µM** (3 genes, none with an alert): [[SEPTIN5]] 1.47× (z +3.7, 4/34 lines), [[PRDM11]] 1.30× (z +3.4, 9/46 lines), [[ENSG00000236498]] 1.37× (z +3.3, 6/45 lines)

**5 µM** (1 gene, none with an alert): [[SLC52A3]] 1.45× (z +3.5, 0/21 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[PLBD2]] 0.827× (z -3.4, 15/48 lines), [[PRSS16]] 0.699× (z -3.4, 3/27 lines), [[LDLRAP1]] 0.803× (z -3.1, 10/43 lines), [[NEURL1B]] 0.769× (z -3.0, 4/38 lines)

**0.5 µM** (1 gene, none with an alert): [[GBP4]] 0.742× (z -2.8, 3/27 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Module 043]] (-2.1) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[HOP62 (line)]] (-3.8), [[A549 (line)]] (-3.3) | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 8 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Imiquimod (hydrochloride) (drug)]] (+0.67, unclear, ⚠ vector dose flagged: toxic); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] (+0.67, Glucose transporter inhibitor); [[Talc (drug)]] (+0.62, unclear, ⚠ only 7 significant genes); [[Elagolix sodium (drug)]] (+0.60, unclear); [[Rimonabant (Hydrochloride) (drug)]] (+0.53, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Saquinavir (drug)]] (+0.52, unclear); [[Fostamatinib (disodium hexahydrate) (drug)]] (+0.52, Other TK inhibitor, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Flutamide (drug)]] (+0.51, Androgen receptor antagonist); [[Bendamustine (drug)]] (+0.50, DNA synthesis/repair inhibitor); [[Silodosin (drug)]] (+0.50, unclear); [[Aprepitant (drug)]] (+0.50, unclear); [[Bicalutamide (drug)]] (+0.49, Androgen receptor antagonist)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 86 arrows, 86 of them with an alert ⚠; grade A 0, B 11, C 75. Shown: the 15 strongest; 71 more arrows (71 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.79× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[CKMT1B]] | 0.5 µM | B | CKMT1B activity raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | lines that do not express CKMT1B (28) vs lines expressing it (20) | the lines without CKMT1B: 0.83× the cells of the other lines | 0.070 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| [[KCNMA1]] | 0.5 µM | B | KCNMA1 activity lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.26× the cells of the other lines | 0.070 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[FAAH2]] | 0.5 µM | B | FAAH2 activity raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | lines that do not express FAAH2 (26) vs lines expressing it (22) | the lines without FAAH2: 0.79× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[SRPX]] | 0.5 µM | B | SRPX activity lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | lines that do not express SRPX (22) vs lines expressing it (26) | the lines without SRPX: 1.18× the cells of the other lines | 0.074 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[ENSG00000230615]] | 0.5 µM | B | ENSG00000230615 activity lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 1.26× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[ARHGEF6]] | 0.5 µM | B | ARHGEF6 activity lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | lines that do not express ARHGEF6 (20) vs lines expressing it (28) | the lines without ARHGEF6: 1.22× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[EPCAM]] | 0.5 µM | B | EPCAM activity raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.83× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[DMTN]] | 0.5 µM | B | DMTN activity raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | lines that do not express DMTN (14) vs lines expressing it (34) | the lines without DMTN: 0.83× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: ICA1, BIK, ELF3-AS1; maybe low, not absent |
| [[AOX1]] | 0.5 µM | B | AOX1 activity lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 1.25× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[SRGN]] | 0.5 µM | B | SRGN activity lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.32× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| [[C2orf74]] | 0.5 µM | C | C2orf74 activity lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.24× the cells of the other lines | 0.025 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[FIGN]] | 0.5 µM | C | FIGN activity lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.21× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[NR3C1]] | 0.5 µM | C | NR3C1 activity lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.23× the cells of the other lines | 0.037 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[SPART-AS1]] | 0.5 µM | C | SPART-AS1 activity lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.18× the cells of the other lines | 0.039 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Clofarabine"
- `tables/drugdoses.parquet` — dd in 275, 276, 277
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

---
drug: "Vismodegib"
type: "drug"
salt_base: "Vismodegib"
targets: "SMO, ABCB1, ABCG2"
moa_fine: "Sonic inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 5
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Vismodegib

*Sonic inhibitor (inhibitor/antagonist) · targets: SMO, ABCB1, ABCG2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 5 / 1 / 2; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.14 / -0.03.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:G11 | 4 / 1 | — | -0.60 | -0.5/-1.1/-1.0 | — |
| 0.5 µM | [[Plate 11]]:G11 | 0 / 1 | — | -0.30 | +0.7/+0.6/+0.4 | — |
| 5 µM | [[Plate 12]]:G11 | 1 / 1 | — | -0.44 | -0.5/-0.4/-1.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[ZNF85]] 1.31× (z +3.3, 2/30 lines), [[ENSG00000285837]] 1.44× (z +3.3, 5/20 lines), [[LINC01829]] 1.29× (z +3.0, 2/42 lines), [[CNGA1]] 1.28× (z +2.8, 1/36 lines)

**5 µM** (1 gene, none with an alert): [[PARD6G]] 1.24× (z +3.0, 1/37 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ATXN1-AS1]] 0.682× (z -3.5, 6/35 lines)

**0.5 µM** (1 gene, none with an alert): [[HSD17B14]] 0.799× (z -3.0, 2/43 lines)

**5 µM** (1 gene, none with an alert): [[SLC29A2]] 0.773× (z -3.1, 3/34 lines)

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
| 0.5 µM | — | — |
| 5 µM | [[SNU-423 (line)]] (-3.6), [[A498 (line)]] (-3.5), [[HOP62 (line)]] (-3.4), [[HS-578T (line)]] (-3.2), [[A549 (line)]] (-3.2) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 5 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Ataluren (drug)]] (+0.79, unclear, ⚠ only 7 significant genes); [[Dapagliflozin (drug)]] (+0.75, Glucose transporter inhibitor); [[Benztropine (mesylate) (drug)]] (+0.73, unclear); [[Bestatin (drug)]] (+0.72, unclear, ⚠ only 3 significant genes); [[Lidocaine (hydrochloride) (drug)]] (+0.71, unclear); [[Finasteride (drug)]] (+0.69, unclear); [[Brimonidine (drug)]] (+0.68, Adrenoceptor agonist); [[Valdecoxib (drug)]] (+0.64, Cyclooxygenase inhibitor); [[Vitamin K4 (drug)]] (+0.63, unclear); [[Bisoprolol (hemifumarate) (drug)]] (+0.60, Adrenoceptor agonist)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 18 arrows, 18 of them with an alert ⚠; grade A 0, B 12, C 6. Shown: the 15 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Vismodegib 5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.33× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[MYH14]] | 5 µM | B | MYH14 activity raises the cells' numbers under Vismodegib 5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.73× the cells of the other lines | 0.048 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[KCNMA1]] | 5 µM | B | KCNMA1 activity lowers the cells' numbers under Vismodegib 5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.37× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[NLGN4X]] | 5 µM | B | NLGN4X activity raises the cells' numbers under Vismodegib 5 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.93× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| [[SRGN]] | 5 µM | B | SRGN activity lowers the cells' numbers under Vismodegib 5 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.45× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| [[ENSG00000230615]] | 5 µM | B | ENSG00000230615 activity lowers the cells' numbers under Vismodegib 5 µM (makes them more sensitive) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 1.36× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity lowers the cells' numbers under Vismodegib 5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.40× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[AOX1]] | 5 µM | B | AOX1 activity lowers the cells' numbers under Vismodegib 5 µM (makes them more sensitive) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 1.31× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[SIRLNT]] | 5 µM | B | SIRLNT activity lowers the cells' numbers under Vismodegib 5 µM (makes them more sensitive) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 1.41× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[EPCAM]] | 5 µM | B | EPCAM activity raises the cells' numbers under Vismodegib 5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.77× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[SRPX]] | 5 µM | B | SRPX activity lowers the cells' numbers under Vismodegib 5 µM (makes them more sensitive) | lines that do not express SRPX (22) vs lines expressing it (26) | the lines without SRPX: 1.24× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[CKMT1B]] | 5 µM | B | CKMT1B activity raises the cells' numbers under Vismodegib 5 µM (protects the cells) | lines that do not express CKMT1B (28) vs lines expressing it (20) | the lines without CKMT1B: 0.79× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| [[FIGN]] | 5 µM | C | FIGN activity lowers the cells' numbers under Vismodegib 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.30× the cells of the other lines | 0.011 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[C2orf74]] | 5 µM | C | C2orf74 activity lowers the cells' numbers under Vismodegib 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.31× the cells of the other lines | 0.026 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[SPART-AS1]] | 5 µM | C | SPART-AS1 activity lowers the cells' numbers under Vismodegib 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.25× the cells of the other lines | 0.043 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Vismodegib"
- `tables/drugdoses.parquet` — dd in 1090, 1091, 1092
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

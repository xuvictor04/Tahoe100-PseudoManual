---
drug: "Econazole"
type: "drug"
salt_base: "Econazole"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 124
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Econazole

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 1 / 124; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.04 / 0.32.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:B5 | 0 / 0 | — | +0.18 | +0.4/+0.5/+0.7 | — |
| 0.5 µM | [[Plate 11]]:B5 | 0 / 1 | — | +0.45 | -1.2/-0.5/-1.4 | — |
| 5 µM | [[Plate 12]]:B5 | 77 / 47 | — | +0.02 | +0.3/+0.4/-0.9 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (77 genes, none with an alert; 12 shown): [[FKBP5]] 6.40× (z +28.0, 29/41 lines), [[KLF9]] 2.01× (z +11.7, 32/43 lines), [[CCND3]] 2.26× (z +11.1, 30/47 lines), [[NNMT]] 2.74× (z +9.2, 19/24 lines), [[B3GNT5]] 1.71× (z +8.9, 24/41 lines), [[ABLIM3]] 1.76× (z +8.1, 21/33 lines), [[ADAMTS9]] 1.69× (z +7.6, 19/29 lines), [[TSC22D3]] 2.45× (z +7.5, 23/37 lines), [[PID1]] 1.67× (z +7.2, 17/26 lines), [[SNAI2]] 2.16× (z +7.0, 16/25 lines), [[DNER]] 1.72× (z +7.0, 15/16 lines), [[FGD4]] 1.39× (z +6.8, 18/38 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[ENSG00000291113]] 0.771× (z -3.2, 4/46 lines)

**5 µM** (47 genes, none with an alert; 12 shown): [[PTHLH]] 0.600× (z -5.1, 16/27 lines), [[WNT7B]] 0.680× (z -5.1, 16/28 lines), [[ADAMTS16]] 0.746× (z -4.9, 16/23 lines), [[SYNJ2]] 0.810× (z -4.6, 22/44 lines), [[ENSG00000259354]] 0.676× (z -4.5, 19/30 lines), [[NAV3]] 0.726× (z -4.5, 16/32 lines), [[PKIA]] 0.771× (z -4.5, 14/26 lines), [[HMGN2P46]] 0.645× (z -4.5, 15/30 lines), [[FAM107B]] 0.816× (z -4.3, 17/37 lines), [[TNFRSF9]] 0.648× (z -4.3, 13/27 lines), [[TRAF1]] 0.700× (z -4.1, 17/36 lines), [[LINC00944]] 0.765× (z -4.1, 7/28 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 098]] (+3.8), [[Module 104]] (+2.3), [[Module 097]] (+2.3) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[H4 (line)]] (2.41), [[NCI-H1573 (line)]] (2.37), [[HOP62 (line)]] (2.24), [[Hs 766T (line)]] (1.97) · weakest: [[RKO (line)]] (0.145), [[COLO 205 (line)]] (0.174), [[A-427 (line)]] (0.175) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Phenylephrine (hydrochloride) (drug)]] (+0.90, Adrenoceptor agonist); [[Dexamethasone (drug)]] (+0.86, Glucocorticoid receptor agonist); [[Budesonide (drug)]] (+0.80, Glucocorticoid receptor agonist); [[Citalopram (hydrobromide) (drug)]] (+0.73, unclear); [[Betamethasone dipropionate (drug)]] (+0.66, Glucocorticoid receptor agonist); [[Clobetasol propionate (drug)]] (+0.62, unclear); [[Quinestrol (drug)]] (+0.62, unclear); [[Triamcinolone (drug)]] (+0.58, Glucocorticoid receptor agonist)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[KLRC4-KLRK1]], [[KLRK1]] | 0.5 µM | B | KLRC4-KLRK1, KLRK1 activity raises the cells' numbers under Econazole 0.5 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.83× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[KLRC3]] | 0.5 µM | B | KLRC3 activity raises the cells' numbers under Econazole 0.5 µM (protects the cells) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 0.85× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| [[PICART1]] | 0.5 µM | C | PICART1 activity lowers the cells' numbers under Econazole 0.5 µM (makes them more sensitive) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 1.35× the cells of the other lines | 0.028 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |
| [[RARG]] | 0.5 µM | C | RARG activity lowers the cells' numbers under Econazole 0.5 µM (makes them more sensitive) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 1.35× the cells of the other lines | 0.060 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| [[TMEM117]] | 0.5 µM | C | TMEM117 activity raises the cells' numbers under Econazole 0.5 µM (protects the cells) | lines that do not express TMEM117 (3) vs lines expressing it (45) | the lines without TMEM117: 0.76× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: KLHL9; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Econazole"
- `tables/drugdoses.parquet` — dd in 395, 396, 397
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

---
drug: "Adenosine"
type: "drug"
salt_base: "Adenosine"
targets: "ADORA1, ADORA2A, ADORA2B, ADORA3"
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 9
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Adenosine

*unclear (unclear) · targets: ADORA1, ADORA2A, ADORA2B, ADORA3 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 9 / 6; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.02 / 0.24.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:E2 | 1 / 0 | — | -0.18 | -0.8/-0.4/-0.7 | — |
| 0.5 µM | [[Plate 05]]:E2 | 1 / 8 | — | +0.63 | -0.2/-0.3/-1.7 | — |
| 5 µM | [[Plate 14]]:E2 | 3 / 3 | 0.742 | -0.13 | -0.4/+0.0/-0.9 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENSG00000249174]] 1.63× (z +3.7, 0/8 lines)

**0.5 µM** (1 gene, none with an alert): [[ALKBH8]] 1.20× (z +3.1, 3/48 lines)

**5 µM** (3 genes, none with an alert): [[RBKS]] 1.23× (z +3.9, 9/41 lines), [[LINC01950]] 1.22× (z +3.1, 2/35 lines), [[ENSG00000286163]] 1.20× (z +2.8, 6/26 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (8 genes, none with an alert): [[CHRDL1]] 0.460× (z -5.3, 1/8 lines), [[NID2]] 0.681× (z -4.0, 0/15 lines), [[RXRB]] 0.761× (z -3.9, 9/48 lines), [[ENSG00000287861]] 0.632× (z -3.8, 0/8 lines), [[UCKL1]] 0.771× (z -3.2, 6/48 lines), [[E2F4]] 0.814× (z -3.1, 5/48 lines), [[DNAJB2]] 0.798× (z -3.1, 6/48 lines), [[PKP3]] 0.796× (z -2.9, 2/33 lines)

**5 µM** (3 genes, none with an alert): [[MEIOC]] 0.775× (z -4.0, 10/47 lines), [[ENSG00000289293]] 0.760× (z -3.5, 5/47 lines), [[MSMO1]] 0.832× (z -2.8, 13/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 194]] (+2.0) | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[A-172 (line)]] (-4.1) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 9 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar.*

- [[Bisoprolol (hemifumarate) (drug)]] (+0.83, Adrenoceptor agonist); [[Fenofibrate (drug)]] (+0.69, unclear); [[MK-8353 (drug)]] (+0.68, Other MAPK inhibitor); [[Erlotinib (drug)]] (+0.66, EGFR/ERBB inhibitor); [[Dapagliflozin (drug)]] (+0.65, Glucose transporter inhibitor); [[Loperamide (hydrochloride) (drug)]] (+0.64, unclear); [[Doxycycline (monohydrate) (drug)]] (+0.59, unclear); [[Benproperine (phosphate) (drug)]] (+0.58, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SEMA4G]] | 5 µM | C | SEMA4G activity raises the cells' numbers under Adenosine 5 µM (protects the cells) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 0.85× the cells of the other lines | 0.024 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| [[CHCHD10]] | 5 µM | C | CHCHD10 activity raises the cells' numbers under Adenosine 5 µM (protects the cells) | lines that do not express CHCHD10 (5) vs lines expressing it (43) | the lines without CHCHD10: 0.84× the cells of the other lines | 0.034 | ⚠ tissue-confounded; across organs |
| [[RRM2]] | 5 µM | C | RRM2 activity lowers the cells' numbers under Adenosine 5 µM (makes them more sensitive) | lines that do not express RRM2 (3) vs lines expressing it (45) | the lines without RRM2: 1.21× the cells of the other lines | 0.048 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: CLSPN, E2F8, TCF19; maybe low, not absent |
| [[C2orf74]] | 5 µM | C | C2orf74 activity lowers the cells' numbers under Adenosine 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.11× the cells of the other lines | 0.060 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[SDC3]] | 5 µM | C | SDC3 activity lowers the cells' numbers under Adenosine 5 µM (makes them more sensitive) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 1.19× the cells of the other lines | 0.062 | ⚠ few lines (4 vs 46); across organs |
| [[RARG]] | 5 µM | C | RARG activity lowers the cells' numbers under Adenosine 5 µM (makes them more sensitive) | lines that do not express RARG (3) vs lines expressing it (45) | the lines without RARG: 1.19× the cells of the other lines | 0.073 | ⚠ few lines (3 vs 47); across organs; also absent: ANXA2, SLC25A43, MYO10; maybe low, not absent |
| [[NR3C1]] | 5 µM | C | NR3C1 activity lowers the cells' numbers under Adenosine 5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.11× the cells of the other lines | 0.079 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[ENSG00000288755]] | 5 µM | C | ENSG00000288755 activity raises the cells' numbers under Adenosine 5 µM (protects the cells) | lines that do not express ENSG00000288755 (3) vs lines expressing it (45) | the lines without ENSG00000288755: 0.82× the cells of the other lines | 0.087 | ⚠ few lines (3 vs 47); across organs; also absent: SLC25A45; maybe low, not absent |
| [[FIGN]] | 5 µM | C | FIGN activity lowers the cells' numbers under Adenosine 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.10× the cells of the other lines | 0.099 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Adenosine"
- `tables/drugdoses.parquet` — dd in 60, 61, 62
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

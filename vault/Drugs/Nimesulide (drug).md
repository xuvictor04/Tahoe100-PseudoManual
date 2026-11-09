---
drug: "Nimesulide"
type: "drug"
salt_base: "Nimesulide"
targets: "PTGS2"
moa_fine: "Cyclooxygenase inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 345
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Nimesulide

*Cyclooxygenase inhibitor (inhibitor/antagonist) · targets: PTGS2 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 1 / 345; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.39 / 0.50.
> Flags by dose: unreliable plate only / unreliable plate only / toxic; unreliable plate only. ⚠ 0.05 µM: unreliable plate only; 0.5 µM: unreliable plate only; 5 µM: toxic; unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:B8 | 1 / 0 | — | -0.38 | +1.1/+1.5/+0.5 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 13]]:B7 | 1 / 0 | — | -0.36 | -0.3/+0.3/+0.6 | ⚠ unreliable plate only |
| 5 µM | [[Plate 13]]:B6 | 337 / 8 | — | -1.18 | -0.3/-0.1/+1.7 | ⚠ toxic; unreliable plate only |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, 1 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[LRPAP1]] ⚠ 1.20× (z +2.8, 10/48 lines)

**0.5 µM** (1 gene, 1 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[KCNIP4]] ⚠ 1.23× (z +2.8, 0/41 lines)

**5 µM** (337 genes, 337 with an alert ⚠; the drug-dose carries ⚠ toxic; unreliable plate only; 12 shown): [[SLC14A1]] ⚠ 1.93× (z +4.6, 0/9 lines), [[ESRP2]] ⚠ 1.52× (z +4.6, 1/21 lines), [[ELAPOR1]] ⚠ 1.59× (z +4.6, 1/28 lines), [[VSIG1]] ⚠ 2.05× (z +4.5, 0/11 lines), [[TMEM52B]] ⚠ 2.07× (z +4.5, 1/7 lines), [[WNT7A]] ⚠ 1.91× (z +4.4, 0/9 lines), [[CHRM5]] ⚠ 1.63× (z +4.4, 5/30 lines), [[DPH2]] ⚠ 1.55× (z +4.4, 7/33 lines), [[ENSG00000267881]] ⚠ 2.19× (z +4.4, 3/6 lines), [[LIMD2]] ⚠ 1.68× (z +4.4, 6/27 lines), [[GRHL3]] ⚠ 1.55× (z +4.4, 2/16 lines), [[TSPOAP1]] ⚠ 1.78× (z +4.4, 2/17 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (8 genes, 8 with an alert ⚠; the drug-dose carries ⚠ toxic; unreliable plate only): [[C10orf88]] ⚠ 0.805× (z -4.1, 13/47 lines), [[SALL4]] ⚠ 0.789× (z -3.3, 7/25 lines), [[ENSG00000290931]] ⚠ 0.804× (z -3.3, 11/26 lines), [[LINC00630]] ⚠ 0.800× (z -3.1, 16/46 lines), [[ENSG00000285043]] ⚠ 0.726× (z -3.0, 9/38 lines), [[IFT122]] ⚠ 0.818× (z -2.9, 15/47 lines), [[ENSG00000284634]] ⚠ 0.806× (z -2.8, 12/43 lines), [[MAML2]] ⚠ 0.822× (z -2.6, 10/39 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 171]] (-2.0) |
| 0.5 µM | — | — |
| 5 µM | [[Module 048]] (+2.6), [[Module 002]] (+2.2), [[Module 131]] (+2.0) | [[Module 029]] (-2.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[HEC-1-A (line)]] (-3.3) | — |
| 0.5 µM | — | — |
| 5 µM | [[SW48 (line)]] (-3.1) | [[NCI-H661 (line)]] (2.01), [[CHP-212 (line)]] (1.60), [[AN3 CA (line)]] (1.59), [[SW48 (line)]] (1.50) · weakest: [[NCI-H2347 (line)]] (0.369), [[PANC-1 (line)]] (0.422), [[MIA PaCa-2 (line)]] (0.447) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: no trustworthy dose (vector dose flagged: toxic; unreliable plate only). Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Canagliflozin (hemihydrate) (drug)]] (+0.85, Glucose transporter inhibitor); [[Methylprednisolone succinate (drug)]] (+0.85, Glucocorticoid receptor agonist); [[Ipatasertib (drug)]] (+0.84, PI3K/AKT inhibitor); [[Thymol (drug)]] (+0.84, unclear); [[Celecoxib (drug)]] (+0.83, Cyclooxygenase inhibitor); [[9-ING-41 (drug)]] (+0.81, GSK3 inhibitor); [[LY-2584702 (tosylate salt) (drug)]] (+0.80, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Darolutamide (drug)]] (+0.80, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Hydroxyurea (drug)]] (+0.80, DNA synthesis/repair inhibitor); [[Bimatoprost (drug)]] (+0.79, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[HENMT1]] | 5 µM | B | HENMT1 activity raises the cells' numbers under Nimesulide 5 µM (protects the cells) | lines that do not express HENMT1 (17) vs lines expressing it (31) | the lines without HENMT1: 0.81× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC16A5, RPP25, ENSG00000267748; cell counts less trustworthy |
| [[PINCR]] | 5 µM | B | PINCR activity lowers the cells' numbers under Nimesulide 5 µM (makes them more sensitive) | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR: 1.20× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; cell counts less trustworthy |
| [[ENSG00000234139]] | 5 µM | B | ENSG00000234139 activity raises the cells' numbers under Nimesulide 5 µM (protects the cells) | lines that do not express ENSG00000234139 (9) vs lines expressing it (39) | the lines without ENSG00000234139: 0.82× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000257489, CTSH, GOLGA2P5-1; maybe low, not absent; cell counts less trustworthy |
| [[LINC01357]] | 5 µM | B | LINC01357 activity raises the cells' numbers under Nimesulide 5 µM (protects the cells) | lines that do not express LINC01357 (24) vs lines expressing it (24) | the lines without LINC01357: 0.86× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: PLBD1-AS1, PLBD1, SYN2; cell counts less trustworthy |
| [[PICART1]] | 5 µM | C | PICART1 activity raises the cells' numbers under Nimesulide 5 µM (protects the cells) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 0.75× the cells of the other lines | 0.081 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent; cell counts less trustworthy |
| [[EID1]], [[TMEM17]] | 5 µM | C | EID1, TMEM17 activity raises the cells' numbers under Nimesulide 5 µM (protects the cells) | lines that do not express EID1, TMEM17 (3) vs lines expressing them (45) | the lines without EID1, TMEM17: 0.74× the cells of the other lines | 0.095 | ⚠ few lines (3 vs 47); across organs; also absent: MNS1, ENSG00000283491, AGK; cell counts less trustworthy; co-absent genes |
| [[SIRT5]] | 5 µM | C | SIRT5's natural level raises the cells' numbers under Nimesulide 5 µM (protects the cells) | SIRT5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.323 over the table, 0.074 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[C6orf62]] | 5 µM | C | C6orf62's natural level raises the cells' numbers under Nimesulide 5 µM (protects the cells) | C6orf62's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.333 over the table, 0.074 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Nimesulide"
- `tables/drugdoses.parquet` — dd in 723, 724, 725
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

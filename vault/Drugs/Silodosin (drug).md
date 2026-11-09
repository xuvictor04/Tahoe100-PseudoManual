---
drug: "Silodosin"
type: "drug"
salt_base: "Silodosin"
targets: "ADRA1A, ADRA1B, ADRA1D"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 83
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Silodosin

*unclear (inhibitor/antagonist) · targets: ADRA1A, ADRA1B, ADRA1D · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 0 / 83; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.33 / -0.29.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:D12 | 0 / 0 | — | -0.10 | +0.1/+0.4/-0.3 | — |
| 0.5 µM | [[Plate 08]]:D12 | 0 / 0 | — | -0.34 | -0.1/-0.1/-0.9 | — |
| 5 µM | [[Plate 09]]:D12 | 49 / 34 | — | -0.64 | +1.5/+1.2/+1.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (49 genes, none with an alert; 12 shown): [[GSG1L]] 1.45× (z +3.8, 3/28 lines), [[SULT2B1]] 1.45× (z +3.7, 3/18 lines), [[PAX7]] 1.77× (z +3.4, 0/6 lines), [[TREM1]] 1.69× (z +3.4, 1/14 lines), [[SLC5A1]] 1.52× (z +3.3, 0/11 lines), [[ITGA4]] 1.38× (z +3.3, 1/14 lines), [[ENSG00000263603]] 1.42× (z +3.3, 0/25 lines), [[ST8SIA6-AS1]] 1.50× (z +3.3, 0/8 lines), [[ENSG00000231317]] 1.74× (z +3.3, 1/10 lines), [[PREX2]] 1.55× (z +3.3, 0/4 lines), [[LINC01610]] 1.97× (z +3.3, 0/2 lines), [[ENSG00000291138]] 1.61× (z +3.3, 3/13 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (34 genes, none with an alert; 12 shown): [[INPP5E]] 0.680× (z -5.0, 14/41 lines), [[ZCWPW2]] 0.755× (z -4.0, 10/47 lines), [[SRRD]] 0.753× (z -4.0, 10/43 lines), [[RCBTB2]] 0.661× (z -4.0, 11/40 lines), [[HEMK1]] 0.720× (z -3.9, 17/44 lines), [[PRKAB1]] 0.766× (z -3.9, 14/43 lines), [[SNAI3-AS1]] 0.690× (z -3.6, 14/39 lines), [[PPP3CB-AS1]] 0.691× (z -3.6, 12/42 lines), [[NCDN]] 0.730× (z -3.6, 9/43 lines), [[ENSG00000273507]] 0.697× (z -3.6, 7/34 lines), [[ZSCAN32]] 0.812× (z -3.6, 10/45 lines), [[THAP6]] 0.823× (z -3.5, 11/46 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 045]] (+2.2) | [[Module 137]] (-2.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[SW 1271 (line)]] (1.68), [[C-33 A (line)]] (1.50), [[CHP-212 (line)]] (1.50), [[SNU-1 (line)]] (1.39) · weakest: [[H4 (line)]] (0.381), [[LOX-IMVI (line)]] (0.424), [[MIA PaCa-2 (line)]] (0.476) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Arbutin (drug)]] (+0.81, unclear); [[Altretamine (drug)]] (+0.80, DNA synthesis/repair inhibitor, ⚠ only 1 significant gene); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.74, unclear); [[Bendamustine (drug)]] (+0.74, DNA synthesis/repair inhibitor); [[Tetracycline (hydrochloride) (drug)]] (+0.64, unclear, ⚠ only 6 significant genes); [[Plicamycin (drug)]] (+0.63, unclear, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Tranilast (drug)]] (+0.63, unclear, ⚠ only 6 significant genes); [[Fluvoxamine (maleate) (drug)]] (+0.63, unclear); [[Bicalutamide (drug)]] (+0.61, Androgen receptor antagonist); [[Azithromycin (hydrate) (drug)]] (+0.61, unclear); [[Minodronic acid (drug)]] (+0.60, unclear); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] (+0.59, Glucose transporter inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[KLRC3]] | 0.5 µM | B | KLRC3 activity raises the cells' numbers under Silodosin 0.5 µM (protects the cells) | lines that do not express KLRC3 (27) vs lines expressing it (21) | the lines without KLRC3: 0.88× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: KLRK1, KLRC2, IGFL4 |
| [[KLRC4-KLRK1]], [[KLRK1]] | 0.5 µM | B | KLRC4-KLRK1, KLRK1 activity raises the cells' numbers under Silodosin 0.5 µM (protects the cells) | lines that do not express KLRC4-KLRK1, KLRK1 (29) vs lines expressing them (19) | the lines without KLRC4-KLRK1, KLRK1: 0.86× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: KLRC3, KLRC2, PIP5K1B; co-absent genes |
| [[PWWP2B]] | 0.5 µM | C | PWWP2B activity raises the cells' numbers under Silodosin 0.5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.72× the cells of the other lines | 0.042 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| [[FIGN]] | 0.5 µM | C | FIGN activity lowers the cells' numbers under Silodosin 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.16× the cells of the other lines | 0.056 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[NR3C1]] | 0.5 µM | C | NR3C1 activity lowers the cells' numbers under Silodosin 0.5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.19× the cells of the other lines | 0.082 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[C2orf74]] | 0.5 µM | C | C2orf74 activity lowers the cells' numbers under Silodosin 0.5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.17× the cells of the other lines | 0.082 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Silodosin"
- `tables/drugdoses.parquet` — dd in 946, 947, 948
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

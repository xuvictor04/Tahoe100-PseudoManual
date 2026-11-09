---
drug: "LY-2584702 (tosylate salt)"
type: "drug"
salt_base: "LY-2584702"
targets: "RPS6KB1"
moa_fine: "MTOR inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1089
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# LY-2584702 (tosylate salt)

*MTOR inhibitor (inhibitor/antagonist) · targets: RPS6KB1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 20 / 1089; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.23 / 0.57.
> Flags by dose: - / low cells (technical?); plate-row cell shift; noisy plate (z scaled) / toxic; noisy plate (z scaled). ⚠ 5 µM: toxic (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:E5 | 0 / 3 | — | -0.45 | -0.6/-0.0/-0.5 | — |
| 0.5 µM | [[Plate 02]]:E5 | 19 / 1 | — | -1.42 | +0.6/+0.4/+1.5 | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:E5 | 966 / 123 | — | -1.70 | +0.4/+0.8/+1.7 | ⚠ toxic · noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (19 genes, none with an alert; 12 shown): [[TMEM9B]] 1.33× (z +3.5, 8/45 lines), [[NUBP1]] 1.31× (z +3.4, 5/45 lines), [[SAMM50]] 1.20× (z +3.4, 5/46 lines), [[FUCA1]] 1.39× (z +3.2, 6/43 lines), [[SLC39A3]] 1.71× (z +3.2, 0/30 lines), [[SPAG17]] 1.47× (z +3.1, 2/23 lines), [[PALMD]] 1.86× (z +3.1, 0/13 lines), [[POLR3F]] 1.23× (z +3.1, 6/47 lines), [[ZNF280B]] 1.36× (z +3.1, 1/31 lines), [[ENSG00000286133]] 1.64× (z +3.0, 0/16 lines), [[VPS26B]] 1.23× (z +3.0, 2/48 lines), [[LMF2]] 1.36× (z +3.0, 4/43 lines)

**5 µM** (966 genes, 966 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[WFS1]] ⚠ 1.88× (z +4.8, 10/22 lines), [[FUT3]] ⚠ 2.29× (z +4.8, 0/7 lines), [[TRAPPC2]] ⚠ 1.52× (z +4.7, 11/31 lines), [[PLCD3]] ⚠ 1.63× (z +4.7, 11/29 lines), [[MIIP]] ⚠ 2.17× (z +4.6, 7/16 lines), [[FBLN2]] ⚠ 2.73× (z +4.6, 2/3 lines), [[MDFI]] ⚠ 2.77× (z +4.6, 2/13 lines), [[TROAP]] ⚠ 1.81× (z +4.6, 7/27 lines), [[WT1]] ⚠ 2.35× (z +4.5, 0/8 lines), [[ENSG00000272688]] ⚠ 2.54× (z +4.5, 0/4 lines), [[ANKRD20A11P]] ⚠ 2.61× (z +4.5, 0/5 lines), [[ZSCAN18]] ⚠ 2.01× (z +4.5, 10/15 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[SLC51A]] 0.667× (z -4.1, 5/38 lines), [[FAHD2A]] 0.805× (z -3.5, 5/47 lines), [[ZFY]] 0.778× (z -3.2, 2/19 lines)

**0.5 µM** (1 gene, none with an alert): [[WDTC1]] 0.824× (z -3.0, 8/48 lines)

**5 µM** (123 genes, 123 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[GNPDA2]] ⚠ 0.625× (z -5.1, 12/29 lines), [[TUT4]] ⚠ 0.740× (z -4.8, 26/44 lines), [[NBPF15]] ⚠ 0.588× (z -4.7, 25/42 lines), [[TLK1]] ⚠ 0.751× (z -4.4, 29/45 lines), [[NIPBL]] ⚠ 0.795× (z -4.3, 26/45 lines), [[JAK1]] ⚠ 0.748× (z -4.2, 20/45 lines), [[PHF3]] ⚠ 0.736× (z -4.1, 30/45 lines), [[OSBPL11]] ⚠ 0.732× (z -4.1, 12/38 lines), [[DICER1]] ⚠ 0.810× (z -4.0, 20/45 lines), [[ZFR]] ⚠ 0.759× (z -4.0, 25/45 lines), [[FAM81A]] ⚠ 0.658× (z -4.0, 11/35 lines), [[SINHCAF]] ⚠ 0.757× (z -3.9, 13/43 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 002]] (+3.1), [[Module 177]] (+2.5), [[Module 157]] (+2.5) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[SW 1271 (line)]] (1.61), [[HCT15 (line)]] (1.61), [[SNU-1 (line)]] (1.50), [[SW 1088 (line)]] (1.47) · weakest: [[C32 (line)]] (0.181), [[HEC-1-A (line)]] (0.250), [[CFPAC-1 (line)]] (0.270) |
| 5 µM | [[NCI-H460 (line)]] (-4.9), [[C32 (line)]] (-4.6), [[RPMI-7951 (line)]] (-4.0), [[A549 (line)]] (-3.8), [[SW480 (line)]] (-3.5) | [[AN3 CA (line)]] (1.64), [[SNU-1 (line)]] (1.52), [[H4 (line)]] (1.42), [[HepG2_C3A (line)]] (1.32) · weakest: [[HEC-1-A (line)]] (0.406), [[NCI-H1573 (line)]] (0.437), [[NCI-H2347 (line)]] (0.448) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: toxic. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[9-ING-41 (drug)]] (+0.83, GSK3 inhibitor); [[XRK3F2 (drug)]] (+0.82, unclear); [[Thymol (drug)]] (+0.81, unclear); [[Nimesulide (drug)]] (+0.80, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Canagliflozin (drug)]] (+0.79, Glucose transporter inhibitor); [[Ipatasertib (drug)]] (+0.75, PI3K/AKT inhibitor); [[Oxaprozin (drug)]] (+0.74, Cyclooxygenase inhibitor); [[Pyridoxine (drug)]] (+0.74, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.73, Glucose transporter inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 14 arrows, 14 of them with an alert ⚠; grade A 0, B 4, C 10.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[TREM1]] | 5 µM | B | TREM1 activity lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | lines that do not express TREM1 (25) vs lines expressing it (23) | the lines without TREM1: 1.30× the cells of the other lines | 0.035 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[DNAJC12]] | 5 µM | B | DNAJC12 activity lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | lines that do not express DNAJC12 (25) vs lines expressing it (23) | the lines without DNAJC12: 1.40× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TSHZ2, ENSG00000232053, PROX1 |
| [[SOX6]] | 5 µM | B | SOX6 activity lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | lines that do not express SOX6 (22) vs lines expressing it (26) | the lines without SOX6: 1.36× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[HS3ST3B1]] | 5 µM | B | HS3ST3B1 activity lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | lines that do not express HS3ST3B1 (18) vs lines expressing it (30) | the lines without HS3ST3B1: 1.28× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[RRM2]] | 0.05 µM | C | RRM2 activity lowers the cells' numbers under LY-2584702 (tosylate salt) 0.05 µM (makes them more sensitive) | lines that do not express RRM2 (3) vs lines expressing it (45) | the lines without RRM2: 1.28× the cells of the other lines | 0.091 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: CLSPN, E2F8, TCF19; maybe low, not absent |
| [[DNMT3B]] | 0.05 µM | C | DNMT3B activity lowers the cells' numbers under LY-2584702 (tosylate salt) 0.05 µM (makes them more sensitive) | lines that do not express DNMT3B (4) vs lines expressing it (44) | the lines without DNMT3B: 1.23× the cells of the other lines | 0.0995 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[UBOX5]] | 5 µM | C | UBOX5's natural level lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | UBOX5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.268 over the table, 0.015 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[UBOX5-AS1]] | 5 µM | C | UBOX5-AS1's natural level lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | UBOX5-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.268 over the table, 0.015 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ENSG00000236986]] | 5 µM | C | ENSG00000236986's natural level lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | ENSG00000236986's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.268 over the table, 0.015 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[PRAF2]] | 5 µM | C | PRAF2's natural level lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | PRAF2's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.352 over the table, 0.048 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[STK35]] | 5 µM | C | STK35's natural level lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | STK35's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.360 over the table, 0.048 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[C9orf78]] | 5 µM | C | C9orf78's natural level lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | C9orf78's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.390 over the table, 0.071 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[FASTKD5]] | 5 µM | C | FASTKD5's natural level lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | FASTKD5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.406 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[VPS16]] | 5 µM | C | VPS16's natural level lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | VPS16's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.417 over the table, 0.095 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "LY-2584702 (tosylate salt)"
- `tables/drugdoses.parquet` — dd in 594, 595, 596
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

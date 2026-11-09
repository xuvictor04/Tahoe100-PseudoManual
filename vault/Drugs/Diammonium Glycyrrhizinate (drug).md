---
drug: "Diammonium Glycyrrhizinate"
type: "drug"
salt_base: "Diammonium Glycyrrhizinate"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 137
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Diammonium Glycyrrhizinate

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 137 / 36 / 8; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.09 / 0.31.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:B10 | 67 / 70 | — | +0.04 | +3.9/+3.0/+1.7 | — |
| 0.5 µM | [[Plate 05]]:B10 | 11 / 25 | — | +0.00 | +0.0/+0.6/+0.4 | — |
| 5 µM | [[Plate 14]]:B10 | 0 / 8 | 0.611 | +0.25 | +0.7/+1.7/+0.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (67 genes, none with an alert; 12 shown): [[DIAPH3]] 1.22× (z +4.2, 21/45 lines), [[CENPK]] 1.26× (z +4.0, 13/46 lines), [[SMC4]] 1.23× (z +3.9, 26/47 lines), [[CIP2A]] 1.29× (z +3.9, 23/47 lines), [[MIR924HG]] 1.36× (z +3.8, 18/40 lines), [[ZGRF1]] 1.20× (z +3.7, 12/48 lines), [[ATAD5]] 1.23× (z +3.7, 16/48 lines), [[MIR4435-2HG]] 1.24× (z +3.6, 20/45 lines), [[ZNF804A]] 1.35× (z +3.6, 4/17 lines), [[FAM111B]] 1.52× (z +3.6, 10/38 lines), [[NCAPH]] 1.26× (z +3.6, 13/47 lines), [[CEP78]] 1.21× (z +3.6, 13/47 lines)

**0.5 µM** (11 genes, none with an alert): [[ARRDC3]] 1.44× (z +4.4, 36/48 lines), [[TRABD2A]] 1.34× (z +4.3, 12/47 lines), [[SDHA]] 1.24× (z +4.0, 22/48 lines), [[SF3B4]] 1.58× (z +3.9, 22/46 lines), [[P4HA3]] 1.38× (z +3.9, 10/44 lines), [[BAG6]] 1.25× (z +3.6, 22/48 lines), [[GRPEL1]] 1.29× (z +3.3, 21/48 lines), [[MT-CO2]] 1.33× (z +3.2, 25/48 lines), [[FASN]] 1.38× (z +3.2, 17/47 lines), [[RPL3]] 1.32× (z +3.2, 35/48 lines), [[TFCP2L1]] 1.23× (z +3.0, 3/26 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (70 genes, none with an alert; 12 shown): [[YPEL2]] 0.773× (z -4.4, 13/45 lines), [[HYPK]] 0.640× (z -4.3, 19/46 lines), [[ADCY10]] 0.633× (z -4.0, 19/45 lines), [[LNX2]] 0.788× (z -4.0, 21/48 lines), [[PIK3IP1]] 0.688× (z -3.9, 11/39 lines), [[C9orf153]] 0.758× (z -3.8, 17/47 lines), [[RNF144B]] 0.773× (z -3.8, 8/33 lines), [[HDAC5]] 0.790× (z -3.8, 16/48 lines), [[BCOR]] 0.826× (z -3.7, 19/48 lines), [[SMO]] 0.748× (z -3.7, 5/29 lines), [[CLEC4A]] 0.672× (z -3.7, 17/46 lines), [[BCL2L11]] 0.759× (z -3.6, 19/48 lines)

**0.5 µM** (25 genes, none with an alert; 12 shown): [[ACOT9]] 0.810× (z -5.1, 17/48 lines), [[CASTOR3P]] 0.739× (z -4.3, 16/48 lines), [[ENSG00000289346]] 0.734× (z -4.2, 25/48 lines), [[MYADM-AS1]] 0.654× (z -4.0, 9/29 lines), [[ENSG00000285589]] 0.692× (z -3.8, 10/42 lines), [[ERICH6-AS1]] 0.718× (z -3.7, 6/37 lines), [[ZNF583]] 0.781× (z -3.7, 10/32 lines), [[ENSG00000285889]] 0.742× (z -3.6, 5/42 lines), [[IPCEF1]] 0.723× (z -3.6, 7/35 lines), [[LINC00393]] 0.707× (z -3.4, 6/35 lines), [[ENSG00000258964]] 0.701× (z -3.4, 11/43 lines), [[TPTE2]] 0.779× (z -3.4, 3/45 lines)

**5 µM** (8 genes, none with an alert): [[ASB6]] 0.799× (z -3.7, 12/47 lines), [[ENSG00000291159]] 0.806× (z -3.7, 4/47 lines), [[MKLN1-AS]] 0.804× (z -3.7, 6/47 lines), [[ENSG00000132832]] 0.749× (z -3.4, 3/32 lines), [[CRAT]] 0.831× (z -3.4, 11/46 lines), [[LZTS3]] 0.809× (z -3.4, 10/48 lines), [[SLC6A9]] 0.778× (z -3.3, 10/45 lines), [[UBE2Q2P13]] 0.823× (z -2.8, 3/24 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 004]] (+2.0) | [[Module 179]] (-2.8), [[Module 207]] (-2.7), [[Module 171]] (-2.4) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1088 (line)]] (1.40), [[HOP62 (line)]] (1.37), [[MIA PaCa-2 (line)]] (1.32), [[A498 (line)]] (1.27) · weakest: [[BT-474 (line)]] (0.472), [[NCI-H1792 (line)]] (0.616), [[NCI-H2347 (line)]] (0.652) |
| 0.5 µM | — | [[hTERT-HPNE (line)]] (1.44), [[SHP-77 (line)]] (1.43), [[NCI-H1573 (line)]] (1.32), [[SNU-423 (line)]] (1.30) · weakest: [[KATO III (line)]] (0.483), [[BT-474 (line)]] (0.582), [[NCI-H23 (line)]] (0.632) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Berbamine (drug)]] (+0.87, unclear); [[Gallic acid (hydrate) (drug)]] (+0.87, Cyclooxygenase inhibitor); [[Megestrol (drug)]] (+0.83, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Busulfan (drug)]] (+0.82, DNA synthesis/repair inhibitor); [[Palmatine (chloride) (drug)]] (+0.82, unclear); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.78, unclear); [[Retinoic acid (drug)]] (+0.78, Retinoic receptor agonist); [[Larotrectinib (drug)]] (+0.74, Other TK inhibitor); [[Brimonidine (drug)]] (+0.68, Adrenoceptor agonist)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 29 arrows, 29 of them with an alert ⚠; grade A 0, B 25, C 4. Shown: the 15 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MPZL3]] | 0.5 µM | B | MPZL3 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express MPZL3 (25) vs lines expressing it (23) | the lines without MPZL3: 0.86× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[STON2]] | 0.5 µM | B | STON2 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express STON2 (19) vs lines expressing it (29) | the lines without STON2: 0.91× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[LYPD3]] | 0.5 µM | B | LYPD3 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express LYPD3 (15) vs lines expressing it (33) | the lines without LYPD3: 0.86× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[ANK3]] | 0.5 µM | B | ANK3 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express ANK3 (23) vs lines expressing it (25) | the lines without ANK3: 0.86× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[ADGRF1]] | 0.5 µM | B | ADGRF1 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express ADGRF1 (35) vs lines expressing it (13) | the lines without ADGRF1: 0.85× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[ENSG00000243004]] | 0.5 µM | B | ENSG00000243004 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express ENSG00000243004 (31) vs lines expressing it (17) | the lines without ENSG00000243004: 0.85× the cells of the other lines | 0.070 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MACC1, TMEM125, GRHL2 |
| [[ADCY4]] | 0.5 µM | B | ADCY4 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express ADCY4 (33) vs lines expressing it (15) | the lines without ADCY4: 0.86× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[IL1R2]] | 0.5 µM | B | IL1R2 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express IL1R2 (23) vs lines expressing it (25) | the lines without IL1R2: 0.87× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[MYO5B]] | 0.5 µM | B | MYO5B activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express MYO5B (26) vs lines expressing it (22) | the lines without MYO5B: 0.87× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: CRB3, KDF1, MARVELD3 |
| [[NFATC4]] | 0.5 µM | B | NFATC4 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express NFATC4 (17) vs lines expressing it (31) | the lines without NFATC4: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ANK3, ENSG00000227486, PKHD1 |
| [[RGS4]] | 0.5 µM | B | RGS4 activity lowers the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (makes them more sensitive) | lines that do not express RGS4 (35) vs lines expressing it (13) | the lines without RGS4: 1.14× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486 |
| [[CATSPERB]] | 0.5 µM | B | CATSPERB activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express CATSPERB (30) vs lines expressing it (18) | the lines without CATSPERB: 0.86× the cells of the other lines | 0.085 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[MAL2]] | 0.5 µM | B | MAL2 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express MAL2 (31) vs lines expressing it (17) | the lines without MAL2: 0.86× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[ARHGEF38]] | 0.5 µM | B | ARHGEF38 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express ARHGEF38 (36) vs lines expressing it (12) | the lines without ARHGEF38: 0.85× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[RCN3]] | 0.5 µM | B | RCN3 activity raises the cells' numbers under Diammonium Glycyrrhizinate 0.5 µM (protects the cells) | lines that do not express RCN3 (11) vs lines expressing it (37) | the lines without RCN3: 0.87× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Diammonium Glycyrrhizinate"
- `tables/drugdoses.parquet` — dd in 350, 351, 352
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

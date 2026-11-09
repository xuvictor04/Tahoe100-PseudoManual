---
drug: "Pimitespib"
type: "drug"
salt_base: "Pimitespib"
targets: "HSP90AA1, HSP90AB1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 26
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Pimitespib

*unclear (inhibitor/antagonist) · targets: HSP90AA1, HSP90AB1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 26 / 5 / 18; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.59 / 0.48.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:G1 | 7 / 19 | — | -0.24 | +1.3/+1.4/+1.8 | — |
| 0.5 µM | [[Plate 02]]:G1 | 5 / 0 | — | -0.00 | +0.7/+1.5/+1.4 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:G1 | 11 / 7 | — | -0.85 | +0.4/+0.4/+0.9 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (7 genes, none with an alert): [[GALNT5]] 1.35× (z +3.9, 6/21 lines), [[PDK3]] 1.40× (z +3.8, 35/46 lines), [[CYP1B1]] 1.77× (z +3.7, 17/19 lines), [[ARL6]] 1.29× (z +3.6, 13/46 lines), [[ALDH1A3]] 1.33× (z +3.5, 6/28 lines), [[PFKFB4]] 1.32× (z +3.4, 24/48 lines), [[H4C3]] 1.71× (z +3.1, 28/48 lines)

**0.5 µM** (5 genes, none with an alert): [[HSPA1B]] 2.13× (z +4.8, 34/48 lines), [[HSPA1A]] 2.86× (z +4.1, 24/35 lines), [[DNAJA4]] 1.40× (z +3.4, 3/25 lines), [[BAG3]] 1.27× (z +3.0, 14/49 lines), [[HSPH1]] 1.44× (z +2.7, 16/49 lines)

**5 µM** (11 genes, none with an alert): [[ANKZF1]] 1.51× (z +3.6, 13/47 lines), [[RFESD]] 1.77× (z +3.6, 0/9 lines), [[RAP1GAP]] 1.59× (z +3.5, 2/35 lines), [[B4GALT3]] 1.65× (z +3.4, 5/37 lines), [[ADAM8]] 2.16× (z +3.3, 5/14 lines), [[FKBP10]] 1.41× (z +3.3, 17/38 lines), [[ULK3]] 1.61× (z +3.2, 3/29 lines), [[LINC02575]] 2.17× (z +3.2, 4/12 lines), [[RNF122]] 1.68× (z +3.1, 3/33 lines), [[QSOX1]] 1.33× (z +3.1, 13/47 lines), [[TMEM184B]] 1.29× (z +2.9, 7/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (19 genes, none with an alert; 12 shown): [[MLIP]] 0.719× (z -4.4, 6/37 lines), [[FSTL3]] 0.626× (z -4.1, 19/40 lines), [[PIGV]] 0.731× (z -3.8, 14/44 lines), [[LINC00663]] 0.684× (z -3.6, 6/42 lines), [[DDR2]] 0.806× (z -3.6, 7/39 lines), [[SLC2A9]] 0.674× (z -3.6, 9/39 lines), [[ENSG00000205236]] 0.754× (z -3.6, 7/45 lines), [[STEAP3]] 0.721× (z -3.5, 16/41 lines), [[ENSG00000289728]] 0.684× (z -3.5, 12/43 lines), [[ABAT]] 0.814× (z -3.5, 11/46 lines), [[TMEM201]] 0.765× (z -3.4, 5/44 lines), [[ENSG00000250519]] 0.732× (z -3.4, 9/46 lines)

**5 µM** (7 genes, none with an alert): [[XRRA1]] 0.788× (z -3.5, 10/48 lines), [[RAPGEF1]] 0.784× (z -3.3, 9/48 lines), [[KPNA3]] 0.802× (z -3.2, 11/48 lines), [[ZMYM1]] 0.744× (z -3.1, 12/46 lines), [[ENSG00000233757]] 0.620× (z -3.0, 4/24 lines), [[MAP3K1]] 0.782× (z -2.9, 10/47 lines), [[N4BP2]] 0.783× (z -2.9, 7/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 137]] (-2.1), [[Module 194]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[A498 (line)]] (1.60), [[SW 900 (line)]] (1.30), [[HT-29 (line)]] (1.25), [[A-427 (line)]] (1.25) · weakest: [[SNU-1 (line)]] (0.315), [[HepG2_C3A (line)]] (0.531), [[Panc 03.27 (line)]] (0.555) |
| 0.5 µM | — | — |
| 5 µM | [[C32 (line)]] (-3.7), [[NCI-H1573 (line)]] (-3.3), [[hTERT-HPNE (line)]] (-3.0) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Dimethyl fumarate (drug)]] (+0.71, unclear); [[CP21R7 (drug)]] (+0.66, GSK3 inhibitor, ⚠ only 1 significant gene); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] (+0.62, unclear); [[Fumaric acid (drug)]] (+0.62, unclear); [[Voriconazole (drug)]] (+0.59, unclear, ⚠ only 6 significant genes); [[Fluvoxamine (maleate) (drug)]] (+0.59, unclear); [[Sacubitril_Valsartan (drug)]] (+0.58, unclear, ⚠ only 1 significant gene); [[Minodronic acid (drug)]] (+0.57, unclear); [[Allopurinol (drug)]] (+0.54, unclear); [[Tazarotene (drug)]] (+0.52, Retinoic receptor agonist); [[Brivudine (drug)]] (+0.49, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[CEMIP]] | 5 µM | B | CEMIP activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express CEMIP (19) vs lines expressing it (29) | the lines without CEMIP: 1.26× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[LGALS3BP]] | 5 µM | B | LGALS3BP activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 1.35× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[ATP1B1]] | 5 µM | B | ATP1B1 activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 1.35× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[AKR1C3]] | 5 µM | B | AKR1C3 activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express AKR1C3 (19) vs lines expressing it (29) | the lines without AKR1C3: 1.24× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3 |
| [[ARHGAP30]] | 5 µM | B | ARHGAP30 activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express ARHGAP30 (22) vs lines expressing it (26) | the lines without ARHGAP30: 1.29× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[PAX2]] | 5 µM | B | PAX2 activity raises the cells' numbers under Pimitespib 5 µM (protects the cells) | lines that do not express PAX2 (33) vs lines expressing it (15) | the lines without PAX2: 0.79× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[IKZF3]] | 5 µM | B | IKZF3 activity raises the cells' numbers under Pimitespib 5 µM (protects the cells) | lines that do not express IKZF3 (31) vs lines expressing it (17) | the lines without IKZF3: 0.82× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| [[TREM1]] | 5 µM | B | TREM1 activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express TREM1 (25) vs lines expressing it (23) | the lines without TREM1: 1.17× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[MGST2]] | 5 µM | B | MGST2 activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express MGST2 (10) vs lines expressing it (38) | the lines without MGST2: 1.29× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| [[PROX1]] | 5 µM | B | PROX1 activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express PROX1 (30) vs lines expressing it (18) | the lines without PROX1: 1.31× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH17, CLRN3, LINC02964 |
| [[SDCBP2]] | 5 µM | B | SDCBP2 activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express SDCBP2 (17) vs lines expressing it (31) | the lines without SDCBP2: 1.24× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[ENSG00000253227]] | 5 µM | B | ENSG00000253227 activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express ENSG00000253227 (18) vs lines expressing it (30) | the lines without ENSG00000253227: 1.14× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: COL16A1, SERPINE2, SLCO2B1; maybe low, not absent |
| [[DUSP10]] | 5 µM | B | DUSP10 activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express DUSP10 (11) vs lines expressing it (37) | the lines without DUSP10: 1.23× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[SH3TC1]] | 5 µM | B | SH3TC1 activity lowers the cells' numbers under Pimitespib 5 µM (makes them more sensitive) | lines that do not express SH3TC1 (10) vs lines expressing it (38) | the lines without SH3TC1: 1.27× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[SLC29A4]] | 5 µM | B | SLC29A4 activity raises the cells' numbers under Pimitespib 5 µM (protects the cells) | lines that do not express SLC29A4 (6) vs lines expressing it (42) | the lines without SLC29A4: 0.72× the cells of the other lines | 0.097 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Pimitespib"
- `tables/drugdoses.parquet` — dd in 812, 813, 814
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

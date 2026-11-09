---
drug: "venetoclax"
type: "drug"
salt_base: "venetoclax"
targets: "BCL2"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1797
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# venetoclax

*unclear (inhibitor/antagonist) · targets: BCL2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 154 / 40 / 1797; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.02 / 0.11.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:B4 | 101 / 53 | — | +0.21 | +2.1/+1.5/+0.4 | — |
| 0.5 µM | [[Plate 02]]:B4 | 19 / 21 | — | +0.44 | +0.6/-0.6/-0.8 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:B4 | 790 / 1,007 | — | -0.31 | +1.3/-1.0/+1.6 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (101 genes, none with an alert; 12 shown): [[HERC5]] 1.63× (z +5.9, 23/33 lines), [[IFIT2]] 2.03× (z +5.5, 28/41 lines), [[PNPT1]] 1.41× (z +5.0, 28/48 lines), [[APOL6]] 1.35× (z +5.0, 20/42 lines), [[ZC3HAV1]] 1.30× (z +5.0, 27/49 lines), [[TRIM22]] 1.66× (z +4.9, 20/30 lines), [[USP18]] 1.71× (z +4.9, 25/44 lines), [[CFB]] 1.79× (z +4.7, 17/28 lines), [[RIGI]] 1.55× (z +4.7, 35/46 lines), [[OASL]] 1.75× (z +4.7, 32/39 lines), [[IFIT1]] 1.92× (z +4.6, 32/45 lines), [[OAS2]] 1.84× (z +4.4, 27/34 lines)

**0.5 µM** (19 genes, none with an alert; 12 shown): [[LRPPRC]] 1.32× (z +3.4, 26/49 lines), [[NSUN2]] 1.35× (z +3.2, 20/49 lines), [[UBE2G2]] 1.24× (z +3.2, 7/49 lines), [[NAA15]] 1.27× (z +3.1, 13/49 lines), [[IARS1]] 1.31× (z +3.0, 16/49 lines), [[E2F6]] 1.28× (z +2.9, 0/48 lines), [[CDC14A]] 1.24× (z +2.9, 1/49 lines), [[EZH2]] 1.31× (z +2.8, 11/49 lines), [[TULP4]] 1.20× (z +2.8, 5/49 lines), [[RABGGTB]] 1.34× (z +2.8, 6/48 lines), [[PTDSS1]] 1.26× (z +2.8, 1/48 lines), [[PPM1H]] 1.25× (z +2.8, 1/37 lines)

**5 µM** (790 genes, none with an alert; 12 shown): [[ZNRF3]] 2.34× (z +8.7, 35/45 lines), [[FRMD5]] 2.30× (z +8.1, 29/38 lines), [[KIF21A]] 1.93× (z +8.0, 39/46 lines), [[YARS1]] 2.08× (z +7.7, 44/48 lines), [[ENAH]] 1.69× (z +7.3, 33/45 lines), [[FRAS1]] 1.88× (z +7.1, 12/26 lines), [[SLC2A8]] 2.80× (z +7.0, 10/25 lines), [[RCAN1]] 2.03× (z +6.8, 27/45 lines), [[MARS1]] 2.15× (z +6.8, 41/48 lines), [[AXIN2]] 3.03× (z +6.8, 2/14 lines), [[PINX1]] 2.02× (z +6.7, 16/43 lines), [[CREB5]] 1.98× (z +6.3, 18/33 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (53 genes, none with an alert; 12 shown): [[EGR1]] 0.525× (z -4.7, 31/47 lines), [[ELK3]] 0.702× (z -4.6, 22/45 lines), [[CDCP1]] 0.746× (z -4.6, 22/33 lines), [[FERMT1]] 0.686× (z -4.3, 16/26 lines), [[ANTXR2]] 0.702× (z -4.2, 27/39 lines), [[PLEKHM1]] 0.787× (z -4.1, 16/49 lines), [[CORO2B]] 0.659× (z -4.1, 13/33 lines), [[ITGB5]] 0.784× (z -4.0, 24/47 lines), [[SNX9]] 0.817× (z -3.9, 27/49 lines), [[ERCC1]] 0.779× (z -3.9, 18/48 lines), [[RASA2]] 0.808× (z -3.8, 23/49 lines), [[ARID3B]] 0.762× (z -3.7, 22/49 lines)

**0.5 µM** (21 genes, none with an alert; 12 shown): [[UBALD2]] 0.579× (z -4.1, 22/48 lines), [[KMT2B]] 0.729× (z -3.7, 17/49 lines), [[SRRM2]] 0.769× (z -3.7, 42/49 lines), [[MT-CO1]] 0.679× (z -3.2, 41/49 lines), [[KLF3]] 0.799× (z -3.2, 6/49 lines), [[CRAT]] 0.713× (z -3.1, 4/46 lines), [[KIFC3]] 0.800× (z -3.1, 4/46 lines), [[PANX2]] 0.647× (z -3.1, 2/37 lines), [[ING4]] 0.797× (z -3.0, 4/48 lines), [[MMP14]] 0.736× (z -3.0, 7/30 lines), [[KLHDC3]] 0.807× (z -3.0, 0/48 lines), [[MXD4]] 0.695× (z -3.0, 4/48 lines)

**5 µM** (1007 genes, none with an alert; 12 shown): [[TFDP2]] 0.397× (z -14.9, 47/48 lines), [[PDCD4]] 0.289× (z -14.2, 46/48 lines), [[KLHL24]] 0.176× (z -14.0, 47/48 lines), [[FBXL20]] 0.253× (z -13.9, 48/48 lines), [[CCDC28A]] 0.218× (z -13.8, 44/47 lines), [[RB1CC1]] 0.342× (z -13.7, 47/48 lines), [[FBXO25]] 0.309× (z -13.5, 39/42 lines), [[WIPI2]] 0.349× (z -12.1, 45/48 lines), [[SERINC3]] 0.411× (z -12.0, 44/48 lines), [[CREBRF]] 0.230× (z -12.0, 48/48 lines), [[PLEKHM3]] 0.313× (z -11.8, 43/47 lines), [[MARF1]] 0.345× (z -11.5, 45/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 032]] (+2.7) | — |
| 0.5 µM | — | [[Module 048]] (-2.1) |
| 5 µM | [[Module 018]] (+3.2), [[Module 033]] (+3.0), [[Module 133]] (+2.8) | [[Module 069]] (-5.5), [[Module 234]] (-5.3), [[Module 187]] (-5.3) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[AsPC-1 (line)]] (1.44), [[HOP62 (line)]] (1.32), [[LoVo (line)]] (1.32), [[RKO (line)]] (1.31) · weakest: [[SNU-1 (line)]] (0.336), [[HEC-1-A (line)]] (0.484), [[H4 (line)]] (0.550) |
| 0.5 µM | [[NCI-H661 (line)]] (-3.6), [[LOX-IMVI (line)]] (-3.2) | [[LS 180 (line)]] (1.20), [[NCI-H661 (line)]] (1.17), [[HEC-1-A (line)]] (1.15), [[PANC-1 (line)]] (1.12) · weakest: [[SK-MEL-2 (line)]] (0.668), [[J82 (line)]] (0.750), [[HCT15 (line)]] (0.829) |
| 5 µM | [[RKO (line)]] (-6.3), [[Hs 766T (line)]] (-6.2), [[RPMI-7951 (line)]] (-5.9), [[CFPAC-1 (line)]] (-5.5), [[A-427 (line)]] (-5.5) | [[NCI-H1792 (line)]] (1.39), [[AsPC-1 (line)]] (1.37), [[MIA PaCa-2 (line)]] (1.36), [[NCI-H460 (line)]] (1.29) · weakest: [[A-427 (line)]] (0.640), [[NCI-H661 (line)]] (0.704), [[LS 180 (line)]] (0.707) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[TAK-733 (drug)]] (+0.87, MEK inhibitor); [[c-Kit-IN-1 (drug)]] (+0.84, Multi-TK inhibitor); [[EX229 (drug)]] (+0.82, unclear); [[Abemaciclib (drug)]] (+0.76, CDK inhibitor); [[Sapanisertib (drug)]] (+0.68, MTOR inhibitor); [[Everolimus (drug)]] (+0.46, MTOR inhibitor); [[Belzutifan (drug)]] (+0.43, unclear); [[Volasertib (drug)]] (+0.42, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SLC2A9]] | 0.5 µM | B | SLC2A9 activity raises the cells' numbers under venetoclax 0.5 µM (protects the cells) | lines that do not express SLC2A9 (6) vs lines expressing it (42) | the lines without SLC2A9: 0.77× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[AHR]] | 0.5 µM | B | AHR activity raises the cells' numbers under venetoclax 0.5 µM (protects the cells) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 0.87× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[PRRG1]] | 0.5 µM | C | PRRG1 activity raises the cells' numbers under venetoclax 0.5 µM (protects the cells) | lines that do not express PRRG1 (3) vs lines expressing it (45) | the lines without PRRG1: 0.71× the cells of the other lines | 0.038 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "venetoclax"
- `tables/drugdoses.parquet` — dd in 1123, 1124, 1125
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

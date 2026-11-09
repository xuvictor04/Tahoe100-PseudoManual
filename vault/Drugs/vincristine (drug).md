---
drug: "vincristine"
type: "drug"
salt_base: "vincristine"
targets: ""
moa_fine: "Microtubule inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 1207
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# vincristine

*Microtubule inhibitor (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 75 / 1207 / 567; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.38 / 0.87.
> Flags by dose: - / low cells (technical?); noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:G12 | 25 / 50 | — | -0.17 | +0.2/+2.1/+1.0 | — |
| 0.5 µM | [[Plate 02]]:G12 | 692 / 515 | — | -1.45 | +0.1/+2.1/+2.7 | low cells (technical?); noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:G12 | 283 / 284 | — | -0.63 | -0.1/+1.9/+1.7 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (25 genes, none with an alert; 12 shown): [[CREB5]] 1.47× (z +6.4, 19/33 lines), [[TNFAIP1]] 1.31× (z +4.8, 21/48 lines), [[ARHGAP29]] 1.24× (z +4.5, 20/38 lines), [[DIAPH3]] 1.23× (z +4.1, 21/45 lines), [[CTNNAL1]] 1.27× (z +4.0, 24/47 lines), [[CCNB1]] 1.40× (z +3.9, 21/47 lines), [[KNSTRN]] 1.28× (z +3.7, 13/48 lines), [[CAPN2]] 1.21× (z +3.6, 17/48 lines), [[CEP55]] 1.31× (z +3.5, 14/46 lines), [[AK4]] 1.21× (z +3.5, 15/47 lines), [[KIF14]] 1.23× (z +3.4, 16/47 lines), [[HEG1]] 1.24× (z +3.3, 12/37 lines)

**0.5 µM** (692 genes, 1 with an alert ⚠; 12 shown): [[CREB5]] 2.45× (z +9.5, 22/33 lines), [[MGLL]] 1.57× (z +7.5, 24/34 lines), [[ENSG00000285845]] 2.82× (z +7.4, 12/16 lines), [[ARHGAP29]] 1.55× (z +6.9, 27/38 lines), [[ANKRD1]] 4.18× (z +6.7, 17/17 lines), [[SCEL]] 2.55× (z +6.4, 7/13 lines), [[RPL18A]] 2.93× (z +6.4, 40/45 lines), [[ENSG00000225339]] 2.10× (z +6.3, 27/44 lines), [[CAPN2]] 1.44× (z +6.3, 30/48 lines), [[RANGAP1]] 1.50× (z +5.8, 25/48 lines), [[AKAP12]] 2.09× (z +5.8, 26/30 lines), [[ACTG1]] 2.17× (z +5.8, 48/48 lines)

**5 µM** (283 genes, 2 with an alert ⚠; 13 shown): [[CREB5]] 2.90× (z +9.7, 27/31 lines), [[MGLL]] 1.72× (z +6.6, 22/32 lines), [[ENSG00000225339]] 2.62× (z +6.0, 20/40 lines), [[PVR]] 1.92× (z +5.7, 25/45 lines), [[ARHGAP29]] 1.62× (z +5.6, 25/36 lines), [[MARCHF4]] 2.35× (z +5.5, 12/18 lines), [[CLDN1]] 1.72× (z +5.2, 12/24 lines), [[ANKRD1]] 4.20× (z +5.2, 13/16 lines), [[RANGAP1]] 1.63× (z +5.1, 21/45 lines), [[LINC00707]] 2.20× (z +5.1, 10/20 lines), [[NF2]] 1.50× (z +5.0, 21/45 lines), [[SLC7A1]] ⚠ 1.46× (z +4.9, 22/45 lines; position correction uncertain), [[LIMK1]] 1.64× (z +4.8, 15/41 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (50 genes, none with an alert; 12 shown): [[TUBB]] 0.605× (z -6.2, 37/47 lines), [[CCDC40]] 0.598× (z -5.3, 25/46 lines), [[ZNF487]] 0.649× (z -5.2, 20/47 lines), [[TC2N]] 0.764× (z -4.5, 2/20 lines), [[PIP5K1B]] 0.710× (z -4.5, 3/15 lines), [[VEGFA]] 0.735× (z -4.3, 34/46 lines), [[SNTB1]] 0.761× (z -4.0, 16/29 lines), [[SEMA3D]] 0.714× (z -4.0, 5/17 lines), [[TGFB3]] 0.671× (z -3.9, 10/42 lines), [[TMEM67]] 0.764× (z -3.8, 24/46 lines), [[HSD17B14]] 0.738× (z -3.8, 5/44 lines), [[TRIM2]] 0.831× (z -3.8, 10/33 lines)

**0.5 µM** (515 genes, none with an alert; 12 shown): [[TNRC6B]] 0.794× (z -7.0, 32/48 lines), [[MEF2C]] 0.566× (z -6.7, 21/34 lines), [[PLEKHH2]] 0.641× (z -6.3, 18/32 lines), [[HERC5]] 0.498× (z -6.2, 20/33 lines), [[FRRS1]] 0.577× (z -5.6, 26/43 lines), [[SUFU]] 0.754× (z -5.6, 21/48 lines), [[PHF21A]] 0.685× (z -5.5, 38/48 lines), [[MAP3K1]] 0.710× (z -5.5, 23/48 lines), [[PIK3C2B]] 0.630× (z -5.5, 19/41 lines), [[CCDC40]] 0.498× (z -5.5, 22/44 lines), [[PMS2P4-1]] 0.699× (z -5.4, 29/48 lines), [[DTWD2]] 0.597× (z -5.4, 22/45 lines)

**5 µM** (284 genes, none with an alert; 12 shown): [[TRIM2]] 0.588× (z -6.0, 22/32 lines), [[MEF2C]] 0.502× (z -5.9, 19/32 lines), [[HERC5]] 0.423× (z -5.7, 24/30 lines), [[PHF3]] 0.677× (z -5.2, 38/46 lines), [[TENT5A]] 0.571× (z -5.1, 26/35 lines), [[PHF21A]] 0.620× (z -5.1, 41/46 lines), [[SETDB2]] 0.610× (z -4.9, 17/43 lines), [[SLC44A1]] 0.721× (z -4.8, 23/41 lines), [[ATP7A]] 0.503× (z -4.8, 25/43 lines), [[LRIG3]] 0.491× (z -4.8, 14/32 lines), [[PIK3C2B]] 0.581× (z -4.7, 14/39 lines), [[LNX1]] 0.613× (z -4.7, 9/21 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 205]] (-2.7) |
| 0.5 µM | [[Module 002]] (+3.6), [[Module 184]] (+3.4), [[Module 060]] (+2.5) | [[Module 205]] (-2.7), [[Module 225]] (-2.3), [[Module 231]] (-2.2) |
| 5 µM | [[Module 002]] (+3.1), [[Module 184]] (+2.9), [[Module 060]] (+2.2) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[PANC-1 (line)]] (-3.7), [[RKO (line)]] (-3.7) | [[MIA PaCa-2 (line)]] (1.74), [[HT-29 (line)]] (1.57), [[AN3 CA (line)]] (1.55), [[SW 900 (line)]] (1.45) · weakest: [[SHP-77 (line)]] (0.352), [[A498 (line)]] (0.533), [[A549 (line)]] (0.659) |
| 0.5 µM | — | [[HT-29 (line)]] (1.28), [[SW 900 (line)]] (1.23), [[SW 1088 (line)]] (1.19), [[MIA PaCa-2 (line)]] (1.19) · weakest: [[SHP-77 (line)]] (0.618), [[J82 (line)]] (0.635), [[HepG2_C3A (line)]] (0.686) |
| 5 µM | [[hTERT-HPNE (line)]] (-6.3), [[RPMI-7951 (line)]] (-5.5), [[C32 (line)]] (-5.3), [[RKO (line)]] (-5.3), [[NCI-H460 (line)]] (-4.7) | [[H4 (line)]] (1.44), [[NCI-H1573 (line)]] (1.38), [[SW 900 (line)]] (1.30), [[HT-29 (line)]] (1.29) · weakest: [[J82 (line)]] (0.604), [[SW1417 (line)]] (0.677), [[HEC-1-A (line)]] (0.700) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Peretinoin (drug)]] (+0.73, Retinoic receptor agonist); [[Vinblastine (sulfate) (drug)]] (+0.68, Microtubule inhibitor); [[Daptomycin (drug)]] (+0.68, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[9-ING-41 (drug)]] (+0.55, GSK3 inhibitor); [[Tubulin inhibitor 6 (drug)]] (+0.54, Microtubule inhibitor, ⚠ only 2 significant genes); [[AZD1390 (drug)]] (+0.53, unclear); [[Celecoxib (drug)]] (+0.52, Cyclooxygenase inhibitor); [[LY-2584702 (tosylate salt) (drug)]] (+0.52, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Naproxen (drug)]] (+0.50, Cyclooxygenase inhibitor); [[Thymol (drug)]] (+0.50, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.50, Glucose transporter inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 42 arrows, 42 of them with an alert ⚠; grade A 0, B 32, C 10. Shown: the 15 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[LGALS3BP]] | 0.05 µM | B | LGALS3BP activity raises the cells' numbers under vincristine 0.05 µM (protects the cells) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 0.76× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity lowers the cells' numbers under vincristine 5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.27× the cells of the other lines | 0.062 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[ARHGAP30]] | 0.05 µM | B | ARHGAP30 activity raises the cells' numbers under vincristine 0.05 µM (protects the cells) | lines that do not express ARHGAP30 (22) vs lines expressing it (26) | the lines without ARHGAP30: 0.86× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[ENSG00000287292]] | 0.05 µM | B | ENSG00000287292 activity raises the cells' numbers under vincristine 0.05 µM (protects the cells) | lines that do not express ENSG00000287292 (13) vs lines expressing it (35) | the lines without ENSG00000287292: 0.83× the cells of the other lines | 0.067 | ⚠ within organs, on part of the lines; also absent: NR3C2, ENSG00000249631, SATB1; maybe low, not absent |
| [[ENSG00000256915]] | 0.5 µM | B | ENSG00000256915 activity lowers the cells' numbers under vincristine 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000256915 (12) vs lines expressing it (36) | the lines without ENSG00000256915: 1.12× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: LDB2, ITGA7, F2R; maybe low, not absent |
| [[LINC02306]] | 5 µM | B | LINC02306 activity lowers the cells' numbers under vincristine 5 µM (makes them more sensitive) | lines that do not express LINC02306 (13) vs lines expressing it (35) | the lines without LINC02306: 1.45× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: KCNMB2, COP1-DT, LINC02398; maybe low, not absent |
| [[DUSP10]] | 0.05 µM | B | DUSP10 activity raises the cells' numbers under vincristine 0.05 µM (protects the cells) | lines that do not express DUSP10 (11) vs lines expressing it (37) | the lines without DUSP10: 0.81× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity lowers the cells' numbers under vincristine 5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.27× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[RASGEF1B]] | 0.05 µM | B | RASGEF1B activity raises the cells' numbers under vincristine 0.05 µM (protects the cells) | lines that do not express RASGEF1B (10) vs lines expressing it (38) | the lines without RASGEF1B: 0.82× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[FGD4]] | 5 µM | B | FGD4 activity raises the cells' numbers under vincristine 5 µM (protects the cells) | lines that do not express FGD4 (10) vs lines expressing it (38) | the lines without FGD4: 0.63× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[TGFA]] | 0.05 µM | B | TGFA activity raises the cells' numbers under vincristine 0.05 µM (protects the cells) | lines that do not express TGFA (17) vs lines expressing it (31) | the lines without TGFA: 0.85× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[ENSG00000290574]] | 0.5 µM | B | ENSG00000290574 activity lowers the cells' numbers under vincristine 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000290574 (13) vs lines expressing it (35) | the lines without ENSG00000290574: 1.21× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: HLA-H, HLA-F, ENSG00000230479; maybe low, not absent |
| [[PYROXD2]] | 0.05 µM | B | PYROXD2 activity raises the cells' numbers under vincristine 0.05 µM (protects the cells) | lines that do not express PYROXD2 (7) vs lines expressing it (41) | the lines without PYROXD2: 0.77× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| [[AHR]] | 0.05 µM | B | AHR activity raises the cells' numbers under vincristine 0.05 µM (protects the cells) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 0.84× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[ENSG00000283573]] | 0.05 µM | B | ENSG00000283573 activity raises the cells' numbers under vincristine 0.05 µM (protects the cells) | lines that do not express ENSG00000283573 (7) vs lines expressing it (41) | the lines without ENSG00000283573: 0.78× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000287100, ENSG00000287292, TENT5A; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "vincristine"
- `tables/drugdoses.parquet` — dd in 1126, 1127, 1128
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

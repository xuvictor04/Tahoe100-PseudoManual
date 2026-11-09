---
drug: "Vinblastine (sulfate)"
type: "drug"
salt_base: "Vinblastine"
targets: ""
moa_fine: "Microtubule inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 1754
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Vinblastine (sulfate)

*Microtubule inhibitor (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 178 / 1701 / 1754; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.54 / 0.86.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:A7 | 82 / 96 | — | +0.32 | +1.7/+2.9/+2.4 | — |
| 0.5 µM | [[Plate 05]]:A7 | 726 / 975 | — | -0.88 | -1.8/+0.6/+2.5 | — |
| 5 µM | [[Plate 14]]:A7 | 625 / 1,129 | 0.951 | -0.23 | -3.6/-0.1/+3.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (82 genes, none with an alert; 12 shown): [[CENPA]] 1.26× (z +5.3, 14/48 lines), [[CCNB1]] 1.53× (z +5.3, 30/47 lines), [[RANGAP1]] 1.27× (z +4.7, 21/48 lines), [[CREB5]] 1.31× (z +4.7, 16/34 lines), [[TACC3]] 1.30× (z +4.6, 20/48 lines), [[CEP55]] 1.33× (z +4.4, 25/46 lines), [[SPDL1]] 1.43× (z +4.2, 21/45 lines), [[AURKA]] 1.36× (z +4.2, 25/48 lines), [[CDC20]] 1.55× (z +4.2, 21/45 lines), [[ARHGAP11A]] 1.28× (z +4.1, 18/47 lines), [[DIAPH3]] 1.21× (z +4.1, 20/46 lines), [[CDCA8]] 1.34× (z +4.0, 19/47 lines)

**0.5 µM** (726 genes, none with an alert; 12 shown): [[CREB5]] 2.62× (z +16.8, 31/33 lines), [[ARHGAP29]] 1.60× (z +10.3, 30/38 lines), [[MGLL]] 1.55× (z +10.2, 25/34 lines), [[SAMD4A]] 1.86× (z +9.7, 40/46 lines), [[CAPN2]] 1.47× (z +9.4, 35/48 lines), [[MYO5B]] 1.59× (z +9.2, 16/22 lines), [[PVR]] 1.50× (z +8.5, 38/47 lines), [[NF2]] 1.42× (z +8.3, 32/47 lines), [[DTNA]] 1.80× (z +8.2, 20/26 lines), [[ENSG00000285845]] 2.27× (z +8.0, 13/16 lines), [[DAAM1]] 1.35× (z +7.9, 28/47 lines), [[PGM5P2-1]] 1.76× (z +7.9, 16/31 lines)

**5 µM** (625 genes, 1 with an alert ⚠; 12 shown): [[CREB5]] 2.75× (z +25.0, 32/34 lines), [[ARHGAP29]] 1.58× (z +14.2, 35/39 lines), [[DTNA]] 1.95× (z +13.2, 24/27 lines), [[SAMD4A]] 1.76× (z +12.5, 39/47 lines), [[MGLL]] 1.44× (z +12.0, 25/35 lines), [[CLIP1]] 1.29× (z +11.6, 32/49 lines), [[MYO5B]] 1.50× (z +11.4, 17/23 lines), [[CLDN1]] 1.51× (z +10.6, 16/26 lines), [[KRTAP5-AS1]] 2.10× (z +10.3, 26/32 lines), [[CAPN2]] 1.34× (z +10.1, 32/49 lines), [[PVR]] 1.40× (z +10.0, 36/48 lines), [[CCDC50]] 1.32× (z +10.0, 32/49 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (96 genes, none with an alert; 12 shown): [[TUBB]] 0.650× (z -5.6, 37/48 lines), [[MAP3K5]] 0.762× (z -5.3, 25/46 lines), [[ZCCHC2]] 0.795× (z -4.8, 20/49 lines), [[CCDC40]] 0.657× (z -4.6, 25/47 lines), [[PLEKHH2]] 0.803× (z -4.4, 12/34 lines), [[ZNF487]] 0.725× (z -4.1, 14/48 lines), [[DIXDC1]] 0.818× (z -4.0, 10/48 lines), [[CDC42EP4]] 0.821× (z -4.0, 11/47 lines), [[TC2N]] 0.803× (z -3.9, 10/21 lines), [[CGNL1]] 0.764× (z -3.9, 9/27 lines), [[SOX13]] 0.789× (z -3.9, 13/44 lines), [[CDH26]] 0.655× (z -3.8, 11/41 lines)

**0.5 µM** (975 genes, none with an alert; 12 shown): [[HERC5]] 0.456× (z -9.9, 25/33 lines), [[ETV1]] 0.478× (z -9.2, 31/37 lines), [[MLLT3]] 0.644× (z -8.1, 27/42 lines), [[TRIM9]] 0.579× (z -8.1, 26/31 lines), [[PDE4D]] 0.607× (z -7.7, 26/35 lines), [[NFIA]] 0.671× (z -7.6, 34/37 lines), [[ADD3]] 0.700× (z -7.5, 33/43 lines), [[MEF2C]] 0.635× (z -7.5, 23/33 lines), [[TRIM2]] 0.710× (z -7.5, 21/33 lines), [[ITPR1]] 0.667× (z -7.4, 26/33 lines), [[TRERF1]] 0.666× (z -7.4, 33/42 lines), [[ACACB]] 0.567× (z -7.4, 32/46 lines)

**5 µM** (1129 genes, none with an alert; 12 shown): [[HERC5]] 0.513× (z -11.8, 30/33 lines), [[ETV1]] 0.515× (z -11.7, 32/37 lines), [[NFIA]] 0.684× (z -10.3, 34/38 lines), [[TRERF1]] 0.671× (z -10.3, 40/43 lines), [[MEF2C]] 0.666× (z -9.5, 23/34 lines), [[PLA2G4A]] 0.683× (z -9.5, 20/27 lines), [[ADD3]] 0.729× (z -9.4, 34/44 lines), [[SORL1]] 0.663× (z -9.3, 22/28 lines), [[LINC00511]] 0.655× (z -9.0, 33/37 lines), [[SLC44A1]] 0.798× (z -9.0, 25/44 lines), [[ZC3HAV1]] 0.729× (z -8.9, 36/49 lines), [[ATP7A]] 0.626× (z -8.8, 44/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 205]] (-2.1) |
| 0.5 µM | [[Module 002]] (+3.6), [[Module 184]] (+3.2), [[Module 135]] (+2.8) | [[Module 205]] (-3.3), [[Module 032]] (-3.1), [[Module 200]] (-3.0) |
| 5 µM | [[Module 184]] (+4.0), [[Module 116]] (+3.6), [[Module 002]] (+3.1) | [[Module 032]] (-4.1), [[Module 223]] (-4.1), [[Module 205]] (-3.9) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[RKO (line)]] (-5.0) | [[HT-29 (line)]] (1.74), [[SW 900 (line)]] (1.46), [[HOP62 (line)]] (1.44), [[NCI-H1573 (line)]] (1.44) · weakest: [[A-427 (line)]] (0.412), [[CHP-212 (line)]] (0.473), [[SHP-77 (line)]] (0.536) |
| 0.5 µM | [[RKO (line)]] (-3.8) | [[CFPAC-1 (line)]] (1.73), [[NCI-H1573 (line)]] (1.58), [[HT-29 (line)]] (1.42), [[MIA PaCa-2 (line)]] (1.41) · weakest: [[J82 (line)]] (0.566), [[HEC-1-A (line)]] (0.623), [[SW1417 (line)]] (0.688) |
| 5 µM | [[RKO (line)]] (-4.4), [[H4 (line)]] (-3.4) | [[CFPAC-1 (line)]] (1.73), [[NCI-H1573 (line)]] (1.54), [[H4 (line)]] (1.48), [[MIA PaCa-2 (line)]] (1.48) · weakest: [[NCI-H2122 (line)]] (0.332), [[HEC-1-A (line)]] (0.600), [[J82 (line)]] (0.674) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Daptomycin (drug)]] (+0.84, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Peretinoin (drug)]] (+0.81, Retinoic receptor agonist); [[vincristine (drug)]] (+0.68, Microtubule inhibitor); [[Neratinib (drug)]] (+0.63, EGFR/ERBB inhibitor); [[Neratinib (maleate) (drug)]] (+0.52, EGFR/ERBB inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Pasireotide (acetate) (drug)]] (+0.46, unclear); [[Mebendazole (drug)]] (+0.44, Microtubule inhibitor); [[5-Azacytidine (drug)]] (+0.44, DNA methyltransferase inhibitor); [[AZD1390 (drug)]] (+0.44, unclear); [[ULK-101 (drug)]] (+0.41, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 135 arrows, 135 of them with an alert ⚠; grade A 0, B 125, C 10. Shown: the 15 strongest; 120 more arrows (120 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MSRB3]] | 0.5 µM | B | MSRB3 activity lowers the cells' numbers under Vinblastine (sulfate) 0.5 µM (makes them more sensitive) | lines that do not express MSRB3 (20) vs lines expressing it (28) | the lines without MSRB3: 1.29× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[ITGB4]] | 0.5 µM | B | ITGB4 activity raises the cells' numbers under Vinblastine (sulfate) 0.5 µM (protects the cells) | lines that do not express ITGB4 (25) vs lines expressing it (23) | the lines without ITGB4: 0.78× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[ITGB4]] | 5 µM | B | ITGB4 activity raises the cells' numbers under Vinblastine (sulfate) 5 µM (protects the cells) | lines that do not express ITGB4 (25) vs lines expressing it (23) | the lines without ITGB4: 0.82× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[SCNN1A]] | 5 µM | B | SCNN1A activity raises the cells' numbers under Vinblastine (sulfate) 5 µM (protects the cells) | lines that do not express SCNN1A (27) vs lines expressing it (21) | the lines without SCNN1A: 0.82× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[MSRB3]] | 5 µM | B | MSRB3 activity lowers the cells' numbers under Vinblastine (sulfate) 5 µM (makes them more sensitive) | lines that do not express MSRB3 (20) vs lines expressing it (28) | the lines without MSRB3: 1.21× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1 |
| [[CLDN4]] | 5 µM | B | CLDN4 activity raises the cells' numbers under Vinblastine (sulfate) 5 µM (protects the cells) | lines that do not express CLDN4 (26) vs lines expressing it (22) | the lines without CLDN4: 0.83× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity lowers the cells' numbers under Vinblastine (sulfate) 5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.18× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[MYH14]] | 0.05 µM | B | MYH14 activity raises the cells' numbers under Vinblastine (sulfate) 0.05 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.86× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[SCNN1A]] | 0.5 µM | B | SCNN1A activity raises the cells' numbers under Vinblastine (sulfate) 0.5 µM (protects the cells) | lines that do not express SCNN1A (27) vs lines expressing it (21) | the lines without SCNN1A: 0.78× the cells of the other lines | 0.027 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[ERBB3]] | 5 µM | B | ERBB3 activity raises the cells' numbers under Vinblastine (sulfate) 5 µM (protects the cells) | lines that do not express ERBB3 (27) vs lines expressing it (21) | the lines without ERBB3: 0.84× the cells of the other lines | 0.030 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[GJB3]] | 0.5 µM | B | GJB3 activity raises the cells' numbers under Vinblastine (sulfate) 0.5 µM (protects the cells) | lines that do not express GJB3 (31) vs lines expressing it (17) | the lines without GJB3: 0.76× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[S100A14]] | 5 µM | B | S100A14 activity raises the cells' numbers under Vinblastine (sulfate) 5 µM (protects the cells) | lines that do not express S100A14 (33) vs lines expressing it (15) | the lines without S100A14: 0.82× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[LAD1]] | 5 µM | B | LAD1 activity raises the cells' numbers under Vinblastine (sulfate) 5 µM (protects the cells) | lines that do not express LAD1 (30) vs lines expressing it (18) | the lines without LAD1: 0.84× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity lowers the cells' numbers under Vinblastine (sulfate) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.11× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[BNC2]] | 0.05 µM | B | BNC2 activity lowers the cells' numbers under Vinblastine (sulfate) 0.05 µM (makes them more sensitive) | lines that do not express BNC2 (21) vs lines expressing it (27) | the lines without BNC2: 1.16× the cells of the other lines | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Vinblastine (sulfate)"
- `tables/drugdoses.parquet` — dd in 1087, 1088, 1089
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

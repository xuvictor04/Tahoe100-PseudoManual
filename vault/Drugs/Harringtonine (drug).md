---
drug: "Harringtonine"
type: "drug"
salt_base: "Harringtonine"
targets: ""
moa_fine: "Protein synthesis inhibitor"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 9773
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Harringtonine

*Protein synthesis inhibitor (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1431 / 7179 / 9773; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.62 / 0.82.
> Flags by dose: low cells (technical?) / cell-cycle shift / cell-cycle shift; composition shift. ⚠ 0.5 µM: cell-cycle shift; 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:C11 | 837 / 594 | — | -1.02 | +1.4/+1.2/+1.2 | low cells (technical?) |
| 0.5 µM | [[Plate 08]]:C11 | 3,260 / 3,919 | — | +0.45 | +2.4/+4.1/+6.5 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 09]]:C11 | 4,849 / 4,924 | — | +0.91 | +4.7/+10.7/+6.1 | ⚠ cell-cycle shift · composition shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (837 genes, none with an alert; 12 shown): [[BIRC3]] 1.84× (z +9.7, 40/42 lines), [[CCAR1]] 1.54× (z +8.8, 43/47 lines), [[OBI1]] 1.51× (z +8.6, 32/47 lines), [[COA7]] 2.09× (z +8.3, 24/44 lines), [[GPATCH4]] 2.67× (z +8.2, 42/46 lines), [[ZNF770]] 1.67× (z +8.1, 36/47 lines), [[ZC3H6]] 1.48× (z +8.1, 38/47 lines), [[CPSF2]] 1.48× (z +7.9, 34/47 lines), [[SNW1]] 1.48× (z +7.9, 36/47 lines), [[RSF1]] 1.25× (z +7.6, 29/47 lines), [[UBE2V2]] 1.46× (z +7.5, 37/47 lines), [[EMG1]] 1.57× (z +7.2, 30/45 lines)

**0.5 µM** (3260 genes, 542 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[BIRC3]] 5.21× (z +28.1, 43/43 lines; cell-cycle shift (explains ~7% here)), [[KLF10]] 5.30× (z +25.2, 48/48 lines; cell-cycle shift (explains ~9% here)), [[CDKN2AIP]] 3.90× (z +23.0, 46/47 lines; cell-cycle shift (explains ~6% here)), [[CBLL1]] 2.56× (z +22.4, 48/48 lines; cell-cycle shift (explains ~1% here)), [[MED1]] 2.18× (z +20.6, 45/48 lines; cell-cycle shift (explains ~8% here)), [[CREB5]] 3.12× (z +19.9, 29/33 lines; cell-cycle shift (explains ~4% here)), [[ARL14EP]] 2.58× (z +19.4, 45/48 lines; cell-cycle shift (explains ~2% here)), [[BAZ1A]] 2.03× (z +18.9, 45/48 lines; cell-cycle shift (explains ~6% here)), [[SRFBP1]] 2.15× (z +18.7, 46/48 lines; cell-cycle shift (explains ~3% here)), [[ENSG00000228793]] 5.44× (z +18.6, 36/43 lines; cell-cycle shift (explains ~0% here)), [[ARRDC4]] 3.30× (z +18.6, 39/40 lines; cell-cycle shift (explains ~6% here)), [[TNFAIP3]] 5.28× (z +18.3, 42/45 lines; cell-cycle shift (explains ~7% here))

**5 µM** (4849 genes, 1,313 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[KLF10]] 19.3× (z +43.0, 48/48 lines; cell-cycle shift (explains ~14% here)), [[REL]] 6.77× (z +40.0, 48/48 lines; cell-cycle shift (explains ~8% here)), [[BAZ1A]] 4.71× (z +39.4, 48/48 lines; cell-cycle shift (explains ~6% here)), [[BIRC3]] 9.79× (z +37.4, 43/43 lines; cell-cycle shift (explains ~13% here)), [[CREB5]] 7.94× (z +34.9, 32/33 lines; cell-cycle shift (explains ~6% here)), [[SLC12A7]] 8.32× (z +33.6, 38/42 lines; cell-cycle shift (explains ~0% here)), [[ARL13B]] 4.36× (z +33.6, 48/48 lines; cell-cycle shift (explains ~7% here)), [[ARRDC4]] 9.43× (z +33.5, 40/40 lines; cell-cycle shift (explains ~7% here)), [[ADNP2]] 3.69× (z +32.7, 47/48 lines; cell-cycle shift (explains ~7% here)), [[ZFPM2-AS1]] 6.17× (z +32.5, 31/32 lines; cell-cycle shift (explains ~3% here)), [[PLA2G4C]] 9.03× (z +32.4, 44/45 lines; cell-cycle shift (explains ~0% here)), [[SPAG1]] 4.44× (z +31.7, 47/47 lines; cell-cycle shift (explains ~5% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (594 genes, none with an alert; 12 shown): [[AARS1]] 0.505× (z -10.2, 42/47 lines), [[SLC1A4]] 0.511× (z -10.2, 27/39 lines), [[PSAT1]] 0.443× (z -9.7, 34/39 lines), [[ASNS]] 0.458× (z -9.3, 38/43 lines), [[SLC1A5]] 0.625× (z -7.9, 32/46 lines), [[GLB1]] 0.736× (z -7.9, 26/47 lines), [[INTS10]] 0.705× (z -7.8, 31/47 lines), [[GFPT1]] 0.645× (z -7.6, 45/47 lines), [[LRRC49]] 0.668× (z -7.5, 23/36 lines), [[WIPI1]] 0.582× (z -7.5, 32/46 lines), [[MAP4]] 0.807× (z -7.4, 28/46 lines), [[MAP3K3]] 0.706× (z -7.2, 27/47 lines)

**0.5 µM** (3919 genes, 801 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[FAM114A1]] 0.300× (z -25.2, 46/46 lines; cell-cycle shift (explains ~7% here)), [[SLC27A1]] 0.282× (z -22.3, 47/48 lines; cell-cycle shift (explains ~6% here)), [[PPARA]] 0.395× (z -20.5, 43/47 lines; cell-cycle shift (explains ~6% here)), [[CD46]] 0.468× (z -20.1, 47/48 lines; cell-cycle shift (explains ~0% here)), [[WIPI1]] 0.268× (z -19.7, 46/47 lines; cell-cycle shift (explains ~8% here)), [[URI1]] 0.508× (z -18.7, 43/48 lines; cell-cycle shift (explains ~6% here)), [[GPR155]] 0.293× (z -18.3, 39/42 lines; cell-cycle shift (explains ~4% here)), [[RAB40B]] 0.307× (z -18.2, 39/44 lines; cell-cycle shift (explains ~7% here)), [[FAM20B]] 0.508× (z -18.1, 41/48 lines; cell-cycle shift (explains ~4% here)), [[SH3PXD2B]] 0.427× (z -17.7, 41/46 lines; cell-cycle shift (explains ~11% here)), [[KANTR]] 0.460× (z -17.5, 44/47 lines; cell-cycle shift (explains ~5% here)), [[SLC1A5]] 0.385× (z -17.3, 37/47 lines; cell-cycle shift (explains ~3% here))

**5 µM** (4924 genes, 2,040 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[FAM114A1]] 0.134× (z -40.5, 46/46 lines; cell-cycle shift (explains ~9% here)), [[BACE2]] 0.177× (z -34.0, 38/38 lines; cell-cycle shift (explains ~12% here)), [[PRKX]] 0.303× (z -33.8, 44/45 lines; cell-cycle shift (explains ~3% here)), [[LOXL2]] 0.130× (z -33.7, 30/30 lines; cell-cycle shift (explains ~3% here)), [[LPCAT1]] 0.175× (z -32.7, 45/47 lines; cell-cycle shift (explains ~8% here)), [[SLC1A1]] 0.139× (z -31.8, 37/37 lines; cell-cycle shift (explains ~7% here)), [[URI1]] 0.309× (z -31.1, 48/48 lines; cell-cycle shift (explains ~7% here)), [[DPYSL2]] 0.193× (z -30.6, 42/43 lines; cell-cycle shift (explains ~2% here)), [[SH3PXD2B]] 0.219× (z -30.4, 42/46 lines; cell-cycle shift (explains ~16% here)), [[FAM117B]] 0.198× (z -30.3, 48/48 lines; cell-cycle shift (explains ~1% here)), [[KIAA1958]] 0.362× (z -29.8, 48/48 lines; cell-cycle shift (explains ~1% here)), [[ZFP64]] 0.293× (z -29.1, 46/48 lines; cell-cycle shift (explains ~10% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 011]] (+4.6), [[Module 068]] (+4.3), [[Module 016]] (+3.9) | [[Module 077]] (-3.6), [[Module 040]] (-3.6), [[Module 063]] (-3.1) |
| 0.5 µM | [[Module 068]] (+14.4), [[Module 011]] (+13.0), [[Module 095]] (+12.9) | [[Module 179]] (-12.1), [[Module 077]] (-12.0), [[Module 040]] (-10.9) |
| 5 µM | [[Module 068]] (+22.9), [[Module 095]] (+20.9), [[Module 051]] (+16.2) | [[Module 077]] (-21.1), [[Module 168]] (-19.4), [[Module 179]] (-17.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[H4 (line)]] (1.63), [[A549 (line)]] (1.46), [[SW48 (line)]] (1.44), [[NCI-H460 (line)]] (1.41) · weakest: [[SHP-77 (line)]] (0.402), [[CFPAC-1 (line)]] (0.599), [[NCI-H2030 (line)]] (0.610) |
| 0.5 µM | [[MIA PaCa-2 (line)]] (-12.4), [[RKO (line)]] (-10.1), [[LOX-IMVI (line)]] (-9.8), [[H4 (line)]] (-9.7), [[A-427 (line)]] (-8.8) | [[A549 (line)]] (1.66), [[NCI-H460 (line)]] (1.64), [[C32 (line)]] (1.60), [[H4 (line)]] (1.52) · weakest: [[SHP-77 (line)]] (0.367), [[HepG2_C3A (line)]] (0.572), [[NCI-H661 (line)]] (0.605) |
| 5 µM | [[MIA PaCa-2 (line)]] (-16.4), [[NCI-H1792 (line)]] (-15.9), [[H4 (line)]] (-15.0), [[NCI-H23 (line)]] (-14.5), [[LOX-IMVI (line)]] (-12.4) | [[HOP62 (line)]] (1.31), [[PANC-1 (line)]] (1.30), [[A549 (line)]] (1.29), [[NCI-H460 (line)]] (1.28) · weakest: [[SHP-77 (line)]] (0.424), [[NCI-H661 (line)]] (0.507), [[C-33 A (line)]] (0.513) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Homoharringtonine (drug)]] (+0.80, Protein synthesis inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[L-Eflornithine (monohydrochloride) (drug)]] (+0.53, unclear); [[Carbamazepine (drug)]] (+0.51, HDAC inhibitor); [[Estrone sulfate (potassium) (drug)]] (+0.50, unclear); [[Esmolol (hydrochloride) (drug)]] (+0.42, unclear); [[Glasdegib (drug)]] (+0.41, Sonic inhibitor, ⚠ only 4 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Meloxicam (drug)]] (+0.41, Cyclooxygenase inhibitor); [[Vitamin K4 (drug)]] (+0.39, unclear); [[Apalutamide (drug)]] (+0.39, Androgen receptor antagonist); [[Abiraterone acetate (drug)]] (+0.39, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 25 arrows, 25 of them with an alert ⚠; grade A 0, B 21, C 4. Shown: the 15 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ATP1B1]] | 5 µM | B | ATP1B1 activity raises the cells' numbers under Harringtonine 5 µM (protects the cells) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 0.45× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[ATP1B1]] | 0.5 µM | B | ATP1B1 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 0.50× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[ARHGAP30]] | 0.5 µM | B | ARHGAP30 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express ARHGAP30 (22) vs lines expressing it (26) | the lines without ARHGAP30: 0.60× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: CEACAM1, IL1RN, NECTIN4; maybe low, not absent |
| [[ARHGAP26]] | 0.5 µM | B | ARHGAP26 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express ARHGAP26 (6) vs lines expressing it (42) | the lines without ARHGAP26: 0.43× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[PYROXD2]] | 0.5 µM | B | PYROXD2 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express PYROXD2 (7) vs lines expressing it (41) | the lines without PYROXD2: 0.57× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |
| [[ENSG00000232884]] | 5 µM | B | ENSG00000232884 activity raises the cells' numbers under Harringtonine 5 µM (protects the cells) | lines that do not express ENSG00000232884 (12) vs lines expressing it (36) | the lines without ENSG00000232884: 0.50× the cells of the other lines | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, NRIP1, ATXN1; maybe low, not absent |
| [[IKZF3]] | 5 µM | B | IKZF3 activity lowers the cells' numbers under Harringtonine 5 µM (makes them more sensitive) | lines that do not express IKZF3 (31) vs lines expressing it (17) | the lines without IKZF3: 1.78× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| [[ENSG00000253227]] | 0.5 µM | B | ENSG00000253227 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express ENSG00000253227 (18) vs lines expressing it (30) | the lines without ENSG00000253227: 0.68× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: COL16A1, SERPINE2, SLCO2B1; maybe low, not absent |
| [[GNA14]] | 0.5 µM | B | GNA14 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express GNA14 (5) vs lines expressing it (43) | the lines without GNA14: 0.50× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[LINC00511]] | 0.5 µM | B | LINC00511 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express LINC00511 (12) vs lines expressing it (36) | the lines without LINC00511: 0.48× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[TNS3]] | 0.5 µM | B | TNS3 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express TNS3 (8) vs lines expressing it (40) | the lines without TNS3: 0.55× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: LGALS3, MAML2, SMOX |
| [[DUSP10]] | 0.5 µM | B | DUSP10 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express DUSP10 (11) vs lines expressing it (37) | the lines without DUSP10: 0.60× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[NFATC2]] | 5 µM | B | NFATC2 activity raises the cells' numbers under Harringtonine 5 µM (protects the cells) | lines that do not express NFATC2 (11) vs lines expressing it (37) | the lines without NFATC2: 0.42× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[ENSG00000232884]] | 0.5 µM | B | ENSG00000232884 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express ENSG00000232884 (12) vs lines expressing it (36) | the lines without ENSG00000232884: 0.57× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, NRIP1, ATXN1; maybe low, not absent |
| [[PLD1]] | 5 µM | B | PLD1 activity raises the cells' numbers under Harringtonine 5 µM (protects the cells) | lines that do not express PLD1 (7) vs lines expressing it (41) | the lines without PLD1: 0.48× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Harringtonine"
- `tables/drugdoses.parquet` — dd in 519, 520, 521
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

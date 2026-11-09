---
drug: "Homoharringtonine"
type: "drug"
salt_base: "Homoharringtonine"
targets: ""
moa_fine: "Protein synthesis inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 11993
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Homoharringtonine

*Protein synthesis inhibitor (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 4014 / 10075 / 11993; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.70 / 0.89.
> Flags by dose: - / cell-cycle shift / cell-cycle shift; composition shift. ⚠ 0.5 µM: cell-cycle shift; 5 µM: cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:G1 | 2,168 / 1,846 | — | +0.03 | -0.8/+0.2/+3.2 | — |
| 0.5 µM | [[Plate 05]]:G1 | 5,584 / 4,491 | — | -0.35 | -1.3/+6.3/+7.3 | ⚠ cell-cycle shift |
| 5 µM | [[Plate 14]]:G1 | 7,203 / 4,790 | 0.995 | -0.43 | +5.5/+19.0/+7.0 | ⚠ cell-cycle shift · composition shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2168 genes, 6 with an alert ⚠; 12 shown): [[RSF1]] 1.50× (z +14.8, 39/48 lines), [[BDP1]] 1.61× (z +14.2, 47/48 lines), [[ZC3H6]] 1.84× (z +13.5, 43/48 lines), [[CBLL1]] 1.76× (z +13.5, 42/48 lines), [[CDKN2AIP]] 2.17× (z +13.1, 36/47 lines), [[BIRC3]] 2.14× (z +12.9, 41/43 lines), [[OBI1]] 1.77× (z +12.8, 42/48 lines), [[MED1]] 1.62× (z +12.7, 45/48 lines), [[REST]] 1.60× (z +12.6, 42/46 lines), [[CMTR2]] 1.98× (z +12.6, 41/47 lines), [[RNF6]] 1.81× (z +12.4, 43/48 lines), [[TRIP11]] 1.76× (z +12.2, 48/48 lines)

**0.5 µM** (5584 genes, 541 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[ZFPM2-AS1]] 7.58× (z +37.6, 32/32 lines; cell-cycle shift (explains ~2% here)), [[ARRDC4]] 10.3× (z +36.2, 37/37 lines; cell-cycle shift (explains ~3% here)), [[HDAC9]] 6.86× (z +36.2, 38/39 lines; cell-cycle shift (explains ~4% here)), [[CREB5]] 7.43× (z +35.2, 33/33 lines; cell-cycle shift (explains ~3% here)), [[KLF10]] 10.1× (z +35.0, 48/48 lines; cell-cycle shift (explains ~10% here)), [[CPEB4]] 3.59× (z +33.8, 40/47 lines; cell-cycle shift (explains ~0% here)), [[PLA2G4C]] 8.43× (z +32.6, 43/44 lines; cell-cycle shift (explains ~0% here)), [[REL]] 4.40× (z +32.3, 46/48 lines; cell-cycle shift (explains ~6% here)), [[BAZ1A]] 3.31× (z +31.8, 46/48 lines; cell-cycle shift (explains ~3% here)), [[CDKN2AIP]] 6.20× (z +30.9, 44/44 lines; cell-cycle shift (explains ~4% here)), [[ENSG00000290808]] 34.6× (z +30.9, 22/22 lines; cell-cycle shift (explains ~2% here)), [[SPAG1]] 3.99× (z +30.6, 47/47 lines; cell-cycle shift (explains ~0% here))

**5 µM** (7203 genes, 1,474 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[HDAC9]] 13.5× (z +69.2, 38/39 lines; cell-cycle shift (explains ~1% here)), [[REL]] 9.37× (z +68.9, 48/48 lines; cell-cycle shift (explains ~8% here)), [[CREB5]] 14.1× (z +65.6, 32/33 lines; cell-cycle shift (explains ~5% here)), [[BAZ1A]] 5.62× (z +65.0, 48/48 lines; cell-cycle shift (explains ~6% here)), [[ZFPM2-AS1]] 11.6× (z +64.4, 32/32 lines; cell-cycle shift (explains ~3% here)), [[KLF10]] 18.9× (z +62.8, 48/48 lines; cell-cycle shift (explains ~16% here)), [[PLA2G4C]] 17.0× (z +61.3, 45/45 lines; cell-cycle shift (explains ~0% here)), [[CPEB4]] 4.88× (z +59.3, 45/47 lines; cell-cycle shift (explains ~0% here)), [[LINC00944]] 15.5× (z +59.2, 28/28 lines; cell-cycle shift (explains ~0% here)), [[ARRDC4]] 14.5× (z +57.8, 38/38 lines; cell-cycle shift (explains ~6% here)), [[ASH1L]] 3.00× (z +57.8, 48/48 lines; cell-cycle shift (explains ~3% here)), [[SLCO5A1]] 15.6× (z +57.1, 40/41 lines; cell-cycle shift (explains ~0% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1846 genes, 4 with an alert ⚠; 12 shown): [[FAM114A1]] 0.509× (z -14.1, 45/46 lines), [[TTC3]] 0.622× (z -13.3, 43/48 lines), [[PPARA]] 0.558× (z -12.8, 42/47 lines), [[PLEKHH2]] 0.527× (z -12.8, 24/34 lines), [[SLC17A5]] 0.478× (z -12.6, 44/48 lines), [[P3H1]] 0.466× (z -12.3, 36/44 lines), [[WIPI1]] 0.443× (z -12.2, 38/47 lines), [[CALU]] 0.480× (z -12.1, 48/48 lines), [[INTS10]] 0.610× (z -11.9, 36/48 lines), [[PDXDC1]] 0.562× (z -11.6, 44/48 lines), [[TPST2]] 0.599× (z -11.5, 30/48 lines), [[SNRPN]] 0.671× (z -11.5, 25/34 lines)

**0.5 µM** (4491 genes, 861 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[FAM114A1]] 0.184× (z -35.5, 46/46 lines; cell-cycle shift (explains ~0% here)), [[DPYSL2]] 0.181× (z -33.0, 42/43 lines; cell-cycle shift (explains ~0% here)), [[BACE2]] 0.199× (z -32.9, 38/38 lines; cell-cycle shift (explains ~2% here)), [[SH3PXD2B]] 0.223× (z -31.2, 46/46 lines; cell-cycle shift (explains ~9% here)), [[KIAA1958]] 0.375× (z -29.9, 48/48 lines; cell-cycle shift (explains ~2% here)), [[ZFP64]] 0.298× (z -29.9, 47/48 lines; cell-cycle shift (explains ~0% here)), [[C1orf21]] 0.205× (z -29.8, 38/38 lines; cell-cycle shift (explains ~1% here)), [[VOPP1]] 0.415× (z -29.0, 39/46 lines; cell-cycle shift (explains ~2% here)), [[LOXL2]] 0.186× (z -29.0, 30/30 lines; cell-cycle shift (explains ~0% here)), [[LIMCH1]] 0.257× (z -28.1, 31/32 lines; cell-cycle shift (explains ~0% here)), [[SEMA4B]] 0.162× (z -28.0, 43/44 lines; cell-cycle shift (explains ~0% here)), [[SLC27A1]] 0.206× (z -27.8, 45/47 lines; cell-cycle shift (explains ~4% here))

**5 µM** (4790 genes, 1,848 with an alert ⚠; the drug-dose carries ⚠ cell-cycle shift; 12 shown): [[FAM114A1]] 0.130× (z -60.4, 46/46 lines; cell-cycle shift (explains ~7% here)), [[BACE2]] 0.128× (z -59.2, 38/38 lines; cell-cycle shift (explains ~10% here)), [[VOPP1]] 0.291× (z -57.5, 45/46 lines; cell-cycle shift (explains ~4% here)), [[PRKX]] 0.268× (z -54.9, 43/45 lines; cell-cycle shift (explains ~3% here)), [[NLN]] 0.304× (z -50.1, 47/48 lines; cell-cycle shift (explains ~11% here)), [[DPYSL2]] 0.163× (z -49.6, 42/43 lines; cell-cycle shift (explains ~1% here)), [[ZFP64]] 0.236× (z -49.6, 48/48 lines; cell-cycle shift (explains ~7% here)), [[CDCP1]] 0.129× (z -49.2, 32/32 lines; cell-cycle shift (explains ~0% here)), [[INTS10]] 0.237× (z -49.2, 48/48 lines; cell-cycle shift (explains ~9% here)), [[SEMA4B]] 0.108× (z -48.4, 44/44 lines; cell-cycle shift (explains ~1% here)), [[SCAMP1]] 0.278× (z -47.8, 48/48 lines; cell-cycle shift (explains ~7% here)), [[URI1]] 0.301× (z -46.8, 47/48 lines; cell-cycle shift (explains ~7% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 068]] (+9.3), [[Module 011]] (+9.0), [[Module 135]] (+8.3) | [[Module 040]] (-6.6), [[Module 179]] (-6.6), [[Module 077]] (-6.2) |
| 0.5 µM | [[Module 068]] (+22.8), [[Module 095]] (+19.3), [[Module 011]] (+18.5) | [[Module 077]] (-18.4), [[Module 006]] (-14.1), [[Module 040]] (-13.6) |
| 5 µM | [[Module 068]] (+35.4), [[Module 095]] (+28.3), [[Module 051]] (+23.6) | [[Module 077]] (-32.5), [[Module 168]] (-28.0), [[Module 018]] (-23.6) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[A-427 (line)]] (-6.7), [[SNU-1 (line)]] (-5.8), [[LOX-IMVI (line)]] (-5.5), [[RKO (line)]] (-4.8), [[MIA PaCa-2 (line)]] (-4.7) | [[NCI-H460 (line)]] (1.86), [[A-172 (line)]] (1.66), [[C32 (line)]] (1.59), [[H4 (line)]] (1.54) · weakest: [[SHP-77 (line)]] (0.453), [[Hs 766T (line)]] (0.565), [[BT-474 (line)]] (0.591) |
| 0.5 µM | [[A-427 (line)]] (-15.5), [[MIA PaCa-2 (line)]] (-14.2), [[NCI-H1792 (line)]] (-13.7), [[RKO (line)]] (-11.6), [[LOX-IMVI (line)]] (-10.9) | [[C32 (line)]] (1.40), [[NCI-H460 (line)]] (1.40), [[A-172 (line)]] (1.38), [[HS-578T (line)]] (1.34) · weakest: [[SHP-77 (line)]] (0.520), [[NCI-H661 (line)]] (0.553), [[HepG2_C3A (line)]] (0.641) |
| 5 µM | [[NCI-H1792 (line)]] (-26.8), [[RKO (line)]] (-23.6), [[A-427 (line)]] (-20.4), [[MIA PaCa-2 (line)]] (-18.2), [[NCI-H23 (line)]] (-17.7) | [[HOP62 (line)]] (1.34), [[C32 (line)]] (1.27), [[NCI-H460 (line)]] (1.26), [[HS-578T (line)]] (1.22) · weakest: [[SHP-77 (line)]] (0.409), [[NCI-H661 (line)]] (0.499), [[C-33 A (line)]] (0.615) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Harringtonine (drug)]] (+0.80, Protein synthesis inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Proglumide (drug)]] (+0.52, unclear); [[Estrone sulfate (potassium) (drug)]] (+0.51, unclear); [[Carbamazepine (drug)]] (+0.50, HDAC inhibitor); [[Pimozide (drug)]] (+0.50, unclear); [[Meloxicam (drug)]] (+0.49, Cyclooxygenase inhibitor); [[Nafamostat (mesylate) (drug)]] (+0.48, unclear, ⚠ only 3 significant genes); [[Bestatin (hydrochloride) (drug)]] (+0.47, unclear); [[Vitamin K4 (drug)]] (+0.46, unclear); [[Filgotinib (drug)]] (+0.46, JAK/STAT inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 52 arrows, 52 of them with an alert ⚠; grade A 0, B 31, C 21. Shown: the 15 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ATP1B1]] | 5 µM | B | ATP1B1 activity raises the cells' numbers under Homoharringtonine 5 µM (protects the cells) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 0.26× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[ATP1B1]] | 0.5 µM | B | ATP1B1 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 0.30× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[ARHGAP26]] | 0.5 µM | B | ARHGAP26 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express ARHGAP26 (6) vs lines expressing it (42) | the lines without ARHGAP26: 0.32× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[ARHGAP26]] | 0.05 µM | B | ARHGAP26 activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express ARHGAP26 (6) vs lines expressing it (42) | the lines without ARHGAP26: 0.66× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[ENSG00000232884]] | 5 µM | B | ENSG00000232884 activity raises the cells' numbers under Homoharringtonine 5 µM (protects the cells) | lines that do not express ENSG00000232884 (12) vs lines expressing it (36) | the lines without ENSG00000232884: 0.29× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, NRIP1, ATXN1; maybe low, not absent |
| [[EPHA1-AS1]] | 5 µM | B | EPHA1-AS1 activity raises the cells' numbers under Homoharringtonine 5 µM (protects the cells) | lines that do not express EPHA1-AS1 (6) vs lines expressing it (42) | the lines without EPHA1-AS1: 0.32× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[ATP1B1]] | 0.05 µM | B | ATP1B1 activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 0.66× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[ARHGAP26]] | 5 µM | B | ARHGAP26 activity raises the cells' numbers under Homoharringtonine 5 µM (protects the cells) | lines that do not express ARHGAP26 (6) vs lines expressing it (42) | the lines without ARHGAP26: 0.30× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SSUH2, ADM2, TBC1D8; maybe low, not absent |
| [[TBC1D8]] | 0.5 µM | B | TBC1D8 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express TBC1D8 (6) vs lines expressing it (42) | the lines without TBC1D8: 0.34× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[OXTR]] | 0.5 µM | B | OXTR activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express OXTR (5) vs lines expressing it (43) | the lines without OXTR: 0.40× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: IPCEF1, SSUH2, OPN3; maybe low, not absent |
| [[EPHA1-AS1]] | 0.5 µM | B | EPHA1-AS1 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express EPHA1-AS1 (6) vs lines expressing it (42) | the lines without EPHA1-AS1: 0.40× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: GNA14, RIPOR2, SSUH2; maybe low, not absent |
| [[ALDH2]] | 0.5 µM | B | ALDH2 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express ALDH2 (9) vs lines expressing it (39) | the lines without ALDH2: 0.45× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |
| [[GNA14]] | 0.05 µM | B | GNA14 activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express GNA14 (5) vs lines expressing it (43) | the lines without GNA14: 0.69× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SSUH2, EXT1, SAMSN1; maybe low, not absent |
| [[LINC00482]] | 5 µM | B | LINC00482 activity raises the cells' numbers under Homoharringtonine 5 µM (protects the cells) | lines that do not express LINC00482 (8) vs lines expressing it (40) | the lines without LINC00482: 0.35× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: SOX13, SEPTIN9-DT |
| [[PYROXD2]] | 0.5 µM | B | PYROXD2 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express PYROXD2 (7) vs lines expressing it (41) | the lines without PYROXD2: 0.34× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: ATP1B1, SMARCA2, ZMIZ1; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Homoharringtonine"
- `tables/drugdoses.parquet` — dd in 528, 529, 530
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

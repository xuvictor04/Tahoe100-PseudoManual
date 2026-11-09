---
drug: "Dihydroartemisinin"
type: "drug"
salt_base: "Dihydroartemisinin"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 451
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Dihydroartemisinin

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 149 / 90 / 451; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.28 / 0.45.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:G12 | 142 / 7 | — | -0.36 | -0.3/-1.3/-0.9 | — |
| 0.5 µM | [[Plate 11]]:G12 | 69 / 21 | — | +0.03 | -0.9/+0.2/+0.8 | — |
| 5 µM | [[Plate 12]]:G12 | 149 / 302 | — | -0.68 | -2.6/-1.4/-0.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (142 genes, none with an alert; 12 shown): [[PKIB]] 1.41× (z +5.5, 12/40 lines), [[CACNA1D]] 1.32× (z +4.3, 9/24 lines), [[IQCH-AS1]] 1.41× (z +4.0, 15/47 lines), [[LINC01091]] 1.45× (z +4.0, 11/30 lines), [[DCDC1]] 1.48× (z +4.0, 11/44 lines), [[ZNF618]] 1.35× (z +3.9, 17/39 lines), [[KIAA0825]] 1.59× (z +3.9, 15/38 lines), [[ZNF346]] 1.24× (z +3.9, 14/48 lines), [[ENSG00000258561]] 1.75× (z +3.9, 12/45 lines), [[BMS1P4-1]] 1.27× (z +3.9, 7/47 lines), [[CRB1]] 1.78× (z +3.8, 5/35 lines), [[ANK3]] 1.24× (z +3.8, 17/25 lines)

**0.5 µM** (69 genes, 1 with an alert ⚠; 13 shown): [[NIBAN1]] 1.64× (z +8.1, 26/37 lines), [[SLC7A1]] ⚠ 1.34× (z +7.2, 34/47 lines; position correction uncertain), [[TRIB3]] 1.67× (z +7.2, 31/44 lines), [[AARS1]] 1.49× (z +6.5, 36/48 lines), [[PCK2]] 1.56× (z +6.1, 18/45 lines), [[LRRC49]] 1.36× (z +6.1, 20/37 lines), [[RPL18A]] 2.08× (z +6.1, 34/47 lines), [[ASNS]] 1.54× (z +5.6, 28/44 lines), [[CARS1]] 1.31× (z +5.5, 28/48 lines), [[NBR2]] 1.43× (z +5.3, 27/47 lines), [[AKNA]] 1.41× (z +5.2, 24/46 lines), [[WARS1]] 1.38× (z +5.2, 26/47 lines), [[PSAT1]] 1.47× (z +4.9, 19/40 lines)

**5 µM** (149 genes, 1 with an alert ⚠; 13 shown): [[NIBAN1]] 1.99× (z +11.3, 31/36 lines), [[TRIB3]] 1.90× (z +9.0, 33/44 lines), [[SLC7A1]] ⚠ 1.43× (z +8.7, 38/46 lines; position correction uncertain), [[AARS1]] 1.64× (z +8.0, 43/47 lines), [[WARS1]] 1.64× (z +8.0, 37/46 lines), [[CARS1]] 1.47× (z +7.9, 36/47 lines), [[AKNA]] 1.66× (z +7.8, 31/46 lines), [[IARS1]] 1.59× (z +7.2, 41/47 lines), [[ASNS]] 1.72× (z +7.0, 35/43 lines), [[MIA2]] 1.40× (z +7.0, 36/47 lines), [[PSAT1]] 1.71× (z +6.9, 27/39 lines), [[LRRC49]] 1.40× (z +6.8, 25/36 lines), [[MOCOS]] 1.55× (z +6.7, 22/41 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (7 genes, none with an alert): [[ITGA5]] 0.773× (z -3.5, 16/37 lines), [[HOXB9]] 0.814× (z -3.3, 4/31 lines), [[CDC42EP1]] 0.822× (z -3.0, 9/42 lines), [[CHMP4C]] 0.832× (z -3.0, 8/32 lines), [[CEBPG]] 0.823× (z -2.9, 14/48 lines), [[EIF4EBP1]] 0.727× (z -2.9, 19/48 lines), [[ARRDC3]] 0.799× (z -2.7, 15/48 lines)

**0.5 µM** (21 genes, none with an alert; 12 shown): [[LRRC20]] 0.726× (z -3.9, 14/40 lines), [[ADAMTSL3]] 0.712× (z -3.8, 4/18 lines), [[C1GALT1C1]] 0.731× (z -3.8, 12/43 lines), [[ZHX3]] 0.830× (z -3.7, 19/48 lines), [[ENSG00000287249]] 0.727× (z -3.6, 10/41 lines), [[LMLN]] 0.777× (z -3.5, 20/46 lines), [[KDM4D]] 0.691× (z -3.5, 8/40 lines), [[POLA2]] 0.824× (z -3.4, 9/47 lines), [[MTAP]] 0.807× (z -3.3, 18/42 lines), [[CHDH]] 0.746× (z -3.2, 4/23 lines), [[TMEM53]] 0.772× (z -3.2, 9/43 lines), [[ENSG00000224905]] 0.830× (z -3.2, 9/36 lines)

**5 µM** (302 genes, none with an alert; 12 shown): [[BRI3BP]] 0.587× (z -5.9, 35/46 lines), [[TGIF2]] 0.739× (z -5.2, 16/43 lines), [[FAM111B]] 0.554× (z -5.1, 26/37 lines), [[C1GALT1C1]] 0.655× (z -5.1, 18/45 lines), [[UHRF1]] 0.591× (z -5.0, 17/44 lines), [[NLGN4X]] 0.636× (z -5.0, 3/10 lines), [[BICC1]] 0.683× (z -4.9, 7/19 lines), [[ZHX3]] 0.781× (z -4.9, 21/47 lines), [[LRRC20]] 0.673× (z -4.9, 9/42 lines), [[MARVELD1]] 0.617× (z -4.7, 18/42 lines), [[SERTAD4]] 0.540× (z -4.6, 11/28 lines), [[DHCR24]] 0.712× (z -4.5, 20/44 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 088]] (+2.1), [[Module 230]] (+2.0), [[Module 124]] (+2.0) | — |
| 0.5 µM | [[Module 133]] (+2.6), [[Module 063]] (+2.6) | — |
| 5 µM | [[Module 133]] (+3.5), [[Module 063]] (+3.2), [[Module 234]] (+2.4) | [[Module 006]] (-2.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[CHP-212 (line)]] (1.27), [[HS-578T (line)]] (1.15), [[H4 (line)]] (1.14), [[A498 (line)]] (1.10) · weakest: [[NCI-H2347 (line)]] (0.381), [[SW480 (line)]] (0.501), [[HepG2_C3A (line)]] (0.516) |
| 0.5 µM | — | [[SNU-1 (line)]] (1.94), [[SHP-77 (line)]] (1.83), [[BT-474 (line)]] (1.73), [[HEC-1-A (line)]] (1.68) · weakest: [[AsPC-1 (line)]] (0.184), [[NCI-H1792 (line)]] (0.326), [[CFPAC-1 (line)]] (0.352) |
| 5 µM | [[A498 (line)]] (-3.5), [[A549 (line)]] (-3.2), [[HS-578T (line)]] (-3.1), [[HOP62 (line)]] (-3.1) | [[SNU-1 (line)]] (1.68), [[RKO (line)]] (1.38), [[HCT15 (line)]] (1.36), [[LS 180 (line)]] (1.31) · weakest: [[SW 1271 (line)]] (0.645), [[AsPC-1 (line)]] (0.662), [[NCI-H661 (line)]] (0.686) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Ivermectin (drug)]] (+0.61, unclear); [[Artesunate (drug)]] (+0.53, JAK/STAT inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Hexylresorcinol (drug)]] (+0.53, unclear); [[Tadalafil (drug)]] (+0.51, unclear); [[Chlorhexidine (diacetate) (drug)]] (+0.50, unclear); [[5-Azacytidine (drug)]] (+0.50, DNA methyltransferase inhibitor); [[Tomivosertib (drug)]] (+0.50, Protein synthesis inhibitor); [[Capivasertib (drug)]] (+0.49, PI3K/AKT inhibitor, ⚠ only 5 significant genes); [[Goserelin (acetate) (drug)]] (+0.48, unclear); [[Cloxacillin (sodium) (drug)]] (+0.45, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 30 arrows, 30 of them with an alert ⚠; grade A 0, B 20, C 10. Shown: the 15 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MYH14]] | 5 µM | B | MYH14 activity raises the cells' numbers under Dihydroartemisinin 5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.71× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[EPCAM]] | 5 µM | B | EPCAM activity raises the cells' numbers under Dihydroartemisinin 5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.73× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[KCNMA1]] | 5 µM | B | KCNMA1 activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.42× the cells of the other lines | 0.032 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[ERBB3]] | 5 µM | B | ERBB3 activity raises the cells' numbers under Dihydroartemisinin 5 µM (protects the cells) | lines that do not express ERBB3 (27) vs lines expressing it (21) | the lines without ERBB3: 0.73× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.42× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[SRGN]] | 5 µM | B | SRGN activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.46× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| [[SIRLNT]] | 5 µM | B | SIRLNT activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 1.43× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[RSPO3]] | 5 µM | B | RSPO3 activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 1.33× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[CLDN3]] | 5 µM | B | CLDN3 activity raises the cells' numbers under Dihydroartemisinin 5 µM (protects the cells) | lines that do not express CLDN3 (28) vs lines expressing it (20) | the lines without CLDN3: 0.75× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[SRPX]] | 5 µM | B | SRPX activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express SRPX (22) vs lines expressing it (26) | the lines without SRPX: 1.25× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[TJP3]] | 5 µM | B | TJP3 activity raises the cells' numbers under Dihydroartemisinin 5 µM (protects the cells) | lines that do not express TJP3 (29) vs lines expressing it (19) | the lines without TJP3: 0.76× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[CKMT1B]] | 5 µM | B | CKMT1B activity raises the cells' numbers under Dihydroartemisinin 5 µM (protects the cells) | lines that do not express CKMT1B (28) vs lines expressing it (20) | the lines without CKMT1B: 0.76× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.34× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[FAAH2]] | 5 µM | B | FAAH2 activity raises the cells' numbers under Dihydroartemisinin 5 µM (protects the cells) | lines that do not express FAAH2 (26) vs lines expressing it (22) | the lines without FAAH2: 0.75× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[MDFI]] | 5 µM | B | MDFI activity raises the cells' numbers under Dihydroartemisinin 5 µM (protects the cells) | lines that do not express MDFI (25) vs lines expressing it (23) | the lines without MDFI: 0.74× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: ESRP1, IRF6, GJB3 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Dihydroartemisinin"
- `tables/drugdoses.parquet` — dd in 356, 357, 358
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

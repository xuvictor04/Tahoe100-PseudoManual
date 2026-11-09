---
drug: "Neratinib"
type: "drug"
salt_base: "Neratinib"
targets: "EGFR, ERBB2"
moa_fine: "EGFR/ERBB inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 279
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Neratinib

*EGFR/ERBB inhibitor (inhibitor/antagonist) · targets: EGFR, ERBB2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 29 / 27 / 279; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.21 / 0.49.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:D12 | 27 / 2 | — | -0.79 | +0.6/-0.4/-0.3 | — |
| 0.5 µM | [[Plate 11]]:D12 | 24 / 3 | — | +0.59 | -0.6/-1.2/-0.4 | — |
| 5 µM | [[Plate 12]]:D12 | 205 / 74 | — | -0.49 | -1.9/-1.7/+0.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (27 genes, none with an alert; 12 shown): [[PRRT3]] 1.43× (z +4.0, 2/39 lines), [[ENSG00000285572]] 1.55× (z +3.7, 3/30 lines), [[C8orf34]] 1.44× (z +3.7, 4/34 lines), [[ENSG00000259053]] 1.36× (z +3.6, 1/41 lines), [[PIGV]] 1.31× (z +3.4, 7/43 lines), [[HERC2P10]] 1.36× (z +3.4, 0/24 lines), [[BRME1]] 1.43× (z +3.3, 2/30 lines), [[WNT3]] 1.38× (z +3.2, 5/32 lines), [[ARSG]] 1.25× (z +3.2, 6/40 lines), [[STK31]] 1.41× (z +3.2, 1/28 lines), [[ENSG00000283982]] 1.36× (z +3.1, 2/15 lines), [[GALNT8]] 1.36× (z +3.1, 1/18 lines)

**0.5 µM** (24 genes, none with an alert; 12 shown): [[PSAT1]] 1.52× (z +5.4, 23/40 lines), [[PCK2]] 1.41× (z +4.8, 15/46 lines), [[JDP2]] 1.40× (z +4.8, 7/35 lines), [[RHOA]] 1.21× (z +4.6, 25/49 lines), [[VLDLR-AS1]] 1.58× (z +4.5, 16/38 lines), [[KRAS]] 1.20× (z +4.3, 16/49 lines), [[SLC1A4]] 1.30× (z +4.3, 8/44 lines), [[NIBAN1]] 1.29× (z +4.1, 14/38 lines), [[SLC7A11]] 1.40× (z +4.1, 21/43 lines), [[PHGDH]] 1.37× (z +3.8, 23/43 lines), [[KLF2]] 1.72× (z +3.7, 20/44 lines), [[AARS1]] 1.26× (z +3.7, 18/49 lines)

**5 µM** (205 genes, none with an alert; 12 shown): [[PSAT1]] 2.08× (z +9.4, 35/39 lines), [[MAP4]] 1.27× (z +8.7, 26/47 lines), [[PCK2]] 1.84× (z +8.4, 35/46 lines), [[NIBAN1]] 1.67× (z +8.4, 26/37 lines), [[TOM1L1]] 1.30× (z +8.1, 26/48 lines), [[ASNS]] 1.86× (z +8.0, 32/44 lines), [[XPOT]] 1.47× (z +7.9, 39/48 lines), [[KLF2]] 3.11× (z +7.8, 37/44 lines), [[KRAS]] 1.39× (z +7.8, 41/48 lines), [[SLC7A1]] 1.37× (z +7.7, 30/47 lines), [[TRIB3]] 1.73× (z +7.6, 33/44 lines), [[VLDLR-AS1]] 2.15× (z +7.5, 24/37 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[PTGS2]] 0.765× (z -3.2, 5/20 lines), [[PLXNB3]] 0.625× (z -2.9, 11/30 lines)

**0.5 µM** (3 genes, none with an alert): [[FAM222A-AS1]] 0.681× (z -3.8, 5/40 lines), [[SHC4]] 0.741× (z -3.2, 7/25 lines), [[TLCD3B]] 0.702× (z -3.2, 8/37 lines)

**5 µM** (74 genes, none with an alert; 12 shown): [[WDPCP]] 0.803× (z -5.1, 27/47 lines), [[ENSG00000282988]] 0.584× (z -4.8, 8/42 lines), [[SFMBT2]] 0.775× (z -4.7, 12/28 lines), [[ENSG00000235007]] 0.725× (z -4.6, 10/45 lines), [[TMEM178B]] 0.798× (z -4.4, 10/26 lines), [[PAG1]] 0.812× (z -4.4, 16/33 lines), [[PLA2G4A]] 0.784× (z -4.3, 13/26 lines), [[EPHA3]] 0.680× (z -4.1, 13/21 lines), [[MEF2C]] 0.780× (z -4.1, 15/33 lines), [[MRPS31P4]] 0.775× (z -4.1, 7/47 lines), [[HCP5]] 0.702× (z -4.1, 16/24 lines), [[TCF4]] 0.775× (z -4.0, 12/23 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 133]] (+3.7), [[Module 063]] (+3.6) | [[Module 179]] (-2.6), [[Module 235]] (-2.3) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[NCI-H2030 (line)]] (-3.2) | [[SNU-423 (line)]] (1.98), [[H4 (line)]] (1.74), [[hTERT-HPNE (line)]] (1.57), [[HT-29 (line)]] (1.48) · weakest: [[A-427 (line)]] (-0.304), [[NCI-H460 (line)]] (-0.146), [[KATO III (line)]] (0.0635) |
| 0.5 µM | — | [[NCI-H2030 (line)]] (1.70), [[C-33 A (line)]] (1.65), [[RPMI-7951 (line)]] (1.64), [[SW 1271 (line)]] (1.58) · weakest: [[CHP-212 (line)]] (0.181), [[NCI-H2122 (line)]] (0.208), [[PANC-1 (line)]] (0.285) |
| 5 µM | [[NCI-H2030 (line)]] (-4.4), [[hTERT-HPNE (line)]] (-3.5), [[A498 (line)]] (-3.3) | [[hTERT-HPNE (line)]] (1.57), [[C-33 A (line)]] (1.48), [[NCI-H460 (line)]] (1.39), [[H4 (line)]] (1.32) · weakest: [[PANC-1 (line)]] (0.434), [[NCI-H1573 (line)]] (0.491), [[KATO III (line)]] (0.540) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[Neratinib (maleate) (drug)]] (+0.80, EGFR/ERBB inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Vinblastine (sulfate) (drug)]] (+0.63, Microtubule inhibitor); [[Cyclosporin A (drug)]] (+0.53, unclear); [[Pitavastatin (Calcium) (drug)]] (+0.49, unclear, ⚠ vector dose flagged: cell-cycle shift); [[5-Azacytidine (drug)]] (+0.47, DNA methyltransferase inhibitor); [[Daptomycin (drug)]] (+0.47, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Artesunate (drug)]] (+0.46, JAK/STAT inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Sunitinib (drug)]] (+0.43, Multi-TK inhibitor, ⚠ vector dose flagged: toxic); [[Peretinoin (drug)]] (+0.42, Retinoic receptor agonist); [[Tomivosertib (drug)]] (+0.42, Protein synthesis inhibitor); [[Cysteamine (hydrochloride) (drug)]] (+0.41, unclear); [[Belumosudil (mesylate) (drug)]] (+0.39, unclear); [[Ponatinib (drug)]] (+0.39, Multi-TK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 22 arrows, 22 of them with an alert ⚠; grade A 0, B 11, C 11. Shown: the 15 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity lowers the cells' numbers under Neratinib 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.24× the cells of the other lines | 0.048 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Neratinib 5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.27× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[MYH14]] | 5 µM | B | MYH14 activity raises the cells' numbers under Neratinib 5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.80× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[KCNMA1]] | 0.05 µM | B | KCNMA1 activity lowers the cells' numbers under Neratinib 0.05 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.22× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[SYT17]] | 5 µM | B | SYT17 activity raises the cells' numbers under Neratinib 5 µM (protects the cells) | lines that do not express SYT17 (13) vs lines expressing it (35) | the lines without SYT17: 0.91× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: SEPTIN3, STOX2, ULK2; maybe low, not absent |
| [[PAPPA]] | 5 µM | B | PAPPA activity lowers the cells' numbers under Neratinib 5 µM (makes them more sensitive) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 1.25× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[RSPO3]] | 5 µM | B | RSPO3 activity lowers the cells' numbers under Neratinib 5 µM (makes them more sensitive) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 1.29× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[RSPO3]] | 0.05 µM | B | RSPO3 activity lowers the cells' numbers under Neratinib 0.05 µM (makes them more sensitive) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 1.27× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[LFNG]] | 5 µM | B | LFNG activity raises the cells' numbers under Neratinib 5 µM (protects the cells) | lines that do not express LFNG (14) vs lines expressing it (34) | the lines without LFNG: 0.86× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: TNFSF10, EPHA4, CXXC5; maybe low, not absent |
| [[F2RL2]] | 5 µM | B | F2RL2 activity lowers the cells' numbers under Neratinib 5 µM (makes them more sensitive) | lines that do not express F2RL2 (32) vs lines expressing it (16) | the lines without F2RL2: 1.31× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA |
| [[AOX1]] | 5 µM | B | AOX1 activity lowers the cells' numbers under Neratinib 5 µM (makes them more sensitive) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 1.27× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[FIGN]] | 5 µM | C | FIGN activity lowers the cells' numbers under Neratinib 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.22× the cells of the other lines | 0.030 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[HES4]] | 0.05 µM | C | HES4 activity lowers the cells' numbers under Neratinib 0.05 µM (makes them more sensitive) | lines that do not express HES4 (4) vs lines expressing it (44) | the lines without HES4: 1.36× the cells of the other lines | 0.046 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |
| [[SPART-AS1]] | 5 µM | C | SPART-AS1 activity lowers the cells' numbers under Neratinib 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.20× the cells of the other lines | 0.047 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[ZNF761]] | 5 µM | C | ZNF761 activity raises the cells' numbers under Neratinib 5 µM (protects the cells) | lines that do not express ZNF761 (3) vs lines expressing it (45) | the lines without ZNF761: 0.70× the cells of the other lines | 0.058 | ⚠ few lines (3 vs 47); across organs; also absent: ZNF468, ZNF845, FAM102A |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Neratinib"
- `tables/drugdoses.parquet` — dd in 711, 712, 713
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

---
drug: "Niclosamide (olamine)"
type: "drug"
salt_base: "Niclosamide"
targets: "STAT3"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 7764
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Niclosamide (olamine)

*unclear (inhibitor/antagonist) · targets: STAT3 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 919 / 7764; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.16 / 0.35.
> Flags by dose: - / - / toxic; cell-cycle shift. ⚠ 5 µM: toxic; cell-cycle shift (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:H7 | 2 / 1 | — | +0.67 | -0.6/-0.1/+0.8 | — |
| 0.5 µM | [[Plate 08]]:H7 | 107 / 812 | — | +0.70 | -2.3/+0.7/+0.1 | — |
| 5 µM | [[Plate 09]]:H7 | 4,190 / 3,574 | — | -1.20 | +7.0/+5.2/+6.1 | ⚠ toxic; cell-cycle shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[FTH1]] 1.51× (z +4.0, 39/44 lines), [[BEST1]] 1.52× (z +3.1, 15/46 lines)

**0.5 µM** (107 genes, none with an alert; 12 shown): [[TRIB3]] 1.63× (z +6.8, 27/45 lines), [[YARS1]] 1.36× (z +6.6, 35/48 lines), [[CARS1]] 1.37× (z +6.5, 34/48 lines), [[AARS1]] 1.49× (z +6.4, 37/48 lines), [[XPOT]] 1.33× (z +5.9, 36/48 lines), [[ASNS]] 1.57× (z +5.8, 28/44 lines), [[MARS1]] 1.39× (z +5.6, 29/48 lines), [[NIBAN1]] 1.39× (z +5.3, 22/37 lines), [[GOT1]] 1.57× (z +5.2, 31/48 lines), [[ENSG00000286125]] 1.85× (z +5.0, 15/47 lines), [[HSPA9]] 1.37× (z +5.0, 40/48 lines), [[GPT2]] 1.37× (z +4.9, 26/46 lines)

**5 µM** (4190 genes, 4,190 with an alert ⚠; the drug-dose carries ⚠ toxic; cell-cycle shift; 12 shown): [[HSPH1]] ⚠ 7.03× (z +19.5, 47/47 lines; toxic; cell-cycle shift (explains ~15% here)), [[LARP4]] ⚠ 2.23× (z +18.1, 44/47 lines; toxic; cell-cycle shift (explains ~12% here)), [[PAWR]] ⚠ 2.02× (z +17.6, 42/45 lines; toxic; cell-cycle shift (explains ~0% here)), [[ENAH]] ⚠ 1.72× (z +16.3, 36/44 lines; toxic; cell-cycle shift (explains ~14% here)), [[PITPNB]] ⚠ 1.75× (z +16.2, 46/47 lines; toxic; cell-cycle shift (explains ~8% here)), [[HSPA1B]] ⚠ 6.47× (z +16.0, 43/45 lines; toxic; cell-cycle shift (explains ~9% here)), [[ZFP91]] ⚠ 1.92× (z +15.6, 45/47 lines; toxic; cell-cycle shift (explains ~18% here)), [[LARP1]] ⚠ 1.64× (z +15.6, 39/47 lines; toxic; cell-cycle shift (explains ~0% here)), [[DNAJB1]] ⚠ 3.33× (z +15.5, 44/47 lines; toxic; cell-cycle shift (explains ~11% here)), [[G3BP1]] ⚠ 1.92× (z +15.5, 46/47 lines; toxic; cell-cycle shift (explains ~22% here)), [[NFKB1]] ⚠ 2.71× (z +15.5, 45/47 lines; toxic; cell-cycle shift (explains ~9% here)), [[GPBP1]] ⚠ 1.93× (z +15.3, 46/47 lines; toxic; cell-cycle shift (explains ~3% here))

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[NDNF]] 0.704× (z -3.2, 1/21 lines)

**0.5 µM** (812 genes, none with an alert; 12 shown): [[ENSG00000261775]] 0.580× (z -5.9, 20/46 lines), [[ZFHX3-AS1]] 0.706× (z -5.8, 30/48 lines), [[CYP4A22-AS1]] 0.477× (z -5.6, 28/45 lines), [[ARHGAP44]] 0.782× (z -5.6, 11/32 lines), [[CFAP44]] 0.528× (z -5.4, 38/46 lines), [[GUCY1B2]] 0.499× (z -5.4, 14/29 lines), [[DDX11-AS1]] 0.604× (z -5.3, 21/45 lines), [[ENSG00000285733]] 0.484× (z -5.3, 17/42 lines), [[ITGB3BP]] 0.743× (z -5.2, 30/47 lines), [[ENSG00000253766]] 0.525× (z -5.2, 14/33 lines), [[ENSG00000265943]] 0.540× (z -5.2, 27/46 lines), [[LINC01515]] 0.585× (z -5.1, 26/33 lines)

**5 µM** (3574 genes, 3,574 with an alert ⚠; the drug-dose carries ⚠ toxic; cell-cycle shift; 12 shown): [[RIMKLA]] ⚠ 0.245× (z -24.1, 32/36 lines; toxic; cell-cycle shift (explains ~1% here)), [[TXNIP]] ⚠ 0.193× (z -20.6, 35/36 lines; toxic; cell-cycle shift (explains ~0% here)), [[ZMYND8]] ⚠ 0.351× (z -19.6, 42/46 lines; toxic; cell-cycle shift (explains ~12% here)), [[TUBGCP5]] ⚠ 0.398× (z -19.5, 39/47 lines; toxic; cell-cycle shift (explains ~0% here)), [[PPFIA4]] ⚠ 0.175× (z -19.4, 43/43 lines; toxic; cell-cycle shift (explains ~11% here)), [[C4orf47]] ⚠ 0.193× (z -19.3, 39/44 lines; toxic; cell-cycle shift (explains ~11% here)), [[EPIC1]] ⚠ 0.297× (z -19.2, 25/25 lines; toxic; cell-cycle shift (explains ~16% here)), [[KDM4B]] ⚠ 0.361× (z -19.1, 45/47 lines; toxic; cell-cycle shift (explains ~8% here)), [[ZNF395]] ⚠ 0.313× (z -18.5, 43/45 lines; toxic; cell-cycle shift (explains ~8% here)), [[P4HA1]] ⚠ 0.313× (z -18.4, 46/47 lines; toxic; cell-cycle shift (explains ~0% here)), [[PRELID2]] ⚠ 0.254× (z -18.1, 45/46 lines; toxic; cell-cycle shift (explains ~15% here)), [[PFKFB4]] ⚠ 0.235× (z -18.1, 46/47 lines; toxic; cell-cycle shift (explains ~7% here))

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 063]] (+2.7), [[Module 041]] (+2.7), [[Module 207]] (+2.2) | [[Module 006]] (-3.1), [[Module 088]] (-2.7), [[Module 010]] (-2.7) |
| 5 µM | [[Module 182]] (+7.7), [[Module 060]] (+6.8), [[Module 214]] (+5.8) | [[Module 170]] (-14.2), [[Module 144]] (-8.9), [[Module 052]] (-8.5) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[BT-474 (line)]] (-3.9) | [[AN3 CA (line)]] (2.05), [[NCI-H2030 (line)]] (1.84), [[SNU-1 (line)]] (1.43), [[HepG2_C3A (line)]] (1.41) · weakest: [[NCI-H2347 (line)]] (0.602), [[HT-29 (line)]] (0.606), [[HOP62 (line)]] (0.612) |
| 5 µM | [[C-33 A (line)]] (-8.2), [[NCI-H23 (line)]] (-8.2), [[H4 (line)]] (-7.8), [[SNU-1 (line)]] (-7.1), [[RPMI-7951 (line)]] (-6.9) | [[COLO 205 (line)]] (1.37), [[NCI-H1792 (line)]] (1.35), [[LoVo (line)]] (1.27), [[NCI-H460 (line)]] (1.27) · weakest: [[NCI-H661 (line)]] (0.395), [[NCI-H2347 (line)]] (0.465), [[SW1417 (line)]] (0.603) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: toxic; cell-cycle shift. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Dinaciclib (drug)]] (+0.47, CDK inhibitor, ⚠ vector dose flagged: toxic; transcription drop; cell-cycle shift); [[Simotinib (drug)]] (+0.45, EGFR/ERBB inhibitor, ⚠ vector dose flagged: toxic); [[Norepinephrine (hydrochloride) (drug)]] (+0.44, Adrenoceptor agonist); [[Belumosudil (drug)]] (+0.37, unclear); [[Orlistat (drug)]] (+0.35, unclear); [[Sildenafil (drug)]] (+0.35, unclear, ⚠ only 5 significant genes); [[Drospirenone (drug)]] (+0.33, unclear); [[Tucidinostat (drug)]] (+0.33, HDAC inhibitor); [[Acetohexamide (drug)]] (+0.33, unclear); [[Cepharanthine (drug)]] (+0.33, unclear); [[Elagolix sodium (drug)]] (+0.32, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 21 arrows, 21 of them with an alert ⚠; grade A 0, B 8, C 13. Shown: the 15 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MAML2]] | 5 µM | B | MAML2 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express MAML2 (8) vs lines expressing it (40) | the lines without MAML2: 0.41× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[NFATC2]] | 5 µM | B | NFATC2 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express NFATC2 (11) vs lines expressing it (37) | the lines without NFATC2: 0.57× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[IL15]] | 5 µM | B | IL15 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 0.49× the cells of the other lines | 0.066 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[LINC02257]] | 5 µM | B | LINC02257 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express LINC02257 (15) vs lines expressing it (33) | the lines without LINC02257: 0.59× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: CTSS, PAG1, ZNF365; maybe low, not absent |
| [[PCED1B]] | 5 µM | B | PCED1B activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express PCED1B (11) vs lines expressing it (37) | the lines without PCED1B: 0.50× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[AMIGO2]] | 5 µM | B | AMIGO2 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express AMIGO2 (12) vs lines expressing it (36) | the lines without AMIGO2: 0.54× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[IGFBP3]] | 5 µM | B | IGFBP3 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express IGFBP3 (20) vs lines expressing it (28) | the lines without IGFBP3: 0.73× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[FGFBP1]] | 5 µM | B | FGFBP1 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express FGFBP1 (36) vs lines expressing it (12) | the lines without FGFBP1: 0.49× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| [[PLS3]] | 5 µM | C | PLS3 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express PLS3 (4) vs lines expressing it (44) | the lines without PLS3: 0.36× the cells of the other lines | 0.014 | ⚠ few lines (4 vs 46); across organs; also absent: FOSL1, IGF2BP2, FCHSD1; maybe low, not absent |
| [[HBEGF]] | 5 µM | C | HBEGF activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express HBEGF (3) vs lines expressing it (45) | the lines without HBEGF: 0.30× the cells of the other lines | 0.019 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, TRAF3IP2; maybe low, not absent |
| [[FCHSD1]] | 5 µM | C | FCHSD1 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express FCHSD1 (3) vs lines expressing it (45) | the lines without FCHSD1: 0.33× the cells of the other lines | 0.021 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: PLS3, CDK6, SH2B3 |
| [[ELF4]] | 5 µM | C | ELF4 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express ELF4 (3) vs lines expressing it (45) | the lines without ELF4: 0.35× the cells of the other lines | 0.034 | ⚠ few lines (3 vs 47); across organs; also absent: FUCA2, AIFM2, SP100; maybe low, not absent |
| [[ZFP36]] | 5 µM | C | ZFP36 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express ZFP36 (3) vs lines expressing it (45) | the lines without ZFP36: 0.36× the cells of the other lines | 0.037 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: FTH1, CDC42EP1, ENSG00000284716 |
| [[CEBPD]], [[GCA]] | 5 µM | C | CEBPD, GCA activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.36× the cells of the other lines | 0.038 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| [[FTH1]] | 5 µM | C | FTH1 activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express FTH1 (4) vs lines expressing it (44) | the lines without FTH1: 0.43× the cells of the other lines | 0.044 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Niclosamide (olamine)"
- `tables/drugdoses.parquet` — dd in 720, 721, 722
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

---
drug: "Terfenadine"
type: "drug"
salt_base: "Terfenadine"
targets: "HRH1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 137
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Terfenadine

*unclear (inhibitor/antagonist) · targets: HRH1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 54 / 137; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.24 / 0.41.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:C8 | 0 / 0 | — | +0.39 | +0.6/+0.2/+0.5 | — |
| 0.5 µM | [[Plate 05]]:C8 | 24 / 30 | — | +0.05 | +0.2/+1.3/+1.2 | — |
| 5 µM | [[Plate 14]]:C8 | 71 / 66 | 0.697 | -0.05 | -1.2/-0.8/+0.9 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (24 genes, none with an alert; 12 shown): [[TBL2]] 1.24× (z +4.5, 12/48 lines), [[TMEM106B]] 1.22× (z +4.1, 19/48 lines), [[LINC00944]] 1.30× (z +4.0, 5/28 lines), [[TMED2]] 1.27× (z +3.9, 36/48 lines), [[ABITRAM]] 1.23× (z +3.8, 5/47 lines), [[PRXL2C]] 1.28× (z +3.7, 14/45 lines), [[HLA-H]] 1.64× (z +3.7, 13/38 lines), [[KDELR3]] 1.33× (z +3.6, 9/45 lines), [[MXI1]] 1.30× (z +3.6, 32/47 lines), [[TWF1]] 1.39× (z +3.5, 30/48 lines), [[PSMD6]] 1.25× (z +3.4, 12/48 lines), [[RPL4]] 1.28× (z +3.4, 34/48 lines)

**5 µM** (71 genes, none with an alert; 12 shown): [[CYP51A1]] 1.33× (z +6.4, 39/47 lines), [[SCD]] 1.37× (z +6.3, 39/48 lines), [[IDI1]] 1.38× (z +6.1, 38/48 lines), [[HMGCR]] 1.34× (z +6.0, 35/48 lines), [[MSMO1]] 1.48× (z +6.0, 37/47 lines), [[FDFT1]] 1.34× (z +5.7, 38/47 lines), [[HMGCS1]] 1.37× (z +5.5, 32/47 lines), [[INSIG1]] 1.47× (z +5.4, 41/47 lines), [[MVK]] 1.31× (z +5.4, 16/47 lines), [[FDPS]] 1.35× (z +5.4, 34/48 lines), [[STARD4]] 1.35× (z +5.0, 34/44 lines), [[DHCR7]] 1.38× (z +4.6, 21/44 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (30 genes, none with an alert; 12 shown): [[VPS9D1]] 0.711× (z -4.6, 19/46 lines), [[ARHGEF18]] 0.801× (z -4.5, 28/48 lines), [[LINC02595]] 0.689× (z -4.2, 16/37 lines), [[CDK11A]] 0.816× (z -3.9, 19/48 lines), [[RRP7BP]] 0.717× (z -3.8, 9/43 lines), [[ZNF346]] 0.812× (z -3.7, 17/48 lines), [[ENSG00000290549]] 0.645× (z -3.7, 7/25 lines), [[ZNF329]] 0.826× (z -3.5, 5/41 lines), [[ENSG00000261766]] 0.684× (z -3.5, 9/39 lines), [[ULK3]] 0.768× (z -3.5, 8/44 lines), [[GIGYF1]] 0.819× (z -3.4, 17/48 lines), [[SH2B3]] 0.810× (z -3.4, 12/43 lines)

**5 µM** (66 genes, none with an alert; 12 shown): [[SYN2]] 0.699× (z -5.4, 13/23 lines), [[CIT]] 0.825× (z -4.5, 26/47 lines), [[CENPI]] 0.806× (z -4.5, 20/46 lines), [[JAG1]] 0.806× (z -4.3, 20/42 lines), [[LTBP2]] 0.777× (z -4.3, 13/31 lines), [[CCN2]] 0.727× (z -4.1, 8/31 lines), [[EVA1A-AS]] 0.649× (z -4.1, 8/23 lines), [[SH3RF2]] 0.791× (z -4.1, 12/32 lines), [[GEN1]] 0.813× (z -4.0, 22/48 lines), [[VCL]] 0.770× (z -3.9, 33/47 lines), [[MELTF]] 0.822× (z -3.8, 18/41 lines), [[ENSG00000176593]] 0.756× (z -3.8, 13/33 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Module 170]] (-2.3) |
| 5 µM | [[Module 086]] (+3.2), [[Module 041]] (+3.0), [[Module 045]] (+2.9) | [[Module 006]] (-2.3), [[Module 160]] (-2.2), [[Module 004]] (-2.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[J82 (line)]] (-4.1) | [[CFPAC-1 (line)]] (1.36), [[Hs 766T (line)]] (1.33), [[SNU-423 (line)]] (1.23), [[RKO (line)]] (1.19) · weakest: [[HepG2_C3A (line)]] (0.392), [[AN3 CA (line)]] (0.493), [[BT-474 (line)]] (0.539) |
| 5 µM | — | [[Hs 766T (line)]] (1.37), [[SW 1088 (line)]] (1.32), [[A-172 (line)]] (1.23), [[RPMI-7951 (line)]] (1.20) · weakest: [[AN3 CA (line)]] (0.459), [[BT-474 (line)]] (0.546), [[RKO (line)]] (0.695) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Almonertinib (hydrochloride) (drug)]] (+0.69, EGFR/ERBB inhibitor); [[Tolcapone (drug)]] (+0.66, unclear, ⚠ only 6 significant genes); [[Adagrasib (drug)]] (+0.65, RAS inhibitor); [[Pasireotide (acetate) (drug)]] (+0.64, unclear); [[Tetracycline (hydrochloride) (drug)]] (+0.63, unclear, ⚠ only 6 significant genes); [[Almonertinib (mesylate) (drug)]] (+0.61, EGFR/ERBB inhibitor); [[Vandetanib (drug)]] (+0.61, Multi-TK inhibitor); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.59, unclear); [[Fluvoxamine (maleate) (drug)]] (+0.55, unclear); [[Quinidine (15% dihydroquinidine) (drug)]] (+0.54, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 147 arrows, 147 of them with an alert ⚠; grade A 0, B 146, C 1. Shown: the 15 strongest; 132 more arrows (132 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MPZL3]] | 0.5 µM | B | MPZL3 activity raises the cells' numbers under Terfenadine 0.5 µM (protects the cells) | lines that do not express MPZL3 (25) vs lines expressing it (23) | the lines without MPZL3: 0.71× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[INAVA]], [[MROH3P]] | 5 µM | B | INAVA, MROH3P activity raises the cells' numbers under Terfenadine 5 µM (protects the cells) | lines that do not express INAVA, MROH3P (29) vs lines expressing them (19) | the lines without INAVA, MROH3P: 0.85× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[RNF39]] | 0.5 µM | B | RNF39 activity raises the cells' numbers under Terfenadine 0.5 µM (protects the cells) | lines that do not express RNF39 (30) vs lines expressing it (18) | the lines without RNF39: 0.72× the cells of the other lines | 0.027 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[FOXQ1]] | 0.5 µM | B | FOXQ1 activity raises the cells' numbers under Terfenadine 0.5 µM (protects the cells) | lines that do not express FOXQ1 (30) vs lines expressing it (18) | the lines without FOXQ1: 0.72× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1 |
| [[IL1R2]] | 0.5 µM | B | IL1R2 activity raises the cells' numbers under Terfenadine 0.5 µM (protects the cells) | lines that do not express IL1R2 (23) vs lines expressing it (25) | the lines without IL1R2: 0.73× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[ADGRF1]] | 5 µM | B | ADGRF1 activity raises the cells' numbers under Terfenadine 5 µM (protects the cells) | lines that do not express ADGRF1 (35) vs lines expressing it (13) | the lines without ADGRF1: 0.84× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[ATP2C2]] | 0.5 µM | B | ATP2C2 activity raises the cells' numbers under Terfenadine 0.5 µM (protects the cells) | lines that do not express ATP2C2 (32) vs lines expressing it (16) | the lines without ATP2C2: 0.69× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[SLC5A1]] | 5 µM | B | SLC5A1 activity raises the cells' numbers under Terfenadine 5 µM (protects the cells) | lines that do not express SLC5A1 (36) vs lines expressing it (12) | the lines without SLC5A1: 0.83× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[MAL2]] | 5 µM | B | MAL2 activity raises the cells' numbers under Terfenadine 5 µM (protects the cells) | lines that do not express MAL2 (31) vs lines expressing it (17) | the lines without MAL2: 0.86× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[SERPINB5]] | 0.5 µM | B | SERPINB5 activity raises the cells' numbers under Terfenadine 0.5 µM (protects the cells) | lines that do not express SERPINB5 (34) vs lines expressing it (14) | the lines without SERPINB5: 0.74× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8 |
| [[ENSG00000243004]] | 0.5 µM | B | ENSG00000243004 activity raises the cells' numbers under Terfenadine 0.5 µM (protects the cells) | lines that do not express ENSG00000243004 (31) vs lines expressing it (17) | the lines without ENSG00000243004: 0.73× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MACC1, TMEM125, GRHL2 |
| [[TNNT2]] | 0.5 µM | B | TNNT2 activity raises the cells' numbers under Terfenadine 0.5 µM (protects the cells) | lines that do not express TNNT2 (29) vs lines expressing it (19) | the lines without TNNT2: 0.75× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[ADCY4]] | 5 µM | B | ADCY4 activity raises the cells' numbers under Terfenadine 5 µM (protects the cells) | lines that do not express ADCY4 (33) vs lines expressing it (15) | the lines without ADCY4: 0.85× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[P2RY2]] | 5 µM | B | P2RY2 activity raises the cells' numbers under Terfenadine 5 µM (protects the cells) | lines that do not express P2RY2 (27) vs lines expressing it (21) | the lines without P2RY2: 0.88× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[MAL2]] | 0.5 µM | B | MAL2 activity raises the cells' numbers under Terfenadine 0.5 µM (protects the cells) | lines that do not express MAL2 (31) vs lines expressing it (17) | the lines without MAL2: 0.74× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Terfenadine"
- `tables/drugdoses.parquet` — dd in 994, 995, 996
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

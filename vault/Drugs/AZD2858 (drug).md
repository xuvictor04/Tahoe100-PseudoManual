---
drug: "AZD2858"
type: "drug"
salt_base: "AZD2858"
targets: "GSK3B, GSK3A"
moa_fine: "GSK3 inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 1277
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# AZD2858

*GSK3 inhibitor (inhibitor/antagonist) · targets: GSK3B, GSK3A · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 1277 / 3; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.22 / 0.55.
> Flags by dose: - / toxic; plate-row cell shift; noisy plate (z scaled) / toxic; noisy plate (z scaled). ⚠ 0.5 µM: toxic; 5 µM: toxic (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:E1 | 1 / 1 | — | +0.20 | +0.8/+0.8/+0.8 | — |
| 0.5 µM | [[Plate 02]]:E1 | 1,254 / 23 | — | -3.30 | +0.4/+0.4/+2.0 | ⚠ toxic · plate-row cell shift; noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:E1 | 1 / 2 | — | -1.13 | +0.8/+0.7/+0.7 | ⚠ toxic · noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENSG00000268833]] 1.63× (z +3.9, 1/39 lines)

**0.5 µM** (1254 genes, 1,254 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[ZNF727]] ⚠ 3.90× (z +7.8, 0/6 lines), [[ZNF667-AS1]] ⚠ 3.57× (z +7.7, 1/8 lines), [[BAG3]] ⚠ 1.78× (z +7.3, 32/47 lines), [[HSPA1B]] ⚠ 3.15× (z +7.3, 36/40 lines), [[CCNYL2-1]] ⚠ 3.97× (z +7.2, 0/7 lines), [[DNAJA4]] ⚠ 1.98× (z +7.0, 11/23 lines), [[ZNF257]] ⚠ 3.63× (z +7.0, 0/8 lines), [[PTPN20]] ⚠ 4.00× (z +6.9, 0/6 lines), [[CCNYL2]] ⚠ 2.14× (z +6.9, 1/10 lines), [[TRPM2-AS]] ⚠ 3.60× (z +6.6, 0/7 lines), [[KDF1]] ⚠ 3.51× (z +6.5, 2/11 lines), [[ENSG00000291130]] ⚠ 2.95× (z +6.5, 0/8 lines)

**5 µM** (1 gene, 1 with an alert ⚠; the drug-dose carries ⚠ toxic): [[EIF2B2]] ⚠ 1.38× (z +2.9, 5/43 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[MED16]] 0.766× (z -2.9, 12/48 lines)

**0.5 µM** (23 genes, 23 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[ENSG00000290832]] ⚠ 0.612× (z -4.7, 10/21 lines), [[ITPK1]] ⚠ 0.791× (z -4.1, 12/40 lines), [[PRDM16]] ⚠ 0.693× (z -3.9, 11/28 lines), [[ALG14]] ⚠ 0.736× (z -3.9, 12/43 lines), [[DCAKD]] ⚠ 0.784× (z -3.5, 15/45 lines), [[HSD17B14]] ⚠ 0.690× (z -3.5, 4/25 lines), [[ZNF70]] ⚠ 0.674× (z -3.5, 10/26 lines), [[ENSG00000291283]] ⚠ 0.657× (z -3.5, 8/26 lines), [[TJAP1]] ⚠ 0.812× (z -3.2, 14/47 lines), [[ENSG00000258017]] ⚠ 0.767× (z -3.2, 11/42 lines), [[ZBTB8A]] ⚠ 0.753× (z -3.2, 12/44 lines), [[SDHAP4-1]] ⚠ 0.763× (z -3.2, 14/45 lines)

**5 µM** (2 genes, 2 with an alert ⚠; the drug-dose carries ⚠ toxic): [[PEX26]] ⚠ 0.786× (z -3.3, 10/45 lines), [[ZNF713]] ⚠ 0.753× (z -3.0, 10/42 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 196]] (+3.0), [[Module 060]] (+2.8), [[Module 087]] (+2.6) | [[Module 124]] (-2.1) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[BT-474 (line)]] (-3.3) | [[AN3 CA (line)]] (2.01), [[SNU-1 (line)]] (1.71), [[HCT15 (line)]] (1.55), [[MIA PaCa-2 (line)]] (1.55) · weakest: [[SW480 (line)]] (0.341), [[NCI-H460 (line)]] (0.353), [[HEC-1-A (line)]] (0.401) |
| 5 µM | [[PANC-1 (line)]] (-4.3), [[C32 (line)]] (-3.5), [[A-172 (line)]] (-3.5), [[A498 (line)]] (-3.2) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: toxic. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Torkinib (drug)]] (+0.83, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Hydroxyfasudil (drug)]] (+0.67, unclear); [[Pimozide (drug)]] (+0.64, unclear); [[Docetaxel (drug)]] (+0.64, Microtubule inhibitor, ⚠ vector dose flagged: transcription drop; cell-cycle shift); [[XRK3F2 (drug)]] (+0.63, unclear); [[Simotinib (drug)]] (+0.62, EGFR/ERBB inhibitor, ⚠ vector dose flagged: toxic); [[olaparib (drug)]] (+0.60, DNA synthesis/repair inhibitor, ⚠ only 3 significant genes); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] (+0.60, Glucose transporter inhibitor); [[BI-78D3 (drug)]] (+0.56, Other MAPK inhibitor); [[Canagliflozin (hemihydrate) (drug)]] (+0.56, Glucose transporter inhibitor); [[Carbamazepine (drug)]] (+0.54, HDAC inhibitor); [[Pioglitazone (drug)]] (+0.54, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 22 arrows, 22 of them with an alert ⚠; grade A 0, B 7, C 15. Shown: the 15 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000275119]] | 0.5 µM | B | ENSG00000275119 activity raises the cells' numbers under AZD2858 0.5 µM (protects the cells) | lines that do not express ENSG00000275119 (10) vs lines expressing it (38) | the lines without ENSG00000275119: 0.80× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: LINC01252; maybe low, not absent |
| [[IKZF3]] | 0.5 µM | B | IKZF3 activity lowers the cells' numbers under AZD2858 0.5 µM (makes them more sensitive) | lines that do not express IKZF3 (31) vs lines expressing it (17) | the lines without IKZF3: 1.24× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| [[MAP3K15]] | 0.5 µM | B | MAP3K15 activity lowers the cells' numbers under AZD2858 0.5 µM (makes them more sensitive) | lines that do not express MAP3K15 (19) vs lines expressing it (29) | the lines without MAP3K15: 1.24× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[RSPO3]] | 0.5 µM | B | RSPO3 activity raises the cells' numbers under AZD2858 0.5 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.78× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[CACNG7]] | 5 µM | B | CACNG7 activity lowers the cells' numbers under AZD2858 5 µM (makes them more sensitive) | lines that do not express CACNG7 (21) vs lines expressing it (27) | the lines without CACNG7: 1.30× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: WNT5B, P3H2, EID2B |
| [[ADAM28]] | 5 µM | B | ADAM28 activity raises the cells' numbers under AZD2858 5 µM (protects the cells) | lines that do not express ADAM28 (31) vs lines expressing it (17) | the lines without ADAM28: 0.90× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[SLC2A9]] | 0.5 µM | B | SLC2A9 activity raises the cells' numbers under AZD2858 0.5 µM (protects the cells) | lines that do not express SLC2A9 (6) vs lines expressing it (42) | the lines without SLC2A9: 0.77× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[FIGN]] | 5 µM | C | FIGN activity lowers the cells' numbers under AZD2858 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.35× the cells of the other lines | 0.004 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[SPART-AS1]] | 5 µM | C | SPART-AS1 activity lowers the cells' numbers under AZD2858 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.31× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[NR3C1]] | 5 µM | C | NR3C1 activity lowers the cells' numbers under AZD2858 5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.40× the cells of the other lines | 0.011 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[C2orf74]] | 5 µM | C | C2orf74 activity lowers the cells' numbers under AZD2858 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.36× the cells of the other lines | 0.012 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[LTBP3]] | 5 µM | C | LTBP3 activity lowers the cells' numbers under AZD2858 5 µM (makes them more sensitive) | lines that do not express LTBP3 (4) vs lines expressing it (44) | the lines without LTBP3: 1.49× the cells of the other lines | 0.033 | ⚠ few lines (4 vs 46); across organs; also absent: DBN1, NUAK1, BLVRA; maybe low, not absent |
| [[ITPK1]] | 5 µM | C | ITPK1 activity raises the cells' numbers under AZD2858 5 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.69× the cells of the other lines | 0.043 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| [[ENSG00000286964]] | 5 µM | C | ENSG00000286964 activity lowers the cells' numbers under AZD2858 5 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.32× the cells of the other lines | 0.056 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |
| [[SIX1]] | 5 µM | C | SIX1 activity lowers the cells' numbers under AZD2858 5 µM (makes them more sensitive) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 1.33× the cells of the other lines | 0.059 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "AZD2858"
- `tables/drugdoses.parquet` — dd in 39, 40, 41
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

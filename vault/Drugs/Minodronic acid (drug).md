---
drug: "Minodronic acid"
type: "drug"
salt_base: "Minodronic acid"
targets: "P2RX2, P2RX3"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 10
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Minodronic acid

*unclear (inhibitor/antagonist) · targets: P2RX2, P2RX3 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 10 / 8 / 10; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.44 / 0.10.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:H8 | 6 / 4 | — | +0.16 | +0.6/-2.1/-0.3 | — |
| 0.5 µM | [[Plate 02]]:H8 | 8 / 0 | — | +0.79 | +0.7/-1.6/-0.4 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:H8 | 10 / 0 | — | +0.19 | +1.6/-0.1/+1.1 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (6 genes, 5 with an alert ⚠): [[HMG20B]] ⚠ 1.71× (z +8.4, 42/48 lines; position correction uncertain), [[MAP7D1]] ⚠ 1.54× (z +7.2, 39/48 lines; position correction uncertain), [[ACOT7]] ⚠ 1.26× (z +4.7, 17/46 lines; position correction uncertain), [[NF2]] ⚠ 1.23× (z +4.6, 13/47 lines; position correction uncertain), [[BRWD3]] 1.24× (z +3.7, 34/48 lines), [[STIP1]] ⚠ 1.23× (z +3.1, 16/48 lines; position correction uncertain)

**0.5 µM** (8 genes, 8 with an alert ⚠): [[HMG20B]] ⚠ 1.93× (z +7.8, 43/48 lines; position correction uncertain), [[MAP7D1]] ⚠ 1.78× (z +7.3, 37/48 lines; position correction uncertain), [[ACOT7]] ⚠ 1.29× (z +3.9, 10/46 lines; position correction uncertain), [[NF2]] ⚠ 1.23× (z +3.4, 5/47 lines; position correction uncertain), [[RANGAP1]] ⚠ 1.22× (z +2.8, 0/48 lines; position correction uncertain), [[NOM1]] ⚠ 1.20× (z +2.6, 1/48 lines; position correction uncertain), [[STIP1]] ⚠ 1.26× (z +2.6, 10/48 lines; position correction uncertain), [[PDCD11]] ⚠ 1.21× (z +2.6, 4/48 lines; position correction uncertain)

**5 µM** (10 genes, 5 with an alert ⚠): [[HMG20B]] ⚠ 2.71× (z +8.7, 42/48 lines; position correction uncertain), [[MAP7D1]] ⚠ 2.01× (z +6.5, 35/48 lines; position correction uncertain), [[TNIP1]] 1.42× (z +4.1, 29/48 lines), [[ACOT7]] ⚠ 1.54× (z +3.4, 1/46 lines; position correction uncertain), [[USP11]] 1.53× (z +3.3, 16/48 lines), [[MSN]] 1.43× (z +3.1, 17/38 lines), [[GOLIM4]] 1.24× (z +2.9, 2/48 lines), [[LRPAP1]] 1.42× (z +2.8, 4/48 lines), [[PDCD11]] ⚠ 1.31× (z +2.7, 8/48 lines; position correction uncertain), [[NOM1]] ⚠ 1.28× (z +2.7, 2/48 lines; position correction uncertain)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[FAM50A]] 0.708× (z -3.8, 27/48 lines), [[NOP14]] 0.802× (z -3.7, 15/48 lines), [[ORMDL2]] 0.740× (z -3.3, 9/48 lines), [[SMIM29]] 0.656× (z -3.1, 13/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[AsPC-1 (line)]] (-3.1) | — |
| 5 µM | [[A549 (line)]] (-3.1) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Erdafitinib (drug)]] (+0.69, Other TK inhibitor, ⚠ only 6 significant genes); [[Pemigatinib (drug)]] (+0.67, Other TK inhibitor); [[Omeprazole (sodium) (drug)]] (+0.66, unclear); [[Anastrozole (drug)]] (+0.63, unclear, ⚠ only 5 significant genes); [[Silodosin (drug)]] (+0.60, unclear); [[Pimitespib (drug)]] (+0.57, unclear); [[Zileuton (drug)]] (+0.55, unclear, ⚠ only 4 significant genes); [[Vortioxetine (drug)]] (+0.55, unclear, ⚠ vector dose flagged: toxic); [[DT-061 (drug)]] (+0.52, unclear); [[Celecoxib (drug)]] (+0.52, Cyclooxygenase inhibitor); [[Methotrexate (drug)]] (+0.52, DNA synthesis/repair inhibitor); [[SBI-0640756 (drug)]] (+0.50, Protein synthesis inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 96 arrows, 96 of them with an alert ⚠; grade A 0, B 91, C 5. Shown: the 15 strongest; 81 more arrows (81 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ADGRF1]] | 0.5 µM | B | ADGRF1 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express ADGRF1 (35) vs lines expressing it (13) | the lines without ADGRF1: 1.23× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[OVOL1]], [[TMPRSS4]] | 0.5 µM | B | OVOL1, TMPRSS4 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express OVOL1, TMPRSS4 (33) vs lines expressing them (15) | the lines without OVOL1, TMPRSS4: 1.22× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: GRHL2, ST14, TMEM30B; co-absent genes |
| [[C1orf116]], [[IRF6]] | 0.5 µM | B | C1orf116, IRF6 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (17) | the lines without C1orf116, IRF6: 1.21× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |
| [[S100A14]] | 0.5 µM | B | S100A14 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express S100A14 (33) vs lines expressing it (15) | the lines without S100A14: 1.22× the cells of the other lines | 0.032 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[TMPRSS2]] | 0.5 µM | B | TMPRSS2 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express TMPRSS2 (35) vs lines expressing it (13) | the lines without TMPRSS2: 1.22× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[SGPP2]] | 0.5 µM | B | SGPP2 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express SGPP2 (32) vs lines expressing it (16) | the lines without SGPP2: 1.20× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[ANK2]] | 0.5 µM | B | ANK2 activity raises the cells' numbers under Minodronic acid 0.5 µM (protects the cells) | lines that do not express ANK2 (16) vs lines expressing it (32) | the lines without ANK2: 0.84× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[TRIM29]] | 0.5 µM | B | TRIM29 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express TRIM29 (28) vs lines expressing it (20) | the lines without TRIM29: 1.19× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[P2RY2]] | 0.5 µM | B | P2RY2 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express P2RY2 (27) vs lines expressing it (21) | the lines without P2RY2: 1.17× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[FAM83B]] | 0.5 µM | B | FAM83B activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express FAM83B (30) vs lines expressing it (18) | the lines without FAM83B: 1.19× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, GRHL2, ST14 |
| [[INAVA]], [[MROH3P]] | 0.5 µM | B | INAVA, MROH3P activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express INAVA, MROH3P (29) vs lines expressing them (19) | the lines without INAVA, MROH3P: 1.18× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[TNNT2]] | 0.5 µM | B | TNNT2 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express TNNT2 (29) vs lines expressing it (19) | the lines without TNNT2: 1.17× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[CEACAM1]] | 0.5 µM | B | CEACAM1 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express CEACAM1 (27) vs lines expressing it (21) | the lines without CEACAM1: 1.17× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29 |
| [[COL17A1]] | 0.5 µM | B | COL17A1 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express COL17A1 (34) vs lines expressing it (14) | the lines without COL17A1: 1.22× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[CDH1]] | 0.5 µM | B | CDH1 activity lowers the cells' numbers under Minodronic acid 0.5 µM (makes them more sensitive) | lines that do not express CDH1 (31) vs lines expressing it (17) | the lines without CDH1: 1.21× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Minodronic acid"
- `tables/drugdoses.parquet` — dd in 687, 688, 689
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

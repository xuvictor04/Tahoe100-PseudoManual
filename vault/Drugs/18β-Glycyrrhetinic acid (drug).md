---
drug: "18β-Glycyrrhetinic acid"
type: "drug"
salt_base: "18β-Glycyrrhetinic acid"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 34
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# 18β-Glycyrrhetinic acid

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 10 / 15 / 34; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.18 / 0.34.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:C6 | 4 / 6 | — | -0.31 | -0.6/-0.5/+0.5 | — |
| 0.5 µM | [[Plate 05]]:C6 | 11 / 4 | — | -0.54 | -1.0/-0.3/+0.4 | — |
| 5 µM | [[Plate 14]]:C6 | 28 / 6 | 0.790 | -0.44 | -1.4/-0.8/+0.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[HRK]] 1.65× (z +3.9, 1/27 lines), [[ZNF727]] 1.54× (z +3.4, 1/11 lines), [[ENSG00000273489]] 1.43× (z +3.4, 1/33 lines), [[COLEC12]] 1.38× (z +2.9, 1/19 lines)

**0.5 µM** (11 genes, none with an alert): [[ZNF574]] 1.42× (z +4.2, 11/44 lines), [[SORBS3]] 1.30× (z +4.0, 12/46 lines), [[TMEM74B]] 1.49× (z +3.8, 7/32 lines), [[ZNF672]] 1.27× (z +3.4, 5/43 lines), [[FAHD2A]] 1.21× (z +3.2, 4/45 lines), [[CENPT]] 1.24× (z +3.1, 9/46 lines), [[SYT7]] 1.22× (z +3.1, 7/38 lines), [[RAVER1]] 1.21× (z +3.1, 10/48 lines), [[SLC37A2]] 1.31× (z +3.0, 0/27 lines), [[THAP10]] 1.36× (z +3.0, 1/27 lines), [[PPP1R3C]] 1.35× (z +2.8, 5/26 lines)

**5 µM** (28 genes, none with an alert; 12 shown): [[TEX11]] 1.44× (z +4.3, 1/27 lines), [[SLFN11]] 1.23× (z +4.1, 3/20 lines), [[LINC02474]] 1.39× (z +3.8, 0/8 lines), [[ENSG00000260927]] 1.25× (z +3.6, 2/45 lines), [[ENSG00000240401]] 1.22× (z +3.5, 9/48 lines), [[VIPR1]] 1.31× (z +3.5, 1/22 lines), [[ENSG00000233491]] 1.33× (z +3.4, 1/11 lines), [[CLIC5]] 1.28× (z +3.3, 2/11 lines), [[HRK]] 1.36× (z +3.3, 3/29 lines), [[KLHL14]] 1.41× (z +3.2, 0/10 lines), [[ENSG00000288720]] 1.31× (z +3.2, 1/31 lines), [[LRFN2]] 1.49× (z +3.2, 0/6 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (6 genes, none with an alert): [[EIF3F]] 0.824× (z -3.6, 13/48 lines), [[ITM2C]] 0.798× (z -3.4, 13/47 lines), [[ZNF845]] 0.772× (z -3.2, 5/41 lines), [[ENSG00000285043]] 0.728× (z -3.2, 6/43 lines), [[RCN3]] 0.757× (z -3.0, 6/34 lines), [[ENSG00000234405]] 0.757× (z -3.0, 4/31 lines)

**0.5 µM** (4 genes, none with an alert): [[TAF6L]] 0.750× (z -4.5, 13/44 lines), [[RFXAP]] 0.725× (z -3.9, 12/40 lines), [[ENSG00000282381]] 0.691× (z -3.7, 5/22 lines), [[INCENP]] 0.790× (z -3.4, 16/48 lines)

**5 µM** (6 genes, none with an alert): [[G6PD]] 0.816× (z -3.8, 20/48 lines), [[ABCA2]] 0.817× (z -3.5, 18/47 lines), [[ENSG00000285043]] 0.790× (z -3.4, 10/43 lines), [[CBX2]] 0.827× (z -3.3, 14/40 lines), [[ICAM1]] 0.832× (z -3.0, 11/29 lines), [[ENSG00000261026]] 0.682× (z -2.9, 12/34 lines)

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
| 0.5 µM | — | — |
| 5 µM | — | [[SW 1088 (line)]] (2.20), [[MIA PaCa-2 (line)]] (1.63), [[SW 1271 (line)]] (1.53), [[LOX-IMVI (line)]] (1.50) · weakest: [[HEC-1-A (line)]] (0.315), [[PANC-1 (line)]] (0.349), [[J82 (line)]] (0.362) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.72, unclear); [[Tranilast (drug)]] (+0.69, unclear, ⚠ only 6 significant genes); [[Almonertinib (hydrochloride) (drug)]] (+0.68, EGFR/ERBB inhibitor); [[Saquinavir (drug)]] (+0.67, unclear); [[Docetaxel (Trihydrate) (drug)]] (+0.67, Microtubule inhibitor); [[Methylprednisolone succinate (drug)]] (+0.65, Glucocorticoid receptor agonist); [[Azithromycin (hydrate) (drug)]] (+0.64, unclear); [[Darolutamide (drug)]] (+0.62, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Decitabine (drug)]] (+0.59, DNA methyltransferase inhibitor); [[Ciclopirox (drug)]] (+0.57, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 82 arrows, 82 of them with an alert ⚠; grade A 0, B 75, C 7. Shown: the 15 strongest; 67 more arrows (67 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[GRHL2]], [[LINC02967]] | 0.5 µM | B | GRHL2, LINC02967 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express GRHL2, LINC02967 (34) vs lines expressing them (14) | the lines without GRHL2, LINC02967: 0.82× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent genes |
| [[ADGRF1]] | 0.5 µM | B | ADGRF1 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express ADGRF1 (35) vs lines expressing it (13) | the lines without ADGRF1: 0.82× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[CLDN3]] | 0.5 µM | B | CLDN3 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express CLDN3 (28) vs lines expressing it (20) | the lines without CLDN3: 0.83× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[ENSG00000285897]] | 0.5 µM | B | ENSG00000285897 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express ENSG00000285897 (27) vs lines expressing it (21) | the lines without ENSG00000285897: 0.85× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: RNF43, CRB3, KDF1 |
| [[TMEM125]] | 0.5 µM | B | TMEM125 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express TMEM125 (33) vs lines expressing it (15) | the lines without TMEM125: 0.82× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[ST14]] | 0.5 µM | B | ST14 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express ST14 (32) vs lines expressing it (16) | the lines without ST14: 0.83× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[ESRP1]] | 0.5 µM | B | ESRP1 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express ESRP1 (31) vs lines expressing it (17) | the lines without ESRP1: 0.83× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[TTC28]] | 0.5 µM | B | TTC28 activity lowers the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (makes them more sensitive) | lines that do not express TTC28 (15) vs lines expressing it (33) | the lines without TTC28: 1.20× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |
| [[SMPDL3B]] | 0.5 µM | B | SMPDL3B activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express SMPDL3B (23) vs lines expressing it (25) | the lines without SMPDL3B: 0.86× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1 |
| [[RNF43]] | 0.5 µM | B | RNF43 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express RNF43 (26) vs lines expressing it (22) | the lines without RNF43: 0.86× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000285897, CRB3, KDF1 |
| [[SCEL]] | 0.5 µM | B | SCEL activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express SCEL (35) vs lines expressing it (13) | the lines without SCEL: 0.83× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |
| [[KDF1]] | 0.5 µM | B | KDF1 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express KDF1 (30) vs lines expressing it (18) | the lines without KDF1: 0.84× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[ITGB6]] | 0.5 µM | B | ITGB6 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express ITGB6 (32) vs lines expressing it (16) | the lines without ITGB6: 0.83× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4 |
| [[ERBB3]] | 0.5 µM | B | ERBB3 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express ERBB3 (27) vs lines expressing it (21) | the lines without ERBB3: 0.84× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[OVOL1]], [[TMPRSS4]] | 0.5 µM | B | OVOL1, TMPRSS4 activity raises the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (protects the cells) | lines that do not express OVOL1, TMPRSS4 (33) vs lines expressing them (15) | the lines without OVOL1, TMPRSS4: 0.83× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: GRHL2, ST14, TMEM30B; co-absent genes |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "18\u03b2-Glycyrrhetinic acid"
- `tables/drugdoses.parquet` — dd in 6, 7, 8
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

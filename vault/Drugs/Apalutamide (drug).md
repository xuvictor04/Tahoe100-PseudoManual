---
drug: "Apalutamide"
type: "drug"
salt_base: "Apalutamide"
targets: "AR"
moa_fine: "Androgen receptor antagonist"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 93
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Apalutamide

*Androgen receptor antagonist (inhibitor/antagonist) · targets: AR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 12 / 93 / 1; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.03 / 0.18.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:H6 | 11 / 1 | — | -0.10 | +0.1/-0.0/+1.2 | — |
| 0.5 µM | [[Plate 08]]:H6 | 38 / 55 | — | +0.48 | +1.0/+0.5/-0.8 | — |
| 5 µM | [[Plate 09]]:H6 | 1 / 0 | — | -0.17 | -0.2/-0.1/+0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (11 genes, none with an alert): [[CD47]] 1.32× (z +4.8, 29/46 lines), [[ENSG00000251652]] 1.44× (z +3.3, 0/11 lines), [[DMBX1]] 1.41× (z +3.3, 1/26 lines), [[CAPN14]] 1.52× (z +3.2, 2/18 lines), [[HYKK]] 1.34× (z +3.1, 2/35 lines), [[HSPA2]] 1.44× (z +3.1, 5/29 lines), [[CBX2]] 1.32× (z +3.0, 3/37 lines), [[CBLC]] 1.41× (z +2.9, 3/17 lines), [[ENSG00000291075]] 1.28× (z +2.9, 0/43 lines), [[NGF]] 1.40× (z +2.9, 0/16 lines), [[MTUS2]] 1.29× (z +2.8, 2/39 lines)

**0.5 µM** (38 genes, none with an alert; 12 shown): [[IRS1]] 1.36× (z +3.9, 17/42 lines), [[FN1]] 1.37× (z +3.8, 12/19 lines), [[SAMD9]] 1.54× (z +3.6, 27/37 lines), [[SH3TC2]] 1.43× (z +3.4, 4/27 lines), [[PLCB1]] 1.24× (z +3.4, 12/29 lines), [[SPOCK3]] 1.43× (z +3.3, 0/22 lines), [[EGR2]] 1.76× (z +3.3, 8/40 lines), [[MX2]] 1.46× (z +3.3, 21/32 lines), [[TXK]] 1.37× (z +3.3, 6/41 lines), [[ENSG00000286850]] 1.27× (z +3.3, 5/37 lines), [[STAT1]] 1.25× (z +3.3, 22/48 lines), [[GDAP1]] 1.27× (z +3.2, 3/41 lines)

**5 µM** (1 gene, none with an alert): [[DHRS3]] 1.23× (z +3.3, 15/35 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[MPP4]] 0.622× (z -3.3, 13/39 lines)

**0.5 µM** (55 genes, none with an alert; 12 shown): [[NDUFV2]] 0.805× (z -4.3, 24/48 lines), [[SRP54-AS1]] 0.697× (z -4.2, 30/48 lines), [[RAB18]] 0.748× (z -4.1, 34/48 lines), [[HYCC2]] 0.792× (z -4.0, 24/48 lines), [[FBXO42]] 0.748× (z -4.0, 29/48 lines), [[ENSG00000284697]] 0.658× (z -3.9, 19/48 lines), [[RAB21]] 0.830× (z -3.8, 22/48 lines), [[CNNM2]] 0.773× (z -3.7, 28/48 lines), [[PPTC7]] 0.776× (z -3.7, 25/48 lines), [[FBXO3]] 0.796× (z -3.6, 12/48 lines), [[FHIP2A]] 0.757× (z -3.6, 23/48 lines), [[CAMTA1]] 0.811× (z -3.6, 25/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[Module 207]] (-2.8), [[Module 179]] (-2.6), [[Module 168]] (-2.3) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[NCI-H1573 (line)]] (1.48), [[CHP-212 (line)]] (1.31), [[AsPC-1 (line)]] (1.28), [[SNU-423 (line)]] (1.23) · weakest: [[BT-474 (line)]] (0.121), [[AN3 CA (line)]] (0.126), [[NCI-H661 (line)]] (0.292) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Mifepristone (drug)]] (+0.93, unclear); [[Esmolol (hydrochloride) (drug)]] (+0.90, unclear); [[Tirabrutinib (drug)]] (+0.89, Other TK inhibitor); [[Estrone sulfate (potassium) (drug)]] (+0.88, unclear); [[Diphenhydramine (drug)]] (+0.86, unclear); [[L-Eflornithine (monohydrochloride) (drug)]] (+0.83, unclear); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.83, unclear); [[Proglumide (drug)]] (+0.78, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 71 arrows, 71 of them with an alert ⚠; grade A 0, B 63, C 8. Shown: the 15 strongest; 56 more arrows (56 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ST14]] | 0.5 µM | B | ST14 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express ST14 (32) vs lines expressing it (16) | the lines without ST14: 1.30× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[OVOL1]], [[TMPRSS4]] | 0.5 µM | B | OVOL1, TMPRSS4 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express OVOL1, TMPRSS4 (33) vs lines expressing them (15) | the lines without OVOL1, TMPRSS4: 1.29× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: GRHL2, ST14, TMEM30B; co-absent genes |
| [[ENSG00000262302]] | 0.5 µM | B | ENSG00000262302 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000262302 (29) vs lines expressing it (19) | the lines without ENSG00000262302: 1.28× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: CLDN7, ESRP1, ATP2C2; maybe low, not absent |
| [[ERBB3]] | 0.5 µM | B | ERBB3 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express ERBB3 (27) vs lines expressing it (21) | the lines without ERBB3: 1.24× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[TNNT2]] | 0.5 µM | B | TNNT2 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express TNNT2 (29) vs lines expressing it (19) | the lines without TNNT2: 1.23× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[ESRP1]] | 0.5 µM | B | ESRP1 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express ESRP1 (31) vs lines expressing it (17) | the lines without ESRP1: 1.28× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[KDF1]] | 0.5 µM | B | KDF1 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express KDF1 (30) vs lines expressing it (18) | the lines without KDF1: 1.24× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[ANKRD22]] | 0.5 µM | B | ANKRD22 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express ANKRD22 (34) vs lines expressing it (14) | the lines without ANKRD22: 1.27× the cells of the other lines | 0.027 | ⚠ within organs, on part of the lines; also absent: TMEM30B, GRHL2, RAB25 |
| [[LAD1]] | 0.5 µM | B | LAD1 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express LAD1 (30) vs lines expressing it (18) | the lines without LAD1: 1.24× the cells of the other lines | 0.027 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[ATP2C2]] | 0.5 µM | B | ATP2C2 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express ATP2C2 (32) vs lines expressing it (16) | the lines without ATP2C2: 1.30× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[GRHL2]], [[LINC02967]] | 0.5 µM | B | GRHL2, LINC02967 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express GRHL2, LINC02967 (34) vs lines expressing them (14) | the lines without GRHL2, LINC02967: 1.28× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent genes |
| [[CLDN3]] | 0.5 µM | B | CLDN3 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express CLDN3 (28) vs lines expressing it (20) | the lines without CLDN3: 1.25× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[EPCAM]] | 0.5 µM | B | EPCAM activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 1.24× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[TMEM125]] | 0.5 µM | B | TMEM125 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express TMEM125 (33) vs lines expressing it (15) | the lines without TMEM125: 1.29× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[C1orf116]], [[IRF6]] | 0.5 µM | B | C1orf116, IRF6 activity lowers the cells' numbers under Apalutamide 0.5 µM (makes them more sensitive) | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (17) | the lines without C1orf116, IRF6: 1.28× the cells of the other lines | 0.038 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Apalutamide"
- `tables/drugdoses.parquet` — dd in 96, 97, 98
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

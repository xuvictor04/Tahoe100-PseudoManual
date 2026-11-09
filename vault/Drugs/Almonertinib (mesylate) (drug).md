---
drug: "Almonertinib (mesylate)"
type: "drug"
salt_base: "Almonertinib"
targets: "EGFR"
moa_fine: "EGFR/ERBB inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 94
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Almonertinib (mesylate)

*EGFR/ERBB inhibitor (inhibitor/antagonist) · targets: EGFR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 15 / 19 / 94; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.22 / 0.38.
> Flags by dose: - / - / plate-row cell shift.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:A11 | 10 / 5 | — | -0.22 | -0.8/-1.2/-1.4 | — |
| 0.5 µM | [[Plate 08]]:A11 | 11 / 8 | — | +1.18 | -0.2/-0.6/-0.3 | — |
| 5 µM | [[Plate 09]]:A11 | 76 / 18 | — | +1.32 | -1.4/-0.6/-0.3 | plate-row cell shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (10 genes, none with an alert): [[PTCD1]] 1.24× (z +3.9, 9/47 lines), [[NUMBL]] 1.22× (z +3.6, 10/47 lines), [[ENSG00000291228]] 1.35× (z +3.6, 9/46 lines), [[A1BG-AS1]] 1.42× (z +3.4, 1/25 lines), [[LINC01399]] 1.28× (z +3.3, 7/33 lines), [[NGF]] 1.45× (z +3.2, 1/17 lines), [[AP4S1]] 1.21× (z +3.2, 6/47 lines), [[ZNF696]] 1.28× (z +3.1, 2/45 lines), [[GCNT7]] 1.39× (z +3.1, 2/41 lines), [[RASGEF1C]] 1.26× (z +3.0, 2/32 lines)

**0.5 µM** (11 genes, none with an alert): [[7SK]] 2.99× (z +4.7, 48/49 lines), [[ENSG00000275993]] 1.68× (z +3.6, 3/38 lines), [[SLC6A8]] 1.32× (z +3.5, 10/44 lines), [[TCIRG1]] 1.30× (z +3.2, 6/43 lines), [[POM121C]] 1.20× (z +3.2, 20/49 lines), [[BAIAP2]] 1.27× (z +3.1, 9/48 lines), [[RAB11FIP5]] 1.27× (z +3.1, 13/48 lines), [[CCDC200]] 1.44× (z +3.0, 7/48 lines), [[ESYT2]] 1.20× (z +3.0, 23/49 lines), [[TP53BP2]] 1.21× (z +3.0, 11/49 lines), [[SNHG17]] 1.24× (z +2.9, 7/48 lines)

**5 µM** (76 genes, none with an alert; 12 shown): [[SCD]] 2.25× (z +11.0, 48/49 lines), [[ACSS2]] 1.82× (z +9.1, 36/48 lines), [[IDI1]] 1.71× (z +6.8, 39/49 lines), [[LPIN1]] 1.36× (z +6.6, 29/49 lines), [[FDPS]] 1.72× (z +6.5, 41/49 lines), [[DHCR7]] 1.90× (z +6.3, 31/44 lines), [[INSIG1]] 1.91× (z +6.1, 39/48 lines), [[HSD17B7]] 1.56× (z +5.9, 19/47 lines), [[ACAT2]] 1.50× (z +5.7, 29/48 lines), [[HMGCR]] 1.51× (z +5.7, 33/49 lines), [[MSMO1]] 1.73× (z +5.7, 36/48 lines), [[FDFT1]] 1.52× (z +5.5, 33/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[POLR2M]] 0.797× (z -3.7, 10/46 lines), [[ATP6AP1]] 0.800× (z -3.3, 13/47 lines), [[TSPAN6]] 0.742× (z -3.2, 9/43 lines), [[HTATIP2]] 0.761× (z -3.1, 12/40 lines), [[GPR146]] 0.777× (z -3.0, 7/45 lines)

**0.5 µM** (8 genes, none with an alert): [[UBE2Q1]] 0.792× (z -3.4, 18/48 lines), [[MTIF2]] 0.793× (z -3.4, 19/49 lines), [[LINC02864]] 0.776× (z -3.3, 0/12 lines), [[FGFRL1]] 0.748× (z -3.1, 4/47 lines), [[FAM149A]] 0.795× (z -3.1, 0/23 lines), [[PHYH]] 0.806× (z -3.0, 3/47 lines), [[LINC00467]] 0.819× (z -2.9, 5/48 lines), [[MIR4713HG]] 0.803× (z -2.9, 0/19 lines)

**5 µM** (18 genes, none with an alert; 12 shown): [[EIF2B3]] 0.801× (z -4.0, 15/48 lines), [[RFTN1]] 0.792× (z -3.8, 3/27 lines), [[MATN2]] 0.768× (z -3.7, 2/41 lines), [[VIM-AS1]] 0.777× (z -3.6, 2/41 lines), [[ENSG00000291003]] 0.747× (z -3.3, 5/46 lines), [[ALDH1A3]] 0.775× (z -3.2, 7/28 lines), [[ROR1]] 0.795× (z -3.2, 9/34 lines), [[PHF19]] 0.810× (z -3.2, 6/48 lines), [[LOXL1]] 0.774× (z -3.2, 4/30 lines), [[WDR76]] 0.802× (z -3.1, 6/46 lines), [[REXO5]] 0.778× (z -3.1, 7/47 lines), [[NT5M]] 0.789× (z -3.0, 2/40 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 086]] (+4.2) | [[Module 006]] (-3.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[H4 (line)]] (1.88), [[C32 (line)]] (1.83), [[HOP62 (line)]] (1.59), [[hTERT-HPNE (line)]] (1.55) · weakest: [[NCI-H661 (line)]] (0.332), [[SHP-77 (line)]] (0.432), [[BT-474 (line)]] (0.485) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Almonertinib (hydrochloride) (drug)]] (+0.67, EGFR/ERBB inhibitor); [[Terfenadine (drug)]] (+0.61, unclear); [[Osimertinib (mesylate) (drug)]] (+0.59, EGFR/ERBB inhibitor); [[Entrectinib (drug)]] (+0.58, Other TK inhibitor); [[Vandetanib (drug)]] (+0.57, Multi-TK inhibitor); [[Adagrasib (drug)]] (+0.55, RAS inhibitor); [[Berbamine (dihydrochloride) (drug)]] (+0.52, unclear); [[Posaconazole (drug)]] (+0.49, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 53 arrows, 53 of them with an alert ⚠; grade A 0, B 40, C 13. Shown: the 15 strongest; 38 more arrows (38 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[EPCAM]] | 5 µM | B | EPCAM activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 1.24× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[ESRP1]] | 5 µM | B | ESRP1 activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express ESRP1 (31) vs lines expressing it (17) | the lines without ESRP1: 1.25× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[ERBB3]] | 5 µM | B | ERBB3 activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express ERBB3 (27) vs lines expressing it (21) | the lines without ERBB3: 1.22× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[MYH14]] | 5 µM | B | MYH14 activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 1.24× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[TNNT2]] | 5 µM | B | TNNT2 activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express TNNT2 (29) vs lines expressing it (19) | the lines without TNNT2: 1.23× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[CLDN3]] | 5 µM | B | CLDN3 activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express CLDN3 (28) vs lines expressing it (20) | the lines without CLDN3: 1.22× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[EPHA1]] | 5 µM | B | EPHA1 activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express EPHA1 (23) vs lines expressing it (25) | the lines without EPHA1: 1.19× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[KDF1]] | 5 µM | B | KDF1 activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express KDF1 (30) vs lines expressing it (18) | the lines without KDF1: 1.24× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[CLDN7]] | 5 µM | B | CLDN7 activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express CLDN7 (30) vs lines expressing it (18) | the lines without CLDN7: 1.23× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: ESRP1, ENSG00000262302, ST14 |
| [[TRIM29]] | 5 µM | B | TRIM29 activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express TRIM29 (28) vs lines expressing it (20) | the lines without TRIM29: 1.21× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, TNNT2 |
| [[ENSG00000226281]] | 5 µM | B | ENSG00000226281 activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express ENSG00000226281 (25) vs lines expressing it (23) | the lines without ENSG00000226281: 1.21× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: TSPAN1, KIAA0040, ESRP1 |
| [[FAAH2]] | 5 µM | B | FAAH2 activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express FAAH2 (26) vs lines expressing it (22) | the lines without FAAH2: 1.24× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[AOX1]] | 5 µM | B | AOX1 activity raises the cells' numbers under Almonertinib (mesylate) 5 µM (protects the cells) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 0.82× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[ATP2C2]] | 5 µM | B | ATP2C2 activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express ATP2C2 (32) vs lines expressing it (16) | the lines without ATP2C2: 1.24× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[TSPAN1]] | 5 µM | B | TSPAN1 activity lowers the cells' numbers under Almonertinib (mesylate) 5 µM (makes them more sensitive) | lines that do not express TSPAN1 (26) vs lines expressing it (22) | the lines without TSPAN1: 1.20× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Almonertinib (mesylate)"
- `tables/drugdoses.parquet` — dd in 78, 79, 80
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

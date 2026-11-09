---
drug: "Berbamine (dihydrochloride)"
type: "drug"
salt_base: "Berbamine"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 64
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Berbamine (dihydrochloride)

*unclear (inhibitor/antagonist) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 7 / 64; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.54 / 0.53.
> Flags by dose: - / - / plate-row cell shift.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:A7 | 1 / 1 | — | -0.01 | -0.9/+0.1/-1.3 | — |
| 0.5 µM | [[Plate 08]]:A7 | 2 / 5 | — | +0.92 | -0.2/+0.7/-1.2 | — |
| 5 µM | [[Plate 09]]:A7 | 52 / 12 | — | +0.75 | -1.7/-0.3/-2.1 | plate-row cell shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[KCNRG]] 1.34× (z +3.1, 1/40 lines)

**0.5 µM** (2 genes, none with an alert): [[LANCL2]] 1.26× (z +3.3, 11/48 lines), [[CYTOR]] 1.23× (z +2.8, 14/47 lines)

**5 µM** (52 genes, none with an alert; 12 shown): [[SCD]] 1.91× (z +8.8, 47/48 lines), [[ACSS2]] 1.74× (z +8.5, 37/47 lines), [[LPIN1]] 1.36× (z +6.6, 28/48 lines), [[HMGCR]] 1.60× (z +6.6, 28/48 lines), [[DHCR7]] 1.94× (z +6.5, 27/44 lines), [[IDI1]] 1.64× (z +6.3, 36/47 lines), [[MVK]] 1.55× (z +5.8, 16/47 lines), [[HMGCS1]] 1.64× (z +5.8, 33/47 lines), [[FASN]] 1.82× (z +5.8, 34/46 lines), [[MSMO1]] 1.75× (z +5.7, 31/47 lines), [[CYP51A1]] 1.46× (z +5.7, 35/47 lines), [[HSD17B7]] 1.53× (z +5.7, 22/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[PSMG1]] 0.782× (z -3.7, 11/46 lines)

**0.5 µM** (5 genes, none with an alert): [[CD2BP2]] 0.786× (z -3.6, 5/48 lines), [[DRAM1]] 0.810× (z -3.5, 5/42 lines), [[NIBAN1]] 0.813× (z -3.4, 16/37 lines), [[HMGN2P46]] 0.779× (z -2.5, 2/30 lines), [[ENSG00000259354]] 0.804× (z -2.5, 2/31 lines)

**5 µM** (12 genes, none with an alert): [[MT-CO1]] 0.719× (z -3.7, 40/48 lines), [[ENSG00000288755]] 0.613× (z -3.5, 11/42 lines), [[TNFAIP3]] 0.717× (z -3.4, 20/45 lines), [[MT-ND4]] 0.705× (z -3.4, 38/48 lines), [[PPIF]] 0.725× (z -3.3, 13/48 lines), [[MCM4]] 0.761× (z -3.2, 12/45 lines), [[SDC1]] 0.763× (z -3.2, 9/38 lines), [[SERPINB9]] 0.813× (z -3.0, 7/24 lines), [[CSF2]] 0.501× (z -3.0, 8/20 lines), [[LINC00944]] 0.814× (z -3.0, 4/28 lines), [[PSMD14]] 0.815× (z -2.9, 19/48 lines), [[ALDH1A3]] 0.797× (z -2.8, 9/27 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 086]] (+4.0) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[LS 180 (line)]] (1.65), [[HEC-1-A (line)]] (1.61), [[HOP62 (line)]] (1.60), [[SNU-423 (line)]] (1.53) · weakest: [[SHP-77 (line)]] (0.203), [[HepG2_C3A (line)]] (0.318), [[RKO (line)]] (0.344) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Posaconazole (drug)]] (+0.53, unclear); [[Almonertinib (mesylate) (drug)]] (+0.52, EGFR/ERBB inhibitor); [[Crizotinib (hydrochloride) (drug)]] (+0.50, Multi-TK inhibitor); [[Fedratinib (hydrochloride hydrate) (drug)]] (+0.47, JAK/STAT inhibitor); [[Cepharanthine (drug)]] (+0.44, unclear); [[Almonertinib (hydrochloride) (drug)]] (+0.42, EGFR/ERBB inhibitor); [[Fulvestrant (drug)]] (+0.42, unclear, ⚠ only 8 significant genes); [[Triclosan (drug)]] (+0.41, unclear, ⚠ only 2 significant genes); [[HI-TOPK-032 (drug)]] (+0.40, unclear); [[Ritonavir (drug)]] (+0.39, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 151 arrows, 151 of them with an alert ⚠; grade A 0, B 149, C 2. Shown: the 15 strongest; 136 more arrows (136 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[FGFBP1]] | 0.5 µM | B | FGFBP1 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express FGFBP1 (36) vs lines expressing it (12) | the lines without FGFBP1: 1.24× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5 |
| [[HS3ST1]] | 0.5 µM | B | HS3ST1 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express HS3ST1 (31) vs lines expressing it (17) | the lines without HS3ST1: 1.23× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[OVOL1]], [[TMPRSS4]] | 0.5 µM | B | OVOL1, TMPRSS4 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express OVOL1, TMPRSS4 (33) vs lines expressing them (15) | the lines without OVOL1, TMPRSS4: 1.22× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: GRHL2, ST14, TMEM30B; co-absent genes |
| [[GJB3]] | 0.5 µM | B | GJB3 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express GJB3 (31) vs lines expressing it (17) | the lines without GJB3: 1.22× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[GRHL2]], [[LINC02967]] | 0.5 µM | B | GRHL2, LINC02967 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express GRHL2, LINC02967 (34) vs lines expressing them (14) | the lines without GRHL2, LINC02967: 1.22× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent genes |
| [[ST14]] | 0.5 µM | B | ST14 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ST14 (32) vs lines expressing it (16) | the lines without ST14: 1.21× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[C1orf116]], [[IRF6]] | 0.5 µM | B | C1orf116, IRF6 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (17) | the lines without C1orf116, IRF6: 1.21× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |
| [[TMEM125]] | 0.5 µM | B | TMEM125 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express TMEM125 (33) vs lines expressing it (15) | the lines without TMEM125: 1.21× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[ESRP1]] | 0.5 µM | B | ESRP1 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ESRP1 (31) vs lines expressing it (17) | the lines without ESRP1: 1.21× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[COL17A1]] | 0.5 µM | B | COL17A1 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express COL17A1 (34) vs lines expressing it (14) | the lines without COL17A1: 1.20× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1 |
| [[CLDN3]] | 0.5 µM | B | CLDN3 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express CLDN3 (28) vs lines expressing it (20) | the lines without CLDN3: 1.20× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[TMEM30B]] | 0.5 µM | B | TMEM30B activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express TMEM30B (35) vs lines expressing it (13) | the lines without TMEM30B: 1.20× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25 |
| [[SGPP2]] | 0.5 µM | B | SGPP2 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express SGPP2 (32) vs lines expressing it (16) | the lines without SGPP2: 1.20× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[ATP2C2]] | 0.5 µM | B | ATP2C2 activity lowers the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express ATP2C2 (32) vs lines expressing it (16) | the lines without ATP2C2: 1.19× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[TTC28]] | 0.5 µM | B | TTC28 activity raises the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express TTC28 (15) vs lines expressing it (33) | the lines without TTC28: 0.84× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SAMD11, RASSF8-AS1, AOX1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Berbamine (dihydrochloride)"
- `tables/drugdoses.parquet` — dd in 170, 171, 172
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

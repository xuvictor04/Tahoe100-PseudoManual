---
drug: "Belumosudil"
type: "drug"
salt_base: "Belumosudil"
targets: "ROCK2, ROCK1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 2394
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Belumosudil

*unclear (inhibitor/antagonist) · targets: ROCK2, ROCK1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 0 / 2394; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.26 / 0.18.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:B7 | 1 / 0 | — | +0.27 | +0.7/-0.1/+0.3 | — |
| 0.5 µM | [[Plate 08]]:B7 | 0 / 0 | — | +0.72 | +0.7/+0.5/+1.1 | — |
| 5 µM | [[Plate 09]]:B7 | 1,277 / 1,117 | — | -0.15 | +1.9/-1.6/+1.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[PPIA]] 1.31× (z +4.1, 27/48 lines)

**5 µM** (1277 genes, none with an alert; 12 shown): [[KLHL42]] 1.50× (z +8.8, 33/48 lines), [[DHX33]] 1.52× (z +8.7, 33/47 lines), [[TNFAIP3]] 2.31× (z +8.6, 38/45 lines), [[ADSS2]] 1.46× (z +8.5, 35/48 lines), [[RIOX2]] 1.61× (z +8.4, 32/47 lines), [[RBBP8]] 1.40× (z +8.2, 27/48 lines), [[DDX10]] 1.65× (z +8.2, 44/48 lines), [[AKAP1]] 1.49× (z +8.2, 28/47 lines), [[GNG2]] 1.80× (z +8.0, 18/26 lines), [[DPH6]] 2.06× (z +8.0, 41/47 lines), [[RRP1]] 1.68× (z +8.0, 28/45 lines), [[ENSG00000237773]] 1.81× (z +7.9, 25/40 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (1117 genes, none with an alert; 12 shown): [[TXNIP]] 0.205× (z -19.8, 37/37 lines), [[ARRDC4]] 0.395× (z -13.9, 35/40 lines), [[GPR155]] 0.529× (z -9.1, 28/42 lines), [[DCAF6]] 0.691× (z -8.9, 43/48 lines), [[SOS1]] 0.751× (z -8.6, 32/48 lines), [[ENSG00000254732]] 0.516× (z -8.4, 30/46 lines), [[KIAA1958]] 0.751× (z -8.4, 32/48 lines), [[TMEM263]] 0.621× (z -7.9, 40/48 lines), [[EIF2AK3]] 0.532× (z -7.9, 37/48 lines), [[RAB6A]] 0.685× (z -7.9, 40/48 lines), [[SLC2A1-DT]] 0.618× (z -7.9, 28/45 lines), [[ENSG00000236255]] 0.529× (z -7.8, 34/46 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 137]] (+5.9), [[Module 001]] (+5.4), [[Module 004]] (+5.4) | [[Module 207]] (-7.0), [[Module 179]] (-7.0), [[Module 041]] (-4.6) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[MIA PaCa-2 (line)]] (-10.2), [[LoVo (line)]] (-8.5), [[NCI-H23 (line)]] (-6.9), [[NCI-H1573 (line)]] (-6.7), [[RKO (line)]] (-6.1) | [[NCI-H1792 (line)]] (1.72), [[NCI-H1573 (line)]] (1.54), [[HS-578T (line)]] (1.39), [[SNU-423 (line)]] (1.37) · weakest: [[SW1417 (line)]] (0.237), [[NCI-H661 (line)]] (0.570), [[A-427 (line)]] (0.582) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Pralsetinib (drug)]] (+0.80, Other TK inhibitor); [[Brimonidine (drug)]] (+0.60, Adrenoceptor agonist); [[Abiraterone acetate (drug)]] (+0.59, unclear); [[Finasteride (drug)]] (+0.58, unclear); [[Meloxicam (drug)]] (+0.56, Cyclooxygenase inhibitor); [[Larotrectinib sulfate (drug)]] (+0.56, Other TK inhibitor, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Benztropine (mesylate) (drug)]] (+0.56, unclear); [[Esmolol (hydrochloride) (drug)]] (+0.54, unclear); [[Palmatine (chloride) (drug)]] (+0.53, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000239462]] | 5 µM | B | ENSG00000239462 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express ENSG00000239462 (18) vs lines expressing it (30) | the lines without ENSG00000239462: 0.62× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LINC00973, IGFBP7, ITGA1 |
| [[PIWIL4]] | 5 µM | B | PIWIL4 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express PIWIL4 (11) vs lines expressing it (37) | the lines without PIWIL4: 0.68× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: FUT4, CTSZ, ARHGAP23 |
| [[COL7A1]] | 5 µM | B | COL7A1 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express COL7A1 (24) vs lines expressing it (24) | the lines without COL7A1: 0.64× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[ARHGDIB]] | 5 µM | B | ARHGDIB activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express ARHGDIB (23) vs lines expressing it (25) | the lines without ARHGDIB: 0.65× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: CD74, MILR1, CACNA2D4 |
| [[KLKP1-1]] | 5 µM | B | KLKP1-1 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express KLKP1-1 (11) vs lines expressing it (37) | the lines without KLKP1-1: 0.52× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[MILR1]] | 5 µM | B | MILR1 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express MILR1 (19) vs lines expressing it (29) | the lines without MILR1: 0.61× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[MSI1]] | 5 µM | B | MSI1 activity lowers the cells' numbers under Belumosudil 5 µM (makes them more sensitive) | lines that do not express MSI1 (26) vs lines expressing it (22) | the lines without MSI1: 1.57× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[ADAM19]] | 5 µM | B | ADAM19 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express ADAM19 (13) vs lines expressing it (35) | the lines without ADAM19: 0.62× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[LMO7]] | 5 µM | B | LMO7 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express LMO7 (11) vs lines expressing it (37) | the lines without LMO7: 0.63× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: LMO7DN, KITLG, TLE4; maybe low, not absent |
| [[ARHGAP23]] | 5 µM | B | ARHGAP23 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express ARHGAP23 (12) vs lines expressing it (36) | the lines without ARHGAP23: 0.60× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, PIWIL4, KLKP1-1; maybe low, not absent |
| [[SLC43A3]] | 5 µM | B | SLC43A3 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express SLC43A3 (28) vs lines expressing it (20) | the lines without SLC43A3: 0.71× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, FN1, ENSG00000234261 |
| [[DCBLD2]] | 5 µM | B | DCBLD2 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express DCBLD2 (9) vs lines expressing it (39) | the lines without DCBLD2: 0.58× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: C12orf75, ST3GAL6, OSBPL6; maybe low, not absent |
| [[ENSG00000253496]] | 5 µM | B | ENSG00000253496 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express ENSG00000253496 (13) vs lines expressing it (35) | the lines without ENSG00000253496: 0.68× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: LINC01807, TUSC3, HSPA2; maybe low, not absent |
| [[IL15]] | 5 µM | B | IL15 activity raises the cells' numbers under Belumosudil 5 µM (protects the cells) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 0.64× the cells of the other lines | 0.0996 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Belumosudil"
- `tables/drugdoses.parquet` — dd in 147, 148, 149
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

---
drug: "Clobetasol propionate"
type: "drug"
salt_base: "Clobetasol propionate"
targets: "CYP3A5,CYP3A4"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 1512
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Clobetasol propionate

*unclear (inhibitor/antagonist) · targets: CYP3A5,CYP3A4 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1512 / 843 / 612; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.79 / 0.62.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:G1 | 1,048 / 464 | — | -0.39 | +1.1/-1.5/-1.8 | — |
| 0.5 µM | [[Plate 11]]:G1 | 505 / 338 | — | -0.40 | -0.0/-1.2/-2.7 | — |
| 5 µM | [[Plate 12]]:G1 | 198 / 414 | — | -0.16 | +0.7/-0.6/-2.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1048 genes, 16 with an alert ⚠; 14 shown): [[FKBP5]] ⚠ 13.9× (z +39.7, 39/41 lines; position correction uncertain), [[CCND3]] 3.88× (z +18.5, 42/46 lines), [[KLF9]] 2.79× (z +17.3, 33/43 lines), [[MAOA]] ⚠ 3.17× (z +15.9, 22/33 lines; position correction uncertain), [[NNMT]] 4.14× (z +13.0, 22/23 lines), [[PID1]] 2.49× (z +12.8, 24/26 lines), [[TSC22D3]] 4.44× (z +12.5, 28/35 lines), [[ABLIM3]] 2.17× (z +11.1, 23/33 lines), [[LDLRAD3]] 1.79× (z +10.7, 30/40 lines), [[ABLIM2]] 2.29× (z +10.7, 23/33 lines), [[IRAK3]] 2.65× (z +10.7, 12/12 lines), [[SAA1]] 9.70× (z +10.3, 16/19 lines), [[JPH2]] 2.39× (z +10.2, 18/27 lines), [[ITGA10]] 2.99× (z +10.2, 24/35 lines)

**0.5 µM** (505 genes, 13 with an alert ⚠; 14 shown): [[FKBP5]] ⚠ 13.3× (z +39.1, 39/41 lines; position correction uncertain), [[KLF9]] 2.64× (z +16.3, 32/43 lines), [[MAOA]] ⚠ 2.87× (z +14.5, 18/33 lines; position correction uncertain), [[CCND3]] 2.89× (z +14.4, 31/46 lines), [[FGD4]] 1.77× (z +11.8, 24/38 lines), [[NNMT]] 3.65× (z +11.8, 23/23 lines), [[TSC22D3]] 4.01× (z +11.6, 28/35 lines), [[ITGA10]] 3.44× (z +11.5, 22/33 lines), [[PID1]] 2.19× (z +11.0, 20/26 lines), [[IRAK3]] 2.67× (z +10.7, 11/12 lines), [[LDLRAD3]] 1.77× (z +10.5, 27/40 lines), [[ABLIM3]] 2.05× (z +10.3, 23/33 lines), [[JPH2]] 2.37× (z +10.1, 19/27 lines), [[ADAMTS9]] 1.93× (z +9.5, 19/29 lines)

**5 µM** (198 genes, 9 with an alert ⚠; 15 shown): [[FKBP5]] ⚠ 12.3× (z +37.8, 33/41 lines; position correction uncertain), [[CCND3]] 3.46× (z +16.9, 31/47 lines), [[KLF9]] 2.52× (z +15.5, 32/43 lines), [[ABLIM3]] 2.39× (z +12.5, 22/33 lines), [[MAOA]] ⚠ 2.34× (z +11.7, 19/34 lines; position correction uncertain), [[TSC22D3]] 3.88× (z +11.4, 27/37 lines), [[NNMT]] 2.95× (z +9.9, 19/24 lines), [[ADAMTS9]] 1.94× (z +9.6, 20/29 lines), [[ACSL1]] ⚠ 1.74× (z +9.3, 28/46 lines; position correction uncertain), [[LDLRAD3]] 1.61× (z +8.8, 27/41 lines), [[PID1]] 1.77× (z +8.0, 19/26 lines), [[ABLIM2]] 1.84× (z +7.9, 13/34 lines), [[ABCG1]] 2.08× (z +7.9, 27/33 lines), [[ITGA10]] 2.29× (z +7.7, 22/37 lines), [[JPH2]] 1.90× (z +7.5, 19/29 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (464 genes, 8 with an alert ⚠; 13 shown): [[ADAMTS16]] 0.571× (z -9.4, 19/23 lines), [[DTNA]] ⚠ 0.532× (z -8.7, 24/26 lines; position correction uncertain), [[AFF3]] 0.565× (z -8.5, 18/26 lines), [[PDGFB]] 0.448× (z -8.3, 24/31 lines), [[PTHLH]] 0.442× (z -8.2, 18/25 lines), [[ENSG00000239462]] 0.523× (z -8.1, 21/28 lines), [[PKIA]] 0.639× (z -7.7, 19/25 lines), [[WNT7B]] 0.557× (z -7.7, 18/27 lines), [[HMGN2P46]] 0.480× (z -7.5, 23/30 lines), [[LIF]] 0.526× (z -7.5, 24/38 lines), [[FAM107B]] 0.704× (z -7.5, 27/37 lines), [[LOXL2]] 0.655× (z -7.3, 24/30 lines), [[UBA6]] 0.627× (z -6.8, 43/48 lines)

**0.5 µM** (338 genes, 6 with an alert ⚠; 12 shown): [[FAM107B]] 0.623× (z -9.1, 22/37 lines), [[ADAMTS16]] 0.597× (z -8.7, 18/23 lines), [[PTHLH]] 0.454× (z -7.9, 21/25 lines), [[HMGN2P46]] 0.462× (z -7.9, 23/30 lines), [[ENSG00000259354]] 0.512× (z -7.8, 25/30 lines), [[BMP2]] 0.552× (z -7.6, 15/25 lines), [[SYNJ2]] 0.724× (z -7.1, 26/44 lines), [[PKIA]] 0.670× (z -6.9, 19/25 lines), [[LRRC49]] 0.718× (z -6.7, 22/37 lines), [[CD44]] 0.714× (z -6.7, 27/33 lines), [[GJA1]] 0.605× (z -6.6, 17/22 lines), [[IFFO2]] 0.700× (z -6.6, 19/47 lines)

**5 µM** (414 genes, 9 with an alert ⚠; 13 shown): [[ENSG00000259354]] 0.403× (z -10.7, 28/30 lines), [[PTHLH]] 0.375× (z -9.9, 21/26 lines), [[AFF3]] 0.523× (z -9.6, 18/26 lines), [[HMGN2P46]] 0.399× (z -9.4, 25/30 lines), [[ADAMTS16]] 0.590× (z -8.9, 16/23 lines), [[BMP2]] 0.527× (z -8.2, 19/27 lines), [[PKIA]] 0.631× (z -7.9, 18/26 lines), [[KCNMA1]] ⚠ 0.667× (z -7.8, 18/22 lines; position correction uncertain), [[SYNJ2]] 0.705× (z -7.7, 27/44 lines), [[WNT7B]] 0.564× (z -7.5, 17/28 lines), [[GBP4]] 0.452× (z -7.4, 21/28 lines), [[GJA1]] 0.598× (z -6.7, 17/22 lines), [[FAM107B]] 0.731× (z -6.7, 22/37 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 098]] (+6.4), [[Module 104]] (+4.3), [[Module 097]] (+4.0) | [[Module 179]] (-3.3), [[Module 224]] (-3.1), [[Module 112]] (-2.9) |
| 0.5 µM | [[Module 098]] (+5.9), [[Module 097]] (+4.1), [[Module 104]] (+3.9) | [[Module 112]] (-3.9), [[Module 224]] (-2.9), [[Module 081]] (-2.7) |
| 5 µM | [[Module 098]] (+4.6), [[Module 097]] (+3.3), [[Module 217]] (+2.9) | [[Module 112]] (-4.0), [[Module 081]] (-2.8), [[Module 184]] (-2.8) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[HOP62 (line)]] (1.81), [[H4 (line)]] (1.70), [[HS-578T (line)]] (1.63), [[A549 (line)]] (1.60) · weakest: [[KATO III (line)]] (0.376), [[NCI-H23 (line)]] (0.449), [[A-427 (line)]] (0.455) |
| 0.5 µM | — | [[HOP62 (line)]] (1.97), [[H4 (line)]] (1.97), [[NCI-H1792 (line)]] (1.83), [[HS-578T (line)]] (1.76) · weakest: [[KATO III (line)]] (0.285), [[SW1417 (line)]] (0.306), [[A-427 (line)]] (0.312) |
| 5 µM | — | [[H4 (line)]] (2.27), [[HOP62 (line)]] (2.09), [[NCI-H1792 (line)]] (1.92), [[HS-578T (line)]] (1.82) · weakest: [[SW1417 (line)]] (0.377), [[COLO 205 (line)]] (0.420), [[SW480 (line)]] (0.426) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Phenylephrine (hydrochloride) (drug)]] (+0.70, Adrenoceptor agonist); [[Citalopram (hydrobromide) (drug)]] (+0.70, unclear); [[Econazole (drug)]] (+0.62, unclear); [[Triamcinolone (drug)]] (+0.60, Glucocorticoid receptor agonist); [[Betamethasone dipropionate (drug)]] (+0.57, Glucocorticoid receptor agonist); [[Budesonide (drug)]] (+0.56, Glucocorticoid receptor agonist); [[Benztropine (mesylate) (drug)]] (+0.50, unclear); [[Abiraterone acetate (drug)]] (+0.48, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ANKRD18CP]] | 0.5 µM | B | ANKRD18CP activity raises the cells' numbers under Clobetasol propionate 0.5 µM (protects the cells) | lines that do not express ANKRD18CP (6) vs lines expressing it (42) | the lines without ANKRD18CP: 0.80× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: ZFHX2; maybe low, not absent |
| [[ALDH3B1]] | 0.5 µM | B | ALDH3B1 activity lowers the cells' numbers under Clobetasol propionate 0.5 µM (makes them more sensitive) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 1.23× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Clobetasol propionate"
- `tables/drugdoses.parquet` — dd in 272, 273, 274
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

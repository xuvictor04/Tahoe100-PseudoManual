---
drug: "Celecoxib"
type: "drug"
salt_base: "Celecoxib"
targets: "PTGS2"
moa_fine: "Cyclooxygenase inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 233
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Celecoxib

*Cyclooxygenase inhibitor (inhibitor/antagonist) · targets: PTGS2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 233 / 0; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.19 / 0.77.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:G11 | 1 / 0 | — | -0.52 | +0.2/-0.2/-1.0 | — |
| 0.5 µM | [[Plate 02]]:G11 | 177 / 56 | — | -0.85 | +1.3/-0.1/+1.2 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:G11 | 0 / 0 | — | -0.04 | +1.7/+0.4/+0.3 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[LINC01151]] 1.38× (z +3.1, 1/26 lines)

**0.5 µM** (177 genes, none with an alert; 12 shown): [[FHIP2B]] 1.57× (z +4.5, 17/47 lines), [[HNRNPH1]] 1.61× (z +4.3, 48/49 lines), [[KIFC2]] 2.17× (z +4.1, 15/44 lines), [[HOXB2]] 2.08× (z +4.1, 5/21 lines), [[SERINC2]] 1.43× (z +4.1, 10/42 lines), [[ENO3]] 1.78× (z +4.1, 6/39 lines), [[POLR2F]] 1.60× (z +4.1, 24/48 lines), [[SEMA4C]] 1.82× (z +4.0, 13/43 lines), [[ASB16-AS1]] 1.66× (z +4.0, 13/46 lines), [[FHOD1]] 1.59× (z +4.0, 8/45 lines), [[HES7]] 1.95× (z +3.9, 9/30 lines), [[LSM7]] 2.06× (z +3.9, 32/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (56 genes, none with an alert; 12 shown): [[SETD2]] 0.801× (z -5.1, 26/49 lines), [[TWF1]] 0.597× (z -4.8, 39/48 lines), [[TMEM106B]] 0.698× (z -4.7, 27/49 lines), [[MT-RNR1]] 0.356× (z -4.3, 49/49 lines), [[RTF2]] 0.828× (z -4.3, 13/49 lines), [[MINPP1]] 0.682× (z -4.0, 12/46 lines), [[ZBTB41]] 0.775× (z -3.9, 22/49 lines), [[LRPPRC]] 0.725× (z -3.9, 38/49 lines), [[CUL4B]] 0.710× (z -3.9, 31/48 lines), [[STK26]] 0.756× (z -3.9, 13/42 lines), [[FASTKD2]] 0.767× (z -3.9, 18/48 lines), [[GMFB]] 0.720× (z -3.8, 21/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 002]] (+2.6), [[Module 024]] (+2.5), [[Module 160]] (+2.3) | [[Module 025]] (-3.1), [[Module 029]] (-3.1), [[Module 020]] (-2.6) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[HOP62 (line)]] (-3.9), [[SNU-423 (line)]] (-3.5), [[PANC-1 (line)]] (-3.2), [[J82 (line)]] (-3.2) | — |
| 0.5 µM | [[LS 180 (line)]] (-4.0), [[RPMI-7951 (line)]] (-3.4), [[AsPC-1 (line)]] (-3.3), [[C32 (line)]] (-3.3), [[LoVo (line)]] (-3.2) | [[SW 1088 (line)]] (1.27), [[C32 (line)]] (1.08), [[LS 180 (line)]] (1.06), [[AsPC-1 (line)]] (1.06) · weakest: [[AN3 CA (line)]] (0.769), [[C-33 A (line)]] (0.784), [[RPMI-7951 (line)]] (0.797) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Methylprednisolone succinate (drug)]] (+0.93, Glucocorticoid receptor agonist); [[Ipatasertib (drug)]] (+0.89, PI3K/AKT inhibitor); [[Nimesulide (drug)]] (+0.83, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Darolutamide (drug)]] (+0.82, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Thymol (drug)]] (+0.81, unclear); [[Bimatoprost (drug)]] (+0.79, unclear); [[Bergenin (drug)]] (+0.78, unclear); [[9-ING-41 (drug)]] (+0.76, GSK3 inhibitor); [[Erythromycin (drug)]] (+0.74, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.72, Glucose transporter inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 31 arrows, 31 of them with an alert ⚠; grade A 0, B 20, C 11. Shown: the 15 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ATP1B1]] | 0.5 µM | B | ATP1B1 activity lowers the cells' numbers under Celecoxib 0.5 µM (makes them more sensitive) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 1.39× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[LGALS3BP]] | 0.5 µM | B | LGALS3BP activity lowers the cells' numbers under Celecoxib 0.5 µM (makes them more sensitive) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 1.51× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[IL15]] | 0.5 µM | B | IL15 activity lowers the cells' numbers under Celecoxib 0.5 µM (makes them more sensitive) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 1.39× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[SPTLC3]] | 0.5 µM | B | SPTLC3 activity lowers the cells' numbers under Celecoxib 0.5 µM (makes them more sensitive) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 1.29× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[ALDH3B1]] | 0.5 µM | B | ALDH3B1 activity lowers the cells' numbers under Celecoxib 0.5 µM (makes them more sensitive) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 1.36× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[CEMIP]] | 0.5 µM | B | CEMIP activity lowers the cells' numbers under Celecoxib 0.5 µM (makes them more sensitive) | lines that do not express CEMIP (19) vs lines expressing it (29) | the lines without CEMIP: 1.29× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4 |
| [[LGALS3BP]] | 5 µM | B | LGALS3BP activity lowers the cells' numbers under Celecoxib 5 µM (makes them more sensitive) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 1.34× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[KLRK1-AS1]] | 0.05 µM | B | KLRK1-AS1 activity raises the cells' numbers under Celecoxib 0.05 µM (protects the cells) | lines that do not express KLRK1-AS1 (11) vs lines expressing it (37) | the lines without KLRK1-AS1: 0.92× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| [[AHR]] | 0.5 µM | B | AHR activity lowers the cells' numbers under Celecoxib 0.5 µM (makes them more sensitive) | lines that do not express AHR (7) vs lines expressing it (41) | the lines without AHR: 1.35× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[SERPINE2]] | 0.5 µM | B | SERPINE2 activity lowers the cells' numbers under Celecoxib 0.5 µM (makes them more sensitive) | lines that do not express SERPINE2 (21) vs lines expressing it (27) | the lines without SERPINE2: 1.23× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[ATP1B1]] | 5 µM | B | ATP1B1 activity lowers the cells' numbers under Celecoxib 5 µM (makes them more sensitive) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 1.28× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[APOL6]] | 0.05 µM | B | APOL6 activity raises the cells' numbers under Celecoxib 0.05 µM (protects the cells) | lines that do not express APOL6 (6) vs lines expressing it (42) | the lines without APOL6: 0.79× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |
| [[IGSF9]] | 0.5 µM | B | IGSF9 activity lowers the cells' numbers under Celecoxib 0.5 µM (makes them more sensitive) | lines that do not express IGSF9 (16) vs lines expressing it (32) | the lines without IGSF9: 1.31× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[MGC32805]] | 0.05 µM | B | MGC32805 activity raises the cells' numbers under Celecoxib 0.05 µM (protects the cells) | lines that do not express MGC32805 (32) vs lines expressing it (16) | the lines without MGC32805: 0.83× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: CEACAM5, ST18, PRR15L; maybe low, not absent |
| [[KHDRBS3]] | 0.5 µM | B | KHDRBS3 activity lowers the cells' numbers under Celecoxib 0.5 µM (makes them more sensitive) | lines that do not express KHDRBS3 (11) vs lines expressing it (37) | the lines without KHDRBS3: 1.22× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: AHR, STC2 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Celecoxib"
- `tables/drugdoses.parquet` — dd in 251, 252, 253
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

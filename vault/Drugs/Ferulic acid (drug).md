---
drug: "Ferulic acid"
type: "drug"
salt_base: "Ferulic acid"
targets: "FGFR1, FGFR2"
moa_fine: "Other TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 39
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Ferulic acid

*Other TK inhibitor (inhibitor/antagonist) · targets: FGFR1, FGFR2 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 6 / 39 / 4; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.14 / 0.41.
> Flags by dose: - / low cells (technical?) / -.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:F7 | 3 / 3 | — | +0.13 | -0.3/+0.4/+0.3 | — |
| 0.5 µM | [[Plate 08]]:F7 | 32 / 7 | — | -1.21 | -1.0/-0.8/-0.8 | low cells (technical?) |
| 5 µM | [[Plate 09]]:F7 | 3 / 1 | — | -0.25 | +0.1/-0.3/+0.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[PODXL]] 1.25× (z +3.4, 7/23 lines), [[LAMC2]] 1.30× (z +3.2, 9/21 lines), [[RARB]] 1.22× (z +2.9, 2/20 lines)

**0.5 µM** (32 genes, none with an alert; 12 shown): [[CNN3-DT]] 1.54× (z +4.2, 3/33 lines), [[ENSG00000286608]] 1.50× (z +4.2, 7/45 lines), [[DLGAP1-AS2]] 1.29× (z +4.1, 13/45 lines), [[ARHGAP31]] 1.36× (z +3.9, 16/37 lines), [[HAGLR]] 1.42× (z +3.7, 3/25 lines), [[LINC01232]] 1.50× (z +3.6, 5/29 lines), [[ENSG00000236212]] 1.54× (z +3.6, 8/23 lines), [[ITGB3]] 1.43× (z +3.5, 13/22 lines), [[ARNT2]] 1.26× (z +3.5, 4/25 lines), [[VSTM4]] 1.53× (z +3.5, 5/16 lines), [[BDKRB2]] 1.31× (z +3.4, 5/29 lines), [[ENSG00000257027]] 1.41× (z +3.3, 3/32 lines)

**5 µM** (3 genes, none with an alert): [[PRXL2B]] 1.36× (z +3.5, 3/43 lines), [[TENM2]] 1.29× (z +3.2, 4/14 lines), [[LMX1B]] 1.29× (z +2.9, 0/23 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[GCNT1]] 0.798× (z -3.8, 14/42 lines), [[RUNDC3A-AS1]] 0.734× (z -3.4, 8/32 lines), [[ENSG00000288710]] 0.695× (z -3.3, 8/41 lines)

**0.5 µM** (7 genes, none with an alert): [[HNRNPA1L3]] 0.671× (z -4.6, 13/45 lines), [[PTPRO]] 0.741× (z -3.5, 7/42 lines), [[IDI2-AS1]] 0.695× (z -3.4, 12/45 lines), [[PTGER4]] 0.767× (z -3.3, 7/34 lines), [[LINC01322]] 0.759× (z -3.1, 0/13 lines), [[FAAP24]] 0.674× (z -3.1, 11/43 lines), [[KCNJ14]] 0.772× (z -3.0, 12/46 lines)

**5 µM** (1 gene, none with an alert): [[FKBP9P1-1]] 0.676× (z -3.1, 6/15 lines)

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
| 0.5 µM | [[HOP62 (line)]] (-4.3), [[HS-578T (line)]] (-4.0), [[A498 (line)]] (-3.6), [[SNU-423 (line)]] (-3.3), [[Hs 766T (line)]] (-3.3) | [[AN3 CA (line)]] (1.60), [[SNU-423 (line)]] (1.54), [[NCI-H661 (line)]] (1.22), [[HS-578T (line)]] (1.21) · weakest: [[LS 180 (line)]] (0.165), [[NCI-H2347 (line)]] (0.210), [[HT-29 (line)]] (0.234) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Imiquimod (maleate) (drug)]] (+0.66, unclear); [[Pemetrexed (drug)]] (+0.60, DNA synthesis/repair inhibitor); [[Adenine (drug)]] (+0.58, unclear); [[OTS514 (drug)]] (+0.55, Other MAPK inhibitor); [[Torkinib (drug)]] (+0.54, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Docetaxel (drug)]] (+0.53, Microtubule inhibitor, ⚠ vector dose flagged: transcription drop; cell-cycle shift); [[Mozavaptan (drug)]] (+0.51, unclear); [[Fluvoxamine (drug)]] (+0.49, unclear); [[Folic acid (drug)]] (+0.45, unclear); [[Lidocaine (hydrochloride) (drug)]] (+0.45, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 15 arrows, 15 of them with an alert ⚠; grade A 0, B 9, C 6.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SRPX]] | 0.5 µM | B | SRPX activity lowers the cells' numbers under Ferulic acid 0.5 µM (makes them more sensitive) | lines that do not express SRPX (22) vs lines expressing it (26) | the lines without SRPX: 1.30× the cells of the other lines | 0.067 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[AOX1]] | 0.5 µM | B | AOX1 activity lowers the cells' numbers under Ferulic acid 0.5 µM (makes them more sensitive) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 1.34× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[ENSG00000230647]] | 0.5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Ferulic acid 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.35× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[KCNMA1]] | 0.5 µM | B | KCNMA1 activity lowers the cells' numbers under Ferulic acid 0.5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.41× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[EPCAM]] | 0.5 µM | B | EPCAM activity raises the cells' numbers under Ferulic acid 0.5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.74× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[ENSG00000230615]] | 0.5 µM | B | ENSG00000230615 activity lowers the cells' numbers under Ferulic acid 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 1.41× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[SSPN]] | 0.5 µM | B | SSPN activity lowers the cells' numbers under Ferulic acid 0.5 µM (makes them more sensitive) | lines that do not express SSPN (15) vs lines expressing it (33) | the lines without SSPN: 1.31× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Ferulic acid 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.71× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[SPOCK1]] | 0.5 µM | B | SPOCK1 activity lowers the cells' numbers under Ferulic acid 0.5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.42× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[PWWP2B]] | 0.5 µM | C | PWWP2B activity raises the cells' numbers under Ferulic acid 0.5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.53× the cells of the other lines | 0.010 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| [[FIGN]] | 0.5 µM | C | FIGN activity lowers the cells' numbers under Ferulic acid 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.29× the cells of the other lines | 0.034 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[C2orf74]] | 0.5 µM | C | C2orf74 activity lowers the cells' numbers under Ferulic acid 0.5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.31× the cells of the other lines | 0.055 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[RAB11FIP1]] | 0.5 µM | C | RAB11FIP1 activity raises the cells' numbers under Ferulic acid 0.5 µM (protects the cells) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 0.60× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| [[ZC3HAV1L]] | 0.5 µM | C | ZC3HAV1L activity raises the cells' numbers under Ferulic acid 0.5 µM (protects the cells) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 0.69× the cells of the other lines | 0.057 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| [[NR3C1]] | 0.5 µM | C | NR3C1 activity lowers the cells' numbers under Ferulic acid 0.5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.31× the cells of the other lines | 0.070 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Ferulic acid"
- `tables/drugdoses.parquet` — dd in 444, 445, 446
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

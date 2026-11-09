---
drug: "Naproxen"
type: "drug"
salt_base: "Naproxen"
targets: "PTGS1, PTGS2"
moa_fine: "Cyclooxygenase inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 45
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Naproxen

*Cyclooxygenase inhibitor (inhibitor/antagonist) · targets: PTGS1, PTGS2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 45 / 10 / 27; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.10 / 0.40.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:B12 | 40 / 5 | — | -0.74 | -0.2/+0.1/-0.5 | — |
| 0.5 µM | [[Plate 08]]:B12 | 6 / 4 | — | +0.66 | +0.6/+0.4/+0.1 | — |
| 5 µM | [[Plate 09]]:B12 | 11 / 16 | — | -0.26 | +1.1/+1.8/+0.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (40 genes, none with an alert; 12 shown): [[TMEM255B]] 1.58× (z +4.2, 11/27 lines), [[PPIEL-1]] 1.54× (z +3.9, 15/42 lines), [[ENSG00000289997]] 1.46× (z +3.8, 9/39 lines), [[ENSG00000287721]] 1.68× (z +3.7, 8/27 lines), [[NOSTRIN]] 1.32× (z +3.6, 5/27 lines), [[GALNT8]] 1.46× (z +3.5, 2/12 lines), [[RFPL3S]] 1.53× (z +3.5, 6/33 lines), [[ENSG00000287975]] 1.57× (z +3.5, 7/30 lines), [[PHEX]] 1.40× (z +3.4, 8/42 lines), [[ENSG00000286652]] 1.51× (z +3.4, 1/23 lines), [[TRHDE]] 1.30× (z +3.4, 2/18 lines), [[ARHGAP22]] 1.30× (z +3.3, 10/27 lines)

**0.5 µM** (6 genes, none with an alert): [[EXTL2]] 1.24× (z +3.4, 7/48 lines), [[ARSG]] 1.26× (z +3.3, 7/42 lines), [[ARHGAP22]] 1.26× (z +3.2, 11/27 lines), [[SH3TC2]] 1.38× (z +3.1, 10/27 lines), [[SOWAHC]] 1.24× (z +3.1, 8/46 lines), [[LPCAT4]] 1.22× (z +3.0, 3/47 lines)

**5 µM** (11 genes, none with an alert): [[TSHZ3]] 1.23× (z +3.6, 4/23 lines), [[LPCAT4]] 1.26× (z +3.4, 10/46 lines), [[NLRP1]] 1.23× (z +3.3, 4/27 lines), [[ADAMTSL4-AS2]] 1.49× (z +3.2, 9/43 lines), [[SPRY2]] 1.22× (z +3.1, 5/44 lines), [[AZU1]] 1.59× (z +3.0, 4/24 lines), [[ADGRL4]] 1.43× (z +2.9, 3/24 lines), [[ATP6V0D2]] 1.47× (z +2.9, 3/24 lines), [[PIK3CD]] 1.20× (z +2.9, 1/37 lines), [[SOWAHC]] 1.23× (z +2.9, 12/45 lines), [[SUSD4]] 1.39× (z +2.7, 1/21 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, 1 with an alert ⚠): [[FZD3]] 0.826× (z -3.8, 12/37 lines), [[LRIG3]] 0.763× (z -3.4, 11/40 lines), [[PRUNE1]] 0.802× (z -3.2, 12/43 lines), [[DRAM1]] 0.824× (z -3.0, 13/41 lines), [[PAQR5]] ⚠ 0.825× (z -2.9, 10/36 lines; position correction uncertain)

**0.5 µM** (4 genes, none with an alert): [[B3GNT4]] 0.664× (z -3.6, 6/44 lines), [[CSTF3-DT]] 0.714× (z -3.5, 4/45 lines), [[PSD2]] 0.668× (z -3.2, 4/30 lines), [[PYM1]] 0.810× (z -3.1, 3/47 lines)

**5 µM** (16 genes, none with an alert; 12 shown): [[AJUBA]] 0.714× (z -4.2, 11/44 lines), [[LPCAT3]] 0.803× (z -4.0, 22/47 lines), [[DRAM1]] 0.784× (z -3.9, 14/42 lines), [[HCN3]] 0.673× (z -3.9, 7/35 lines), [[RAB15]] 0.736× (z -3.9, 12/43 lines), [[PKNOX2]] 0.664× (z -3.9, 5/19 lines), [[KANSL1L]] 0.833× (z -3.5, 18/48 lines), [[LINC02889]] 0.697× (z -3.5, 3/27 lines), [[DYNLL2]] 0.829× (z -3.4, 9/47 lines), [[CHDH]] 0.726× (z -3.4, 4/23 lines), [[HSD17B7P2]] 0.661× (z -3.4, 6/33 lines), [[LINC00705]] 0.733× (z -3.4, 8/28 lines)

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
| 0.05 µM | — | [[CHP-212 (line)]] (2.25), [[SW 1271 (line)]] (1.34), [[C-33 A (line)]] (1.28), [[AN3 CA (line)]] (1.25) · weakest: [[NCI-H2347 (line)]] (-0.0351), [[HT-29 (line)]] (0.0443), [[HOP62 (line)]] (0.115) |
| 0.5 µM | — | — |
| 5 µM | — | [[SW48 (line)]] (1.66), [[AsPC-1 (line)]] (1.62), [[RPMI-7951 (line)]] (1.50), [[NCI-H1792 (line)]] (1.45) · weakest: [[NCI-H460 (line)]] (0.189), [[SW480 (line)]] (0.269), [[A-172 (line)]] (0.377) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Idoxuridine (drug)]] (+0.69, DNA synthesis/repair inhibitor, ⚠ only 4 significant genes); [[Thymol (drug)]] (+0.67, unclear); [[Tubulin inhibitor 6 (drug)]] (+0.63, Microtubule inhibitor, ⚠ only 2 significant genes); [[Nimesulide (drug)]] (+0.63, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Hydroxyurea (drug)]] (+0.63, DNA synthesis/repair inhibitor); [[Bimatoprost (drug)]] (+0.62, unclear); [[Proglumide (drug)]] (+0.59, unclear); [[LY-2584702 (tosylate salt) (drug)]] (+0.58, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Ipatasertib (drug)]] (+0.57, PI3K/AKT inhibitor); [[Lactate (calcium) (drug)]] (+0.56, unclear); [[Celecoxib (drug)]] (+0.56, Cyclooxygenase inhibitor); [[Pyridoxine (drug)]] (+0.56, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 27 arrows, 27 of them with an alert ⚠; grade A 0, B 19, C 8. Shown: the 15 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MYH14]] | 5 µM | B | MYH14 activity lowers the cells' numbers under Naproxen 5 µM (makes them more sensitive) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 1.20× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[FHL1]] | 5 µM | B | FHL1 activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express FHL1 (19) vs lines expressing it (29) | the lines without FHL1: 0.86× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[CCL5]] | 5 µM | B | CCL5 activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express CCL5 (22) vs lines expressing it (26) | the lines without CCL5: 0.82× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| [[KCNMA1]] | 5 µM | B | KCNMA1 activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.82× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[ADGRG2]] | 5 µM | B | ADGRG2 activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express ADGRG2 (10) vs lines expressing it (38) | the lines without ADGRG2: 0.85× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: KCNN3, SLC17A7, STARD8; maybe low, not absent |
| [[SSPN]] | 5 µM | B | SSPN activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express SSPN (15) vs lines expressing it (33) | the lines without SSPN: 0.86× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: FZD8, ENSG00000259363, EML1; maybe low, not absent |
| [[IL7R]] | 5 µM | B | IL7R activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express IL7R (30) vs lines expressing it (18) | the lines without IL7R: 0.81× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1 |
| [[HTRA3]] | 5 µM | B | HTRA3 activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express HTRA3 (31) vs lines expressing it (17) | the lines without HTRA3: 0.85× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[SIRLNT]] | 5 µM | B | SIRLNT activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.80× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[GJA1]] | 5 µM | B | GJA1 activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express GJA1 (26) vs lines expressing it (22) | the lines without GJA1: 0.84× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| [[CGN]] | 5 µM | B | CGN activity lowers the cells' numbers under Naproxen 5 µM (makes them more sensitive) | lines that do not express CGN (21) vs lines expressing it (27) | the lines without CGN: 1.15× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[ENSG00000286162]] | 5 µM | B | ENSG00000286162 activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express ENSG00000286162 (5) vs lines expressing it (43) | the lines without ENSG00000286162: 0.84× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: ITPR2-AS1, ITPR2, MPP4; maybe low, not absent |
| [[SMIM31]] | 5 µM | B | SMIM31 activity lowers the cells' numbers under Naproxen 5 µM (makes them more sensitive) | lines that do not express SMIM31 (34) vs lines expressing it (14) | the lines without SMIM31: 1.14× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: CEACAM5, PPP1R1B, ENSG00000267881 |
| [[SRGN]] | 5 µM | B | SRGN activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 0.80× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| [[PRR36]] | 5 µM | B | PRR36 activity lowers the cells' numbers under Naproxen 5 µM (makes them more sensitive) | lines that do not express PRR36 (19) vs lines expressing it (29) | the lines without PRR36: 1.16× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Naproxen"
- `tables/drugdoses.parquet` — dd in 708, 709, 710
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

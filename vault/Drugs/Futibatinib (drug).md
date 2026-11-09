---
drug: "Futibatinib"
type: "drug"
salt_base: "Futibatinib"
targets: "FGFR1, FGFR2, FGFR3, FGFR4"
moa_fine: "Other TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 53
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Futibatinib

*Other TK inhibitor (inhibitor/antagonist) · targets: FGFR1, FGFR2, FGFR3, FGFR4 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 53 / 0 / 16; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.15 / -0.14.
> Flags by dose: - / transcription drop; noisy plate (z scaled) / noisy plate (z scaled). ⚠ 0.5 µM: transcription drop (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:F5 | 0 / 53 | — | +0.02 | -0.4/-0.7/+0.6 | — |
| 0.5 µM | [[Plate 02]]:F5 | 0 / 0 | — | +0.23 | -1.5/-1.1/-0.0 | ⚠ transcription drop · noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:F5 | 1 / 15 | — | -0.67 | -2.0/-1.8/+0.3 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (1 gene, none with an alert): [[RDUR]] 1.69× (z +2.7, 1/11 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (53 genes, none with an alert; 12 shown): [[ENSG00000233928]] 0.536× (z -5.8, 0/9 lines), [[CAVIN2-AS1]] 0.630× (z -5.0, 2/16 lines), [[COL5A1]] 0.710× (z -4.4, 0/18 lines), [[COL4A1]] 0.756× (z -4.4, 0/19 lines), [[LINC00540]] 0.702× (z -4.3, 0/15 lines), [[MAL2]] 0.790× (z -4.0, 0/17 lines), [[NID2]] 0.666× (z -4.0, 2/15 lines), [[GAS7]] 0.696× (z -4.0, 3/22 lines), [[DPP4]] 0.773× (z -3.9, 2/19 lines), [[KIRREL3]] 0.706× (z -3.9, 1/12 lines), [[RNF43]] 0.780× (z -3.9, 1/22 lines), [[UBOX5-AS1]] 0.658× (z -3.9, 8/42 lines)

**5 µM** (15 genes, none with an alert; 12 shown): [[DLEU2]] 0.781× (z -3.4, 14/46 lines), [[ENSG00000284906]] 0.746× (z -3.3, 16/46 lines), [[ENSG00000197332]] 0.672× (z -3.2, 9/32 lines), [[ENSG00000214719]] 0.759× (z -3.2, 14/43 lines), [[SHCBP1]] 0.662× (z -3.2, 14/45 lines), [[CHURC1-FNTB]] 0.719× (z -3.1, 11/42 lines), [[RHOT1]] 0.818× (z -3.1, 9/46 lines), [[CCNG1]] 0.722× (z -3.0, 16/45 lines), [[NUSAP1]] 0.678× (z -3.0, 17/46 lines), [[DIAPH3]] 0.769× (z -2.9, 15/43 lines), [[LIN9]] 0.757× (z -2.9, 10/44 lines), [[ENSG00000291214]] 0.783× (z -2.9, 10/44 lines)

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
| 0.05 µM | — | [[RKO (line)]] (2.08), [[C-33 A (line)]] (2.05), [[SHP-77 (line)]] (1.95), [[AN3 CA (line)]] (1.85) · weakest: [[SW 900 (line)]] (0.492), [[SW1417 (line)]] (0.567), [[A549 (line)]] (0.677) |
| 0.5 µM | [[Hs 766T (line)]] (-4.0) | — |
| 5 µM | [[NCI-H460 (line)]] (-3.2) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Carbidopa (monohydrate) (drug)]] (+0.66, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only; position not correctable)); [[Ivabradine (hydrochloride) (drug)]] (+0.63, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Anethole trithione (drug)]] (+0.61, unclear); [[Lucanthone (drug)]] (+0.61, unclear); [[Tucatinib (drug)]] (+0.58, EGFR/ERBB inhibitor); [[Ranolazine (drug)]] (+0.58, unclear); [[Erlotinib (drug)]] (+0.58, EGFR/ERBB inhibitor); [[Menadione (drug)]] (+0.55, unclear); [[Rutin (trihydrate) (drug)]] (+0.54, unclear); [[Fenofibrate (drug)]] (+0.54, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 24 arrows, 24 of them with an alert ⚠; grade A 0, B 11, C 13. Shown: the 15 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MSRB3-AS1]] | 0.5 µM | B | MSRB3-AS1 activity raises the cells' numbers under Futibatinib 0.5 µM (protects the cells) | lines that do not express MSRB3-AS1 (42) vs lines expressing it (6) | the lines without MSRB3-AS1: 0.80× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2 |
| [[ARHGAP24]] | 0.05 µM | B | ARHGAP24 activity lowers the cells' numbers under Futibatinib 0.05 µM (makes them more sensitive) | lines that do not express ARHGAP24 (17) vs lines expressing it (31) | the lines without ARHGAP24: 1.19× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, GPR176 |
| [[TSC22D3]] | 5 µM | B | TSC22D3 activity lowers the cells' numbers under Futibatinib 5 µM (makes them more sensitive) | lines that do not express TSC22D3 (11) vs lines expressing it (37) | the lines without TSC22D3: 1.19× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[HIPK2]] | 0.5 µM | B | HIPK2 activity lowers the cells' numbers under Futibatinib 0.5 µM (makes them more sensitive) | lines that do not express HIPK2 (5) vs lines expressing it (43) | the lines without HIPK2: 1.29× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[LY75]] | 0.05 µM | B | LY75 activity lowers the cells' numbers under Futibatinib 0.05 µM (makes them more sensitive) | lines that do not express LY75 (30) vs lines expressing it (18) | the lines without LY75: 1.15× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: IL20RA, TINAGL1, CARD11 |
| [[ENSG00000286533]] | 0.5 µM | B | ENSG00000286533 activity lowers the cells' numbers under Futibatinib 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000286533 (5) vs lines expressing it (43) | the lines without ENSG00000286533: 1.25× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: HIPK2, ZMIZ1, LGALS3BP; maybe low, not absent |
| [[BMPER]] | 0.5 µM | B | BMPER activity lowers the cells' numbers under Futibatinib 0.5 µM (makes them more sensitive) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 1.09× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[PLXNA2]] | 0.5 µM | B | PLXNA2 activity lowers the cells' numbers under Futibatinib 0.5 µM (makes them more sensitive) | lines that do not express PLXNA2 (15) vs lines expressing it (33) | the lines without PLXNA2: 1.15× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[COX7B2]] | 0.5 µM | B | COX7B2 activity raises the cells' numbers under Futibatinib 0.5 µM (protects the cells) | lines that do not express COX7B2 (42) vs lines expressing it (6) | the lines without COX7B2: 0.78× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205 |
| [[ENSG00000289942]] | 0.5 µM | B | ENSG00000289942 activity lowers the cells' numbers under Futibatinib 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000289942 (7) vs lines expressing it (41) | the lines without ENSG00000289942: 1.15× the cells of the other lines | 0.097 | ⚠ within organs, on part of the lines; also absent: MT2A, MT1X; maybe low, not absent |
| [[HS3ST3B1]] | 0.5 µM | B | HS3ST3B1 activity lowers the cells' numbers under Futibatinib 0.5 µM (makes them more sensitive) | lines that do not express HS3ST3B1 (18) vs lines expressing it (30) | the lines without HS3ST3B1: 1.11× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, SRPX, APCDD1L-DT |
| [[RAB11FIP1]] | 0.5 µM | C | RAB11FIP1 activity raises the cells' numbers under Futibatinib 0.5 µM (protects the cells) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 0.70× the cells of the other lines | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| [[ENSG00000285458]] | 0.05 µM | C | ENSG00000285458 activity lowers the cells' numbers under Futibatinib 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000285458 (5) vs lines expressing it (43) | the lines without ENSG00000285458: 1.27× the cells of the other lines | 0.023 | ⚠ tissue-confounded; across organs; also absent: TBILA, GCA, RILP; maybe low, not absent |
| [[ITPK1]] | 0.05 µM | C | ITPK1 activity raises the cells' numbers under Futibatinib 0.05 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.80× the cells of the other lines | 0.075 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| [[SLC25A45]] | 0.5 µM | C | SLC25A45 activity lowers the cells' numbers under Futibatinib 0.5 µM (makes them more sensitive) | lines that do not express SLC25A45 (3) vs lines expressing it (45) | the lines without SLC25A45: 1.34× the cells of the other lines | 0.076 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; co-occurs with WNK2; also absent: CASP8, SP100, PRRG1; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Futibatinib"
- `tables/drugdoses.parquet` — dd in 486, 487, 488
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

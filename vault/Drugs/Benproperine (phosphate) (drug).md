---
drug: "Benproperine (phosphate)"
type: "drug"
salt_base: "Benproperine"
targets: "ARPC2"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 55
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Benproperine (phosphate)

*unclear (inhibitor/antagonist) · targets: ARPC2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 55 / 0 / 36; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.33 / 0.38.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:C3 | 11 / 44 | — | +0.35 | -1.2/-1.6/-1.0 | — |
| 0.5 µM | [[Plate 08]]:C3 | 0 / 0 | — | -0.06 | -0.5/-0.7/+0.1 | — |
| 5 µM | [[Plate 09]]:C3 | 1 / 35 | — | -0.08 | -0.8/-0.6/+0.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (11 genes, none with an alert): [[DNAJC13]] 1.24× (z +3.7, 22/48 lines), [[ZNF484]] 1.34× (z +3.2, 11/47 lines), [[LRPPRC]] 1.22× (z +3.2, 24/48 lines), [[ZNF470]] 1.20× (z +3.2, 3/29 lines), [[PTP4A1]] 1.38× (z +3.1, 14/47 lines), [[LIN7C]] 1.31× (z +3.1, 23/48 lines), [[RPE]] 1.28× (z +3.0, 14/47 lines), [[TMEM30A]] 1.23× (z +3.0, 22/48 lines), [[DDX3X]] 1.22× (z +2.9, 21/48 lines), [[DDX20]] 1.22× (z +2.9, 2/47 lines), [[USP38]] 1.28× (z +2.9, 9/47 lines)

**5 µM** (1 gene, none with an alert): [[PYDC2-AS1]] 1.26× (z +3.1, 0/21 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (44 genes, none with an alert; 12 shown): [[RNF212]] 0.632× (z -4.7, 1/12 lines), [[ZNF732]] 0.443× (z -4.1, 0/6 lines), [[HHLA2]] 0.568× (z -4.0, 0/10 lines), [[ENSG00000287507]] 0.586× (z -3.9, 11/42 lines), [[VENTXP1]] 0.574× (z -3.9, 3/26 lines), [[MIR493HG]] 0.439× (z -3.8, 2/10 lines), [[LINC01456]] 0.555× (z -3.8, 0/4 lines), [[ENSG00000291113]] 0.721× (z -3.7, 9/45 lines), [[APBA1]] 0.737× (z -3.6, 4/40 lines), [[CD163L1]] 0.749× (z -3.5, 3/24 lines), [[CARM1]] 0.783× (z -3.5, 16/47 lines), [[LINC01029]] 0.506× (z -3.5, 1/6 lines)

**5 µM** (35 genes, none with an alert; 12 shown): [[A3GALT2]] 0.502× (z -5.0, 13/35 lines), [[MTNR1A]] 0.533× (z -4.1, 12/30 lines), [[ATP2A1]] 0.717× (z -4.1, 11/45 lines), [[LINC00672]] 0.666× (z -4.1, 14/41 lines), [[DCPS]] 0.815× (z -4.0, 10/47 lines), [[THUMPD3-AS1]] 0.779× (z -3.9, 29/48 lines), [[KBTBD11-OT1-1]] 0.670× (z -3.8, 8/35 lines), [[ENSG00000245025]] 0.625× (z -3.8, 19/43 lines), [[AGAP13P]] 0.666× (z -3.7, 9/36 lines), [[CLCN2]] 0.778× (z -3.7, 13/46 lines), [[BCORL1]] 0.828× (z -3.6, 14/47 lines), [[LAG3]] 0.616× (z -3.5, 11/31 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 025]] (+2.8), [[Module 029]] (+2.5), [[Module 020]] (+2.3) | [[Module 048]] (-2.6), [[Module 024]] (-2.4), [[Module 059]] (-2.2) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[CHP-212 (line)]] (1.38), [[HepG2_C3A (line)]] (1.33), [[LOX-IMVI (line)]] (1.27), [[A-172 (line)]] (1.23) · weakest: [[HEC-1-A (line)]] (0.574), [[Panc 03.27 (line)]] (0.598), [[PANC-1 (line)]] (0.647) |
| 0.5 µM | — | — |
| 5 µM | — | [[C-33 A (line)]] (1.65), [[SW48 (line)]] (1.63), [[A-427 (line)]] (1.56), [[SK-MEL-2 (line)]] (1.54) · weakest: [[SW 1088 (line)]] (-0.553), [[PANC-1 (line)]] (0.378), [[A498 (line)]] (0.433) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Erlotinib (drug)]] (+0.92, EGFR/ERBB inhibitor); [[Fenofibrate (drug)]] (+0.90, unclear); [[Lucanthone (drug)]] (+0.87, unclear); [[Tucatinib (drug)]] (+0.81, EGFR/ERBB inhibitor); [[Anethole trithione (drug)]] (+0.80, unclear); [[Paclitaxel (drug)]] (+0.76, Microtubule inhibitor, ⚠ only 3 significant genes); [[Rutin (trihydrate) (drug)]] (+0.76, unclear); [[MK-8353 (drug)]] (+0.75, Other MAPK inhibitor); [[Encorafenib (drug)]] (+0.72, RAF inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ALDH3A1]] | 0.05 µM | B | ALDH3A1 activity raises the cells' numbers under Benproperine (phosphate) 0.05 µM (protects the cells) | lines that do not express ALDH3A1 (36) vs lines expressing it (12) | the lines without ALDH3A1: 0.85× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, MUC17, NPSR1 |
| [[FIGN]] | 0.05 µM | C | FIGN activity lowers the cells' numbers under Benproperine (phosphate) 0.05 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.17× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[SPART-AS1]] | 0.05 µM | C | SPART-AS1 activity lowers the cells' numbers under Benproperine (phosphate) 0.05 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.15× the cells of the other lines | 0.027 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[C2orf74]] | 0.05 µM | C | C2orf74 activity lowers the cells' numbers under Benproperine (phosphate) 0.05 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.16× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[NR3C1]] | 0.05 µM | C | NR3C1 activity lowers the cells' numbers under Benproperine (phosphate) 0.05 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.18× the cells of the other lines | 0.033 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[ENSG00000285458]] | 0.05 µM | C | ENSG00000285458 activity lowers the cells' numbers under Benproperine (phosphate) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000285458 (5) vs lines expressing it (43) | the lines without ENSG00000285458: 1.20× the cells of the other lines | 0.036 | ⚠ tissue-confounded; across organs; also absent: TBILA, GCA, RILP; maybe low, not absent |
| [[ENSG00000214265]], [[SNHG14]], [[SNRPN]] | 0.05 µM | C | ENSG00000214265, SNHG14, SNRPN activity lowers the cells' numbers under Benproperine (phosphate) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.15× the cells of the other lines | 0.066 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| [[SPAG16]] | 0.05 µM | C | SPAG16 activity lowers the cells' numbers under Benproperine (phosphate) 0.05 µM (makes them more sensitive) | lines that do not express SPAG16 (6) vs lines expressing it (42) | the lines without SPAG16: 1.19× the cells of the other lines | 0.071 | ⚠ tissue-confounded; across organs; co-occurs with WNK2, BRCA2; also absent: ZNF140, LUCAT1, GCA |
| [[RNF150]] | 0.05 µM | C | RNF150 activity lowers the cells' numbers under Benproperine (phosphate) 0.05 µM (makes them more sensitive) | lines that do not express RNF150 (16) vs lines expressing it (32) | the lines without RNF150: 1.14× the cells of the other lines | 0.084 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SNRPN, BVES, MPDZ |
| [[ENSG00000286964]] | 0.05 µM | C | ENSG00000286964 activity lowers the cells' numbers under Benproperine (phosphate) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.14× the cells of the other lines | 0.097 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Benproperine (phosphate)"
- `tables/drugdoses.parquet` — dd in 158, 159, 160
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it

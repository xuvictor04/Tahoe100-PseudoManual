---
cell_line: "CFPAC-1"
type: "cell line"
cell_line_id: "CVCL_1119"
depmap_id: "ACH-000138"
organ: "Pancreas"
tp53_status: "altered"
drivers: ["KRAS(Missense)", "SMAD4(Deletion)", "TP53(Missense)"]
n_dd_depleted: 9
median_response: 0.974
tags: ["cell-line", "organ/pancreas"]
generated_by: "tahoemap"
---

# CFPAC-1

*Pancreas · TP53 altered · CVCL_1119 · ACH-000138*

|  |  |
|---|---|
| Organ | Pancreas |
| TP53 status | altered |
| Drivers | KRAS(Missense); SMAD4(Deletion); TP53(Missense) |
| Driver changes | KRAS p.G12V; TP53 p.C242R |
| Cells over all wells | 2,404,516 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.974 (1 = a typical line) |
| Drug-doses that deplete it | 9 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 8 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 15,062 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 28): the line loses cells relative to the other lines in the same wells. Drug-doses: 9 in all, 1 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[venetoclax (drug)]] 5 µM |  | -5.5 | -0.94 |
| [[EX229 (drug)]] 5 µM |  | -3.9 | -0.65 |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -3.7 | -0.65 |
| [[BAY1125976 (drug)]] 5 µM |  | -3.6 | -0.58 |
| [[TAK-733 (drug)]] 5 µM |  | -3.5 | -0.57 |
| [[Mebendazole (drug)]] 5 µM |  | -3.3 | -0.52 |
| [[Clopidogrel (drug)]] 0.05 µM |  | -3.3 | -0.51 |
| [[Sapanisertib (drug)]] 5 µM |  | -3.2 | -0.50 |
| [[Dabrafenib (drug)]] 5 µM |  | -3.1 | -0.49 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Malotilate (drug)]] 0.5 µM (2.04); [[Vinblastine (sulfate) (drug)]] 5 µM (1.73); [[Vinblastine (sulfate) (drug)]] 0.5 µM (1.73); [[Tofacitinib (drug)]] 5 µM (1.66); [[Fluvoxamine (maleate) (drug)]] 0.5 µM (1.64); [[Quinestrol (drug)]] 5 µM (1.56); [[Simotinib (drug)]] 0.05 µM (1.54); [[Tofacitinib (citrate) (drug)]] 5 µM (1.54)
- Weakest: [[Crizotinib (hydrochloride) (drug)]] 0.5 µM (-0.0660); [[Elagolix sodium (drug)]] 0.5 µM (0.106); [[Oxaprozin (drug)]] 0.5 µM (0.109); [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM (0.270); [[Pimozide (drug)]] 0.05 µM (0.294); [[Vortioxetine (drug)]] 5 µM (0.300, ⚠ toxic); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM (0.303); [[Decitabine (drug)]] 0.5 µM (0.320); [[Orlistat (drug)]] 0.05 µM (0.328)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 28): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[FKBP5]] (23, 6 ⚠), [[CCND3]] (20), [[VSTM2L]] (18), [[ATP1A1]] (18, 3 ⚠), [[CEP70]] (16), [[COBLL1]] (15), [[BIRC3]] (15, 4 ⚠), [[GPHN]] (14, 5 ⚠), [[PDZD2]] (13), [[TLR2]] (13), [[ELOVL5]] (13, 4 ⚠), [[TFCP2L1]] (13, 4 ⚠), [[SNAPC1]] (13, 6 ⚠), [[SLIT2]] (11), [[SERPINA3]] (11), [[CFB]] (11)
- down: [[ST8SIA6]] (24, 15 ⚠), [[FAM114A1]] (23, 12 ⚠), [[ADAM28]] (22, 11 ⚠), [[ITGA2]] (21, 4 ⚠), [[NTSR1]] (21, 6 ⚠), [[CAMK1D]] (21, 7 ⚠), [[RAD51B]] (20, 8 ⚠), [[PTPRR]] (20, 13 ⚠), [[ENSG00000260877]] (19, 1 ⚠), [[ZMYND8]] (19, 7 ⚠), [[PTPN12]] (19, 8 ⚠), [[IRAK3]] (19, 13 ⚠), [[PATJ]] (19, 15 ⚠), [[MX1]] (18, 5 ⚠), [[ANTXR2]] (14), [[RASGRP3]] (14, 1 ⚠), [[AGO2]] (13), [[PHLDA1]] (13), [[ETV1]] (12), [[EIF2AK2]] (12)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[MMP7]] (+7.6), [[MUC4]] (+6.8), [[IRAK3]] (+6.8), [[ENSG00000286546]] (+6.7, ⚠ noise-class RNA), [[ADAM28]] (+6.5), [[SLC6A14]] (+6.5), [[CP]] (+6.4), [[MUC16]] (+6.3), [[HLA-DRB1]] (+6.3), [[GABRP]] (+6.2), [[TMPRSS4]] (+6.2), [[HNF1B]] (+6.2), [[PRSS8]] (+6.1), [[PADI1]] (+6.1), [[DUOX2]] (+6.1), [[NRG3]] (+6.0) (1,530 genes, 87 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[SMAD4]] (-4.1), [[PTPRG]] (-3.2), [[DUXAP10]] (-3.2), [[ITPR2]] (-3.1), [[PARP6]] (-3.0), [[DUXAP9]] (-2.9), [[MIR100HG]] (-2.9), [[ERC1]] (-2.9), [[MSRB3]] (-2.9), [[EVC]] (-2.8), [[GLI3]] (-2.8), [[EPIC1]] (-2.7), [[MVB12B]] (-2.7), [[BNC2]] (-2.7), [[DCLK2]] (-2.6) (134 genes, 2 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 28): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.832 to 1.42).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 3 in all, 3 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 61 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[SMAD4]] | SMAD4 loss of function (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; SMAD4 not expressed in 2 of the 6 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,497 in all, 1,497 with an alert ⚠; shown: the 15 strongest; 1,482 more line sets (1,482 of them with an alert ⚠) not shown; 1,522 genes; 1,271 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[LINC01559]] | 38 vs 12 | 0 / 182 / 0 | B 36, C 146; 182 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01819]] | 29 vs 21 | 2 / 141 / 1 | B 27, C 117; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[NPSR1]] | 42 vs 8 | 2 / 142 / 0 | B 26, C 118; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ATP10B]] | 40 vs 10 | 0 / 140 / 0 | B 27, C 113; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC13]] | 40 vs 10 | 2 / 138 / 0 | B 33, C 107; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LGALS4]] | 39 vs 11 | 0 / 116 / 0 | B 23, C 93; 116 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SYK]] | 30 vs 20 | 0 / 116 / 0 | B 31, C 85; 116 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CEACAM5]] | 39 vs 11 | 4 / 110 / 1 | B 25, C 90; 115 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CDH17]] | 40 vs 10 | 1 / 112 / 1 | B 21, C 93; 114 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[FXYD3]] | 34 vs 16 | 0 / 101 / 8 | B 20, C 89; 109 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PRR15L]] | 38 vs 12 | 0 / 109 / 0 | B 18, C 91; 109 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SPOCK1]] | 29 vs 21 | 1 / 62 / 45 | B 58, C 50; 108 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CDC25A]] | 5 vs 45 | 0 / 107 / 0 | B 100, C 7; 107 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MYO7B]] | 36 vs 14 | 0 / 105 / 0 | B 25, C 80; 105 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[FAM3D]] | 43 vs 7 | 1 / 103 / 0 | B 16, C 88; 104 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 28; `tables/line_effects.parquet` — line == 28
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 28; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 28]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include CFPAC-1

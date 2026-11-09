---
cell_line: "NCI-H1573"
type: "cell line"
cell_line_id: "CVCL_1478"
depmap_id: "ACH-000916"
organ: "Lung"
tp53_status: "altered"
drivers: ["CDKN2A(Missense)", "EGFR(Gain)", "ERBB3(Missense)", "FBXW7(Missense)", "FBXW7(Stopgain)", "KMT2D(Missense)", "KRAS(Missense)", "MET(Gain)", "NRAS(Missense)", "PIK3R1(Stopgain)", "PTPN11(Stopgain)", "RNF43(Missense)", "SMARCA4(Stopgain)", "STK11(Missense)", "TP53(Missense)"]
n_dd_depleted: 12
median_response: 0.999
tags: ["cell-line", "organ/lung"]
generated_by: "tahoemap"
---

# NCI-H1573

*Lung · TP53 altered · CVCL_1478 · ACH-000916*

|  |  |
|---|---|
| Organ | Lung |
| TP53 status | altered |
| Drivers | CDKN2A(Missense); EGFR(Gain); ERBB3(Missense); FBXW7(Missense); FBXW7(Stopgain); KMT2D(Missense); KRAS(Missense); MET(Gain); NRAS(Missense); PIK3R1(Stopgain); PTPN11(Stopgain); RNF43(Missense); SMARCA4(Stopgain); STK11(Missense); TP53(Missense) |
| Driver changes | CDKN2A p.D23P; ERBB3 p.E332K; FBXW7 p.V619L; FBXW7 p.W593*; KMT2D p.L2398P; KMT2D p.V361F; KRAS p.G12A; NRAS p.Q61K; PIK3R1 p.G71*; PTPN11 p.R351*; RNF43 p.A605G; SMARCA4 p.E1399*; STK11 p.S216F; TP53 p.R248L |
| Cells over all wells | 2,016,838 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.999 (1 = a typical line) |
| Drug-doses that deplete it | 12 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 8 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,882 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 33): the line loses cells relative to the other lines in the same wells. Drug-doses: 12 in all, 4 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.6 | -1.74 |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.4 | -2.45 |
| [[Belumosudil (drug)]] 5 µM |  | -6.7 | -1.19 |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | -1.14 |
| [[Pralsetinib (drug)]] 5 µM |  | -4.5 | -0.86 |
| [[CP21R7 (drug)]] 0.5 µM |  | -4.3 | -0.74 |
| [[DTP3 (drug)]] 5 µM |  | -3.6 | -0.65 |
| [[GSK1059615 (drug)]] 0.5 µM |  | -3.5 | -0.61 |
| [[Erythromycin (drug)]] 0.5 µM |  | -3.3 | -0.56 |
| [[Pimitespib (drug)]] 5 µM |  | -3.3 | -0.60 |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | -0.59 |
| [[Volasertib (drug)]] 5 µM |  | -3.1 | -0.56 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Econazole (drug)]] 5 µM (2.37); [[Citalopram (hydrobromide) (drug)]] 0.05 µM (2.26); [[Medroxyprogesterone acetate (drug)]] 5 µM (2.21); [[Phenylephrine (hydrochloride) (drug)]] 5 µM (2.16); [[Medroxyprogesterone acetate (drug)]] 0.05 µM (2.12); [[Triamcinolone (drug)]] 0.05 µM (2.09); [[Dexamethasone (drug)]] 0.05 µM (2.00); [[Betamethasone dipropionate (drug)]] 0.05 µM (1.85)
- Weakest: [[Monocrotaline (drug)]] 0.05 µM (-0.197); [[Oxaprozin (drug)]] 0.5 µM (-0.104); [[Finasteride (drug)]] 5 µM (0.185); [[Verteporfin (drug)]] 0.5 µM (0.186); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (0.194, ⚠ cell-cycle shift); [[Roxadustat (drug)]] 0.05 µM (0.198); [[Epirubicin (hydrochloride) (drug)]] 5 µM (0.235, ⚠ cell-cycle shift); [[Simotinib (drug)]] 5 µM (0.243, ⚠ toxic); [[Auranofin (drug)]] 0.5 µM (0.294); [[Orlistat (drug)]] 0.05 µM (0.325); [[Verteporfin (drug)]] 0.05 µM (0.326)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 33): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[FKBP5]] (29, 6 ⚠), [[ATP1A1]] (26, 1 ⚠), [[DIP2C]] (25, 2 ⚠), [[CPD]] (23), [[MAP2K1]] (23), [[ACSL1]] (23, 3 ⚠), [[COPS8]] (22, 3 ⚠), [[ZFP36L1]] (21), [[CAV1]] (20), [[FGD4]] (19), [[TBC1D8]] (19), [[PACSIN2]] (18), [[NEBL]] (18, 1 ⚠)
- down: [[STC1]] (39, 1 ⚠), [[IGFBP3]] (32, 5 ⚠), [[ATP2B1]] (31, 7 ⚠), [[DUSP4]] (29, 1 ⚠), [[IFI44L]] (29, 10 ⚠), [[BMP7]] (28, 3 ⚠), [[GPI]] (28, 6 ⚠), [[MIR31HG]] (28, 6 ⚠), [[PITPNC1]] (28, 11 ⚠), [[LIF]] (26, 5 ⚠), [[ZMYND8]] (26, 8 ⚠), [[SEMA3C]] (25, 4 ⚠), [[MAP7]] (23, 2 ⚠), [[EDIL3]] (22, 1 ⚠), [[NPTX1]] (21)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[CES1]] (+7.7), [[ENSG00000286329]] (+7.3, ⚠ noise-class RNA), [[LINC01446]] (+7.2), [[CYP24A1]] (+7.0), [[CEACAM6]] (+6.8), [[ENSG00000258028]] (+6.7, ⚠ noise-class RNA), [[SCEL]] (+6.7), [[ENSG00000288087]] (+6.6, ⚠ noise-class RNA), [[ADGRG7]] (+6.6), [[PHF2P2]] (+6.4), [[ENSG00000259692]] (+6.3, ⚠ noise-class RNA), [[LINC02484]] (+6.2), [[LINC02327]] (+6.2), [[ENSG00000286016]] (+6.1, ⚠ noise-class RNA), [[LINC02616]] (+6.1), [[MAGEA4]] (+6.1), [[NLGN4X]] (+6.0), [[CEACAM5]] (+5.9), [[LRP1B]] (+5.8), [[EYA2]] (+5.8) (1,448 genes, 175 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[VIM]] (-3.9), [[HEXA]] (-3.5), [[ECHDC1]] (-3.4), [[MPDZ]] (-3.3), [[KCNQ1OT1]] (-3.3), [[AKT3]] (-3.3), [[NNT]] (-3.3), [[NECTIN3]] (-3.2), [[ENSG00000260729]] (-3.1, ⚠ noise-class RNA), [[ICAM1]] (-3.1), [[PTPRG]] (-3.1), [[AXL]] (-3.1), [[FAM171A1]] (-2.9), [[SACS]] (-2.8), [[ZNF714]] (-2.8), [[TENM3]] (-2.8) (235 genes, 3 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 33): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 59 (0.639; genes ZFP36L1, CHST11, ADAM19, PLK2 / KCNMA1, CSGALNACT1, STC1, BMERB1)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 14 in all, 14 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 47 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[NRAS]] | NRAS gain of function (7 lines) vs not recorded (43) | 0 / 2 / 0 | C 2; 2 with an alert ⚠ | ⚠ within organs, on part of the lines |
| [[KMT2D]] | KMT2D altered (any record) (15 lines) vs not recorded (35) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[FBXW7]] | FBXW7 loss of function (5 lines) vs not recorded (45) | 0 / 1 / 0 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[EGFR]] | EGFR altered (any record) (4 lines) vs not recorded (46) | 0 / 0 / 0 | — | ⚠ few lines (4 vs 46); within organs, on part of the lines; mechanism partly not recorded; EGFR not expressed in 1 of the 4 altered lines |
| [[ERBB3]] | ERBB3 altered (any record) (3 lines) vs not recorded (47) | 0 / 0 / 0 | — | ⚠ few lines (3 vs 47); within organs, on part of the lines; mechanism partly not recorded |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[MET]] | MET altered (any record) (3 lines) vs not recorded (47) | 0 / 0 / 0 | — | ⚠ few lines (3 vs 47); tissue-confounded; across organs; mechanism partly not recorded; MET not expressed in 1 of the 3 altered lines |
| [[PIK3R1]] | PIK3R1 altered (any record) (5 lines) vs not recorded (45) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; PIK3R1 not expressed in 1 of the 5 altered lines |
| [[RNF43]] | RNF43 altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with EP300, ACVR2A |
| [[SMARCA4]] | SMARCA4 altered (any record) (12 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[SMARCA4]] | SMARCA4 loss of function (10 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[STK11]] | STK11 loss of function (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,655 in all, 1,655 with an alert ⚠; shown: the 15 strongest; 1,640 more line sets (1,640 of them with an alert ⚠) not shown; 1,678 genes; 1,462 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[SLC44A4]] | 37 vs 13 | 9 / 186 / 9 | B 57, C 147; 204 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[EPS8L3]] | 35 vs 15 | 0 / 196 / 1 | B 46, C 151; 197 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CLIC5]] | 37 vs 13 | 4 / 185 / 7 | B 59, C 137; 196 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GCNT3]] | 38 vs 12 | 2 / 184 / 0 | B 43, C 143; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01559]] | 38 vs 12 | 0 / 182 / 0 | B 36, C 146; 182 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC03040]] | 31 vs 19 | 3 / 147 / 4 | B 38, C 116; 154 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[HNF4A]] | 34 vs 16 | 0 / 145 / 0 | B 29, C 116; 145 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01819]] | 29 vs 21 | 2 / 141 / 1 | B 27, C 117; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[NPSR1]] | 42 vs 8 | 2 / 142 / 0 | B 26, C 118; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ATP10B]] | 40 vs 10 | 0 / 140 / 0 | B 27, C 113; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC13]] | 40 vs 10 | 2 / 138 / 0 | B 33, C 107; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC5B]] | 37 vs 13 | 2 / 135 / 2 | B 33, C 106; 139 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PBK]] | 4 vs 46 | 1 / 138 / 0 | C 139; 139 with an alert ⚠ | within organs | ⚠ few lines (4 vs 46); within organs, on part of the lines |
| [[PROM1]] | 37 vs 13 | 0 / 137 / 0 | B 32, C 105; 137 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[AURKB]] | 4 vs 46 | 2 / 134 / 0 | C 136; 136 with an alert ⚠ | within organs | ⚠ few lines (4 vs 46); within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 33; `tables/line_effects.parquet` — line == 33
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 33; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 33]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include NCI-H1573

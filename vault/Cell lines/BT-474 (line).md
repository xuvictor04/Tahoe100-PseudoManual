---
cell_line: "BT-474"
type: "cell line"
cell_line_id: "CVCL_0179"
depmap_id: "ACH-000927"
organ: "Breast"
tp53_status: "altered"
drivers: ["ACVR2A(Missense)", "ATM(Missense)", "BRCA2(Stopgain)", "ERBB2(Gain)", "HNF1A(Stopgain)", "KMT2D(Missense)", "LASP1(Gain)", "MAPK1(Missense)", "PIK3CA(Missense)", "TGFBR2(Missense)", "TP53(Missense)", "WNK2(Missense)"]
n_dd_depleted: 15
median_response: 0.898
tags: ["cell-line", "organ/breast"]
generated_by: "tahoemap"
---

# BT-474

*Breast · TP53 altered · CVCL_0179 · ACH-000927*

|  |  |
|---|---|
| Organ | Breast |
| TP53 status | altered |
| Drivers | ACVR2A(Missense); ATM(Missense); BRCA2(Stopgain); ERBB2(Gain); HNF1A(Stopgain); KMT2D(Missense); LASP1(Gain); MAPK1(Missense); PIK3CA(Missense); TGFBR2(Missense); TP53(Missense); WNK2(Missense) |
| Driver changes | ACVR2A p.S17F; ATM p.E2468K; BRCA2 p.S3094*; HNF1A p.Q495*; KMT2D p.E1623K; MAPK1 p.H61Q; PIK3CA p.K111N; TGFBR2 p.M36I; TP53 p.E285K; WNK2 p.E398Q |
| Cells over all wells | 1,271,782 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.898 (1 = a typical line) |
| Drug-doses that deplete it | 15 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 10 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,289 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 6): the line loses cells relative to the other lines in the same wells. Drug-doses: 15 in all, 5 with an alert ⚠; shown: the 12 strongest and the 2 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -7.6 | -2.28 |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | -1.27 |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.1 | -1.22 |
| [[Tomivosertib (drug)]] 5 µM |  | -5.8 | -0.98 |
| [[Afatinib (drug)]] 5 µM |  | -4.4 | -0.52 |
| [[EX229 (drug)]] 5 µM |  | -4.2 | -0.73 |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.49 |
| [[Neratinib (maleate) (drug)]] 5 µM |  | -4.0 | -0.46 |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.9 | -0.63 |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.7 | -0.65 |
| [[Tucatinib (drug)]] 5 µM |  | -3.6 | -0.59 |
| [[ML264 (drug)]] 5 µM |  | -3.3 | -0.55 |
| [[Afatinib (drug)]] 0.5 µM |  | -3.2 | -0.36 |
| [[venetoclax (drug)]] 5 µM |  | -3.1 | -0.54 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Tofacitinib (citrate) (drug)]] 0.05 µM (2.44); [[Auranofin (drug)]] 0.5 µM (2.16); [[Tofacitinib (drug)]] 0.5 µM (2.02); [[Tofacitinib (citrate) (drug)]] 0.5 µM (1.97); [[Tofacitinib (drug)]] 0.05 µM (1.78); [[Tofacitinib (drug)]] 5 µM (1.74); [[Lonafarnib (drug)]] 5 µM (1.73, ⚠ toxic); [[Dihydroartemisinin (drug)]] 0.5 µM (1.73); [[Tofacitinib (citrate) (drug)]] 5 µM (1.72)
- Weakest: [[Tirabrutinib (drug)]] 0.5 µM (-0.0547); [[Carbamazepine (drug)]] 0.5 µM (-0.0356); [[Roxadustat (drug)]] 0.05 µM (-0.0279); [[Pitavastatin (Calcium) (drug)]] 0.05 µM (-0.0202); [[Apalutamide (drug)]] 0.5 µM (0.121); [[Vilanterol (drug)]] 0.05 µM (0.140); [[Entecavir (monohydrate) (drug)]] 0.5 µM (0.167); [[Filgotinib (drug)]] 0.05 µM (0.192)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 6): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[CREB5]] (17, 5 ⚠), [[DOCK4]] (13, 4 ⚠), [[MED1]] (12, 3 ⚠), [[RSRC2]] (12, 4 ⚠), [[RUNX1]] (11), [[ME1]] (11, 1 ⚠), [[SIRT1]] (11, 1 ⚠), [[CPEB4]] (11, 1 ⚠), [[ZBTB10]] (11, 1 ⚠), [[ENSG00000285744]] (11, 1 ⚠), [[SNX9]] (11, 3 ⚠), [[HNRNPM]] (11, 5 ⚠), [[KLF10]] (11, 5 ⚠), [[MYO10]] (11, 7 ⚠), [[TFPI2]] (11, 9 ⚠), [[WAC]] (10, 1 ⚠), [[MED13]] (10, 1 ⚠), [[SUPT6H]] (10, 1 ⚠)
- down: [[ABCC3]] (58, 8 ⚠), [[SAMD5]] (50, 10 ⚠), [[ITGA2]] (48, 8 ⚠), [[LINC00342]] (47, 18 ⚠), [[SERPINB3]] (44, 8 ⚠), [[ANKRD36C]] (44, 20 ⚠), [[TNIK]] (43, 9 ⚠), [[SERPINB4]] (42, 11 ⚠), [[CEMIP]] (40, 10 ⚠), [[ITGA3]] (35, 5 ⚠), [[ENSG00000227681]] (34, 5 ⚠), [[OSMR]] (34, 15 ⚠), [[DOCK5]] (33, 8 ⚠), [[RPS6KA3]] (33, 8 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[ENSG00000244468]] (+7.7, ⚠ noise-class RNA), [[S100A9]] (+7.2), [[LINC01440]] (+6.9), [[S100A8]] (+6.7), [[CATSPERB]] (+6.6), [[PRLR]] (+6.6), [[LINC02899]] (+6.5), [[KIF1A]] (+6.3), [[VIPR2]] (+6.2), [[SERPINA3]] (+6.2), [[IKZF3]] (+6.2), [[SERPINB4]] (+6.1), [[RARRES1]] (+6.1), [[PGR]] (+6.1), [[IL1RAPL2]] (+6.1), [[TCN1]] (+6.1) (1,380 genes, 98 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[IGF2BP3]] (-3.8), [[ZNF655]] (-3.7), [[CPNE8]] (-3.7), [[ETS1]] (-3.7), [[AXL]] (-3.7), [[TNFRSF10D]] (-3.7), [[VIM]] (-3.6), [[CCDC88A]] (-3.6), [[LIX1L]] (-3.6), [[KIRREL1]] (-3.6), [[CAVIN1]] (-3.6), [[LGALS1]] (-3.5), [[MIR222HG]] (-3.5), [[DANT2]] (-3.5), [[FKBP10]] (-3.5) (379 genes, 13 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 6): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 59 (0.602; genes ZFP36L1, CHST11, ADAM19, PLK2 / KCNMA1, CSGALNACT1, STC1, BMERB1); component 45 (0.608; genes VCL, NRDC, SCARB1, FERMT2 / NLGN1, RHBDD1, PACS1, PCAT1); component 13 (0.657; genes UGP2, KLF9, TSC22D3, SSBP2 / LUC7L3, PER3, TCP10L, SEMA3A); component 8 (0.677; genes VCP, TXNRD1, DNAJB1, KATNIP / SPRED1, CAPRIN2, SPRY4, SPRY4-AS1)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 13 in all, 13 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 47 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[BRCA2]] | BRCA2 loss of function (7 lines) vs not recorded (41) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, WNK2, ACVR2A |
| [[KMT2D]] | KMT2D altered (any record) (15 lines) vs not recorded (35) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[HNF1A]] | HNF1A loss of function (6 lines) vs not recorded (44) | 1 / 0 / 0 | C 1; 1 with an alert ⚠ | ⚠ tissue-confounded; across organs |
| [[ACVR2A]] | ACVR2A altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with TGFBR2, SETD1B, PRDM2 |
| [[ATM]] | ATM altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[ATM]] | ATM loss of function (6 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[BRCA2]] | BRCA2 altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with WNK2, TGFBR2, PIK3CA |
| [[ERBB2]] | ERBB2 gain of function (3 lines) vs not recorded (47) | 0 / 0 / 0 | — | ⚠ few lines (3 vs 47); tissue-confounded; across organs |
| [[PIK3CA]] | PIK3CA altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3 |
| [[PIK3CA]] | PIK3CA gain of function (9 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, TGFBR2, ACVR2A |
| [[TGFBR2]] | TGFBR2 altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with BRCA2, ACVR2A, PRDM2; TGFBR2 not expressed in 1 of the 8 altered lines |
| [[WNK2]] | WNK2 altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with BRCA2, SETD1B, PRDM2 |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,215 in all, 2,215 with an alert ⚠; shown: the 15 strongest; 2,200 more line sets (2,200 of them with an alert ⚠) not shown; 2,252 genes; 1,897 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[INAVA]], [[MROH3P]] | 29 vs 21 | 11 / 194 / 19 | B 109, C 115; 224 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SLC44A4]] | 37 vs 13 | 9 / 186 / 9 | B 57, C 147; 204 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[EPS8L3]] | 35 vs 15 | 0 / 196 / 1 | B 46, C 151; 197 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CLIC5]] | 37 vs 13 | 4 / 185 / 7 | B 59, C 137; 196 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[B3GNT3]] | 31 vs 19 | 6 / 174 / 6 | B 72, C 114; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GCNT3]] | 38 vs 12 | 2 / 184 / 0 | B 43, C 143; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01559]] | 38 vs 12 | 0 / 182 / 0 | B 36, C 146; 182 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ADGRF1]] | 35 vs 15 | 14 / 138 / 16 | B 64, C 104; 168 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC03040]] | 31 vs 19 | 3 / 147 / 4 | B 38, C 116; 154 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[HS3ST1]] | 31 vs 19 | 3 / 137 / 9 | B 58, C 91; 149 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[HNF4A]] | 34 vs 16 | 0 / 145 / 0 | B 29, C 116; 145 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01819]] | 29 vs 21 | 2 / 141 / 1 | B 27, C 117; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[NPSR1]] | 42 vs 8 | 2 / 142 / 0 | B 26, C 118; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TMC4]] | 26 vs 24 | 3 / 134 / 7 | B 51, C 93; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GPX2]] | 36 vs 14 | 2 / 139 / 0 | B 23, C 118; 141 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 6; `tables/line_effects.parquet` — line == 6
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 6; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 6]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include BT-474

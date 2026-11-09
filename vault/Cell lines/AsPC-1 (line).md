---
cell_line: "AsPC-1"
type: "cell line"
cell_line_id: "CVCL_0152"
depmap_id: "ACH-000222"
organ: "Pancreas"
tp53_status: "altered"
drivers: ["CDKN2A(Frameshift)", "FBXW7(Missense)", "KRAS(Missense)", "RNF43(Stopgain)", "SMAD4(Missense)", "TP53(Frameshift)"]
n_dd_depleted: 10
median_response: 0.975
tags: ["cell-line", "organ/pancreas"]
generated_by: "tahoemap"
---

# AsPC-1

*Pancreas · TP53 altered · CVCL_0152 · ACH-000222*

|  |  |
|---|---|
| Organ | Pancreas |
| TP53 status | altered |
| Drivers | CDKN2A(Frameshift); FBXW7(Missense); KRAS(Missense); RNF43(Stopgain); SMAD4(Missense); TP53(Frameshift) |
| Driver changes | CDKN2A p.L27fs; FBXW7 p.R385C; KRAS p.G12D; RNF43 p.S720*; SMAD4 p.R100T; TP53 p.C135fs |
| Cells over all wells | 2,258,980 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.975 (1 = a typical line) |
| Drug-doses that deplete it | 10 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 7 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 13,366 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 5): the line loses cells relative to the other lines in the same wells. Drug-doses: 10 in all, 3 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -12.6 | -1.19 |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -7.6 | -1.10 |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -6.4 | -1.29 |
| [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -0.49 |
| [[PH-797804 (drug)]] 0.5 µM |  | -3.5 | -0.45 |
| [[Thymol (drug)]] 0.5 µM |  | -3.4 | -0.45 |
| [[GSK1059615 (drug)]] 0.5 µM |  | -3.4 | -0.44 |
| [[Celecoxib (drug)]] 0.5 µM |  | -3.3 | -0.41 |
| [[Minodronic acid (drug)]] 0.5 µM |  | -3.1 | -0.38 |
| [[Tomivosertib (drug)]] 5 µM |  | -3.0 | -0.39 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Citalopram (hydrobromide) (drug)]] 0.5 µM (1.97); [[RMC-6236 (drug)]] 0.5 µM (1.76); [[Posaconazole (drug)]] 5 µM (1.76); [[Radotinib (drug)]] 5 µM (1.70); [[Alpelisib (drug)]] 5 µM (1.69); [[AZD-8055 (drug)]] 0.05 µM (1.69); [[Elimusertib hydrochloride (drug)]] 0.05 µM (1.69); [[Binimetinib (drug)]] 0.5 µM (1.67)
- Weakest: [[Trifluridine (drug)]] 5 µM (0.0568, ⚠ cell-cycle shift); [[Dihydroartemisinin (drug)]] 0.5 µM (0.184); [[Pentamidine (isethionate) (drug)]] 5 µM (0.243); [[Norepinephrine (hydrochloride) (drug)]] 5 µM (0.261); [[Trifluridine (drug)]] 0.5 µM (0.283, ⚠ cell-cycle shift); [[Roxadustat (drug)]] 5 µM (0.308); [[Tucidinostat (drug)]] 0.05 µM (0.308); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (0.319, ⚠ cell-cycle shift); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM (0.367); [[Neratinib (drug)]] 0.05 µM (0.380); [[Docetaxel (Trihydrate) (drug)]] 0.05 µM (0.402)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 5): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[FKBP5]] (25, 5 ⚠), [[TXNIP]] (23, 3 ⚠), [[ABLIM2]] (21), [[COBLL1]] (20), [[ATP1A1]] (20, 5 ⚠), [[LDLRAD3]] (18, 3 ⚠), [[BIRC3]] (18, 4 ⚠), [[IRAK3]] (17), [[PON2]] (17), [[TOP1]] (17, 2 ⚠), [[DIP2C]] (15), [[KIAA0232]] (15, 1 ⚠)
- down: [[PLEK2]] (27, 5 ⚠), [[FERMT1]] (26, 2 ⚠), [[PLCXD1]] (24, 1 ⚠), [[FLNB]] (24, 4 ⚠), [[ASAP2]] (23, 2 ⚠), [[CLMP]] (23, 2 ⚠), [[BMP6]] (23, 5 ⚠), [[PHLDA1]] (22, 1 ⚠), [[ITGA2]] (22, 2 ⚠), [[PPP2R2C]] (22, 7 ⚠), [[ELK3]] (21, 1 ⚠), [[KIAA1549L]] (21, 4 ⚠), [[BMAL2]] (20, 3 ⚠), [[ITGB5]] (18, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[MUC17]] (+8.0), [[DHRS9]] (+7.8), [[FAM83A]] (+7.4), [[KLK10]] (+7.0), [[CDH17]] (+6.1), [[ENSG00000250920]] (+6.1, ⚠ noise-class RNA), [[COL17A1]] (+6.1), [[CEACAM6]] (+5.8), [[CEACAM1]] (+5.8), [[LINC02864]] (+5.7), [[TNFRSF6B]] (+5.7), [[NPSR1]] (+5.6), [[SLC22A3]] (+5.6), [[MYO7B]] (+5.5), [[SLC15A1]] (+5.5), [[VCAN]] (+5.5) (1,039 genes, 48 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[MAP2K4]] (-3.6), [[PLOD2]] (-3.5), [[AKT3]] (-3.5), [[FERMT2]] (-3.4), [[MLLT3]] (-3.4), [[BNIP3]] (-3.4), [[SMARCA1]] (-3.4), [[MPDZ]] (-3.3), [[ENSG00000214265]] (-3.3, ⚠ noise-class RNA), [[LDHB]] (-3.3), [[FKBP10]] (-3.3), [[HDGFL3]] (-3.3), [[MAP1B]] (-3.3), [[TSPAN5]] (-3.3), [[PDGFC]] (-3.2), [[CALD1]] (-3.2) (475 genes, 15 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 5): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 42 (0.597; genes FHOD3, PMEPA1, LINC01505, CAPZB / STARD4, C4orf47, PRKCI, TCF4); component 52 (0.661; genes CHST15, PHLDB2, TNS4, SNTB1 / SH3RF3, LTBP1, FUT8, NRG2); component 19 (0.684; genes DIAPH3, ANLN, TES, HIF1A-AS3 / ETV1, NR4A2, FOSB, FOS)
- Strong here (> 1.5): component 3 (1.59; genes MCL1, NABP1, DUSP6, EGR1 / KCTD3, TMEM123, XPO1, TNRC6A)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 8 in all, 8 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 56 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[FBXW7]] | FBXW7 loss of function (5 lines) vs not recorded (45) | 0 / 1 / 0 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[RNF43]] | RNF43 altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with EP300, ACVR2A |
| [[RNF43]] | RNF43 loss of function (5 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with EP300, MSH6, ACVR2A |
| [[SMAD4]] | SMAD4 loss of function (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; SMAD4 not expressed in 2 of the 6 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,889 in all, 2,889 with an alert ⚠; shown: the 15 strongest; 2,874 more line sets (2,874 of them with an alert ⚠) not shown; 2,956 genes; 2,489 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[ARHGEF38]] | 36 vs 14 | 5 / 172 / 9 | B 49, C 137; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GPX2]] | 36 vs 14 | 2 / 139 / 0 | B 23, C 118; 141 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ATP10B]] | 40 vs 10 | 0 / 140 / 0 | B 27, C 113; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PBK]] | 4 vs 46 | 1 / 138 / 0 | C 139; 139 with an alert ⚠ | within organs | ⚠ few lines (4 vs 46); within organs, on part of the lines |
| [[PROM1]] | 37 vs 13 | 0 / 137 / 0 | B 32, C 105; 137 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TMEM30B]] | 35 vs 15 | 3 / 117 / 17 | B 44, C 93; 137 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[AURKB]] | 4 vs 46 | 2 / 134 / 0 | C 136; 136 with an alert ⚠ | within organs | ⚠ few lines (4 vs 46); within organs, on part of the lines |
| [[TMEM125]] | 33 vs 17 | 3 / 113 / 19 | B 46, C 89; 135 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SLC5A1]] | 36 vs 14 | 2 / 114 / 14 | B 42, C 88; 130 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ST6GALNAC1]] | 37 vs 13 | 1 / 120 / 5 | B 26, C 100; 126 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GRHL2]], [[LINC02967]] | 34 vs 16 | 1 / 92 / 22 | B 60, C 55; 115 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MAL2]] | 31 vs 19 | 6 / 91 / 18 | B 36, C 79; 115 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[RNF183]] | 36 vs 14 | 1 / 108 / 2 | B 27, C 84; 111 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[RAB25]] | 33 vs 17 | 2 / 94 / 14 | B 25, C 85; 110 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PRR15L]] | 38 vs 12 | 0 / 109 / 0 | B 18, C 91; 109 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 5; `tables/line_effects.parquet` — line == 5
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 5; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 5]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include AsPC-1

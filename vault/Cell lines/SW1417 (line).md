---
cell_line: "SW1417"
type: "cell line"
cell_line_id: "CVCL_1717"
depmap_id: "ACH-000236"
organ: "Bowel"
tp53_status: "altered"
drivers: ["APC(Stopgain)", "BRAF(Missense)", "PIK3R1(Deletion)", "TP53(Frameshift)"]
n_dd_depleted: 5
median_response: 0.803
tags: ["cell-line", "organ/bowel"]
generated_by: "tahoemap"
---

# SW1417

*Bowel · TP53 altered · CVCL_1717 · ACH-000236*

|  |  |
|---|---|
| Organ | Bowel |
| TP53 status | altered |
| Drivers | APC(Stopgain); BRAF(Missense); PIK3R1(Deletion); TP53(Frameshift) |
| Driver changes | APC p.R1450*; BRAF p.V600E; TP53 p.C238fs |
| Cells over all wells | 1,921,596 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.803 (1 = a typical line) |
| Drug-doses that deplete it | 5 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 3 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,456 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 46): the line loses cells relative to the other lines in the same wells. Drug-doses: 5 in all, 2 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.2 | -0.80 |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.1 | -0.61 |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -0.27 |
| [[Demeclocycline (drug)]] 5 µM |  | -3.6 | -0.26 |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | -3.6 | -0.24 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Simotinib (drug)]] 0.05 µM (1.88); [[Ivabradine (hydrochloride) (drug)]] 5 µM (1.83, ⚠ unreliable plate only); [[Ranolazine (drug)]] 0.5 µM (1.70); [[Norepinephrine (hydrochloride) (drug)]] 5 µM (1.66); [[Allantoin (drug)]] 0.5 µM (1.46); [[Mifepristone (drug)]] 5 µM (1.43); [[Malotilate (drug)]] 0.5 µM (1.42); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM (1.40); [[Pentoxifylline (drug)]] 0.5 µM (1.39)
- Weakest: [[Saquinavir (drug)]] 0.05 µM (0.143); [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM (0.160); [[BI-3406 (drug)]] 5 µM (0.193); [[Budesonide (drug)]] 0.5 µM (0.196); [[Betamethasone dipropionate (drug)]] 0.05 µM (0.215); [[Betamethasone dipropionate (drug)]] 0.5 µM (0.219); [[Vortioxetine (drug)]] 5 µM (0.236, ⚠ toxic); [[Belumosudil (drug)]] 5 µM (0.237); [[Triamcinolone (drug)]] 0.05 µM (0.251)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 46): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[HSPH1]] (13, 6 ⚠), [[EPB41L2]] (13, 7 ⚠), [[CCDC88A]] (12, 8 ⚠), [[HSPA4L]] (11), [[ZBTB11]] (11, 1 ⚠), [[ACSL3]] (11, 1 ⚠), [[SQSTM1]] (11, 1 ⚠), [[SON]] (11, 2 ⚠), [[TPST1]] (11, 2 ⚠), [[HIBCH]] (11, 4 ⚠), [[STIP1]] (11, 7 ⚠), [[HYCC1]] (10), [[RYBP]] (10), [[CADM1]] (10), [[SPAG9]] (10, 1 ⚠), [[ARID4A]] (9), [[ATP6V1A]] (9), [[KLHL29]] (9), [[ADAMTS17]] (9)
- down: [[JDP2]] (19, 11 ⚠), [[GPRC5A]] (19, 12 ⚠), [[CLMN]] (17, 7 ⚠), [[BABAM2]] (16, 11 ⚠), [[GTF2IRD1]] (15, 8 ⚠), [[SAMD12]] (15, 8 ⚠), [[RAPGEF5]] (14, 6 ⚠), [[SNTB1]] (14, 6 ⚠), [[SNX9]] (14, 7 ⚠), [[PVT1]] (14, 9 ⚠), [[ENSG00000235609]] (14, 13 ⚠), [[MX1]] (13), [[ETV5]] (13, 1 ⚠), [[SMYD3]] (13, 3 ⚠), [[SPRED2]] (13, 3 ⚠), [[EPB41L1]] (13, 9 ⚠), [[SLC7A1]] (12, 1 ⚠), [[LRRK1]] (12, 1 ⚠), [[WWOX]] (12, 2 ⚠), [[SUCLG2]] (11), [[XPOT]] (11, 1 ⚠), [[DUSP6]] (10), [[EIF2AK2]] (9)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[HEPHL1]] (+6.6), [[KRT20]] (+6.5), [[IGFL2-AS1]] (+6.2), [[KLK6]] (+6.2), [[CPLX2]] (+6.1), [[CADPS]] (+6.0), [[MACC1]] (+5.8), [[XKR7]] (+5.8), [[ENSG00000285822]] (+5.8, ⚠ noise-class RNA), [[KCNH8]] (+5.7), [[SRRM3]] (+5.7), [[SCG3]] (+5.7), [[HNF4A]] (+5.7), [[APCDD1]] (+5.6), [[ENSG00000249174]] (+5.6, ⚠ noise-class RNA), [[PHF2P2]] (+5.5), [[NTRK2]] (+5.5) (1,368 genes, 61 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[VIM]] (-3.9), [[NR3C1]] (-3.8), [[PLOD2]] (-3.7), [[ZNF655]] (-3.7), [[BNIP3]] (-3.7), [[OSMR-DT]] (-3.7), [[OSMR]] (-3.6), [[AKT3]] (-3.6), [[STARD13]] (-3.5), [[ENSG00000214265]] (-3.5, ⚠ noise-class RNA), [[HDGFL3]] (-3.5), [[ZNF264]] (-3.5), [[PIK3R1]] (-3.5), [[REST]] (-3.5), [[DNAAF9]] (-3.5), [[MPDZ]] (-3.5) (290 genes, 13 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 46): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.800 to 1.47).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 6 in all, 6 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 58 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[APC]] | APC altered (any record) (10 lines) vs not recorded (40) | 7 / 0 / 0 | C 7; 7 with an alert ⚠ | ⚠ tissue-confounded; across organs; mechanism partly not recorded |
| [[APC]] | APC loss of function (7 lines) vs not recorded (40) | 5 / 0 / 0 | C 5; 5 with an alert ⚠ | ⚠ tissue-confounded; across organs |
| [[BRAF]] | BRAF altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[BRAF]] | BRAF gain of function (7 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[PIK3R1]] | PIK3R1 altered (any record) (5 lines) vs not recorded (45) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; PIK3R1 not expressed in 1 of the 5 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,109 in all, 2,109 with an alert ⚠; shown: the 15 strongest; 2,094 more line sets (2,094 of them with an alert ⚠) not shown; 2,142 genes; 1,804 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[SLC44A4]] | 37 vs 13 | 9 / 186 / 9 | B 57, C 147; 204 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CATSPERB]] | 30 vs 20 | 1 / 147 / 12 | B 50, C 110; 160 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[NPSR1]] | 42 vs 8 | 2 / 142 / 0 | B 26, C 118; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC5B]] | 37 vs 13 | 2 / 135 / 2 | B 33, C 106; 139 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GBP4]] | 20 vs 30 | 13 / 118 / 0 | B 104, C 27; 131 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ST6GALNAC1]] | 37 vs 13 | 1 / 120 / 5 | B 26, C 100; 126 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CEACAM5]] | 39 vs 11 | 4 / 110 / 1 | B 25, C 90; 115 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[DAPP1]] | 39 vs 11 | 3 / 101 / 10 | B 37, C 77; 114 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[RNF183]] | 36 vs 14 | 1 / 108 / 2 | B 27, C 84; 111 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SLC6A14]] | 39 vs 11 | 3 / 101 / 4 | B 29, C 79; 108 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SPOCK1]] | 29 vs 21 | 1 / 62 / 45 | B 58, C 50; 108 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[FAM3D]] | 43 vs 7 | 1 / 103 / 0 | B 16, C 88; 104 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MMP7]] | 39 vs 11 | 5 / 97 / 0 | B 39, C 63; 102 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SAMD9L]] | 18 vs 32 | 11 / 90 / 1 | B 85, C 17; 102 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[APCDD1L]] | 34 vs 16 | 2 / 99 / 0 | B 16, C 85; 101 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 46; `tables/line_effects.parquet` — line == 46
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 46; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 46]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include SW1417

---
cell_line: "HEC-1-A"
type: "cell line"
cell_line_id: "CVCL_0293"
depmap_id: "ACH-000954"
organ: "Uterus"
tp53_status: "altered"
drivers: ["ACVR2A(Missense)", "ARID1A(Missense)", "ARID1A(Stopgain)", "ATM(Missense)", "BRAF(Missense)", "EP300(Missense)", "ERBB2(Missense)", "KMT2D(Missense)", "KRAS(Missense)", "MET(Missense)", "MSH6(Frameshift)", "MSH6(Splice_site)", "MTOR(Missense)", "NF1(Missense)", "PIK3CA(Missense)", "PMS2(Stopgain)", "PRDM2(Missense)", "RNF43(Frameshift)", "SETD1B(Frameshift)", "SMAD4(Missense)", "SMARCA4(Frameshift)", "TP53(Missense)", "ZFHX3(Frameshift)", "ZFHX3(Stopgain)"]
n_dd_depleted: 18
median_response: 0.896
tags: ["cell-line", "organ/uterus"]
generated_by: "tahoemap"
---

# HEC-1-A

*Uterus · TP53 altered · CVCL_0293 · ACH-000954*

|  |  |
|---|---|
| Organ | Uterus |
| TP53 status | altered |
| Drivers | ACVR2A(Missense); ARID1A(Missense); ARID1A(Stopgain); ATM(Missense); BRAF(Missense); EP300(Missense); ERBB2(Missense); KMT2D(Missense); KRAS(Missense); MET(Missense); MSH6(Frameshift); MSH6(Splice_site); MTOR(Missense); NF1(Missense); PIK3CA(Missense); PMS2(Stopgain); PRDM2(Missense); RNF43(Frameshift); SETD1B(Frameshift); SMAD4(Missense); SMARCA4(Frameshift); TP53(Missense); ZFHX3(Frameshift); ZFHX3(Stopgain) |
| Driver changes | ACVR2A p.A349T; ACVR2A p.L329M; ARID1A p.G1544C; ARID1A p.Q1618*; ARID1A p.Q1898*; ARID1A p.Q404H; ATM p.P2353H; BRAF p.R682Q; EP300 p.D1399N; ERBB2 p.T798I; ERBB2 p.V842I; KMT2D p.P2641H; KRAS p.G12D; MET p.V1350D; MSH6 p.F1088fs; MTOR p.R2254M; NF1 p.L792I; PIK3CA p.G1049R; PMS2 p.R802*; PRDM2 p.N1324I; RNF43 p.G659fs; SETD1B p.H8fs; SETD1B p.P1361fs; SMAD4 p.L344S; SMARCA4 p.G271fs; TP53 p.R248Q; ZFHX3 p.R1114*; ZFHX3 p.S2505fs |
| Cells over all wells | 2,514,352 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.896 (1 = a typical line) |
| Drug-doses that deplete it | 18 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 15 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,439 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 9): the line loses cells relative to the other lines in the same wells. Drug-doses: 19 in all, 4 with an alert ⚠; shown: the 12 strongest and the 3 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.9 | -1.07 |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -8.1 | -1.49 |
| [[Filgotinib (drug)]] 0.05 µM |  | -4.4 | -0.50 |
| [[Carbamazepine (drug)]] 5 µM |  | -4.0 | -0.46 |
| [[Rimonabant (drug)]] 5 µM |  | -3.9 | -0.31 |
| [[Tirabrutinib (drug)]] 0.5 µM |  | -3.5 | -0.39 |
| [[Proglumide (drug)]] 0.05 µM |  | -3.4 | -0.40 |
| [[venetoclax (drug)]] 5 µM |  | -3.3 | -0.40 |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | -3.3 | -0.37 |
| [[Lactate (calcium) (drug)]] 5 µM |  | -3.3 | -0.37 |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -3.3 | -0.37 |
| [[Nimesulide (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | -0.38 |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -3.3 | -0.36 |
| [[Levobupivacaine (hydrochloride) (drug)]] 5 µM |  | -3.2 | -0.38 |
| [[Omeprazole (drug)]] 5 µM |  | -3.1 | -0.34 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Posaconazole (drug)]] 5 µM (1.83); [[Malotilate (drug)]] 0.5 µM (1.75); [[Dihydroartemisinin (drug)]] 0.5 µM (1.68); [[Berbamine (dihydrochloride) (drug)]] 5 µM (1.61); [[Berbamine (drug)]] 0.5 µM (1.56); [[Diphenhydramine (drug)]] 5 µM (1.53); [[Tadalafil (drug)]] 5 µM (1.53); [[Fluvoxamine (drug)]] 0.5 µM (1.49)
- Weakest: [[Rosiglitazone (drug)]] 5 µM (-0.147); [[Tofacitinib (drug)]] 5 µM (0.0819); [[Tofacitinib (citrate) (drug)]] 5 µM (0.0858); [[Tofacitinib (drug)]] 0.5 µM (0.142); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (0.159, ⚠ cell-cycle shift); [[Tofacitinib (citrate) (drug)]] 0.5 µM (0.168); [[Verteporfin (drug)]] 0.05 µM (0.194); [[Tofacitinib (citrate) (drug)]] 0.05 µM (0.196); [[Econazole (drug)]] 5 µM (0.240)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 9): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[HSPA4]] (17, 9 ⚠), [[NEAT1]] (14, 3 ⚠), [[PCLO]] (13), [[CLU]] (13, 4 ⚠), [[DNAJB1]] (13, 4 ⚠), [[SORBS1]] (12), [[SUPT6H]] (12), [[HSPA4L]] (12), [[SLFN5]] (12), [[SNX29]] (12, 1 ⚠), [[SQSTM1]] (12, 1 ⚠), [[OXR1]] (12, 1 ⚠), [[ARL13B]] (12, 1 ⚠), [[USP47]] (12, 1 ⚠), [[SPEN]] (12, 3 ⚠), [[KLF10]] (12, 3 ⚠), [[ATP6V1A]] (11)
- down: [[SPRY4-AS1]] (37, 7 ⚠), [[ENSG00000285471]] (27, 8 ⚠), [[ENSG00000260877]] (25, 4 ⚠), [[SIPA1L3]] (25, 8 ⚠), [[DLC1]] (25, 8 ⚠), [[ASAP2]] (23, 5 ⚠), [[CD44]] (23, 7 ⚠), [[ITGA3]] (22, 1 ⚠), [[ELK3]] (22, 2 ⚠), [[HMGA2]] (22, 2 ⚠), [[EPIC1]] (22, 12 ⚠), [[MAP3K5]] (21, 3 ⚠), [[BCAR3]] (21, 7 ⚠), [[NT5E]] (20), [[THSD4]] (17)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[ENSG00000262198]] (+7.1, ⚠ noise-class RNA), [[RHEX]] (+7.0), [[ENSG00000287530]] (+6.5, ⚠ noise-class RNA), [[PAX8]] (+6.2), [[LINC00958]] (+6.0), [[ENSG00000285471]] (+6.0, ⚠ noise-class RNA), [[ENSG00000286546]] (+6.0, ⚠ noise-class RNA), [[DSCAML1]] (+5.9), [[ENSG00000286481]] (+5.8, ⚠ noise-class RNA), [[LINC02999]] (+5.8), [[LINC02899]] (+5.7), [[LINC01036]] (+5.7), [[KRT7]] (+5.5), [[FXYD2]] (+5.5), [[LINC01322]] (+5.5), [[ITGB6]] (+5.4), [[POU5F1]] (+5.4), [[POU3F3]] (+5.3), [[UGT2B7]] (+5.3), [[SYT13]] (+5.3) (1,713 genes, 212 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[VIM]] (-3.8), [[PLOD2]] (-3.7), [[TXNIP]] (-3.7), [[OSMR-DT]] (-3.6), [[AKT3]] (-3.6), [[OSMR]] (-3.6), [[MAGED1]] (-3.5), [[UBB]] (-3.5), [[HLA-A]] (-3.5), [[BACE2]] (-3.5), [[ARID5B]] (-3.4), [[TFCP2]] (-3.4), [[MAP1B]] (-3.4), [[CHIC1]] (-3.3), [[SLC25A43]] (-3.3) (263 genes, 5 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 9): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 13 (0.661; genes UGP2, KLF9, TSC22D3, SSBP2 / LUC7L3, PER3, TCP10L, SEMA3A)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 30 in all, 30 with an alert ⚠; shown: the 15 strongest; 15 more groups (15 of them with an alert ⚠) not shown. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 30 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[KMT2D]] | KMT2D altered (any record) (15 lines) vs not recorded (35) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[SETD1B]] | SETD1B altered (any record) (11 lines) vs not recorded (39) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, ARID1A |
| [[ARID1A]] | ARID1A altered (any record) (15 lines) vs not recorded (35) | 0 / 0 / 1 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[ACVR2A]] | ACVR2A altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with TGFBR2, SETD1B, PRDM2 |
| [[ACVR2A]] | ACVR2A loss of function (7 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B, PRDM2, EP300 |
| [[ARID1A]] | ARID1A loss of function (12 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[ATM]] | ATM altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[ATM]] | ATM loss of function (6 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[BRAF]] | BRAF altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[EP300]] | EP300 altered (any record) (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, SETD1B |
| [[EP300]] | EP300 loss of function (4 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ few lines (4 vs 43); within organs, on part of the lines; co-occurs with RNF43, MSH6, ACVR2A |
| [[ERBB2]] | ERBB2 gain of function (3 lines) vs not recorded (47) | 0 / 0 / 0 | — | ⚠ few lines (3 vs 47); tissue-confounded; across organs |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[MET]] | MET altered (any record) (3 lines) vs not recorded (47) | 0 / 0 / 0 | — | ⚠ few lines (3 vs 47); tissue-confounded; across organs; mechanism partly not recorded; MET not expressed in 1 of the 3 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,147 in all, 2,147 with an alert ⚠; shown: the 15 strongest; 2,132 more line sets (2,132 of them with an alert ⚠) not shown; 2,174 genes; 1,880 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[TMPRSS2]] | 35 vs 15 | 6 / 197 / 18 | B 77, C 144; 221 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TMEM45B]] | 32 vs 18 | 3 / 199 / 12 | B 58, C 156; 214 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SLC44A4]] | 37 vs 13 | 9 / 186 / 9 | B 57, C 147; 204 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CLIC5]] | 37 vs 13 | 4 / 185 / 7 | B 59, C 137; 196 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GCNT3]] | 38 vs 12 | 2 / 184 / 0 | B 43, C 143; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01559]] | 38 vs 12 | 0 / 182 / 0 | B 36, C 146; 182 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TOX3]] | 31 vs 19 | 4 / 168 / 1 | B 46, C 127; 173 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[HNF4A]] | 34 vs 16 | 0 / 145 / 0 | B 29, C 116; 145 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[NPSR1]] | 42 vs 8 | 2 / 142 / 0 | B 26, C 118; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GPX2]] | 36 vs 14 | 2 / 139 / 0 | B 23, C 118; 141 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ATP10B]] | 40 vs 10 | 0 / 140 / 0 | B 27, C 113; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC13]] | 40 vs 10 | 2 / 138 / 0 | B 33, C 107; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC5B]] | 37 vs 13 | 2 / 135 / 2 | B 33, C 106; 139 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PROM1]] | 37 vs 13 | 0 / 137 / 0 | B 32, C 105; 137 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TMEM30B]] | 35 vs 15 | 3 / 117 / 17 | B 44, C 93; 137 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 9; `tables/line_effects.parquet` — line == 9
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 9; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 9]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include HEC-1-A

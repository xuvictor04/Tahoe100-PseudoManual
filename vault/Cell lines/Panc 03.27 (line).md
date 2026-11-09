---
cell_line: "Panc 03.27"
type: "cell line"
cell_line_id: "CVCL_1635"
depmap_id: "ACH-000139"
organ: "Pancreas"
tp53_status: "altered"
drivers: ["ATM(Missense)", "CDKN2A(Deletion)", "CDKN2B(Deletion)", "KRAS(Missense)", "TP53(Splice_site)", "ZFHX3(Missense)"]
n_dd_depleted: 21
median_response: 0.979
tags: ["cell-line", "organ/pancreas"]
generated_by: "tahoemap"
---

# Panc 03.27

*Pancreas · TP53 altered · CVCL_1635 · ACH-000139*

|  |  |
|---|---|
| Organ | Pancreas |
| TP53 status | altered |
| Drivers | ATM(Missense); CDKN2A(Deletion); CDKN2B(Deletion); KRAS(Missense); TP53(Splice_site); ZFHX3(Missense) |
| Driver changes | ATM p.E2351G; KRAS p.G12V; ZFHX3 p.P802A |
| Cells over all wells | 1,699,941 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.979 (1 = a typical line) |
| Drug-doses that deplete it | 21 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 12 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,848 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 41): the line loses cells relative to the other lines in the same wells. Drug-doses: 22 in all, 10 with an alert ⚠; shown: the 12 strongest and the 7 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -9.7 | -0.91 |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -8.8 | -2.51 |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | -0.87 |
| [[Bimiralisib (drug)]] 5 µM |  | -6.7 | -0.81 |
| [[TAK-733 (drug)]] 5 µM |  | -6.0 | -0.80 |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.5 | -0.80 |
| [[venetoclax (drug)]] 5 µM |  | -5.2 | -0.71 |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.1 | -0.96 |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -0.60 |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | -0.80 |
| [[EX229 (drug)]] 5 µM |  | -4.6 | -0.62 |
| [[AZD-8055 (drug)]] 5 µM |  | -4.2 | -0.52 |
| [[Sapanisertib (drug)]] 5 µM |  | -4.1 | -0.49 |
| [[Afatinib (drug)]] 5 µM |  | -4.0 | -0.35 |
| [[XRK3F2 (drug)]] 5 µM |  | -3.9 | -0.47 |
| [[GSK1059615 (drug)]] 5 µM |  | -3.6 | -0.44 |
| [[RMC-6236 (drug)]] 5 µM |  | -3.6 | -0.44 |
| [[Alpelisib (drug)]] 5 µM |  | -3.6 | -0.47 |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -0.44 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Lonafarnib (drug)]] 5 µM (1.96, ⚠ toxic); [[Lopinavir (drug)]] 5 µM (1.82); [[Phenylephrine (hydrochloride) (drug)]] 5 µM (1.79); [[Malotilate (drug)]] 0.5 µM (1.76); [[Mifepristone (drug)]] 5 µM (1.72); [[Elagolix sodium (drug)]] 0.5 µM (1.67); [[Ranolazine (drug)]] 0.5 µM (1.67); [[Econazole (drug)]] 5 µM (1.65); [[Cyclosporin A (drug)]] 0.5 µM (1.63)
- Weakest: [[Pentamidine (isethionate) (drug)]] 5 µM (0.262); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (0.270, ⚠ cell-cycle shift); [[Monocrotaline (drug)]] 0.05 µM (0.308); [[Saquinavir (drug)]] 0.5 µM (0.334); [[Pitavastatin (Calcium) (drug)]] 0.05 µM (0.362); [[Pyridoxine (drug)]] 0.5 µM (0.365); [[Drospirenone (drug)]] 0.5 µM (0.374); [[Orlistat (drug)]] 0.05 µM (0.393); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM (0.397)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 41): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[BIRC3]] (26, 2 ⚠), [[FKBP5]] (26, 6 ⚠), [[CCND3]] (20), [[TFCP2L1]] (19, 4 ⚠), [[TSC22D3]] (18), [[LDLRAD3]] (18), [[CPD]] (17), [[ATP1A1]] (14, 4 ⚠), [[IRAK3]] (13), [[HSPA4]] (13, 7 ⚠), [[G3BP1]] (12, 6 ⚠), [[CCDC88A]] (12, 8 ⚠), [[KLF9]] (11), [[KLF5]] (10), [[ZBTB11]] (9)
- down: [[DHRS3]] (23, 10 ⚠), [[RNF19A]] (21, 8 ⚠), [[DLEU1]] (20, 14 ⚠), [[TFDP2]] (18, 6 ⚠), [[CMTM7]] (18, 8 ⚠), [[BACE2]] (18, 10 ⚠), [[ITGA2]] (17, 3 ⚠), [[TRERF1]] (17, 5 ⚠), [[RHBDF2]] (17, 7 ⚠), [[TMEM51]] (17, 7 ⚠), [[LINC01876]] (17, 10 ⚠), [[ITGB5]] (16), [[CCND1]] (16), [[MYEOV]] (16, 1 ⚠), [[GPRC5A]] (16, 12 ⚠), [[ETV5]] (13), [[ENSG00000260877]] (13), [[IFI44]] (12), [[DUSP6]] (12)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[MUC4]] (+8.2), [[MUC16]] (+7.6), [[KRT17]] (+6.8), [[WFDC2]] (+6.7), [[TACSTD2]] (+6.5), [[HSD11B1]] (+6.4), [[ADGRF1]] (+6.0), [[UCA1]] (+5.8), [[STEAP4]] (+5.7), [[KRT7]] (+5.6), [[HS3ST1]] (+5.6), [[MAL2]] (+5.6), [[G0S2]] (+5.6), [[ITGB6]] (+5.5), [[EHF]] (+5.4) (1,272 genes, 67 with an alert ⚠; shown: the 15 strongest)
- Lacks: [[TUSC3]] (-3.8), [[TMEM168]] (-3.6), [[KCNQ1OT1]] (-3.5), [[MAP1B]] (-3.1), [[TTN-AS1]] (-3.0), [[TBX3]] (-2.9), [[EPIC1]] (-2.9), [[PLCB4]] (-2.9), [[GP6-AS1]] (-2.7), [[LINC01515]] (-2.7), [[LARGE1]] (-2.7), [[CDKN2A]] (-2.7), [[AUTS2]] (-2.7), [[ENSG00000249413]] (-2.6, ⚠ noise-class RNA), [[PTPRS]] (-2.6), [[DCLK2]] (-2.6) (107 genes, 7 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 41): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.854 to 1.41).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 8 in all, 8 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 55 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[CDKN2B]] | CDKN2B loss of function (13 lines) vs not recorded (37) | 4 / 2 / 0 | B 3, C 3; 6 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[ATM]] | ATM altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[ATM]] | ATM loss of function (6 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[ZFHX3]] | ZFHX3 altered (any record) (13 lines) vs not recorded (37) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B, PIK3CA |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,758 in all, 1,758 with an alert ⚠; shown: the 15 strongest; 1,743 more line sets (1,743 of them with an alert ⚠) not shown; 1,781 genes; 1,460 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[EPS8L3]] | 35 vs 15 | 0 / 196 / 1 | B 46, C 151; 197 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GCNT3]] | 38 vs 12 | 2 / 184 / 0 | B 43, C 143; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[HNF4A]] | 34 vs 16 | 0 / 145 / 0 | B 29, C 116; 145 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[NPSR1]] | 42 vs 8 | 2 / 142 / 0 | B 26, C 118; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GPX2]] | 36 vs 14 | 2 / 139 / 0 | B 23, C 118; 141 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ATP10B]] | 40 vs 10 | 0 / 140 / 0 | B 27, C 113; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC13]] | 40 vs 10 | 2 / 138 / 0 | B 33, C 107; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TRIM31]] | 39 vs 11 | 2 / 130 / 0 | B 43, C 89; 132 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[POF1B]] | 34 vs 16 | 2 / 124 / 0 | B 25, C 101; 126 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CYP3A5]] | 32 vs 18 | 6 / 114 / 0 | B 45, C 75; 120 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CEACAM6]] | 37 vs 13 | 2 / 113 / 2 | B 27, C 90; 117 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LGALS4]] | 39 vs 11 | 0 / 116 / 0 | B 23, C 93; 116 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CEACAM5]] | 39 vs 11 | 4 / 110 / 1 | B 25, C 90; 115 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CDH17]] | 40 vs 10 | 1 / 112 / 1 | B 21, C 93; 114 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[RNF183]] | 36 vs 14 | 1 / 108 / 2 | B 27, C 84; 111 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 41; `tables/line_effects.parquet` — line == 41
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 41; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 41]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include Panc 03.27

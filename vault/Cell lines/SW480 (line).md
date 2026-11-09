---
cell_line: "SW480"
type: "cell line"
cell_line_id: "CVCL_0546"
depmap_id: "ACH-000842"
organ: "Bowel"
tp53_status: "altered"
drivers: ["APC(Stopgain)", "ATM(Missense)", "KRAS(Missense)", "MYC(Gain)", "TP53(Missense)"]
n_dd_depleted: 15
median_response: 0.885
tags: ["cell-line", "organ/bowel"]
generated_by: "tahoemap"
---

# SW480

*Bowel · TP53 altered · CVCL_0546 · ACH-000842*

|  |  |
|---|---|
| Organ | Bowel |
| TP53 status | altered |
| Drivers | APC(Stopgain); ATM(Missense); KRAS(Missense); MYC(Gain); TP53(Missense) |
| Driver changes | APC p.Q1338*; ATM p.R2461P; KRAS p.G12V; TP53 p.P309S; TP53 p.R273H |
| Cells over all wells | 6,039,823 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.885 (1 = a typical line) |
| Drug-doses that deplete it | 15 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 8 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,817 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 22): the line loses cells relative to the other lines in the same wells. Drug-doses: 15 in all, 7 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -11.3 | -1.87 |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -10.1 | -1.46 |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.9 | -1.20 |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.2 | -1.11 |
| [[Ipatasertib (drug)]] 0.5 µM |  | -5.4 | -0.62 |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.47 |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.7 | -0.43 |
| [[Alpelisib (drug)]] 5 µM |  | -3.7 | -0.43 |
| [[DT-061 (drug)]] 5 µM |  | -3.5 | -0.42 |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | -3.5 | -0.46 |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.39 |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | -3.4 | -0.39 |
| [[Sonidegib (drug)]] 5 µM |  | -3.3 | -0.41 |
| [[ULK-101 (drug)]] 5 µM |  | -3.3 | -0.39 |
| [[BI-3406 (drug)]] 5 µM |  | -3.1 | -0.35 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[palbociclib (drug)]] 5 µM (1.78); [[Digitoxin (drug)]] 0.05 µM (1.72, ⚠ cell-cycle shift); [[Malotilate (drug)]] 0.5 µM (1.68); [[Binimetinib (drug)]] 0.5 µM (1.65); [[Bexarotene (drug)]] 0.05 µM (1.61); [[Binimetinib (drug)]] 0.05 µM (1.60); [[Irinotecan (drug)]] 0.5 µM (1.60); [[Bexarotene (drug)]] 0.5 µM (1.52); [[Trametinib (drug)]] 0.05 µM (1.50)
- Weakest: [[Monocrotaline (drug)]] 0.05 µM (-0.171); [[Allantoin (drug)]] 0.05 µM (-0.0419, ⚠ transcription drop); [[Orlistat (drug)]] 0.05 µM (0.0608); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM (0.0670); [[Saquinavir (drug)]] 0.5 µM (0.0794); [[Pimozide (drug)]] 0.05 µM (0.143); [[Dexamethasone (drug)]] 0.05 µM (0.145); [[Betamethasone dipropionate (drug)]] 0.5 µM (0.178); [[Econazole (drug)]] 5 µM (0.178)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 22): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[ACSL3]] (19, 3 ⚠), [[PSMD1]] (19, 10 ⚠), [[HSPA4]] (19, 12 ⚠), [[MED27]] (18, 4 ⚠), [[B3GALNT2]] (18, 4 ⚠), [[RYBP]] (17, 2 ⚠), [[ZBTB11]] (17, 5 ⚠), [[LARP4]] (17, 5 ⚠), [[PSMD12]] (17, 9 ⚠), [[STIP1]] (17, 11 ⚠), [[NAA15]] (16, 4 ⚠), [[ODC1]] (16, 10 ⚠), [[LARGE1]] (15, 1 ⚠), [[ARRDC4]] (15, 1 ⚠), [[ZNF277]] (15, 1 ⚠), [[CRAMP1]] (15, 2 ⚠), [[SUPT6H]] (14, 1 ⚠), [[ITPR2]] (14, 1 ⚠), [[CPEB4]] (13), [[ARID5B]] (13)
- down: [[LINC02320]] (38, 9 ⚠), [[ETV1]] (34, 8 ⚠), [[ENSG00000266088]] (33, 4 ⚠), [[ENSG00000258919]] (32, 5 ⚠), [[SPRY4-AS1]] (31, 6 ⚠), [[SH3D19]] (31, 12 ⚠), [[BACE2]] (30, 10 ⚠), [[NAV2]] (30, 15 ⚠), [[NTSR1]] (28, 10 ⚠), [[PDGFA]] (28, 12 ⚠), [[ITGB5]] (26, 6 ⚠), [[TNS4]] (26, 6 ⚠), [[ANO1]] (25, 3 ⚠), [[DPYSL2]] (25, 4 ⚠), [[CDCP1]] (25, 4 ⚠), [[ENSG00000279806]] (25, 4 ⚠), [[CCND1]] (25, 5 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[NKD1]] (+6.3), [[LINC02964]] (+6.2), [[RBP1]] (+6.2), [[ENSG00000287923]] (+6.1, ⚠ noise-class RNA), [[ROBO2]] (+6.1), [[KRT5]] (+5.9), [[TMEM163]] (+5.8), [[PROX1-AS1]] (+5.7), [[ENSG00000213981]] (+5.6, ⚠ noise-class RNA), [[BMP5]] (+5.6), [[JAKMIP2-AS1]] (+5.6), [[SKAP1]] (+5.5), [[PROX1]] (+5.5), [[ENSG00000289605]] (+5.4, ⚠ noise-class RNA), [[APCDD1]] (+5.4), [[LINC01169]] (+5.3), [[FGD5]] (+5.3), [[FGF19]] (+5.3) (1,418 genes, 138 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[ZNF264]] (-3.8), [[SMAD4]] (-3.7), [[OSMR-DT]] (-3.7), [[ZNF655]] (-3.7), [[BNIP3]] (-3.7), [[OSMR]] (-3.7), [[ENSG00000214265]] (-3.6, ⚠ noise-class RNA), [[MPDZ]] (-3.5), [[IFI6]] (-3.5), [[LIFR]] (-3.5), [[SPART]] (-3.4), [[CPNE8]] (-3.4), [[TMED3]] (-3.4), [[NR3C1]] (-3.4), [[TUSC3]] (-3.3), [[MDFIC]] (-3.3) (209 genes, 7 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 22): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Strong here (> 1.5): component 3 (1.62; genes MCL1, NABP1, DUSP6, EGR1 / KCTD3, TMEM123, XPO1, TNRC6A); component 37 (1.59; genes CARS1, MAGI2, PTCHD4, MARS1 / TBL2, MANF, DENND4C, CDR2); component 33 (1.58; genes ITGB8, FBXO32, MAGI1, GULP1 / TPM3, KLF13, SENP7, DSP); component 7 (1.57; genes ARCN1, GOLGB1, LYSMD3, HDLBP / UCK2, MEMO1, SRPK2, PLEKHA5)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 7 in all, 7 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 57 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[APC]] | APC altered (any record) (10 lines) vs not recorded (40) | 7 / 0 / 0 | C 7; 7 with an alert ⚠ | ⚠ tissue-confounded; across organs; mechanism partly not recorded |
| [[APC]] | APC loss of function (7 lines) vs not recorded (40) | 5 / 0 / 0 | C 5; 5 with an alert ⚠ | ⚠ tissue-confounded; across organs |
| [[ATM]] | ATM altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[ATM]] | ATM loss of function (6 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[MYC]] | MYC gain of function (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,782 in all, 1,782 with an alert ⚠; shown: the 15 strongest; 1,767 more line sets (1,767 of them with an alert ⚠) not shown; 1,812 genes; 1,546 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[TMPRSS4]], [[OVOL1]] | 33 vs 17 | 14 / 223 / 24 | B 115, C 146; 261 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SLC44A4]] | 37 vs 13 | 9 / 186 / 9 | B 57, C 147; 204 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GCNT3]] | 38 vs 12 | 2 / 184 / 0 | B 43, C 143; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ADGRF1]] | 35 vs 15 | 14 / 138 / 16 | B 64, C 104; 168 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[HS3ST1]] | 31 vs 19 | 3 / 137 / 9 | B 58, C 91; 149 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[NPSR1]] | 42 vs 8 | 2 / 142 / 0 | B 26, C 118; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[KLK10]] | 34 vs 16 | 2 / 131 / 8 | B 43, C 98; 141 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ATP10B]] | 40 vs 10 | 0 / 140 / 0 | B 27, C 113; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC13]] | 40 vs 10 | 2 / 138 / 0 | B 33, C 107; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC5B]] | 37 vs 13 | 2 / 135 / 2 | B 33, C 106; 139 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TMEM30B]] | 35 vs 15 | 3 / 117 / 17 | B 44, C 93; 137 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TRIM31]] | 39 vs 11 | 2 / 130 / 0 | B 43, C 89; 132 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GBP4]] | 20 vs 30 | 13 / 118 / 0 | B 104, C 27; 131 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[OAS1]] | 13 vs 37 | 23 / 107 / 0 | B 120, C 10; 130 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[OAS2]] | 14 vs 36 | 36 / 91 / 0 | B 111, C 16; 127 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 22; `tables/line_effects.parquet` — line == 22
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 22; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 22]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include SW480

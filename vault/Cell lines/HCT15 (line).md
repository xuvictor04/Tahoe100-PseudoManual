---
cell_line: "HCT15"
type: "cell line"
cell_line_id: "CVCL_0292"
depmap_id: "ACH-000997"
organ: "Bowel"
tp53_status: "altered"
drivers: ["ACVR2A(Frameshift)", "APC(Frameshift)", "APC(Missense)", "APC(Stopgain)", "ARID1A(Missense)", "ATM(Missense)", "B2M(Splice_site)", "B2M(Stopgain)", "BRCA2(Frameshift)", "BRCA2(Missense)", "CHEK2(Missense)", "EP300(Stopgain)", "ERBB3(Missense)", "GNAS(Missense)", "KMT2D(Missense)", "KRAS(Missense)", "MSH6(Frameshift)", "MSH6(Missense)", "NF1(Missense)", "PIK3CA(Missense)", "PIK3R1(Missense)", "POLE(Missense)", "PRDM2(Stopgain)", "RNF43(Frameshift)", "RNF43(Missense)", "SETD1B(Missense)", "SMARCA4(Missense)", "TGFBR2(Missense)", "TP53(Missense)", "TP53(Splice_site)", "WNK2(Missense)", "ZFHX3(Frameshift)", "ZFHX3(Missense)"]
n_dd_depleted: 20
median_response: 0.972
tags: ["cell-line", "organ/bowel"]
generated_by: "tahoemap"
---

# HCT15

*Bowel · TP53 altered · CVCL_0292 · ACH-000997*

|  |  |
|---|---|
| Organ | Bowel |
| TP53 status | altered |
| Drivers | ACVR2A(Frameshift); APC(Frameshift); APC(Missense); APC(Stopgain); ARID1A(Missense); ATM(Missense); B2M(Splice_site); B2M(Stopgain); BRCA2(Frameshift); BRCA2(Missense); CHEK2(Missense); EP300(Stopgain); ERBB3(Missense); GNAS(Missense); KMT2D(Missense); KRAS(Missense); MSH6(Frameshift); MSH6(Missense); NF1(Missense); PIK3CA(Missense); PIK3R1(Missense); POLE(Missense); PRDM2(Stopgain); RNF43(Frameshift); RNF43(Missense); SETD1B(Missense); SMARCA4(Missense); TGFBR2(Missense); TP53(Missense); TP53(Splice_site); WNK2(Missense); ZFHX3(Frameshift); ZFHX3(Missense) |
| Driver changes | ACVR2A p.K437fs; APC p.E2550Q; APC p.I1417fs; APC p.I1779M; APC p.K1561N; APC p.K993N; APC p.R2166*; APC p.R727M; ARID1A p.R270H; ATM p.E586D; B2M p.Y30*; BRCA2 p.A487V; BRCA2 p.N1784fs; BRCA2 p.R2784Q; CHEK2 p.A247D; CHEK2 p.R145W; EP300 p.E1014*; ERBB3 p.R667H; GNAS p.K338N; KMT2D p.E1517D; KMT2D p.P1152H; KMT2D p.P1931H; KRAS p.G13D; MSH6 p.D1171fs; MSH6 p.L290fs; MSH6 p.R1172del; MSH6 p.T1189I; NF1 p.A2596V; NF1 p.A74D; NF1 p.P2456S; PIK3CA p.D549N; PIK3CA p.E545K; PIK3R1 p.P312L; POLE p.A1375V; PRDM2 p.E1259*; PRDM2 p.Q1699*; RNF43 p.G659fs; RNF43 p.L214M; SETD1B p.D159N; SETD1B p.Q780H; SMARCA4 p.R885C; TGFBR2 p.L452P; TP53 p.S241F; WNK2 p.V1971M; ZFHX3 p.E763fs; ZFHX3 p.P1707H; ZFHX3 p.P3069T; ZFHX3 p.R1402C; ZFHX3 p.S1180N |
| Cells over all wells | 1,499,816 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.972 (1 = a typical line) |
| Drug-doses that deplete it | 20 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 14 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,357 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 8): the line loses cells relative to the other lines in the same wells. Drug-doses: 20 in all, 6 with an alert ⚠; shown: the 12 strongest and the 4 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | -8.3 | -1.89 |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.0 | -1.87 |
| [[Alpelisib (drug)]] 5 µM |  | -6.2 | -1.52 |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | -1.29 |
| [[PH-797804 (drug)]] 0.5 µM |  | -4.9 | -1.05 |
| [[Belzutifan (drug)]] 5 µM |  | -4.6 | -1.13 |
| [[GSK1059615 (drug)]] 0.5 µM |  | -4.4 | -0.94 |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | -0.91 |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -4.0 | -0.89 |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -0.88 |
| [[4EGI-1 (drug)]] 5 µM |  | -3.9 | -0.90 |
| [[9-ING-41 (drug)]] 0.5 µM |  | -3.9 | -0.82 |
| [[Thymol (drug)]] 0.5 µM |  | -3.6 | -0.79 |
| [[ULK-101 (drug)]] 0.5 µM |  | -3.5 | -0.73 |
| [[BAY1125976 (drug)]] 0.5 µM |  | -3.4 | -0.70 |
| [[AZD1390 (drug)]] 5 µM |  | -3.4 | -0.74 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Bexarotene (drug)]] 0.05 µM (1.71); [[Cytarabine (drug)]] 0.05 µM (1.70); [[Artesunate (drug)]] 5 µM (1.69, ⚠ cell-cycle shift); [[Futibatinib (drug)]] 0.05 µM (1.67); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM (1.64); [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM (1.61); [[Irinotecan (hydrochloride) (drug)]] 0.5 µM (1.60); [[Sonidegib (drug)]] 0.5 µM (1.58); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM (1.56)
- Weakest: [[Econazole (drug)]] 5 µM (0.255); [[Rosiglitazone (drug)]] 5 µM (0.305); [[Dexamethasone (drug)]] 5 µM (0.352); [[Triamcinolone (drug)]] 0.05 µM (0.372); [[Bentamapimod (drug)]] 5 µM (0.383); [[Finasteride (drug)]] 5 µM (0.386); [[Tofacitinib (citrate) (drug)]] 5 µM (0.400); [[Dexamethasone (drug)]] 0.05 µM (0.403)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 8): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[CLU]] (11, 3 ⚠), [[MALAT1]] (9, 3 ⚠), [[MED13]] (8, 1 ⚠), [[RHOA]] (8, 4 ⚠), [[DNAJB1]] (7), [[RABEP1]] (7, 1 ⚠), [[SLMAP]] (7, 1 ⚠), [[NIPBL]] (7, 1 ⚠), [[NFKB1]] (7, 2 ⚠), [[SON]] (7, 2 ⚠), [[DDX5]] (7, 3 ⚠), [[SFPQ]] (7, 3 ⚠), [[NEDD4L]] (6), [[XPO1]] (6), [[CYLD]] (6), [[ARRDC4]] (6), [[SPAG9]] (6, 1 ⚠)
- down: [[PRELID2]] (19, 9 ⚠), [[PRAG1]] (18, 4 ⚠), [[SPRY4-AS1]] (18, 5 ⚠), [[NR2F2-AS1]] (18, 9 ⚠), [[NIHCOLE]] (18, 13 ⚠), [[RAD51B]] (17, 7 ⚠), [[TMTC2]] (17, 9 ⚠), [[IMMP2L]] (17, 10 ⚠), [[ENSG00000226965]] (17, 10 ⚠), [[SMYD3]] (16, 6 ⚠), [[FHIT]] (16, 9 ⚠), [[LINC01876]] (16, 10 ⚠), [[LUCAT1]] (15, 2 ⚠), [[MIR4435-2HG]] (13), [[ABCC3]] (11), [[CDCP1]] (11), [[PHLDA1]] (11, 1 ⚠), [[ITGA2]] (11, 1 ⚠), [[ETV5]] (11, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[LINC01748]] (+5.9), [[LINC01967]] (+5.8), [[LINC02253]] (+5.6), [[USP9Y]] (+5.6), [[LYPD5]] (+5.5), [[AFAP1-AS1]] (+5.4), [[BSPRY]] (+5.3), [[ANOS2P]] (+5.2), [[ENSG00000286797]] (+5.1, ⚠ noise-class RNA), [[UTY]] (+4.9), [[GRHL2]] (+4.9), [[DDX3Y]] (+4.8), [[ENSG00000289349]] (+4.7, ⚠ noise-class RNA), [[SH3GL2]] (+4.6), [[SLCO1B3]] (+4.6), [[PRSS8]] (+4.6), [[CADPS]] (+4.5) (1,166 genes, 108 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[VIM]] (-3.7), [[ANO6]] (-3.6), [[FERMT2]] (-3.5), [[OSMR-DT]] (-3.5), [[OSMR]] (-3.5), [[CPNE8]] (-3.4), [[BNIP3]] (-3.4), [[SMARCA1]] (-3.4), [[DNAAF9]] (-3.3), [[ELOVL5]] (-3.3), [[ENSG00000214265]] (-3.3, ⚠ noise-class RNA), [[AXL]] (-3.3), [[PMEPA1]] (-3.3), [[HDAC9]] (-3.3), [[MPDZ]] (-3.3), [[LIFR]] (-3.2) (280 genes, 5 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 8): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 13 (0.586; genes UGP2, KLF9, TSC22D3, SSBP2 / LUC7L3, PER3, TCP10L, SEMA3A); component 45 (0.665; genes VCL, NRDC, SCARB1, FERMT2 / NLGN1, RHBDD1, PACS1, PCAT1)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 36 in all, 36 with an alert ⚠; shown: the 15 strongest; 21 more groups (21 of them with an alert ⚠) not shown. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 23 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[APC]] | APC altered (any record) (10 lines) vs not recorded (40) | 7 / 0 / 0 | C 7; 7 with an alert ⚠ | ⚠ tissue-confounded; across organs; mechanism partly not recorded |
| [[APC]] | APC loss of function (7 lines) vs not recorded (40) | 5 / 0 / 0 | C 5; 5 with an alert ⚠ | ⚠ tissue-confounded; across organs |
| [[POLE]] | POLE altered (any record) (8 lines) vs not recorded (42) | 1 / 0 / 0 | A 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[BRCA2]] | BRCA2 loss of function (7 lines) vs not recorded (41) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, WNK2, ACVR2A |
| [[KMT2D]] | KMT2D altered (any record) (15 lines) vs not recorded (35) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[SETD1B]] | SETD1B altered (any record) (11 lines) vs not recorded (39) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, ARID1A |
| [[ARID1A]] | ARID1A altered (any record) (15 lines) vs not recorded (35) | 0 / 0 / 1 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[ACVR2A]] | ACVR2A altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with TGFBR2, SETD1B, PRDM2 |
| [[ACVR2A]] | ACVR2A loss of function (7 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B, PRDM2, EP300 |
| [[ATM]] | ATM altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[B2M]] | B2M altered (any record) (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[B2M]] | B2M loss of function (5 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, NF1, EP300 |
| [[BRCA2]] | BRCA2 altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with WNK2, TGFBR2, PIK3CA |
| [[EP300]] | EP300 altered (any record) (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, SETD1B |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,251 in all, 2,251 with an alert ⚠; shown: the 15 strongest; 2,236 more line sets (2,236 of them with an alert ⚠) not shown; 2,281 genes; 1,954 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[TMPRSS2]] | 35 vs 15 | 6 / 197 / 18 | B 77, C 144; 221 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CLIC5]] | 37 vs 13 | 4 / 185 / 7 | B 59, C 137; 196 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ARHGEF38]] | 36 vs 14 | 5 / 172 / 9 | B 49, C 137; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GCNT3]] | 38 vs 12 | 2 / 184 / 0 | B 43, C 143; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01559]] | 38 vs 12 | 0 / 182 / 0 | B 36, C 146; 182 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TOX3]] | 31 vs 19 | 4 / 168 / 1 | B 46, C 127; 173 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ITGB6]] | 32 vs 18 | 5 / 148 / 18 | B 47, C 124; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ADGRF1]] | 35 vs 15 | 14 / 138 / 16 | B 64, C 104; 168 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01819]] | 29 vs 21 | 2 / 141 / 1 | B 27, C 117; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[NPSR1]] | 42 vs 8 | 2 / 142 / 0 | B 26, C 118; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GPX2]] | 36 vs 14 | 2 / 139 / 0 | B 23, C 118; 141 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ATP10B]] | 40 vs 10 | 0 / 140 / 0 | B 27, C 113; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC13]] | 40 vs 10 | 2 / 138 / 0 | B 33, C 107; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC5B]] | 37 vs 13 | 2 / 135 / 2 | B 33, C 106; 139 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PROM1]] | 37 vs 13 | 0 / 137 / 0 | B 32, C 105; 137 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 8; `tables/line_effects.parquet` — line == 8
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 8; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 8]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include HCT15

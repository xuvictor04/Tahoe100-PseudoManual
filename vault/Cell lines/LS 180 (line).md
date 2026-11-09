---
cell_line: "LS 180"
type: "cell line"
cell_line_id: "CVCL_0397"
depmap_id: "ACH-000957"
organ: "Bowel"
tp53_status: "wild type"
drivers: ["ACVR2A(Frameshift)", "APC(Missense)", "ARID1A(Frameshift)", "BRAF(Missense)", "BRCA2(Frameshift)", "CTNNB1(Missense)", "EP300(Missense)", "HNF1A(Frameshift)", "JAK1(Missense)", "KRAS(Missense)", "PIK3CA(Missense)", "PRDM2(Frameshift)", "PTEN(Missense)", "RNF43(Missense)", "SETD1B(Frameshift)", "STK11(Missense)", "TGFBR2(Frameshift)", "WNK2(Frameshift)", "WNK2(Missense)", "ZFHX3(Frameshift)", "ZFHX3(Missense)"]
n_dd_depleted: 7
median_response: 0.954
tags: ["cell-line", "organ/bowel"]
generated_by: "tahoemap"
---

# LS 180

*Bowel · TP53 wild type · CVCL_0397 · ACH-000957*

|  |  |
|---|---|
| Organ | Bowel |
| TP53 status | wild type |
| Drivers | ACVR2A(Frameshift); APC(Missense); ARID1A(Frameshift); BRAF(Missense); BRCA2(Frameshift); CTNNB1(Missense); EP300(Missense); HNF1A(Frameshift); JAK1(Missense); KRAS(Missense); PIK3CA(Missense); PRDM2(Frameshift); PTEN(Missense); RNF43(Missense); SETD1B(Frameshift); STK11(Missense); TGFBR2(Frameshift); WNK2(Frameshift); WNK2(Missense); ZFHX3(Frameshift); ZFHX3(Missense) |
| Driver changes | ACVR2A p.K437fs; APC p.R1788C; ARID1A p.K1094fs; BRAF p.D211G; BRCA2 p.T3033fs; CTNNB1 p.S45F; EP300 p.G30V; HNF1A p.P291fs; JAK1 p.R681W; KRAS p.G12D; PIK3CA p.H1047R; PRDM2 p.V1490fs; PTEN p.I67K; RNF43 p.K108E; RNF43 p.R389H; SETD1B p.H8fs; SETD1B p.Q1589fs; STK11 p.I46T; TGFBR2 p.K128fs; WNK2 p.A1529T; WNK2 p.D1638fs; ZFHX3 p.A3407fs; ZFHX3 p.D3699G |
| Cells over all wells | 1,828,087 |
| Wells with usable expression | 1,328 (99.9%) |
| Median response strength (β) | 0.954 (1 = a typical line) |
| Drug-doses that deplete it | 7 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 5 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,194 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 16): the line loses cells relative to the other lines in the same wells. Drug-doses: 7 in all, 2 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -8.6 | -4.02 |
| [[Celecoxib (drug)]] 0.5 µM |  | -4.0 | -0.64 |
| [[GSK1059615 (drug)]] 0.5 µM |  | -4.0 | -0.65 |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | -0.81 |
| [[Alpelisib (drug)]] 5 µM |  | -3.3 | -0.55 |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | -3.2 | -0.52 |
| [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -0.49 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 488, 84 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Berbamine (drug)]] 0.5 µM (2.40); [[DTP3 (drug)]] 5 µM (1.76); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM (1.75); [[BAY1125976 (drug)]] 5 µM (1.68); [[Berbamine (dihydrochloride) (drug)]] 5 µM (1.65); [[Raltitrexed (drug)]] 5 µM (1.65, ⚠ cell-cycle shift); [[Vandetanib (drug)]] 5 µM (1.65); [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM (1.62); [[Berbamine (drug)]] 0.05 µM (1.60)
- Weakest: [[Tofacitinib (drug)]] 5 µM (0.155); [[Ferulic acid (drug)]] 0.5 µM (0.165); [[Tofacitinib (citrate) (drug)]] 5 µM (0.166); [[Naproxen (drug)]] 0.05 µM (0.173); [[Ixazomib (drug)]] 5 µM (0.225); [[Allantoin (drug)]] 0.05 µM (0.240, ⚠ transcription drop); [[Tofacitinib (drug)]] 0.5 µM (0.252); [[Tofacitinib (citrate) (drug)]] 0.5 µM (0.252); [[Dexamethasone (drug)]] 0.05 µM (0.255)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 16): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[HSPA4]] (15, 7 ⚠), [[CLU]] (14, 3 ⚠), [[YWHAG]] (14, 3 ⚠), [[SAMD4A]] (14, 5 ⚠), [[SQSTM1]] (13, 1 ⚠), [[B3GALNT2]] (13, 1 ⚠), [[ELOVL5]] (13, 3 ⚠), [[XPO1]] (13, 4 ⚠), [[ABTB2]] (13, 5 ⚠), [[HSPH1]] (13, 7 ⚠), [[DOCK4]] (12, 2 ⚠), [[TIGAR]] (12, 3 ⚠), [[CTNNAL1]] (12, 11 ⚠), [[SORBS1]] (11), [[ATP6V0A1]] (11, 1 ⚠), [[BACH2]] (11, 1 ⚠), [[TXNDC16]] (10), [[CPEB4]] (10), [[ATP6V1A]] (10)
- down: [[TNS4]] (28, 4 ⚠), [[ADAM19]] (26, 6 ⚠), [[ST3GAL1]] (23, 6 ⚠), [[ILDR2]] (23, 12 ⚠), [[PTPRR]] (23, 15 ⚠), [[PRELID2]] (22, 12 ⚠), [[IL33]] (21, 5 ⚠), [[PTPRB]] (21, 13 ⚠), [[CEMIP]] (21, 16 ⚠), [[LINC02320]] (20, 2 ⚠), [[GTF2IRD1]] (20, 9 ⚠), [[FAM114A1]] (20, 12 ⚠), [[ETV4]] (19, 3 ⚠), [[MAML2]] (19, 6 ⚠), [[ITGB5]] (17, 1 ⚠), [[RIN2]] (16, 3 ⚠), [[SH3PXD2A]] (16, 4 ⚠), [[IL20RA]] (15, 3 ⚠), [[NT5E]] (12)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[PIGR]] (+8.0), [[MUC6]] (+7.9), [[ONECUT3]] (+7.4), [[CADPS]] (+7.3), [[MUC5AC]] (+7.2), [[NPSR1]] (+7.1), [[GRIN2B]] (+6.8), [[CDH17]] (+6.6), [[MUC5B]] (+6.6), [[LINC02582]] (+6.5), [[GPA33]] (+6.5), [[TNS4]] (+6.5), [[HEPH]] (+6.5), [[PCK1]] (+6.3), [[ENSG00000250920]] (+6.2, ⚠ noise-class RNA), [[MUC17]] (+6.1) (1,435 genes, 85 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[VIM]] (-4.0), [[NR3C1]] (-4.0), [[QKI]] (-4.0), [[RBMS1]] (-3.8), [[DIP2C]] (-3.7), [[TANC2]] (-3.7), [[UBE2E2]] (-3.7), [[FERMT2]] (-3.7), [[AKT3]] (-3.7), [[ZNF655]] (-3.7), [[OSMR-DT]] (-3.6), [[DMXL2]] (-3.6), [[OSMR]] (-3.6), [[SMARCA1]] (-3.6), [[DNAAF9]] (-3.6) (302 genes, 4 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 16): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.764 to 1.28).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 28 in all, 28 with an alert ⚠; shown: the 15 strongest; 13 more groups (13 of them with an alert ⚠) not shown. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 32 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[APC]] | APC altered (any record) (10 lines) vs not recorded (40) | 7 / 0 / 0 | C 7; 7 with an alert ⚠ | ⚠ tissue-confounded; across organs; mechanism partly not recorded |
| [[BRCA2]] | BRCA2 loss of function (7 lines) vs not recorded (41) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, WNK2, ACVR2A |
| [[SETD1B]] | SETD1B altered (any record) (11 lines) vs not recorded (39) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, ARID1A |
| [[ARID1A]] | ARID1A altered (any record) (15 lines) vs not recorded (35) | 0 / 0 / 1 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[HNF1A]] | HNF1A loss of function (6 lines) vs not recorded (44) | 1 / 0 / 0 | C 1; 1 with an alert ⚠ | ⚠ tissue-confounded; across organs |
| [[ACVR2A]] | ACVR2A altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with TGFBR2, SETD1B, PRDM2 |
| [[ACVR2A]] | ACVR2A loss of function (7 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B, PRDM2, EP300 |
| [[ARID1A]] | ARID1A loss of function (12 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[BRAF]] | BRAF altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[BRCA2]] | BRCA2 altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with WNK2, TGFBR2, PIK3CA |
| [[CTNNB1]] | CTNNB1 altered (any record) (5 lines) vs not recorded (45) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[CTNNB1]] | CTNNB1 gain of function (4 lines) vs not recorded (45) | 0 / 0 / 0 | — | ⚠ few lines (4 vs 45); within organs, on part of the lines |
| [[EP300]] | EP300 altered (any record) (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, SETD1B |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[PIK3CA]] | PIK3CA altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3 |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,350 in all, 2,350 with an alert ⚠; shown: the 15 strongest; 2,335 more line sets (2,335 of them with an alert ⚠) not shown; 2,392 genes; 2,041 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[PROM1]] | 37 vs 13 | 0 / 137 / 0 | B 32, C 105; 137 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GBP4]] | 20 vs 30 | 13 / 118 / 0 | B 104, C 27; 131 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[HSD17B2]] | 35 vs 15 | 1 / 126 / 0 | B 30, C 97; 127 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GBP1]] | 16 vs 34 | 4 / 106 / 1 | B 92, C 19; 111 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[IFI6]] | 13 vs 37 | 39 / 72 / 0 | B 100, C 11; 111 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SPOCK1]] | 29 vs 21 | 1 / 62 / 45 | B 58, C 50; 108 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MMP7]] | 39 vs 11 | 5 / 97 / 0 | B 39, C 63; 102 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[APCDD1L]] | 34 vs 16 | 2 / 99 / 0 | B 16, C 85; 101 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC4]] | 41 vs 9 | 1 / 93 / 4 | B 25, C 73; 98 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ITGA11]] | 34 vs 16 | 2 / 95 / 0 | B 19, C 78; 97 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01411]] | 38 vs 12 | 0 / 97 / 0 | B 13, C 84; 97 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TACSTD2]] | 34 vs 16 | 2 / 94 / 1 | B 17, C 80; 97 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PDGFRB]] | 36 vs 14 | 1 / 94 / 1 | B 21, C 75; 96 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[FRK]] | 22 vs 28 | 3 / 84 / 7 | B 44, C 50; 94 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[STEAP4]] | 38 vs 12 | 2 / 87 / 5 | B 27, C 67; 94 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 16; `tables/line_effects.parquet` — line == 16
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 16; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 16]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include LS 180

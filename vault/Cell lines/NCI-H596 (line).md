---
cell_line: "NCI-H596"
type: "cell line"
cell_line_id: "CVCL_1571"
depmap_id: "ACH-000628"
organ: "Lung"
tp53_status: "altered"
drivers: ["KMT2D(Missense)", "PIK3CA(Missense)", "RB1(Frameshift)", "TGFBR2(Frameshift)", "TP53(Missense)"]
n_dd_depleted: null
median_response: 0.169
tags: ["cell-line", "organ/lung"]
generated_by: "tahoemap"
---

# NCI-H596

*Lung · TP53 altered · CVCL_1571 · ACH-000628*

|  |  |
|---|---|
| Organ | Lung |
| TP53 status | altered |
| Drivers | KMT2D(Missense); PIK3CA(Missense); RB1(Frameshift); TGFBR2(Frameshift); TP53(Missense) |
| Driver changes | KMT2D p.M4058V; PIK3CA p.E545K; RB1 p.S182fs; TGFBR2 p.S75fs; TP53 p.G245C |
| Cells over all wells | 18,337 |
| Wells with usable expression | 27 (2.03%) |
| Median response strength (β) | 0.169 (1 = a typical line) |
| Drug-doses that deplete it | not measured (the line is not in the growth analysis) |
| Genes it measures (expresses above the ambient level) | 16,641 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 39): the line loses cells relative to the other lines in the same wells. Drug-doses: none. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

None.

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 9, 3 with an alert ⚠. The 4 strongest and weakest, and any of the 4 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Citalopram (hydrobromide) (drug)]] 0.05 µM (0.942); [[Bimiralisib (drug)]] 5 µM (0.569); [[Trametinib (drug)]] 5 µM (0.489, ⚠ cell-cycle shift); [[Irinotecan (drug)]] 5 µM (0.357)
- Weakest: [[Epirubicin (hydrochloride) (drug)]] 5 µM (-0.0622, ⚠ cell-cycle shift); [[Adagrasib (drug)]] 0.05 µM (0, ⚠ position not correctable); [[Everolimus (drug)]] 5 µM (0.0183); [[Elimusertib hydrochloride (drug)]] 0.5 µM (0.110)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 39): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[BMAL2]] (2), [[OPHN1]] (2), [[HIRA]] (2), [[UQCC1]] (2), [[FSD1L]] (2), [[ATE1]] (2), [[ASCC3]] (2), [[GALNT1]] (2), [[GNA12]] (2), [[AGPAT3]] (2), [[RBM10]] (2), [[MMP1]] (2), [[VPS13D]] (2, 1 ⚠), [[RELB]] (2, 1 ⚠), [[OPTN]] (2, 1 ⚠), [[FANCI]] (2, 1 ⚠)
- down: [[UQCC1]] (4), [[GALNT1]] (4, 1 ⚠), [[VAPA]] (3), [[VPS4B]] (3), [[AGPAT3]] (3), [[UBE2V2]] (3), [[TGOLN2]] (3, 1 ⚠), [[KCNMA1]] (3, 2 ⚠), [[ALS2]] (2), [[ST3GAL1]] (2), [[CDH1]] (2), [[SNX29]] (2), [[FAF2]] (2), [[PODXL]] (2), [[KDM7A]] (2, 1 ⚠), [[BMAL2]] (2, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[LHFPL3-AS1]] (+4.2), [[LINC03000]] (+4.1), [[ENSG00000286329]] (+4.0, ⚠ noise-class RNA), [[LINC01035]] (+4.0), [[SGIP1]] (+4.0), [[ENSG00000238054]] (+3.8, ⚠ noise-class RNA), [[NKD1]] (+3.8), [[LINC00824]] (+3.7), [[CHL1]] (+3.7), [[ROBO2]] (+3.7), [[LINC01446]] (+3.7), [[CALCA]] (+3.7), [[EPB41L3]] (+3.7), [[TBXT]] (+3.7), [[IGFBP5]] (+3.7), [[COL6A3]] (+3.7), [[UTY]] (+3.7) (1,335 genes, 144 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: none

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 39): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 55 (-0.307; genes FAM135A, SSBP3, MTSS1, FGD4 / RNF24, SLC25A36, MAP3K20, CDCP1); component 16 (-0.147; genes EXT1, CEP63, MB21D2, ARHGAP29 / CEP295, ABHD3, FANCI, SPATS2); component 57 (-0.147; genes UGDH, PIR, CLDN12, PELI2 / CCN1, BMERB1, STC1, F3); component 60 (-0.0961; genes STK17A, FAT1, JAG1, NRP2 / ADGRF1, ANKS1B, PCBP3, TMCC3)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 8 in all, 8 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 55 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[RB1]] | RB1 loss of function (3 lines) vs not recorded (46) | 2 / 1 / 0 | C 3; 3 with an alert ⚠ | ⚠ few lines (3 vs 46); tissue-confounded; across organs |
| [[RB1]] | RB1 altered (any record) (4 lines) vs not recorded (46) | 2 / 0 / 0 | C 2; 2 with an alert ⚠ | ⚠ few lines (4 vs 46); tissue-confounded; across organs; mechanism partly not recorded |
| [[KMT2D]] | KMT2D altered (any record) (15 lines) vs not recorded (35) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[PIK3CA]] | PIK3CA altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3 |
| [[PIK3CA]] | PIK3CA gain of function (9 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, TGFBR2, ACVR2A |
| [[TGFBR2]] | TGFBR2 altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with BRCA2, ACVR2A, PRDM2; TGFBR2 not expressed in 1 of the 8 altered lines |
| [[TGFBR2]] | TGFBR2 loss of function (7 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with PRDM2, BRCA2, ACVR2A; TGFBR2 not expressed in 1 of the 7 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2 in all, 2 with an alert ⚠; 2 genes; 1 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[ZBED2]] | 39 vs 11 | 0 / 20 / 0 | B 6, C 14; 20 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PREX2]] | 45 vs 5 | 0 / 0 / 0 | — | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 39; `tables/line_effects.parquet` — line == 39
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 39; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 39]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include NCI-H596

---
cell_line: "NCI-H2122"
type: "cell line"
cell_line_id: "CVCL_1531"
depmap_id: "ACH-000311"
organ: "Lung"
tp53_status: "altered"
drivers: ["CDKN2A(Deletion)", "CDKN2B(Deletion)", "KRAS(Missense)", "MYC(Gain)", "STK11(Frameshift)", "TP53(Missense)"]
n_dd_depleted: null
median_response: 0.57
tags: ["cell-line", "organ/lung"]
generated_by: "tahoemap"
---

# NCI-H2122

*Lung · TP53 altered · CVCL_1531 · ACH-000311*

|  |  |
|---|---|
| Organ | Lung |
| TP53 status | altered |
| Drivers | CDKN2A(Deletion); CDKN2B(Deletion); KRAS(Missense); MYC(Gain); STK11(Frameshift); TP53(Missense) |
| Driver changes | KRAS p.G12C; STK11 p.P281fs; TP53 p.C176F; TP53 p.Q16L |
| Cells over all wells | 28,626 |
| Wells with usable expression | 250 (18.8%) |
| Median response strength (β) | 0.570 (1 = a typical line) |
| Drug-doses that deplete it | not measured (the line is not in the growth analysis) |
| Genes it measures (expresses above the ambient level) | 16,638 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 36): the line loses cells relative to the other lines in the same wells. Drug-doses: none. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

None.

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 92, 15 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM (1.93); [[Sodium Salicylate (drug)]] 5 µM (1.41); [[Everolimus (drug)]] 5 µM (1.35); [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM (1.25); [[Abiraterone acetate (drug)]] 0.05 µM (1.23); [[Rapamycin (drug)]] 0.05 µM (1.18); [[Clotrimazole (drug)]] 5 µM (1.18); [[Bimatoprost (drug)]] 0.5 µM (1.17)
- Weakest: [[Loperamide (hydrochloride) (drug)]] 0.5 µM (-0.500); [[NG25 (drug)]] 0.05 µM (-0.193); [[Entecavir (monohydrate) (drug)]] 0.5 µM (-0.188); [[Pralsetinib (drug)]] 0.05 µM (-0.181); [[Tofacitinib (citrate) (drug)]] 0.05 µM (-0.0586); [[HI-TOPK-032 (drug)]] 0.5 µM (-0.0444); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM (6.1e-04); [[Tofacitinib (citrate) (drug)]] 5 µM (0.0212)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 36): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[CXCL3]] (3, 1 ⚠), [[AASS]] (1), [[DCT]] (1), [[SNX16]] (1), [[PPM1H]] (1), [[CC2D1A]] (1), [[SLC2A1-DT]] (1), [[ENSG00000289605]] (1), [[CALCA]] (1, 1 ⚠), [[KIF23]] (1, 1 ⚠), [[KSR1]] (1, 1 ⚠)
- down: [[PXK]] (2), [[ZNF654]] (2), [[NRG3]] (2, 1 ⚠), [[ZFAT]] (1), [[PLD1]] (1), [[XRCC5]] (1), [[TBC1D10A]] (1), [[SNX16]] (1), [[SPATA6L]] (1), [[STX2]] (1), [[VEGFA]] (1), [[CLINT1]] (1), [[GCA]] (1), [[NCOA1]] (1, 1 ⚠), [[CNOT2]] (1, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[KRT17]] (+7.3), [[ATP2C2]] (+7.1), [[S100A9]] (+6.7), [[MUC16]] (+6.7), [[STEAP4]] (+6.3), [[ENSG00000288087]] (+6.0, ⚠ noise-class RNA), [[IL1RN]] (+5.9), [[XIST]] (+5.8), [[SLC6A14]] (+5.5), [[FAM83A]] (+5.1), [[CEACAM5]] (+5.1), [[RSPO3]] (+5.0), [[SMOC1]] (+5.0), [[CEACAM6]] (+5.0), [[NECTIN4]] (+4.9), [[SLC24A3]] (+4.9) (1,533 genes, 124 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: none

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 36): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 43 (-0.0675; genes MYO5B, TRPS1, FGD6, OCLN / LIMK2, TGFBR1, CYB5B, ITPK1); component 24 (0.00206; genes GOT1, YARS1, DDIT3, AARS1 / ASCC3, ADAM32, GPRC5D-AS1, LUC7L3); component 36 (0.0164; genes MIR34AHG, POLH, STAT3, CCNG1 / PLCB1, LINGO2, SATB2, WDR76); component 28 (0.0225; genes OGDH, TTC17, LINC00598, ABCC3 / CCN1, DTNA, JUN, FNIP2)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 7 in all, 7 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 57 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[CDKN2B]] | CDKN2B loss of function (13 lines) vs not recorded (37) | 4 / 2 / 0 | B 3, C 3; 6 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[MYC]] | MYC gain of function (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[STK11]] | STK11 loss of function (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 5 in all, 5 with an alert ⚠; 5 genes; 4 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[CTSE]] | 42 vs 8 | 0 / 30 / 0 | B 7, C 23; 30 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MYLK2]] | 3 vs 47 | 0 / 6 / 0 | C 6; 6 with an alert ⚠ | within organs | ⚠ few lines (3 vs 47); within organs, on part of the lines |
| [[PPP1R14A]] | 39 vs 11 | 0 / 2 / 0 | B 2; 2 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[VCAM1]] | 40 vs 10 | 0 / 1 / 0 | C 1; 1 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ENSG00000286853]] | 42 vs 8 | 0 / 0 / 0 | — | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 36; `tables/line_effects.parquet` — line == 36
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 36; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 36]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include NCI-H2122

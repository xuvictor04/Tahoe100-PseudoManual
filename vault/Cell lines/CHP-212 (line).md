---
cell_line: "CHP-212"
type: "cell line"
cell_line_id: "CVCL_1125"
depmap_id: "ACH-000120"
organ: "Peripheral Nervous System"
tp53_status: "wild type"
drivers: ["NRAS(Missense)"]
n_dd_depleted: 42
median_response: 0.946
tags: ["cell-line", "organ/peripheral-nervous-system"]
generated_by: "tahoemap"
---

# CHP-212

*Peripheral Nervous System · TP53 wild type · CVCL_1125 · ACH-000120*

|  |  |
|---|---|
| Organ | Peripheral Nervous System |
| TP53 status | wild type |
| Drivers | NRAS(Missense) |
| Driver changes | NRAS p.Q61K |
| Cells over all wells | 537,744 |
| Wells with usable expression | 1,322 (99.5%) |
| Median response strength (β) | 0.946 (1 = a typical line) |
| Drug-doses that deplete it | 42 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 34 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,528 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 29): the line loses cells relative to the other lines in the same wells. Drug-doses: 42 in all, 8 with an alert ⚠; shown: the 12 strongest and the 4 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -7.7 | -1.47 |
| [[RMC-6236 (drug)]] 5 µM |  | -7.7 | -2.36 |
| [[Bimiralisib (drug)]] 5 µM |  | -7.7 | -2.32 |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.4 | -1.61 |
| [[GSK1059615 (drug)]] 5 µM |  | -7.0 | -2.15 |
| [[Binimetinib (drug)]] 0.5 µM |  | -6.7 | -1.28 |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.6 | -1.96 |
| [[Binimetinib (drug)]] 0.05 µM |  | -6.2 | -1.15 |
| [[Binimetinib (drug)]] 5 µM |  | -6.1 | -1.24 |
| [[Trametinib (drug)]] 0.5 µM |  | -6.0 | -1.15 |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -2.18 |
| [[AT7519 (drug)]] 5 µM |  | -5.4 | -1.76 |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -5.3 | -1.34 |
| [[Ponatinib (drug)]] 5 µM |  | -5.2 | -1.30 |
| [[BI-3406 (drug)]] 5 µM |  | -5.1 | -1.55 |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | -5.1 | -1.46 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 484, 82 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Glycyrrhizic acid (drug)]] 0.05 µM (2.36); [[Naproxen (drug)]] 0.05 µM (2.25); [[Saquinavir (drug)]] 0.05 µM (2.23); [[Pimozide (drug)]] 0.5 µM (2.14, ⚠ transcription drop); [[Roxadustat (drug)]] 0.05 µM (2.05); [[Tofacitinib (citrate) (drug)]] 0.05 µM (2.02); [[Pimozide (drug)]] 0.05 µM (1.89); [[Futibatinib (drug)]] 0.05 µM (1.84); [[Flumatinib (mesylate) (drug)]] 0.5 µM (1.81)
- Weakest: [[Irinotecan (drug)]] 0.5 µM (-0.297); [[Malotilate (drug)]] 0.5 µM (-0.184); [[RMC-6236 (drug)]] 0.05 µM (-0.107); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM (-0.0583); [[NG25 (drug)]] 0.05 µM (0.0447); [[Pentoxifylline (drug)]] 0.5 µM (0.175); [[Neratinib (drug)]] 0.5 µM (0.181); [[Temsirolimus (drug)]] 5 µM (0.184)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 29): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[HSPH1]] (11, 7 ⚠), [[ASH1L]] (8, 1 ⚠), [[GPBP1]] (8, 4 ⚠), [[HSP90AA1]] (8, 4 ⚠), [[PCLO]] (6), [[DNAJB1]] (6, 2 ⚠), [[KLF10]] (5), [[HSPA8]] (5, 1 ⚠), [[HSPD1]] (5, 1 ⚠), [[MED13]] (4), [[MDM2]] (4), [[CHD2]] (4), [[HSP90AB1]] (4, 1 ⚠), [[APLP2]] (4, 3 ⚠)
- down: [[PTPRD]] (18, 8 ⚠), [[IFI44L]] (17, 2 ⚠), [[ENSG00000286134]] (17, 11 ⚠), [[MX2]] (14, 2 ⚠), [[MX1]] (14, 3 ⚠), [[CDH10]] (14, 9 ⚠), [[LSAMP]] (14, 11 ⚠), [[LIMCH1]] (13, 6 ⚠), [[SYTL3]] (12, 4 ⚠), [[MEIS2]] (12, 6 ⚠), [[ANGPT1]] (12, 9 ⚠), [[PTPRE]] (11, 1 ⚠), [[EIF2AK2]] (10), [[RIGI]] (10, 1 ⚠), [[NPAS2]] (10, 1 ⚠), [[DIAPH2]] (9, 1 ⚠), [[ETV5]] (8), [[TFPI]] (7)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[HGF]] (+9.1), [[CDH10]] (+8.4), [[HAND2-AS1]] (+8.2), [[LRFN5]] (+8.0), [[SLITRK6]] (+7.8), [[ENSG00000251294]] (+7.7, ⚠ noise-class RNA), [[MIR3681HG]] (+7.5), [[LINC02506]] (+7.4), [[ENSG00000285822]] (+7.3, ⚠ noise-class RNA), [[COL3A1]] (+7.3), [[ENSG00000239268]] (+7.2, ⚠ noise-class RNA), [[UNC5C]] (+7.2), [[LGR5]] (+6.9), [[KLHL13]] (+6.9), [[KC6]] (+6.9), [[RUNX1T1]] (+6.7), [[LINC02268]] (+6.7), [[IGF2]] (+6.7) (1,361 genes, 91 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[SKAP2]] (-3.1), [[PARVA]] (-3.1), [[TNFRSF10D]] (-3.1), [[IFITM3]] (-3.0), [[MSN]] (-3.0), [[CDCP1]] (-3.0), [[PRELID2]] (-3.0), [[PTER]] (-3.0), [[MIR924HG]] (-2.9), [[MICA]] (-2.9), [[TES]] (-2.8), [[SLC35D2]] (-2.8), [[MYC]] (-2.8), [[LTBR]] (-2.8), [[MGMT]] (-2.8) (270 genes, 16 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 29): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 34 (0.371; genes MAP3K14, MYH9, TMEM41B, VMP1 / BACE2, ABHD17C, MARCHF3, MTSS1); component 14 (0.410; genes PNPT1, HILPDA, P4HB, ASCC3 / MBOAT2, SMARCA2, CSNK1G3, MACO1); component 51 (0.427; genes EPHB2, PLCXD1, ATP1B1, RUNX1 / RBMS2, AP1S3, PMEPA1, MBP); component 59 (0.429; genes ZFP36L1, CHST11, ADAM19, PLK2 / KCNMA1, CSGALNACT1, STC1, BMERB1)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 1 in all, 1 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 63 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[NRAS]] | NRAS gain of function (7 lines) vs not recorded (43) | 0 / 2 / 0 | C 2; 2 with an alert ⚠ | ⚠ within organs, on part of the lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,995 in all, 1,995 with an alert ⚠; shown: the 15 strongest; 1,980 more line sets (1,980 of them with an alert ⚠) not shown; 2,036 genes; 1,703 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[TMPRSS4]], [[OVOL1]] | 33 vs 17 | 14 / 223 / 24 | B 115, C 146; 261 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[IRF6]], [[C1orf116]] | 31 vs 19 | 18 / 216 / 24 | B 128, C 130; 258 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ST14]] | 32 vs 18 | 11 / 196 / 21 | B 88, C 140; 228 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[INAVA]], [[MROH3P]] | 29 vs 21 | 11 / 194 / 19 | B 109, C 115; 224 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TMPRSS2]] | 35 vs 15 | 6 / 197 / 18 | B 77, C 144; 221 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TMEM45B]] | 32 vs 18 | 3 / 199 / 12 | B 58, C 156; 214 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SLC44A4]] | 37 vs 13 | 9 / 186 / 9 | B 57, C 147; 204 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[EPS8L3]] | 35 vs 15 | 0 / 196 / 1 | B 46, C 151; 197 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CLIC5]] | 37 vs 13 | 4 / 185 / 7 | B 59, C 137; 196 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ARHGEF38]] | 36 vs 14 | 5 / 172 / 9 | B 49, C 137; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[B3GNT3]] | 31 vs 19 | 6 / 174 / 6 | B 72, C 114; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GCNT3]] | 38 vs 12 | 2 / 184 / 0 | B 43, C 143; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01559]] | 38 vs 12 | 0 / 182 / 0 | B 36, C 146; 182 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TOX3]] | 31 vs 19 | 4 / 168 / 1 | B 46, C 127; 173 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ITGB6]] | 32 vs 18 | 5 / 148 / 18 | B 47, C 124; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 29; `tables/line_effects.parquet` — line == 29
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 29; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 29]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include CHP-212

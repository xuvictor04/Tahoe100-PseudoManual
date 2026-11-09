---
cell_line: "NCI-H2030"
type: "cell line"
cell_line_id: "CVCL_1517"
depmap_id: "ACH-000521"
organ: "Lung"
tp53_status: "altered"
drivers: ["KRAS(Missense)", "POLE(Missense)", "STK11(Missense)", "STK11(Stopgain)", "TP53(Missense)"]
n_dd_depleted: 15
median_response: 0.957
tags: ["cell-line", "organ/lung"]
generated_by: "tahoemap"
---

# NCI-H2030

*Lung · TP53 altered · CVCL_1517 · ACH-000521*

|  |  |
|---|---|
| Organ | Lung |
| TP53 status | altered |
| Drivers | KRAS(Missense); POLE(Missense); STK11(Missense); STK11(Stopgain); TP53(Missense) |
| Driver changes | KRAS p.G12C; POLE p.S780L; STK11 p.E317*; STK11 p.E357K; STK11 p.M392I; TP53 p.G262V |
| Cells over all wells | 1,937,024 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.957 (1 = a typical line) |
| Drug-doses that deplete it | 15 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 10 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,578 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 35): the line loses cells relative to the other lines in the same wells. Drug-doses: 15 in all, 5 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.1 | -0.89 |
| [[Pralsetinib (drug)]] 5 µM |  | -5.0 | -0.88 |
| [[Neratinib (drug)]] 5 µM |  | -4.4 | -0.74 |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.1 | -0.75 |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | -4.0 | -0.69 |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -0.47 |
| [[Pemetrexed (drug)]] 0.5 µM |  | -3.8 | -0.66 |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -0.62 |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.54 |
| [[Belumosudil (drug)]] 5 µM |  | -3.3 | -0.57 |
| [[Erlotinib (drug)]] 5 µM |  | -3.2 | -0.55 |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | -3.2 | -0.55 |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM |  | -3.2 | -0.52 |
| [[Neratinib (drug)]] 0.05 µM |  | -3.2 | -0.54 |
| [[Gallic acid (drug)]] 0.05 µM |  | -3.1 | -0.52 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Fluvoxamine (drug)]] 0.5 µM (1.85); [[Niclosamide (olamine) (drug)]] 0.5 µM (1.84); [[Pentamidine (isethionate) (drug)]] 5 µM (1.81); [[Neratinib (drug)]] 0.5 µM (1.70); [[Ranolazine (drug)]] 0.5 µM (1.67); [[Docetaxel (drug)]] 0.5 µM (1.60, ⚠ cell-cycle shift); [[Vortioxetine (drug)]] 0.5 µM (1.53); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (1.49); [[(S)-Crizotinib (drug)]] 0.05 µM (1.40)
- Weakest: [[Saquinavir (drug)]] 0.05 µM (0.120); [[Tofacitinib (citrate) (drug)]] 0.05 µM (0.189); [[Tofacitinib (citrate) (drug)]] 0.5 µM (0.212); [[Tofacitinib (citrate) (drug)]] 5 µM (0.244); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM (0.307); [[Tofacitinib (drug)]] 5 µM (0.309); [[Decitabine (drug)]] 0.05 µM (0.321); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM (0.326)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 35): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[CREB5]] (13, 5 ⚠), [[SNAPC1]] (11, 5 ⚠), [[CPEB4]] (10), [[RASAL2]] (10, 2 ⚠), [[MCTP1]] (10, 2 ⚠), [[ZFPM2-AS1]] (10, 2 ⚠), [[DLGAP1]] (10, 4 ⚠), [[NFAT5]] (9, 1 ⚠), [[NIBAN1]] (9, 1 ⚠), [[TSC22D2]] (9, 2 ⚠), [[PEA15]] (9, 3 ⚠), [[ARRDC4]] (8), [[ASH1L]] (8, 1 ⚠), [[DNTTIP2]] (8, 2 ⚠), [[SIRT1]] (7), [[HMGCS1]] (7), [[SORT1]] (7)
- down: [[MAP3K5]] (22, 8 ⚠), [[ETV1]] (18, 2 ⚠), [[UBASH3B]] (18, 7 ⚠), [[CSGALNACT1]] (18, 8 ⚠), [[PITPNC1]] (18, 8 ⚠), [[AADACP1]] (16, 3 ⚠), [[ZMYND8]] (16, 6 ⚠), [[ITGB5]] (15, 1 ⚠), [[PHLDA1]] (15, 1 ⚠), [[SRGAP1]] (14, 8 ⚠), [[SFMBT2]] (14, 9 ⚠), [[CDCP1]] (13, 1 ⚠), [[APBA2]] (13, 3 ⚠), [[ARHGAP44]] (13, 9 ⚠), [[ETV5]] (12, 1 ⚠), [[EGR1]] (11, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[FGB]] (+7.9), [[LINC02945]] (+7.1), [[FGG]] (+7.0), [[FGA]] (+6.8), [[RPS4Y1]] (+6.7), [[ROBO2]] (+6.6), [[CPS1]] (+6.2), [[GRAMD1B]] (+6.2), [[EPGN]] (+5.9), [[ZFY]] (+5.9), [[SMOC1]] (+5.8), [[CDH4]] (+5.8), [[RSPO3]] (+5.8), [[EDIL3-DT]] (+5.8), [[BMP5]] (+5.6) (1,498 genes, 83 with an alert ⚠; shown: the 15 strongest)
- Lacks: [[ZNF655]] (-3.7), [[TBL1X]] (-3.6), [[SMARCA4]] (-3.6), [[ZNF532]] (-3.5), [[MBNL2]] (-3.4), [[ZKSCAN8]] (-3.4), [[WWC3]] (-3.4), [[TXNIP]] (-3.4), [[DHRS3]] (-3.3), [[ZNF10]] (-3.3), [[KCNQ1OT1]] (-3.3), [[ZNF266]] (-3.3), [[ZNF264]] (-3.2), [[MGMT]] (-3.2), [[ZNF761]] (-3.2) (204 genes, 4 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 35): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.836 to 1.31).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 4 in all, 4 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 60 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[POLE]] | POLE altered (any record) (8 lines) vs not recorded (42) | 1 / 0 / 0 | A 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[STK11]] | STK11 loss of function (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,985 in all, 1,985 with an alert ⚠; shown: the 15 strongest; 1,970 more line sets (1,970 of them with an alert ⚠) not shown; 2,021 genes; 1,706 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 35; `tables/line_effects.parquet` — line == 35
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 35; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 35]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include NCI-H2030

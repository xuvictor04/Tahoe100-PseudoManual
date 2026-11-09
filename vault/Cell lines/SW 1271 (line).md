---
cell_line: "SW 1271"
type: "cell line"
cell_line_id: "CVCL_1716"
depmap_id: "ACH-000890"
organ: "Lung"
tp53_status: "altered"
drivers: ["CDKN2A(Deletion)", "CDKN2B(Deletion)", "NRAS(Missense)", "PMS2(Missense)", "SMARCA4(Missense)", "TP53(Missense)"]
n_dd_depleted: 4
median_response: 0.989
tags: ["cell-line", "organ/lung"]
generated_by: "tahoemap"
---

# SW 1271

*Lung · TP53 altered · CVCL_1716 · ACH-000890*

|  |  |
|---|---|
| Organ | Lung |
| TP53 status | altered |
| Drivers | CDKN2A(Deletion); CDKN2B(Deletion); NRAS(Missense); PMS2(Missense); SMARCA4(Missense); TP53(Missense) |
| Driver changes | NRAS p.Q61R; PMS2 p.H88Y; SMARCA4 p.N774K; TP53 p.C277F |
| Cells over all wells | 209,272 |
| Wells with usable expression | 1,313 (98.8%) |
| Median response strength (β) | 0.989 (1 = a typical line) |
| Drug-doses that deplete it | 4 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 4 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,715 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 45): the line loses cells relative to the other lines in the same wells. Drug-doses: 4 in all, none with an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | -4.3 | -1.17 |
| [[vincristine (drug)]] 5 µM |  | -3.4 | -1.23 |
| [[Capivasertib (drug)]] 5 µM |  | -3.2 | -1.10 |
| [[Belzutifan (drug)]] 5 µM |  | -3.2 | -1.13 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 479, 80 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Pyridoxine (drug)]] 0.5 µM (2.45); [[Pimozide (drug)]] 0.05 µM (2.29); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (2.24); [[Imiquimod (hydrochloride) (drug)]] 5 µM (2.19, ⚠ toxic); [[Gallic acid (hydrate) (drug)]] 0.5 µM (2.08); [[Saquinavir (drug)]] 5 µM (1.98); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (1.90); [[PH-797804 (drug)]] 0.05 µM (1.90); [[Monocrotaline (drug)]] 0.05 µM (1.90)
- Weakest: [[Malotilate (drug)]] 0.5 µM (-0.229); [[Carbamazepine (drug)]] 0.5 µM (-0.0816); [[Tofacitinib (drug)]] 5 µM (0.125); [[Tofacitinib (citrate) (drug)]] 5 µM (0.167); [[Gemcitabine (drug)]] 5 µM (0.176); [[Tofacitinib (drug)]] 0.5 µM (0.223); [[Pentoxifylline (drug)]] 0.5 µM (0.281); [[Tofacitinib (citrate) (drug)]] 0.5 µM (0.286)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 45): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[HSP90AA1]] (8, 4 ⚠), [[HSPH1]] (5, 1 ⚠), [[HSPA8]] (4), [[DNAJB1]] (4), [[HSPD1]] (4), [[UBC]] (4), [[SQSTM1]] (4), [[WAC]] (4, 1 ⚠), [[HSP90AB1]] (4, 1 ⚠), [[ZFAND3]] (4, 1 ⚠), [[BIRC3]] (3), [[HDAC9]] (3), [[BAG3]] (3)
- down: [[SPRY4-AS1]] (12, 3 ⚠), [[SMYD3]] (12, 4 ⚠), [[ETV1]] (9, 1 ⚠), [[ZMYND8]] (9, 1 ⚠), [[LUCAT1]] (9, 4 ⚠), [[ERO1A]] (8, 1 ⚠), [[CDCP1]] (8, 2 ⚠), [[F11-AS1]] (8, 3 ⚠), [[IGFBP3]] (8, 4 ⚠), [[AGAP1]] (8, 5 ⚠), [[PITPNC1]] (7, 1 ⚠), [[MAP3K5]] (7, 1 ⚠), [[HILPDA]] (7, 2 ⚠), [[SEMA4B]] (7, 2 ⚠), [[FNDC3B]] (7, 4 ⚠), [[MIR100HG]] (6), [[MT-ND4]] (6, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[LINC02109]] (+9.4), [[ENSG00000251652]] (+6.0, ⚠ noise-class RNA), [[LINC01579]] (+5.7), [[LINC02725]] (+5.6), [[F11-AS1]] (+5.5), [[LINC00540]] (+5.5), [[CDH4]] (+5.4), [[MIR646HG]] (+5.4), [[LINC02864]] (+5.4), [[ENSG00000251598]] (+5.3, ⚠ noise-class RNA), [[ENSG00000287069]] (+5.3, ⚠ noise-class RNA), [[RNF212]] (+5.2), [[STAG3]] (+5.2), [[ENSG00000287352]] (+5.2, ⚠ noise-class RNA), [[ENSG00000272297]] (+5.2, ⚠ noise-class RNA), [[IL31RA]] (+5.1), [[DNER]] (+5.1), [[FBXL7]] (+5.0), [[SYCP2]] (+4.9), [[MAGEA4]] (+4.6) (1,439 genes, 159 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[DIAPH2]] (-3.3), [[ARHGEF10]] (-3.3), [[CTSB]] (-3.2), [[ERICH1]] (-3.2), [[PRDX2]] (-3.1), [[FDFT1]] (-3.1), [[LONRF1]] (-3.1), [[ADGRE5]] (-3.1), [[EHD2]] (-3.1), [[USP40]] (-3.1), [[TFPI]] (-3.1), [[DHRS3]] (-3.0), [[REEP5]] (-3.0), [[DSG2]] (-2.9), [[PHGDH]] (-2.9) (177 genes, 6 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 45): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 56 (0.319; genes PARVA, PARP8, MME, LIMS1 / ATP2B4, NAV3, PLCXD1, MIR31HG); component 46 (0.340; genes NALF1, DNAH11, EPHA6, PCLO / EMP3, ITGA5, ALCAM, FUT8); component 59 (0.366; genes ZFP36L1, CHST11, ADAM19, PLK2 / KCNMA1, CSGALNACT1, STC1, BMERB1); component 36 (0.371; genes MIR34AHG, POLH, STAT3, CCNG1 / PLCB1, LINGO2, SATB2, WDR76)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 8 in all, 8 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 56 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[CDKN2B]] | CDKN2B loss of function (13 lines) vs not recorded (37) | 4 / 2 / 0 | B 3, C 3; 6 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[NRAS]] | NRAS gain of function (7 lines) vs not recorded (43) | 0 / 2 / 0 | C 2; 2 with an alert ⚠ | ⚠ within organs, on part of the lines |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[PMS2]] | PMS2 altered (any record) (4 lines) vs not recorded (46) | 0 / 0 / 0 | — | ⚠ few lines (4 vs 46); within organs, on part of the lines; mechanism partly not recorded |
| [[SMARCA4]] | SMARCA4 altered (any record) (12 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[SMARCA4]] | SMARCA4 loss of function (10 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,878 in all, 1,878 with an alert ⚠; shown: the 15 strongest; 1,863 more line sets (1,863 of them with an alert ⚠) not shown; 1,909 genes; 1,642 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 45; `tables/line_effects.parquet` — line == 45
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 45; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 45]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include SW 1271

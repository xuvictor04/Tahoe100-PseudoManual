---
cell_line: "NCI-H661"
type: "cell line"
cell_line_id: "CVCL_1577"
depmap_id: "ACH-000853"
organ: "Lung"
tp53_status: "altered"
drivers: ["BRCA2(Missense)", "CDKN2A(Splice_site)", "LASP1(Stopgain)", "PTPN11(Missense)", "SMARCA4(Frameshift)", "TP53(Missense)", "WNK2(Frameshift)", "ZFHX3(Missense)"]
n_dd_depleted: 8
median_response: 0.795
tags: ["cell-line", "organ/lung"]
generated_by: "tahoemap"
---

# NCI-H661

*Lung · TP53 altered · CVCL_1577 · ACH-000853*

|  |  |
|---|---|
| Organ | Lung |
| TP53 status | altered |
| Drivers | BRCA2(Missense); CDKN2A(Splice_site); LASP1(Stopgain); PTPN11(Missense); SMARCA4(Frameshift); TP53(Missense); WNK2(Frameshift); ZFHX3(Missense) |
| Driver changes | BRCA2 p.G2584V; LASP1 p.E48*; PTPN11 p.N58S; SMARCA4 p.L1161fs; TP53 p.R158L; TP53 p.S215I; WNK2 p.G64fs; ZFHX3 p.H2506P |
| Cells over all wells | 130,239 |
| Wells with usable expression | 1,310 (98.6%) |
| Median response strength (β) | 0.795 (1 = a typical line) |
| Drug-doses that deplete it | 8 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 8 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,305 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 40): the line loses cells relative to the other lines in the same wells. Drug-doses: 8 in all, none with an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | -4.0 | -1.23 |
| [[Lapatinib ditosylate (drug)]] 0.5 µM |  | -3.6 | -1.13 |
| [[venetoclax (drug)]] 0.5 µM |  | -3.6 | -1.02 |
| [[Tofacitinib (drug)]] 0.05 µM |  | -3.5 | -1.15 |
| [[Irinotecan (drug)]] 0.5 µM |  | -3.3 | -1.10 |
| [[Clopidogrel (drug)]] 0.05 µM |  | -3.3 | -0.88 |
| [[NVP-BHG712 (drug)]] 5 µM |  | -3.2 | -1.10 |
| [[Tucatinib (drug)]] 0.5 µM |  | -3.1 | -0.91 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 480, 82 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Hydroxyurea (drug)]] 0.05 µM (2.36); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (2.03); [[Nimesulide (drug)]] 5 µM (2.01, ⚠ toxic; unreliable plate only); [[RMC-6236 (drug)]] 0.05 µM (1.96); [[Lucanthone (drug)]] 0.05 µM (1.88); [[Malotilate (drug)]] 0.05 µM (1.83); [[Drospirenone (drug)]] 0.5 µM (1.82); [[Imiquimod (hydrochloride) (drug)]] 5 µM (1.80, ⚠ toxic); [[Pyridoxine (drug)]] 0.5 µM (1.77); [[Everolimus (drug)]] 5 µM (1.75)
- Weakest: [[Ritonavir (drug)]] 0.5 µM (-0.435); [[Menadione (drug)]] 5 µM (-0.111); [[Clopidogrel (drug)]] 0.05 µM (-0.0856); [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM (-0.0821); [[Tofacitinib (citrate) (drug)]] 0.05 µM (-0.0792); [[Omeprazole (drug)]] 0.05 µM (0.0293); [[AZD-8055 (drug)]] 0.05 µM (0.124); [[Tofacitinib (drug)]] 0.5 µM (0.125)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 40): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[HSP90AA1]] (4), [[HSPH1]] (4), [[DNAJB1]] (4), [[HSPA1A]] (4), [[HSPD1]] (3), [[HSP90AB1]] (2), [[PTGES3]] (2), [[BAZ1A]] (2), [[SNAPC1]] (2, 1 ⚠), [[BNC2]] (2, 1 ⚠), [[HIVEP2]] (1), [[ENTPD2]] (1), [[SPAG1]] (1)
- down: [[ARID1B]] (7, 2 ⚠), [[NCOA2]] (6, 2 ⚠), [[DYRK1A]] (5, 2 ⚠), [[SOX2]] (5, 2 ⚠), [[FNDC3B]] (5, 3 ⚠), [[BACH2]] (5, 3 ⚠), [[PDGFC]] (5, 3 ⚠), [[PHIP]] (5, 3 ⚠), [[ZFAND3]] (5, 4 ⚠), [[ADNP]] (4, 1 ⚠), [[MEIS2]] (4, 1 ⚠), [[RHOH]] (4, 1 ⚠), [[ARID2]] (4, 1 ⚠), [[GAB2]] (4, 2 ⚠), [[PLPP1]] (4, 4 ⚠), [[HSPA5]] (3), [[SEPTIN6]] (3), [[CALU]] (3), [[AHNAK2]] (3)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[COL11A1]] (+10.2), [[CDH6]] (+9.6), [[CDH10]] (+9.2), [[ENSG00000243620]] (+8.4, ⚠ noise-class RNA), [[LINC02484]] (+8.1), [[CDH7]] (+8.1), [[GPC3]] (+7.9), [[HCN1]] (+7.8), [[LINC01551]] (+7.8), [[TEX41]] (+7.8), [[HS3ST5]] (+7.7), [[COL3A1]] (+7.7), [[FOXG1]] (+7.6), [[ERBB4]] (+7.5), [[PCDH18]] (+7.3), [[POU3F2]] (+7.3) (1,532 genes, 108 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[LGALS3BP]] (-3.2), [[BACE2]] (-3.1), [[UBE2E2]] (-3.1), [[TRIM38]] (-3.1), [[PLSCR1]] (-3.1), [[ALCAM]] (-3.1), [[CDCP1]] (-3.1), [[SOX9]] (-3.1), [[AHR]] (-3.0), [[ITGA2]] (-3.0), [[SP100]] (-3.0), [[MYO1B]] (-3.0), [[DIAPH2]] (-3.0), [[HLA-A]] (-3.0), [[TSPAN5]] (-3.0) (454 genes, 14 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 40): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 3 (0.182; genes MCL1, NABP1, DUSP6, EGR1 / KCTD3, TMEM123, XPO1, TNRC6A); component 43 (0.201; genes MYO5B, TRPS1, FGD6, OCLN / LIMK2, TGFBR1, CYB5B, ITPK1); component 10 (0.239; genes ASNS, GOLGA4, YARS1, TTC3 / SAMD9, PML, SAMD9L, IFIT1); component 18 (0.241; genes SLC25A26, TAF4B, CSPP1, UBAP2 / TSEN15, FAF2, PTGR1, ARCN1)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 10 in all, 10 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 53 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[BRCA2]] | BRCA2 loss of function (7 lines) vs not recorded (41) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, WNK2, ACVR2A |
| [[BRCA2]] | BRCA2 altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with WNK2, TGFBR2, PIK3CA |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[SMARCA4]] | SMARCA4 altered (any record) (12 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[SMARCA4]] | SMARCA4 loss of function (10 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[WNK2]] | WNK2 altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with BRCA2, SETD1B, PRDM2 |
| [[WNK2]] | WNK2 loss of function (3 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ few lines (3 vs 42); within organs, on part of the lines |
| [[ZFHX3]] | ZFHX3 altered (any record) (13 lines) vs not recorded (37) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B, PIK3CA |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,234 in all, 2,234 with an alert ⚠; shown: the 15 strongest; 2,219 more line sets (2,219 of them with an alert ⚠) not shown; 2,273 genes; 1,982 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 40; `tables/line_effects.parquet` — line == 40
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 40; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 40]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include NCI-H661

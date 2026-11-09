---
cell_line: "NCI-H23"
type: "cell line"
cell_line_id: "CVCL_1547"
depmap_id: "ACH-000900"
organ: "Lung"
tp53_status: "altered"
drivers: ["ATM(Missense)", "KMT2D(Missense)", "KRAS(Missense)", "MYC(Gain)", "PMS2(Missense)", "SMARCA4(Stopgain)", "STK11(Stopgain)", "TP53(Missense)"]
n_dd_depleted: 43
median_response: 0.92
tags: ["cell-line", "organ/lung"]
generated_by: "tahoemap"
---

# NCI-H23

*Lung · TP53 altered · CVCL_1547 · ACH-000900*

|  |  |
|---|---|
| Organ | Lung |
| TP53 status | altered |
| Drivers | ATM(Missense); KMT2D(Missense); KRAS(Missense); MYC(Gain); PMS2(Missense); SMARCA4(Stopgain); STK11(Stopgain); TP53(Missense) |
| Driver changes | ATM p.Q1919P; KMT2D p.G3465V; KMT2D p.S4328T; KRAS p.G12C; PMS2 p.E491K; SMARCA4 p.1566_1567KE>N*; STK11 p.W332*; TP53 p.M246I |
| Cells over all wells | 1,774,225 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.920 (1 = a typical line) |
| Drug-doses that deplete it | 43 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 23 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,805 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 37): the line loses cells relative to the other lines in the same wells. Drug-doses: 45 in all, 22 with an alert ⚠; shown: the 12 strongest and the 10 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -17.7 | -2.09 |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -15.7 | -2.66 |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -14.5 | -2.37 |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -12.7 | -2.19 |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -12.3 | -1.43 |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -11.8 | -2.79 |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -10.3 | -1.91 |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.7 | -2.20 |
| [[Brivudine (drug)]] 5 µM |  | -8.5 | -1.28 |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -8.2 | -1.56 |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.8 | -2.27 |
| [[Auranofin (drug)]] 5 µM |  | -7.4 | -1.17 |
| [[GSK1059615 (drug)]] 5 µM |  | -7.0 | -1.03 |
| [[Belumosudil (drug)]] 5 µM |  | -6.9 | -1.12 |
| [[Pralsetinib (drug)]] 5 µM |  | -5.4 | -0.92 |
| [[Adagrasib (drug)]] 5 µM |  | -5.2 | -0.79 |
| [[Alpelisib (drug)]] 5 µM |  | -4.8 | -0.76 |
| [[BI-3406 (drug)]] 5 µM |  | -4.8 | -0.71 |
| [[Peretinoin (drug)]] 0.5 µM |  | -4.5 | -0.69 |
| [[RMC-6236 (drug)]] 5 µM |  | -4.1 | -0.59 |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.9 | -0.58 |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.8 | -0.59 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Everolimus (drug)]] 5 µM (1.98); [[Tofacitinib (citrate) (drug)]] 0.05 µM (1.81); [[Regorafenib (drug)]] 5 µM (1.59); [[Peretinoin (drug)]] 0.5 µM (1.58); [[Pitavastatin (Calcium) (drug)]] 0.05 µM (1.56); [[Berbamine (drug)]] 0.5 µM (1.56); [[Berbamine (drug)]] 5 µM (1.56); [[BI-3406 (drug)]] 5 µM (1.55)
- Weakest: [[Elagolix sodium (drug)]] 0.5 µM (-0.187); [[Citalopram (hydrobromide) (drug)]] 0.5 µM (-0.113); [[Tazarotene (drug)]] 0.5 µM (-0.0327); [[Canagliflozin (drug)]] 0.05 µM (0.130); [[Vilanterol (drug)]] 0.05 µM (0.145); [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM (0.175); [[Imiquimod (maleate) (drug)]] 0.5 µM (0.176); [[Omeprazole (drug)]] 0.5 µM (0.232)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 37): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[CLU]] (16, 6 ⚠), [[SLMAP]] (13, 2 ⚠), [[DAAM1]] (12), [[TOP1]] (12, 5 ⚠), [[TIGAR]] (11, 2 ⚠), [[ADA]] (11, 2 ⚠), [[PPFIA1]] (11, 5 ⚠), [[PTCD3]] (11, 7 ⚠), [[ARID4B]] (10, 2 ⚠), [[WAC]] (10, 2 ⚠), [[RABEP1]] (10, 3 ⚠), [[POLR2B]] (10, 3 ⚠), [[CDC27]] (10, 5 ⚠), [[BCLAF1]] (10, 6 ⚠), [[FGFR1OP2]] (9), [[LRP6]] (9, 1 ⚠), [[MED13]] (9, 1 ⚠), [[SYT1]] (8), [[SCD]] (8)
- down: [[SPRY4-AS1]] (33, 9 ⚠), [[NTSR1]] (33, 12 ⚠), [[CDCP1]] (31, 5 ⚠), [[ZBTB20]] (29, 15 ⚠), [[PLSCR1]] (28, 10 ⚠), [[THSD4]] (26, 7 ⚠), [[ZMYND8]] (26, 8 ⚠), [[NT5E]] (25, 2 ⚠), [[ELK3]] (24, 2 ⚠), [[PARP9]] (24, 7 ⚠), [[SHB]] (23, 6 ⚠), [[MARCHF4]] (23, 6 ⚠), [[ACTN1]] (21, 1 ⚠), [[SLC4A7]] (21, 3 ⚠), [[ITGA2]] (20, 2 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[CCND2]] (+6.4), [[MTND1P23]] (+6.3, ⚠ noise-class RNA), [[ENSG00000251652]] (+6.2, ⚠ noise-class RNA), [[ENSG00000267327]] (+5.8, ⚠ noise-class RNA), [[OLR1]] (+5.7), [[GRAMD1B]] (+5.7), [[CHMP1B2P]] (+5.7), [[ENSG00000286481]] (+5.6, ⚠ noise-class RNA), [[MAGEA4]] (+5.6), [[MDGA2]] (+5.6), [[ENSG00000286385]] (+5.5, ⚠ noise-class RNA), [[MARCHF4]] (+5.4), [[KIF1A]] (+5.4), [[ST8SIA6-AS1]] (+5.1), [[KLRC2]] (+5.1), [[KLRC3]] (+5.1), [[ACP7]] (+5.1), [[BMP5]] (+5.1), [[EVC2]] (+5.0), [[LGSN]] (+5.0) (1,786 genes, 182 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[NNT]] (-3.4), [[EMP1]] (-3.4), [[MIR924HG]] (-3.4), [[KCNQ1OT1]] (-3.4), [[GPX1]] (-3.3), [[S100A16]] (-3.3), [[ZNF736]] (-3.2), [[LGALS3BP]] (-3.1), [[ZNF91]] (-3.1), [[ENSG00000285744]] (-3.1, ⚠ noise-class RNA), [[LTBR]] (-3.1), [[SMARCA2]] (-3.0), [[SCOC]] (-3.0), [[ADGRG1]] (-3.0), [[LARGE1]] (-2.9), [[ZFPM2-AS1]] (-2.9) (233 genes, 7 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 37): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.822 to 1.28).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 10 in all, 10 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 53 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[KMT2D]] | KMT2D altered (any record) (15 lines) vs not recorded (35) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[ATM]] | ATM altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[ATM]] | ATM loss of function (6 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[MYC]] | MYC gain of function (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[PMS2]] | PMS2 altered (any record) (4 lines) vs not recorded (46) | 0 / 0 / 0 | — | ⚠ few lines (4 vs 46); within organs, on part of the lines; mechanism partly not recorded |
| [[SMARCA4]] | SMARCA4 altered (any record) (12 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[SMARCA4]] | SMARCA4 loss of function (10 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[STK11]] | STK11 loss of function (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,793 in all, 1,793 with an alert ⚠; shown: the 15 strongest; 1,778 more line sets (1,778 of them with an alert ⚠) not shown; 1,825 genes; 1,561 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 37; `tables/line_effects.parquet` — line == 37
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 37; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 37]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include NCI-H23

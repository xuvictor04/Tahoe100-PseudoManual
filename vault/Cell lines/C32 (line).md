---
cell_line: "C32"
type: "cell line"
cell_line_id: "CVCL_1097"
depmap_id: "ACH-000580"
organ: "Skin"
tp53_status: "wild type"
drivers: ["BRAF(Missense)", "CDKN2A(Stoploss)", "PTEN(Deletion)", "TERT(Promoter)"]
n_dd_depleted: 31
median_response: 1.003
tags: ["cell-line", "organ/skin"]
generated_by: "tahoemap"
---

# C32

*Skin · TP53 wild type · CVCL_1097 · ACH-000580*

|  |  |
|---|---|
| Organ | Skin |
| TP53 status | wild type |
| Drivers | BRAF(Missense); CDKN2A(Stoploss); PTEN(Deletion); TERT(Promoter) |
| Driver changes | BRAF p.V600E; CDKN2A p.Ter157Serext*13 |
| Cells over all wells | 1,991,123 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 1.00 (1 = a typical line) |
| Drug-doses that deplete it | 31 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 18 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,329 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 26): the line loses cells relative to the other lines in the same wells. Drug-doses: 31 in all, 13 with an alert ⚠; shown: the 12 strongest and the 6 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -8.5 | -1.12 |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -6.1 | -1.20 |
| [[AZD-7648 (drug)]] 5 µM |  | -6.1 | -0.82 |
| [[Ponatinib (drug)]] 5 µM |  | -5.9 | -0.64 |
| [[vincristine (drug)]] 5 µM |  | -5.3 | -0.73 |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.2 | -0.72 |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | -5.1 | -0.75 |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -0.55 |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -0.54 |
| [[Ipatasertib (drug)]] 0.5 µM |  | -4.6 | -0.54 |
| [[AZD1390 (drug)]] 5 µM |  | -4.6 | -0.56 |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | -4.6 | -0.79 |
| [[Cobimetinib (drug)]] 0.05 µM |  | -4.3 | -0.53 |
| [[DT-061 (drug)]] 5 µM |  | -4.2 | -0.55 |
| [[Pimitespib (drug)]] 5 µM |  | -3.7 | -0.51 |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | -3.5 | -0.45 |
| [[DTP3 (drug)]] 5 µM |  | -3.5 | -0.45 |
| [[BAY1125976 (drug)]] 0.5 µM |  | -3.3 | -0.38 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Pimozide (drug)]] 5 µM (2.08); [[Quinestrol (drug)]] 5 µM (1.85); [[Norepinephrine (hydrochloride) (drug)]] 5 µM (1.83); [[Cobimetinib (drug)]] 0.05 µM (1.83); [[Almonertinib (mesylate) (drug)]] 5 µM (1.83); [[Amsacrine (drug)]] 0.5 µM (1.81); [[Futibatinib (drug)]] 0.05 µM (1.77); [[Elagolix sodium (drug)]] 0.5 µM (1.77)
- Weakest: [[Cyclosporin A (drug)]] 0.5 µM (-0.314); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM (-0.165); [[BI-3406 (drug)]] 5 µM (0.00169); [[Roxadustat (drug)]] 0.05 µM (0.0867); [[Menadione (drug)]] 5 µM (0.177); [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM (0.181); [[Ponatinib (drug)]] 5 µM (0.183); [[Fluvoxamine (maleate) (drug)]] 0.5 µM (0.191)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 26): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[GLUD1]] (21, 2 ⚠), [[FKBP5]] (18, 3 ⚠), [[PEG10]] (18, 8 ⚠), [[SEMA3C]] (16, 1 ⚠), [[YWHAZ]] (16, 11 ⚠), [[PPP1R12B]] (15, 1 ⚠), [[RASAL2]] (15, 4 ⚠), [[CD44]] (15, 5 ⚠), [[KIF13A]] (14, 1 ⚠), [[IGF2BP2]] (14, 6 ⚠), [[CREB5]] (14, 6 ⚠), [[HSPA4]] (14, 6 ⚠), [[ROBO1]] (13), [[LARGE1]] (13, 1 ⚠), [[ZFPM2-AS1]] (13, 1 ⚠), [[SLIT2]] (13, 2 ⚠), [[RHOBTB3]] (13, 2 ⚠), [[DENND4A]] (13, 2 ⚠)
- down: [[HIVEP3]] (43, 9 ⚠), [[ST3GAL1]] (37, 11 ⚠), [[CLMN]] (37, 12 ⚠), [[PARVB]] (35, 11 ⚠), [[COL13A1]] (33, 4 ⚠), [[ZFYVE28]] (33, 7 ⚠), [[ITGB8]] (32, 9 ⚠), [[ENSG00000286251]] (31, 9 ⚠), [[STAMBPL1]] (30, 8 ⚠), [[PTPN14]] (30, 9 ⚠), [[ACTN1]] (29, 3 ⚠), [[KCNN4]] (29, 6 ⚠), [[IL1RAP]] (29, 6 ⚠), [[PHC2]] (28, 3 ⚠), [[CEACAM1]] (24, 2 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[LHFPL3-AS1]] (+8.5), [[DCT]] (+7.9), [[COL19A1]] (+7.7), [[MDGA2]] (+7.5), [[A2M]] (+7.4), [[CTTNBP2]] (+7.4), [[VGF]] (+7.3), [[PAX3]] (+7.2), [[PI15]] (+7.0), [[IGFBP5]] (+7.0), [[LEF1]] (+6.9), [[C10orf90]] (+6.9), [[CD74]] (+6.7), [[RHOJ]] (+6.6), [[GDNF]] (+6.6) (1,512 genes, 130 with an alert ⚠; shown: the 15 strongest)
- Lacks: [[ZNF254]] (-3.6), [[TNFRSF10D]] (-3.5), [[SCRN1]] (-3.5), [[DANT2]] (-3.4), [[SOX9]] (-3.3), [[FGFR1]] (-3.3), [[IL4R]] (-3.3), [[MGMT]] (-3.2), [[ATAD1]] (-3.2), [[NUTM2A-AS1]] (-3.2), [[OCIAD2]] (-3.2), [[MAP3K21]] (-3.1), [[NHS]] (-3.1), [[GPR39]] (-3.0), [[ZNF736]] (-3.0) (293 genes, 8 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 26): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 48 (0.665; genes LINC01876, RNF19A, PDE4D, NEBL / CYP51A1, LPIN1, INSIG1, LYST)
- Strong here (> 1.5): component 56 (1.52; genes PARVA, PARP8, MME, LIMS1 / ATP2B4, NAV3, PLCXD1, MIR31HG)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 6 in all, 6 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 57 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TERT]] | TERT gain of function (8 lines) vs not recorded (39) | 5 / 0 / 0 | C 5; 5 with an alert ⚠ | ⚠ tissue-confounded; across organs; TERT not expressed in 1 of the 8 altered lines |
| [[BRAF]] | BRAF altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[BRAF]] | BRAF gain of function (7 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[PTEN]] | PTEN loss of function (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; PTEN not expressed in 4 of the 9 altered lines |
| [[TERT]] | TERT altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; TERT not expressed in 2 of the 11 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,208 in all, 2,208 with an alert ⚠; shown: the 15 strongest; 2,193 more line sets (2,193 of them with an alert ⚠) not shown; 2,242 genes; 1,933 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 26; `tables/line_effects.parquet` — line == 26
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 26; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 26]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include C32

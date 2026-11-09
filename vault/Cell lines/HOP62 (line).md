---
cell_line: "HOP62"
type: "cell line"
cell_line_id: "CVCL_1285"
depmap_id: "ACH-000861"
organ: "Lung"
tp53_status: "altered"
drivers: ["B2M(Missense)", "KRAS(Missense)", "MSH6(Missense)", "POLE(Missense)", "RAF1(Missense)", "TERT(Promoter)", "TP53(Splice_site)"]
n_dd_depleted: 30
median_response: 1.091
tags: ["cell-line", "organ/lung"]
generated_by: "tahoemap"
---

# HOP62

*Lung · TP53 altered · CVCL_1285 · ACH-000861*

|  |  |
|---|---|
| Organ | Lung |
| TP53 status | altered |
| Drivers | B2M(Missense); KRAS(Missense); MSH6(Missense); POLE(Missense); RAF1(Missense); TERT(Promoter); TP53(Splice_site) |
| Driver changes | B2M p.E70Q; KRAS p.G12C; MSH6 p.E221D; POLE p.K604N; RAF1 p.R143Q |
| Cells over all wells | 3,307,153 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 1.09 (1 = a typical line) |
| Drug-doses that deplete it | 30 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 24 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,879 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 31): the line loses cells relative to the other lines in the same wells. Drug-doses: 31 in all, 7 with an alert ⚠; shown: the 12 strongest and the 4 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -6.5 | -1.15 |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.1 | -0.81 |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -5.8 | -0.80 |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -5.7 | -0.82 |
| [[Penfluridol (drug)]] 0.5 µM |  | -5.6 | -0.75 |
| [[PH-797804 (drug)]] 5 µM |  | -5.1 | -0.68 |
| [[Fluvoxamine (drug)]] 0.5 µM |  | -4.9 | -0.64 |
| [[Pemetrexed (drug)]] 0.5 µM |  | -4.8 | -0.64 |
| [[Mozavaptan (drug)]] 0.5 µM |  | -4.8 | -0.62 |
| [[Adagrasib (drug)]] 0.5 µM |  | -4.6 | -0.60 |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -0.45 |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -0.60 |
| [[Ferulic acid (drug)]] 0.5 µM |  | -4.3 | -0.57 |
| [[Imiquimod (maleate) (drug)]] 0.5 µM |  | -4.3 | -0.58 |
| [[Celecoxib (drug)]] 0.05 µM |  | -3.9 | -0.52 |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -3.8 | -0.50 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Econazole (drug)]] 5 µM (2.24); [[Dexamethasone (drug)]] 5 µM (2.20); [[Citalopram (hydrobromide) (drug)]] 0.05 µM (2.15); [[Dexamethasone (drug)]] 0.05 µM (2.15); [[Budesonide (drug)]] 5 µM (2.11); [[Betamethasone dipropionate (drug)]] 5 µM (2.10); [[Clobetasol propionate (drug)]] 5 µM (2.09); [[Budesonide (drug)]] 0.5 µM (2.06)
- Weakest: [[Citalopram (hydrobromide) (drug)]] 0.5 µM (0.0540); [[Naproxen (drug)]] 0.05 µM (0.115); [[Monocrotaline (drug)]] 0.05 µM (0.152); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM (0.233); [[Orlistat (drug)]] 0.05 µM (0.247); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM (0.320); [[Tofacitinib (citrate) (drug)]] 5 µM (0.338); [[Pyridoxine (drug)]] 0.5 µM (0.349)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 31): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[FKBP5]] (28, 8 ⚠), [[ALCAM]] (27, 6 ⚠), [[TSC22D3]] (21, 1 ⚠), [[CCND3]] (20), [[ADAMTS9]] (20, 1 ⚠), [[TMX4]] (20, 3 ⚠), [[IRAK3]] (19), [[NPR3]] (18), [[PID1]] (18), [[AKAP13]] (18), [[SH3RF3]] (18), [[ABLIM3]] (18), [[DNER]] (18), [[FGD4]] (18, 1 ⚠), [[ARHGAP26]] (18, 4 ⚠), [[ACSL1]] (18, 4 ⚠)
- down: [[ITGA2]] (46, 8 ⚠), [[IGFBP3]] (44, 12 ⚠), [[MIR34AHG]] (43, 15 ⚠), [[HMGA2]] (42, 11 ⚠), [[UACA]] (42, 17 ⚠), [[MANCR]] (40, 10 ⚠), [[CORO2B]] (37, 3 ⚠), [[CDCP1]] (37, 9 ⚠), [[SIPA1L3]] (37, 15 ⚠), [[ANTXR2]] (33, 2 ⚠), [[IL11]] (33, 3 ⚠), [[LAMA4]] (32, 10 ⚠), [[PDE4DIP]] (29, 5 ⚠), [[ITGB5]] (24, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[RFX8]] (+7.1), [[IRAG2]] (+6.7), [[COL5A1]] (+6.6), [[LINC02899]] (+6.5), [[ENSG00000222032]] (+5.9, ⚠ noise-class RNA), [[IL11]] (+5.9), [[TENM2]] (+5.8), [[PDGFRB]] (+5.8), [[IL1B]] (+5.7), [[COL6A3]] (+5.7), [[ENSG00000251652]] (+5.6, ⚠ noise-class RNA), [[COL6A2]] (+5.6), [[LOX]] (+5.5), [[SERPINE1]] (+5.5), [[THBS2]] (+5.5), [[WNT5A]] (+5.4), [[LINC01629]] (+5.4) (1,092 genes, 80 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[TDP1]] (-3.2), [[CMBL]] (-3.0), [[ALDOC]] (-3.0), [[IFI6]] (-2.9), [[OAS3]] (-2.9), [[PPP1R9A]] (-2.8), [[MAFIP]] (-2.8), [[LRRC8B]] (-2.6), [[MTUS1]] (-2.5), [[ENSG00000290199]] (-2.5, ⚠ noise-class RNA), [[GP6-AS1]] (-2.5), [[CYFIP2]] (-2.5), [[EPIC1]] (-2.5), [[NEBL]] (-2.5), [[PROS1]] (-2.4), [[CPNE8]] (-2.4) (157 genes, 3 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 31): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Strong here (> 1.5): component 13 (1.78; genes UGP2, KLF9, TSC22D3, SSBP2 / LUC7L3, PER3, TCP10L, SEMA3A); component 5 (1.60; genes MPHOSPH10, ESF1, CEP290, PHAX / ITM2B, TMEM30A, LASP1, APLP2); component 58 (1.60; genes SDK1, WFDC3, WFDC10B, RUNX2 / TEAD1, ATP2C2, ARHGAP18, NFIB); component 3 (1.58; genes MCL1, NABP1, DUSP6, EGR1 / KCTD3, TMEM123, XPO1, TNRC6A)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 7 in all, 7 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 55 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[TERT]] | TERT gain of function (8 lines) vs not recorded (39) | 5 / 0 / 0 | C 5; 5 with an alert ⚠ | ⚠ tissue-confounded; across organs; TERT not expressed in 1 of the 8 altered lines |
| [[POLE]] | POLE altered (any record) (8 lines) vs not recorded (42) | 1 / 0 / 0 | A 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[B2M]] | B2M altered (any record) (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[MSH6]] | MSH6 altered (any record) (4 lines) vs not recorded (46) | 0 / 0 / 0 | — | ⚠ few lines (4 vs 46); within organs, on part of the lines; mechanism partly not recorded; co-occurs with EP300, RNF43 |
| [[TERT]] | TERT altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; TERT not expressed in 2 of the 11 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,710 in all, 1,710 with an alert ⚠; shown: the 15 strongest; 1,695 more line sets (1,695 of them with an alert ⚠) not shown; 1,745 genes; 1,478 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 31; `tables/line_effects.parquet` — line == 31
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 31; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 31]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include HOP62

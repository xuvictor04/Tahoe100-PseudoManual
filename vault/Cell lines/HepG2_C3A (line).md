---
cell_line: "HepG2/C3A"
type: "cell line"
cell_line_id: "CVCL_1098"
depmap_id: "ACH-001021"
organ: "Liver"
tp53_status: "wild type"
drivers: ["ATM(Missense)", "EGFR(Missense)", "ERBB3(Missense)", "NRAS(Missense)", "TERT(Promoter)"]
n_dd_depleted: 5
median_response: 0.905
tags: ["cell-line", "organ/liver"]
generated_by: "tahoemap"
---

# HepG2/C3A

*Liver · TP53 wild type · CVCL_1098 · ACH-001021*

|  |  |
|---|---|
| Organ | Liver |
| TP53 status | wild type |
| Drivers | ATM(Missense); EGFR(Missense); ERBB3(Missense); NRAS(Missense); TERT(Promoter) |
| Driver changes | ATM p.V2906I; EGFR p.C186S; ERBB3 p.R421K; NRAS p.Q61L |
| Cells over all wells | 1,244,072 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.905 (1 = a typical line) |
| Drug-doses that deplete it | 5 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 2 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 13,886 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 27): the line loses cells relative to the other lines in the same wells. Drug-doses: 5 in all, 3 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | -6.0 | -1.26 |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.4 | -1.40 |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.74 |
| [[Verteporfin (drug)]] 5 µM |  | -4.1 | -0.96 |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.7 | -0.90 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Crizotinib (hydrochloride) (drug)]] 0.5 µM (2.04); [[Fluvoxamine (drug)]] 0.5 µM (1.98); [[Imiquimod (hydrochloride) (drug)]] 5 µM (1.86, ⚠ toxic); [[Vortioxetine (drug)]] 5 µM (1.85, ⚠ toxic); [[Simotinib (drug)]] 0.05 µM (1.72); [[Trimetrexate (drug)]] 5 µM (1.70); [[Fluvoxamine (maleate) (drug)]] 0.5 µM (1.62); [[Roxadustat (drug)]] 0.05 µM (1.60); [[Lucanthone (drug)]] 0.05 µM (1.57); [[Drospirenone (drug)]] 0.5 µM (1.48)
- Weakest: [[Berbamine (dihydrochloride) (drug)]] 5 µM (0.318); [[Docetaxel (Trihydrate) (drug)]] 0.05 µM (0.319); [[Posaconazole (drug)]] 5 µM (0.325); [[Vilanterol (drug)]] 0.05 µM (0.337); [[Lopinavir (drug)]] 5 µM (0.341); [[Tirabrutinib (drug)]] 0.5 µM (0.344); [[Norepinephrine (hydrochloride) (drug)]] 5 µM (0.363); [[Ponatinib (drug)]] 5 µM (0.382)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 27): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[FKBP5]] (18, 7 ⚠), [[SQSTM1]] (11, 2 ⚠), [[GPHN]] (11, 4 ⚠), [[SFPQ]] (11, 5 ⚠), [[MAP1B]] (11, 5 ⚠), [[ARRDC4]] (10, 1 ⚠), [[ENSG00000237596]] (10, 1 ⚠), [[CLEC16A]] (9), [[CFB]] (9), [[SPAG9]] (9, 1 ⚠), [[ARHGAP26]] (9, 1 ⚠), [[HSP90AA1]] (9, 5 ⚠), [[DNAJC1]] (9, 5 ⚠), [[HSPD1]] (9, 5 ⚠), [[WDPCP]] (8), [[CLIP1]] (8, 1 ⚠), [[USP15]] (8, 1 ⚠), [[AGPAT5]] (8, 1 ⚠)
- down: [[SPRY4-AS1]] (32, 10 ⚠), [[SLC38A2]] (29, 11 ⚠), [[ITGB5]] (27, 5 ⚠), [[ITGA2]] (27, 6 ⚠), [[FRMD5]] (27, 11 ⚠), [[SORL1]] (27, 13 ⚠), [[NIHCOLE]] (27, 18 ⚠), [[MAML2]] (26, 12 ⚠), [[PRAG1]] (25, 8 ⚠), [[ATP10A]] (24, 9 ⚠), [[LRRTM4]] (22, 15 ⚠), [[MOCS2-DT]] (21, 6 ⚠), [[MTUS1]] (21, 14 ⚠), [[DCBLD2]] (19, 2 ⚠), [[AKAP12]] (18, 1 ⚠), [[IFITM1]] (18, 3 ⚠), [[LINC01844]] (18, 3 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[APOB]] (+9.0), [[AFP]] (+8.6), [[ALB]] (+8.6), [[PEG3]] (+8.5), [[AHSG]] (+8.4), [[SERPINA1]] (+8.3), [[TF]] (+8.3), [[IGF2]] (+8.3), [[GPC3]] (+8.2), [[IGFBP1]] (+8.2), [[APOA2]] (+8.2), [[AMBP]] (+7.8), [[ITIH2]] (+7.8), [[SERPINA3]] (+7.7), [[APOA1]] (+7.5) (1,386 genes, 108 with an alert ⚠; shown: the 15 strongest)
- Lacks: [[VIM]] (-3.7), [[INSIG1]] (-3.6), [[GNG12]] (-3.6), [[NSD1]] (-3.6), [[KIRREL1]] (-3.5), [[TRPS1]] (-3.5), [[FAR1]] (-3.5), [[ATL3]] (-3.5), [[GPD2]] (-3.4), [[CD81]] (-3.4), [[CTBP2]] (-3.4), [[LDHB]] (-3.4), [[HDHD5]] (-3.4), [[GSTP1]] (-3.4), [[HDGFL3]] (-3.4) (457 genes, 5 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 27): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 6 (0.576; genes KIF18B, CDC25C, KIF2C, SGO2 / MALAT1, ANXA1, DYNC1H1, DST); component 23 (0.625; genes NUDCD1, GPR176, MTURN, TBC1D9 / SLC7A11, ZFAND6, MARS1, SREBF1); component 52 (0.639; genes CHST15, PHLDB2, TNS4, SNTB1 / SH3RF3, LTBP1, FUT8, NRG2); component 17 (0.660; genes ALDOA, SLC2A1, BNIP3, FAM117B / ITGAV, B4GALT1, NKTR, SLC39A8)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 6 in all, 6 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 57 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TERT]] | TERT gain of function (8 lines) vs not recorded (39) | 5 / 0 / 0 | C 5; 5 with an alert ⚠ | ⚠ tissue-confounded; across organs; TERT not expressed in 1 of the 8 altered lines |
| [[NRAS]] | NRAS gain of function (7 lines) vs not recorded (43) | 0 / 2 / 0 | C 2; 2 with an alert ⚠ | ⚠ within organs, on part of the lines |
| [[ATM]] | ATM altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[EGFR]] | EGFR altered (any record) (4 lines) vs not recorded (46) | 0 / 0 / 0 | — | ⚠ few lines (4 vs 46); within organs, on part of the lines; mechanism partly not recorded; EGFR not expressed in 1 of the 4 altered lines |
| [[ERBB3]] | ERBB3 altered (any record) (3 lines) vs not recorded (47) | 0 / 0 / 0 | — | ⚠ few lines (3 vs 47); within organs, on part of the lines; mechanism partly not recorded |
| [[TERT]] | TERT altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; TERT not expressed in 2 of the 11 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,561 in all, 2,561 with an alert ⚠; shown: the 15 strongest; 2,546 more line sets (2,546 of them with an alert ⚠) not shown; 2,598 genes; 2,208 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[TMPRSS4]], [[OVOL1]] | 33 vs 17 | 14 / 223 / 24 | B 115, C 146; 261 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[IRF6]], [[C1orf116]] | 31 vs 19 | 18 / 216 / 24 | B 128, C 130; 258 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ST14]] | 32 vs 18 | 11 / 196 / 21 | B 88, C 140; 228 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TMPRSS2]] | 35 vs 15 | 6 / 197 / 18 | B 77, C 144; 221 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CLIC5]] | 37 vs 13 | 4 / 185 / 7 | B 59, C 137; 196 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ARHGEF38]] | 36 vs 14 | 5 / 172 / 9 | B 49, C 137; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01559]] | 38 vs 12 | 0 / 182 / 0 | B 36, C 146; 182 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ITGB6]] | 32 vs 18 | 5 / 148 / 18 | B 47, C 124; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TC2N]] | 28 vs 22 | 3 / 163 / 5 | B 52, C 119; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ADGRF1]] | 35 vs 15 | 14 / 138 / 16 | B 64, C 104; 168 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CATSPERB]] | 30 vs 20 | 1 / 147 / 12 | B 50, C 110; 160 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[HS3ST1]] | 31 vs 19 | 3 / 137 / 9 | B 58, C 91; 149 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[NPSR1]] | 42 vs 8 | 2 / 142 / 0 | B 26, C 118; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CLDN3]] | 28 vs 22 | 2 / 124 / 16 | B 48, C 94; 142 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[KLK10]] | 34 vs 16 | 2 / 131 / 8 | B 43, C 98; 141 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 27; `tables/line_effects.parquet` — line == 27
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 27; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 27]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include HepG2/C3A

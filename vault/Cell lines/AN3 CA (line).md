---
cell_line: "AN3 CA"
type: "cell line"
cell_line_id: "CVCL_0028"
depmap_id: "ACH-000940"
organ: "Uterus"
tp53_status: "altered"
drivers: ["ARID1A(Frameshift)", "ARID1A(Missense)", "FBXW7(Missense)", "FGFR2(Missense)", "HRAS(Missense)", "KMT2D(Frameshift)", "MAPK3(Missense)", "MET(Missense)", "PIK3R1(Missense)", "POLE(Missense)", "PTEN(Frameshift)", "SETD1B(Frameshift)", "SMARCA4(Missense)", "TERT(Missense)", "TP53(Frameshift)", "TP53(Missense)", "WNK2(Missense)", "ZFHX3(Frameshift)"]
n_dd_depleted: 17
median_response: 0.865
tags: ["cell-line", "organ/uterus"]
generated_by: "tahoemap"
---

# AN3 CA

*Uterus · TP53 altered · CVCL_0028 · ACH-000940*

|  |  |
|---|---|
| Organ | Uterus |
| TP53 status | altered |
| Drivers | ARID1A(Frameshift); ARID1A(Missense); FBXW7(Missense); FGFR2(Missense); HRAS(Missense); KMT2D(Frameshift); MAPK3(Missense); MET(Missense); PIK3R1(Missense); POLE(Missense); PTEN(Frameshift); SETD1B(Frameshift); SMARCA4(Missense); TERT(Missense); TP53(Frameshift); TP53(Missense); WNK2(Missense); ZFHX3(Frameshift) |
| Driver changes | ARID1A p.D1633fs; ARID1A p.LEMLRENT1836del; FBXW7 p.R361W; FGFR2 p.K82R; FGFR2 p.N321K; HRAS p.F82L; KMT2D p.P2210fs; MAPK3 p.P373S; MET p.G344R; PIK3R1 p.R557_561NA; POLE p.S30L; PTEN p.R130fs; SETD1B p.P749fs; SMARCA4 p.P1456L; TERT p.D848G; TP53 p.G389W; TP53 p.R213Q; TP53 p.S90fs; WNK2 p.P702S; ZFHX3 p.R1893fs |
| Cells over all wells | 565,996 |
| Wells with usable expression | 1,328 (99.9%) |
| Median response strength (β) | 0.865 (1 = a typical line) |
| Drug-doses that deplete it | 17 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 9 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,243 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 1): the line loses cells relative to the other lines in the same wells. Drug-doses: 17 in all, 8 with an alert ⚠; shown: the 12 strongest and the 1 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -13.7 | -3.74 |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -9.5 | -3.57 |
| [[GSK1059615 (drug)]] 5 µM |  | -8.2 | -2.84 |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.7 | -2.58 |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | -2.48 |
| [[Bimiralisib (drug)]] 5 µM |  | -6.3 | -2.01 |
| [[Ponatinib (drug)]] 5 µM |  | -5.8 | -1.85 |
| [[PH-797804 (drug)]] 5 µM |  | -5.0 | -1.79 |
| [[AT7519 (drug)]] 5 µM |  | -4.8 | -1.60 |
| [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -1.35 |
| [[BAY1125976 (drug)]] 5 µM |  | -3.9 | -1.22 |
| [[Mebendazole (drug)]] 5 µM |  | -3.5 | -1.11 |
| [[Infigratinib (drug)]] 5 µM |  | -3.1 | -0.99 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 488, 84 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Glycyrrhizic acid (drug)]] 0.05 µM (2.25); [[Malotilate (drug)]] 0.05 µM (2.18); [[Decitabine (drug)]] 0.5 µM (2.15); [[Niclosamide (olamine) (drug)]] 0.5 µM (2.05); [[Monocrotaline (drug)]] 0.05 µM (2.02); [[AZD2858 (drug)]] 0.5 µM (2.01, ⚠ toxic); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM (1.99); [[Fluvoxamine (drug)]] 0.5 µM (1.96); [[Lucanthone (drug)]] 0.05 µM (1.92)
- Weakest: [[Malotilate (drug)]] 0.5 µM (-0.466); [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM (-0.0286); [[AZD-8055 (drug)]] 0.05 µM (-0.0266); [[Apalutamide (drug)]] 0.5 µM (0.126); [[Norepinephrine (hydrochloride) (drug)]] 5 µM (0.137); [[Lactate (calcium) (drug)]] 0.5 µM (0.140); [[Tirabrutinib (drug)]] 0.5 µM (0.156); [[Filgotinib (drug)]] 0.05 µM (0.175)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 1): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[KLF10]] (6), [[TRIO]] (6, 2 ⚠), [[HSP90AA1]] (6, 2 ⚠), [[EGR1]] (6, 2 ⚠), [[ALCAM]] (5, 2 ⚠), [[HNRNPA2B1]] (5, 4 ⚠), [[IER2]] (5, 4 ⚠), [[PPP1R15A]] (4), [[NFAT5]] (4), [[NFKB1]] (4), [[TNFAIP3]] (4), [[ARHGAP26]] (4), [[UBC]] (4), [[REL]] (4), [[POLR2A]] (4), [[SPAG9]] (4, 1 ⚠), [[MYH9]] (4, 4 ⚠)
- down: [[PRELID2]] (19, 11 ⚠), [[MEOX2]] (16, 7 ⚠), [[ATG10]] (15, 10 ⚠), [[FGFR1]] (15, 11 ⚠), [[IMMP2L]] (15, 11 ⚠), [[EPIC1]] (14, 6 ⚠), [[THSD4]] (13, 3 ⚠), [[PDE4D]] (13, 6 ⚠), [[GPM6B]] (13, 9 ⚠), [[RAD51B]] (12, 5 ⚠), [[ARID1B]] (12, 8 ⚠), [[NFIB]] (12, 8 ⚠), [[HMGA2]] (10, 3 ⚠), [[DHRS3]] (10, 3 ⚠), [[ZFX]] (9, 2 ⚠), [[KIAA1328]] (9, 2 ⚠), [[SMYD3]] (9, 2 ⚠), [[PLEKHA2]] (8, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[MGP]] (+8.6), [[MEOX2]] (+8.4), [[MEST]] (+7.9), [[CADM2]] (+6.8), [[PRKG1]] (+6.6), [[TSHZ2]] (+6.4), [[COL1A2]] (+6.3), [[GPM6B]] (+6.2), [[B3GALT1]] (+6.2), [[PRLR]] (+6.0), [[BOC]] (+6.0), [[HOXC10]] (+6.0), [[ENSG00000259692]] (+5.9, ⚠ noise-class RNA), [[FBXL7]] (+5.8), [[LIN28B]] (+5.8), [[ATOH8]] (+5.7) (1,575 genes, 93 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[NR3C1]] (-2.8), [[SDC4]] (-2.7), [[PFKP]] (-2.7), [[AXL]] (-2.7), [[TSPAN5]] (-2.6), [[UBE2E2]] (-2.6), [[SPART]] (-2.6), [[HLA-A]] (-2.5), [[AHR]] (-2.5), [[FXYD5]] (-2.5), [[ZC3H12C]] (-2.5), [[HDAC9]] (-2.5), [[ATXN1]] (-2.5), [[ETS1]] (-2.5), [[AKT3]] (-2.5) (410 genes, 12 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 1): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 13 (0.354; genes UGP2, KLF9, TSC22D3, SSBP2 / LUC7L3, PER3, TCP10L, SEMA3A); component 3 (0.366; genes MCL1, NABP1, DUSP6, EGR1 / KCTD3, TMEM123, XPO1, TNRC6A); component 14 (0.372; genes PNPT1, HILPDA, P4HB, ASCC3 / MBOAT2, SMARCA2, CSNK1G3, MACO1); component 11 (0.411; genes BCL2L1, CCND3, TBC1D8, B4GALT1 / E2F7, MAP1B, NGLY1, KIF21A)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 17 in all, 17 with an alert ⚠; shown: the 15 strongest; 2 more groups (2 of them with an alert ⚠) not shown. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 44 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[POLE]] | POLE altered (any record) (8 lines) vs not recorded (42) | 1 / 0 / 0 | A 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[KMT2D]] | KMT2D altered (any record) (15 lines) vs not recorded (35) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[SETD1B]] | SETD1B altered (any record) (11 lines) vs not recorded (39) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, ARID1A |
| [[ARID1A]] | ARID1A altered (any record) (15 lines) vs not recorded (35) | 0 / 0 / 1 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[FBXW7]] | FBXW7 loss of function (5 lines) vs not recorded (45) | 0 / 1 / 0 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines |
| [[ARID1A]] | ARID1A loss of function (12 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[KMT2D]] | KMT2D loss of function (8 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[MET]] | MET altered (any record) (3 lines) vs not recorded (47) | 0 / 0 / 0 | — | ⚠ few lines (3 vs 47); tissue-confounded; across organs; mechanism partly not recorded; MET not expressed in 1 of the 3 altered lines |
| [[PIK3R1]] | PIK3R1 altered (any record) (5 lines) vs not recorded (45) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; PIK3R1 not expressed in 1 of the 5 altered lines |
| [[PTEN]] | PTEN loss of function (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; PTEN not expressed in 4 of the 9 altered lines |
| [[SETD1B]] | SETD1B loss of function (10 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, PRDM2, ARID1A |
| [[SMARCA4]] | SMARCA4 altered (any record) (12 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[TERT]] | TERT altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; TERT not expressed in 2 of the 11 altered lines |
| [[WNK2]] | WNK2 altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with BRCA2, SETD1B, PRDM2 |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,330 in all, 2,330 with an alert ⚠; shown: the 15 strongest; 2,315 more line sets (2,315 of them with an alert ⚠) not shown; 2,370 genes; 2,068 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 1; `tables/line_effects.parquet` — line == 1
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 1; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 1]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include AN3 CA

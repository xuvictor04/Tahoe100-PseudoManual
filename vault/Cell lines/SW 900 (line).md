---
cell_line: "SW 900"
type: "cell line"
cell_line_id: "CVCL_1731"
depmap_id: "ACH-000669"
organ: "Lung"
tp53_status: "altered"
drivers: ["CDKN2A(Deletion)", "CDKN2B(Deletion)", "KMT2D(Stopgain)", "KRAS(Missense)", "SMAD3(Missense)", "TP53(Stopgain)"]
n_dd_depleted: 25
median_response: 1.055
tags: ["cell-line", "organ/lung"]
generated_by: "tahoemap"
---

# SW 900

*Lung · TP53 altered · CVCL_1731 · ACH-000669*

|  |  |
|---|---|
| Organ | Lung |
| TP53 status | altered |
| Drivers | CDKN2A(Deletion); CDKN2B(Deletion); KMT2D(Stopgain); KRAS(Missense); SMAD3(Missense); TP53(Stopgain) |
| Driver changes | KMT2D p.K5522*; KRAS p.G12V; SMAD3 p.K334E; TP53 p.Q167* |
| Cells over all wells | 1,708,739 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 1.06 (1 = a typical line) |
| Drug-doses that deplete it | 25 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 12 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 15,266 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 48): the line loses cells relative to the other lines in the same wells. Drug-doses: 26 in all, 14 with an alert ⚠; shown: the 12 strongest and the 9 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -10.0 | -1.13 |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.0 | -0.62 |
| [[PH-797804 (drug)]] 5 µM |  | -7.6 | -0.89 |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.7 | -0.73 |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.2 | -0.63 |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -0.57 |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -0.53 |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.4 | -0.57 |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -0.43 |
| [[Lopinavir (drug)]] 5 µM |  | -4.1 | -0.41 |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.42 |
| [[Alpelisib (drug)]] 5 µM |  | -4.0 | -0.47 |
| [[BI-3406 (drug)]] 5 µM |  | -3.8 | -0.39 |
| [[venetoclax (drug)]] 5 µM |  | -3.7 | -0.44 |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.7 | -0.43 |
| [[Gallic acid (drug)]] 0.05 µM |  | -3.4 | -0.36 |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | -3.3 | -0.42 |
| [[RMC-6236 (drug)]] 5 µM |  | -3.1 | -0.31 |
| [[Vismodegib (drug)]] 5 µM |  | -3.1 | -0.31 |
| [[Macitentan (drug)]] 5 µM |  | -3.1 | -0.34 |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -0.33 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Ritonavir (drug)]] 0.5 µM (1.86); [[Econazole (drug)]] 5 µM (1.82); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (1.74, ⚠ cell-cycle shift); [[Phenylephrine (hydrochloride) (drug)]] 5 µM (1.70); [[Citalopram (hydrobromide) (drug)]] 0.05 µM (1.64); [[Dexamethasone (drug)]] 0.05 µM (1.64); [[Budesonide (drug)]] 0.5 µM (1.63); [[Ivabradine (hydrochloride) (drug)]] 5 µM (1.59, ⚠ unreliable plate only); [[Clobetasol propionate (drug)]] 0.5 µM (1.59); [[Decitabine (drug)]] 0.05 µM (1.57)
- Weakest: [[Crizotinib (hydrochloride) (drug)]] 0.5 µM (0.103); [[Monocrotaline (drug)]] 0.05 µM (0.181); [[Bicalutamide (drug)]] 0.5 µM (0.307); [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM (0.329); [[Elagolix sodium (drug)]] 0.5 µM (0.368); [[Cyclosporin A (drug)]] 0.5 µM (0.392); [[Almonertinib (hydrochloride) (drug)]] 5 µM (0.404); [[Bimatoprost (drug)]] 0.5 µM (0.418)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 48): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[BIRC3]] (27, 5 ⚠), [[FKBP5]] (26, 6 ⚠), [[SAMD4A]] (21, 2 ⚠), [[RBMS3]] (19), [[CPD]] (18), [[TSC22D3]] (17), [[IRS2]] (17), [[ACSL1]] (17, 3 ⚠), [[ERGIC1]] (16), [[KLF9]] (16), [[SORT1]] (16), [[PEG10]] (16, 8 ⚠), [[IRAK3]] (15)
- down: [[HMGA2]] (28, 6 ⚠), [[ITGA1]] (27, 9 ⚠), [[DHRS3]] (27, 12 ⚠), [[SMOX]] (26, 17 ⚠), [[ZMYND8]] (23, 8 ⚠), [[VEGFA]] (23, 15 ⚠), [[ZNF652]] (22, 9 ⚠), [[FAM114A1]] (22, 12 ⚠), [[PLD1]] (22, 13 ⚠), [[ITGA2]] (21, 5 ⚠), [[ARHGAP35]] (21, 15 ⚠), [[FRY]] (20, 10 ⚠), [[ITGB5]] (19, 3 ⚠), [[ETV1]] (19, 4 ⚠), [[DUSP6]] (18, 2 ⚠), [[RDH10]] (18, 5 ⚠), [[NRP1]] (16, 2 ⚠), [[NT5E]] (15), [[IFI44L]] (15, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[PTGS2]] (+6.7), [[IRAK3]] (+6.4), [[TMEM156]] (+6.4), [[CYP1B1]] (+6.3), [[AQP4-AS1]] (+6.1), [[CLDN10-AS1]] (+5.8), [[MMP13]] (+5.5), [[ADGRF5]] (+5.5), [[SFRP1]] (+5.4), [[LINC00540]] (+5.4), [[KRT81]] (+5.2), [[ENSG00000229618]] (+5.2, ⚠ noise-class RNA), [[CRTAC1]] (+5.2), [[CD38]] (+5.1), [[EYA1]] (+5.1), [[ADAM8]] (+5.0) (1,164 genes, 83 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[CRYBB2P1-1]] (-3.1), [[MTAP]] (-3.0), [[KCNQ1OT1]] (-2.9), [[MAFIP]] (-2.6), [[ENSG00000290199]] (-2.4, ⚠ noise-class RNA), [[GRK3]] (-2.3), [[EPIC1]] (-2.3), [[ENSG00000249413]] (-2.3, ⚠ noise-class RNA), [[CDKN2A]] (-2.1), [[LDLRAD3]] (-2.1), [[PRTG]] (-2.0), [[ZC3H12B]] (-2.0), [[SLC6A8]] (-2.0), [[MVB12B]] (-2.0), [[ENSG00000264545]] (-2.0, ⚠ noise-class RNA), [[NIHCOLE]] (-1.9), [[PDE3B]] (-1.9), [[GALNT10]] (-1.9) (60 genes, 5 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 48): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.903 to 1.44).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 8 in all, 8 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 56 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[CDKN2B]] | CDKN2B loss of function (13 lines) vs not recorded (37) | 4 / 2 / 0 | B 3, C 3; 6 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[KMT2D]] | KMT2D altered (any record) (15 lines) vs not recorded (35) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[KMT2D]] | KMT2D loss of function (8 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[SMAD3]] | SMAD3 altered (any record) (3 lines) vs not recorded (47) | 0 / 0 / 0 | — | ⚠ few lines (3 vs 47); within organs, on part of the lines; mechanism partly not recorded; SMAD3 not expressed in 1 of the 3 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,340 in all, 1,340 with an alert ⚠; shown: the 15 strongest; 1,325 more line sets (1,325 of them with an alert ⚠) not shown; 1,368 genes; 1,123 of the sets gave arrows. Ranked by the number of arrows.*

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
| [[ITGB6]] | 32 vs 18 | 5 / 148 / 18 | B 47, C 124; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TJP3]] | 29 vs 21 | 7 / 155 / 9 | B 61, C 110; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 48; `tables/line_effects.parquet` — line == 48
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 48; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 48]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include SW 900

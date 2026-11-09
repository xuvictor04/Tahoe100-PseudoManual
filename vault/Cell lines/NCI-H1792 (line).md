---
cell_line: "NCI-H1792"
type: "cell line"
cell_line_id: "CVCL_1495"
depmap_id: "ACH-000496"
organ: "Lung"
tp53_status: "altered"
drivers: ["CDKN2A(Stopgain)", "KRAS(Missense)", "MYC(Gain)", "SOS1(Gain)", "TP53(Splice_site)"]
n_dd_depleted: 52
median_response: 1.012
tags: ["cell-line", "organ/lung"]
generated_by: "tahoemap"
---

# NCI-H1792

*Lung · TP53 altered · CVCL_1495 · ACH-000496*

|  |  |
|---|---|
| Organ | Lung |
| TP53 status | altered |
| Drivers | CDKN2A(Stopgain); KRAS(Missense); MYC(Gain); SOS1(Gain); TP53(Splice_site) |
| Driver changes | CDKN2A p.W110*; KRAS p.G12C |
| Cells over all wells | 1,838,436 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 1.01 (1 = a typical line) |
| Drug-doses that deplete it | 52 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 39 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,847 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 34): the line loses cells relative to the other lines in the same wells. Drug-doses: 54 in all, 15 with an alert ⚠; shown: the 12 strongest and the 10 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -26.8 | -3.32 |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -15.9 | -1.70 |
| [[RMC-6236 (drug)]] 5 µM |  | -15.4 | -1.74 |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -15.0 | -1.67 |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -13.7 | -1.73 |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -12.9 | -1.41 |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -12.6 | -0.92 |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -12.1 | -1.04 |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.1 | -1.14 |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -8.7 | -0.95 |
| [[BI-3406 (drug)]] 5 µM |  | -8.6 | -0.94 |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -8.5 | -1.62 |
| [[Bimiralisib (drug)]] 5 µM |  | -8.1 | -0.83 |
| [[Trametinib (drug)]] 0.5 µM |  | -8.1 | -0.59 |
| [[Binimetinib (drug)]] 5 µM |  | -6.9 | -0.51 |
| [[AT7519 (drug)]] 5 µM |  | -6.7 | -0.74 |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.6 | -0.65 |
| [[Afatinib (drug)]] 5 µM |  | -6.5 | -0.49 |
| [[BI-3406 (drug)]] 0.5 µM |  | -6.4 | -0.63 |
| [[GSK1059615 (drug)]] 5 µM |  | -6.2 | -0.64 |
| [[Binimetinib (drug)]] 0.5 µM |  | -6.1 | -0.44 |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.9 | -0.73 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Dexamethasone (drug)]] 5 µM (2.07); [[Dexamethasone (drug)]] 0.05 µM (1.99); [[Econazole (drug)]] 5 µM (1.94); [[Citalopram (hydrobromide) (drug)]] 0.05 µM (1.93); [[Clobetasol propionate (drug)]] 5 µM (1.92); [[Medroxyprogesterone acetate (drug)]] 5 µM (1.92); [[Budesonide (drug)]] 5 µM (1.91); [[Budesonide (drug)]] 0.5 µM (1.89)
- Weakest: [[Citalopram (hydrobromide) (drug)]] 0.5 µM (-0.0332); [[Trifluridine (drug)]] 0.5 µM (-0.0318, ⚠ cell-cycle shift); [[Raltitrexed (drug)]] 0.5 µM (0.0825); [[Orlistat (drug)]] 0.05 µM (0.201); [[Canagliflozin (drug)]] 0.05 µM (0.247); [[Saquinavir (drug)]] 0.5 µM (0.313); [[Glycyrrhizic acid (drug)]] 0.05 µM (0.316); [[Dihydroartemisinin (drug)]] 0.5 µM (0.326); [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM (0.389)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 34): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[FKBP5]] (26, 5 ⚠), [[IRAK3]] (21), [[TANC2]] (21), [[ZHX3]] (21), [[CCND3]] (21, 1 ⚠), [[ITGA10]] (21, 1 ⚠), [[TSC22D3]] (20), [[TOP1]] (20, 2 ⚠), [[HIPK2]] (19), [[COPS8]] (19, 2 ⚠), [[NRCAM]] (18), [[SORBS2]] (18), [[ACSL1]] (18, 4 ⚠), [[MAP2]] (17)
- down: [[SGIP1]] (34, 11 ⚠), [[ENSG00000259354]] (32, 14 ⚠), [[WNT7B]] (27, 4 ⚠), [[IGFBP3]] (27, 12 ⚠), [[MRPS6]] (25, 9 ⚠), [[PLD1]] (25, 11 ⚠), [[HMGA2]] (24, 2 ⚠), [[CDCP1]] (24, 5 ⚠), [[IFI44L]] (24, 8 ⚠), [[SLC5A3]] (24, 8 ⚠), [[MX2]] (23, 6 ⚠), [[HMGN2P46]] (23, 12 ⚠), [[MX1]] (22, 5 ⚠), [[SEMA3A]] (20, 2 ⚠), [[PTGS2]] (20, 3 ⚠), [[ANXA10]] (19, 2 ⚠), [[EIF2AK2]] (18, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[PTGIS]] (+6.1), [[ADAMTS14]] (+6.1), [[AADACP1]] (+6.1), [[ANXA10]] (+6.1), [[ENSG00000255595]] (+6.1, ⚠ noise-class RNA), [[LOX]] (+6.1), [[HTRA3]] (+6.1), [[ENSG00000286010]] (+6.0, ⚠ noise-class RNA), [[MIR3171HG]] (+6.0), [[CXCL5]] (+6.0), [[CASC11]] (+5.9), [[AADAC]] (+5.9), [[ENSG00000259639]] (+5.9, ⚠ noise-class RNA), [[PKP1]] (+5.8), [[ENSG00000265980]] (+5.8, ⚠ noise-class RNA), [[LINC03047]] (+5.8), [[PRRX1]] (+5.7), [[ACKR3]] (+5.6), [[IRAK3]] (+5.6) (1,499 genes, 129 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[USP25]] (-4.0), [[HSPA13]] (-3.8), [[NRIP1]] (-3.7), [[RIN2]] (-3.6), [[BTG3]] (-3.6), [[PRNP]] (-3.5), [[ENSG00000235609]] (-3.4, ⚠ noise-class RNA), [[JAG1]] (-3.4), [[CXADR]] (-3.2), [[ROBO1]] (-3.1), [[HDX]] (-3.0), [[TENM3]] (-3.0), [[USP43]] (-3.0), [[NEO1]] (-2.9), [[GLI3]] (-2.9), [[LSR]] (-2.8) (103 genes, 3 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 34): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Strong here (> 1.5): component 13 (1.55; genes UGP2, KLF9, TSC22D3, SSBP2 / LUC7L3, PER3, TCP10L, SEMA3A)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 5 in all, 5 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 59 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[MYC]] | MYC gain of function (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,723 in all, 1,723 with an alert ⚠; shown: the 15 strongest; 1,708 more line sets (1,708 of them with an alert ⚠) not shown; 1,753 genes; 1,474 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 34; `tables/line_effects.parquet` — line == 34
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 34; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 34]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include NCI-H1792

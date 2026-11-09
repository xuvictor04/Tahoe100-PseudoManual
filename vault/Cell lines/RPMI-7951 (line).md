---
cell_line: "RPMI-7951"
type: "cell line"
cell_line_id: "CVCL_1666"
depmap_id: "ACH-000348"
organ: "Skin"
tp53_status: "altered"
drivers: ["BRAF(Missense)", "CDKN2A(Missense)", "PTEN(Deletion)", "TERT(Promoter)", "TP53(Stopgain)"]
n_dd_depleted: 31
median_response: 1.006
tags: ["cell-line", "organ/skin"]
generated_by: "tahoemap"
---

# RPMI-7951

*Skin · TP53 altered · CVCL_1666 · ACH-000348*

|  |  |
|---|---|
| Organ | Skin |
| TP53 status | altered |
| Drivers | BRAF(Missense); CDKN2A(Missense); PTEN(Deletion); TERT(Promoter); TP53(Stopgain) |
| Driver changes | BRAF p.V600E; CDKN2A p.L16R; TP53 p.S166* |
| Cells over all wells | 1,607,393 |
| Wells with usable expression | 1,328 (99.9%) |
| Median response strength (β) | 1.01 (1 = a typical line) |
| Drug-doses that deplete it | 31 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 15 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 15,003 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 42): the line loses cells relative to the other lines in the same wells. Drug-doses: 33 in all, 18 with an alert ⚠; shown: the 12 strongest and the 9 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -10.9 | -1.37 |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -8.4 | -1.34 |
| [[EX229 (drug)]] 5 µM |  | -7.8 | -1.14 |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -7.6 | -2.82 |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.0 | -0.84 |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.9 | -1.01 |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | -0.98 |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.4 | -0.73 |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.2 | -1.19 |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | -0.68 |
| [[Ipatasertib (drug)]] 0.5 µM |  | -5.9 | -0.76 |
| [[venetoclax (drug)]] 5 µM |  | -5.9 | -0.86 |
| [[vincristine (drug)]] 5 µM |  | -5.5 | -0.85 |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.4 | -0.63 |
| [[Auranofin (drug)]] 5 µM |  | -4.8 | -0.57 |
| [[Belzutifan (drug)]] 5 µM |  | -4.5 | -0.68 |
| [[GSK1059615 (drug)]] 0.5 µM |  | -4.5 | -0.56 |
| [[TAK-733 (drug)]] 5 µM |  | -4.3 | -0.56 |
| [[DTP3 (drug)]] 5 µM |  | -4.1 | -0.57 |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.1 | -0.56 |
| [[Celecoxib (drug)]] 0.5 µM |  | -3.4 | -0.40 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 488, 84 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Malotilate (drug)]] 0.5 µM (1.76); [[Hydroxyfasudil (drug)]] 0.05 µM (1.68, ⚠ unreliable plate only); [[LJI308 (drug)]] 0.05 µM (1.66); [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM (1.65, ⚠ unreliable plate only); [[Belumosudil (mesylate) (drug)]] 5 µM (1.65); [[Neratinib (drug)]] 0.5 µM (1.64); [[Econazole (drug)]] 5 µM (1.63); [[Rapamycin (drug)]] 0.05 µM (1.59); [[Dexamethasone (drug)]] 5 µM (1.59); [[Dexamethasone (drug)]] 0.05 µM (1.58)
- Weakest: [[Amsacrine (drug)]] 0.5 µM (0.238); [[BI-3406 (drug)]] 5 µM (0.311); [[Lidocaine (hydrochloride) (drug)]] 5 µM (0.311); [[Ferulic acid (drug)]] 0.5 µM (0.346); [[Trifluridine (drug)]] 5 µM (0.373, ⚠ cell-cycle shift); [[AZD-8055 (drug)]] 0.05 µM (0.422); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM (0.425); [[Alpelisib (drug)]] 5 µM (0.464); [[Canagliflozin (drug)]] 0.05 µM (0.475)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 42): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[HIPK2]] (19), [[IRAK3]] (18), [[HIP1]] (18), [[AKAP12]] (17), [[TOP1]] (16), [[TBC1D8]] (16), [[SDK1]] (14), [[FOXO1]] (13), [[ACSL1]] (13, 3 ⚠), [[PTPRG]] (11), [[HSPA4]] (11, 6 ⚠), [[ENSG00000285744]] (10), [[ASH1L]] (10, 1 ⚠)
- down: [[EML5]] (27, 10 ⚠), [[IFI44L]] (24, 6 ⚠), [[ZMYND8]] (23, 9 ⚠), [[RHBDF2]] (21, 8 ⚠), [[PSD3]] (20, 9 ⚠), [[MTSS1]] (20, 13 ⚠), [[PLSCR1]] (19, 4 ⚠), [[TBC1D32]] (19, 5 ⚠), [[MX1]] (19, 5 ⚠), [[TNS1]] (19, 14 ⚠), [[TRIM22]] (18, 3 ⚠), [[PARP9]] (18, 3 ⚠), [[PLD1]] (18, 10 ⚠), [[CA12]] (18, 12 ⚠), [[EIF2AK2]] (17, 2 ⚠), [[CMPK2]] (16, 2 ⚠), [[HMGA2]] (16, 2 ⚠), [[NT5E]] (15), [[OAS3]] (14)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[COL1A2]] (+7.4), [[LINC02109]] (+7.4), [[LINC02476]] (+7.3), [[APCDD1L]] (+7.3), [[MMP2]] (+7.1), [[TIMP3]] (+6.6), [[SYNDIG1]] (+6.5), [[LINC01435]] (+6.4), [[MSR1]] (+6.3), [[COLEC10]] (+6.3), [[APCDD1L-DT]] (+6.2), [[ITGA11]] (+6.1), [[THY1]] (+6.0), [[SPARC]] (+6.0), [[AEBP1]] (+6.0) (1,495 genes, 144 with an alert ⚠; shown: the 15 strongest)
- Lacks: [[TNFRSF10D]] (-3.6), [[PTEN]] (-3.4), [[GPX1]] (-3.4), [[DSG2]] (-3.3), [[PPP1R9A]] (-3.2), [[ATAD1]] (-3.2), [[CMTM8]] (-3.2), [[LRP5]] (-3.1), [[EFNA5]] (-3.0), [[ADGRG6]] (-3.0), [[WWC1]] (-2.9), [[ARAP2]] (-2.9), [[MAP3K21]] (-2.9), [[EPB41L4B]] (-2.9), [[CHMP4C]] (-2.8) (151 genes, 1 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 42): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.822 to 1.30).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 7 in all, 7 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 56 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[BRAF]] | BRAF altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[BRAF]] | BRAF gain of function (7 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[PTEN]] | PTEN loss of function (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; PTEN not expressed in 4 of the 9 altered lines |
| [[TERT]] | TERT altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; TERT not expressed in 2 of the 11 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,601 in all, 1,601 with an alert ⚠; shown: the 15 strongest; 1,586 more line sets (1,586 of them with an alert ⚠) not shown; 1,634 genes; 1,402 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[TMPRSS4]], [[OVOL1]] | 33 vs 17 | 14 / 223 / 24 | B 115, C 146; 261 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[IRF6]], [[C1orf116]] | 31 vs 19 | 18 / 216 / 24 | B 128, C 130; 258 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ST14]] | 32 vs 18 | 11 / 196 / 21 | B 88, C 140; 228 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
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
| [[TC2N]] | 28 vs 22 | 3 / 163 / 5 | B 52, C 119; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 42; `tables/line_effects.parquet` — line == 42
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 42; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 42]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include RPMI-7951

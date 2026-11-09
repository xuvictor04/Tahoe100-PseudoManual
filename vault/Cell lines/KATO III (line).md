---
cell_line: "KATO III"
type: "cell line"
cell_line_id: "CVCL_0371"
depmap_id: "ACH-000793"
organ: "Esophagus/Stomach"
tp53_status: "altered"
drivers: ["ATM(Missense)", "BRCA2(Missense)", "CTNNB1(Gain)", "FGFR2(Gain)", "KMT2D(Missense)", "KMT2D(Stopgain)", "TP53(Deletion)"]
n_dd_depleted: 14
median_response: 0.892
tags: ["cell-line", "organ/esophagus_stomach"]
generated_by: "tahoemap"
---

# KATO III

*Esophagus/Stomach · TP53 altered · CVCL_0371 · ACH-000793*

|  |  |
|---|---|
| Organ | Esophagus/Stomach |
| TP53 status | altered |
| Drivers | ATM(Missense); BRCA2(Missense); CTNNB1(Gain); FGFR2(Gain); KMT2D(Missense); KMT2D(Stopgain); TP53(Deletion) |
| Driver changes | ATM p.S2581I; BRCA2 p.G2044V; KMT2D p.A3242P; KMT2D p.E1747* |
| Cells over all wells | 2,229,454 |
| Wells with usable expression | 1,328 (99.9%) |
| Median response strength (β) | 0.892 (1 = a typical line) |
| Drug-doses that deplete it | 14 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 3 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 13,840 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 15): the line loses cells relative to the other lines in the same wells. Drug-doses: 14 in all, 11 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -12.1 | -1.08 |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -10.1 | -4.26 |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.3 | -1.29 |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -8.4 | -1.02 |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.1 | -0.84 |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | -0.75 |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | -0.72 |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | -0.89 |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | -0.66 |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.6 | -0.80 |
| [[vincristine (drug)]] 5 µM |  | -3.9 | -0.51 |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -0.44 |
| [[Verteporfin (drug)]] 0.05 µM |  | -3.5 | -0.42 |
| [[9-ING-41 (drug)]] 5 µM |  | -3.3 | -0.38 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 488, 84 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Sonidegib (drug)]] 0.05 µM (2.05, ⚠ unreliable plate only); [[Hydroxyfasudil (drug)]] 0.05 µM (1.97, ⚠ unreliable plate only); [[Quinestrol (drug)]] 5 µM (1.96); [[palbociclib (drug)]] 5 µM (1.85); [[Mifepristone (drug)]] 5 µM (1.82); [[Cabozantinib (S-malate) (drug)]] 5 µM (1.81); [[Vandetanib (drug)]] 5 µM (1.74); [[palbociclib (drug)]] 0.5 µM (1.73, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 0.05 µM (1.66); [[Ponatinib (drug)]] 0.5 µM (1.55); [[Bexarotene (drug)]] 0.05 µM (1.52)
- Weakest: [[Neratinib (drug)]] 0.05 µM (0.0635); [[Hydroxyurea (drug)]] 0.05 µM (0.122); [[Piroxicam (drug)]] 0.05 µM (0.129); [[Pitavastatin (Calcium) (drug)]] 0.05 µM (0.133); [[Allantoin (drug)]] 0.05 µM (0.176, ⚠ transcription drop); [[Econazole (drug)]] 5 µM (0.188); [[Triamcinolone (drug)]] 0.5 µM (0.229); [[Phenylephrine (hydrochloride) (drug)]] 5 µM (0.255); [[Budesonide (drug)]] 0.5 µM (0.268)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 15): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[CREB5]] (20, 7 ⚠), [[SQSTM1]] (15, 4 ⚠), [[STIP1]] (15, 11 ⚠), [[YWHAG]] (14, 2 ⚠), [[KPNA4]] (14, 2 ⚠), [[ATP6V1A]] (14, 3 ⚠), [[HSPA4]] (14, 7 ⚠), [[ARRDC4]] (13, 1 ⚠), [[RSRC2]] (13, 3 ⚠), [[PSMD14]] (13, 3 ⚠), [[ATP6V1H]] (12, 1 ⚠), [[RAB7A]] (12, 1 ⚠), [[OSBPL9]] (12, 1 ⚠), [[ZFPM2-AS1]] (12, 1 ⚠), [[MAP4K5]] (12, 4 ⚠), [[SPAG9]] (11, 1 ⚠), [[PPP1R15A]] (11, 1 ⚠)
- down: [[CEMIP]] (30, 16 ⚠), [[ABCC3]] (29, 8 ⚠), [[ITGA2]] (27, 6 ⚠), [[ENSG00000260877]] (24, 7 ⚠), [[LDLRAD4]] (24, 13 ⚠), [[DUSP6]] (23, 7 ⚠), [[FLNB]] (23, 9 ⚠), [[MAML2]] (23, 11 ⚠), [[LRP8]] (22, 5 ⚠), [[DLC1]] (22, 5 ⚠), [[EHBP1]] (22, 9 ⚠), [[CASC19]] (20, 4 ⚠), [[TNFRSF6B]] (20, 7 ⚠), [[DDX60]] (19, 5 ⚠), [[ETV5]] (19, 5 ⚠), [[APOL6]] (17, 3 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[FGFR2]] (+8.7), [[CEACAM5]] (+7.7), [[NPSR1]] (+7.4), [[CEACAM6]] (+7.2), [[AGR3]] (+7.1), [[LINC01610]] (+7.1), [[ENSG00000233928]] (+6.8, ⚠ noise-class RNA), [[TFF2]] (+6.7), [[CAPN8]] (+6.7), [[AGR2]] (+6.5), [[CTSE]] (+6.4), [[ENSG00000286134]] (+6.4, ⚠ noise-class RNA), [[LINC02930]] (+6.3), [[TMPRSS4]] (+6.3), [[GPX2]] (+6.2), [[TMC5]] (+6.2), [[MGAM2]] (+6.2) (1,626 genes, 124 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[NR3C1]] (-4.0), [[VIM]] (-4.0), [[QKI]] (-3.9), [[WDFY3]] (-3.8), [[KLF7]] (-3.8), [[PLOD2]] (-3.8), [[PAM]] (-3.7), [[FERMT2]] (-3.7), [[ERBIN]] (-3.7), [[UBE2E1]] (-3.7), [[BMPR1A]] (-3.7), [[ZNF655]] (-3.7), [[KIRREL1]] (-3.7), [[DIP2C]] (-3.7), [[AKT3]] (-3.6) (490 genes, 12 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 15): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.790 to 1.37).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 7 in all, 7 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 55 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[KMT2D]] | KMT2D altered (any record) (15 lines) vs not recorded (35) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[ATM]] | ATM altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[BRCA2]] | BRCA2 altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with WNK2, TGFBR2, PIK3CA |
| [[CTNNB1]] | CTNNB1 altered (any record) (5 lines) vs not recorded (45) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[CTNNB1]] | CTNNB1 gain of function (4 lines) vs not recorded (45) | 0 / 0 / 0 | — | ⚠ few lines (4 vs 45); within organs, on part of the lines |
| [[KMT2D]] | KMT2D loss of function (8 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,580 in all, 2,580 with an alert ⚠; shown: the 15 strongest; 2,565 more line sets (2,565 of them with an alert ⚠) not shown; 2,637 genes; 2,249 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[CLIC5]] | 37 vs 13 | 4 / 185 / 7 | B 59, C 137; 196 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SPOCK1]] | 29 vs 21 | 1 / 62 / 45 | B 58, C 50; 108 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PADI1]] | 34 vs 16 | 3 / 102 / 1 | B 35, C 71; 106 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MYO7B]] | 36 vs 14 | 0 / 105 / 0 | B 25, C 80; 105 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[FAM3D]] | 43 vs 7 | 1 / 103 / 0 | B 16, C 88; 104 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MMP7]] | 39 vs 11 | 5 / 97 / 0 | B 39, C 63; 102 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[APCDD1L]] | 34 vs 16 | 2 / 99 / 0 | B 16, C 85; 101 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ITGA11]] | 34 vs 16 | 2 / 95 / 0 | B 19, C 78; 97 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01411]] | 38 vs 12 | 0 / 97 / 0 | B 13, C 84; 97 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PDGFRB]] | 36 vs 14 | 1 / 94 / 1 | B 21, C 75; 96 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[KCNMA1]] | 26 vs 24 | 3 / 43 / 47 | B 70, C 23; 93 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[INSYN2B]] | 31 vs 19 | 0 / 92 / 0 | B 18, C 74; 92 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[NECTIN4]] | 33 vs 17 | 4 / 85 / 0 | B 24, C 65; 89 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[FRMD4A]] | 24 vs 26 | 2 / 85 / 1 | B 28, C 60; 88 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[COL5A1]] | 30 vs 20 | 3 / 84 / 0 | B 20, C 67; 87 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 15; `tables/line_effects.parquet` — line == 15
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 15; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 15]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include KATO III

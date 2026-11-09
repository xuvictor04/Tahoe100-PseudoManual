---
cell_line: "SK-MEL-2"
type: "cell line"
cell_line_id: "CVCL_0069"
depmap_id: "ACH-001190"
organ: "Skin"
tp53_status: "altered"
drivers: ["CCND1(Gain)", "EP300(Missense)", "NRAS(Missense)", "POLE(Missense)", "SETD1B(Frameshift)", "TERT(Promoter)", "TP53(Missense)", "ZFHX3(Frameshift)"]
n_dd_depleted: 44
median_response: 0.9
tags: ["cell-line", "organ/skin"]
generated_by: "tahoemap"
---

# SK-MEL-2

*Skin · TP53 altered · CVCL_0069 · ACH-001190*

|  |  |
|---|---|
| Organ | Skin |
| TP53 status | altered |
| Drivers | CCND1(Gain); EP300(Missense); NRAS(Missense); POLE(Missense); SETD1B(Frameshift); TERT(Promoter); TP53(Missense); ZFHX3(Frameshift) |
| Driver changes | EP300 p.P989S; NRAS p.Q61R; POLE p.T1052A; SETD1B p.L1255fs; TP53 p.G245S; ZFHX3 p.H3611fs |
| Cells over all wells | 1,548,634 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.900 (1 = a typical line) |
| Drug-doses that deplete it | 44 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 27 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,940 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 2): the line loses cells relative to the other lines in the same wells. Drug-doses: 44 in all, 17 with an alert ⚠; shown: the 12 strongest and the 8 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -16.0 | -1.99 |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -14.1 | -1.82 |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -13.6 | -2.49 |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -10.8 | -1.84 |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -10.6 | -2.16 |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -9.7 | -1.73 |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.8 | -2.26 |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -7.4 | -0.80 |
| [[Binimetinib (drug)]] 5 µM |  | -7.0 | -0.80 |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.9 | -1.12 |
| [[GSK1059615 (drug)]] 5 µM |  | -6.7 | -1.05 |
| [[RMC-6236 (drug)]] 5 µM |  | -6.6 | -1.02 |
| [[Abemaciclib (drug)]] 5 µM |  | -6.2 | -1.04 |
| [[BI-3406 (drug)]] 5 µM |  | -6.0 | -0.97 |
| [[Bimiralisib (drug)]] 5 µM |  | -5.8 | -0.90 |
| [[Infigratinib (drug)]] 5 µM |  | -5.8 | -0.97 |
| [[Brivudine (drug)]] 5 µM |  | -5.5 | -0.86 |
| [[EX229 (drug)]] 5 µM |  | -5.3 | -0.91 |
| [[Encorafenib (drug)]] 5 µM |  | -5.2 | -0.79 |
| [[Belumosudil (drug)]] 5 µM |  | -5.1 | -0.81 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Pitavastatin (Calcium) (drug)]] 0.05 µM (1.70); [[Futibatinib (drug)]] 0.05 µM (1.67); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (1.64); [[Benproperine (phosphate) (drug)]] 5 µM (1.54); [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM (1.50, ⚠ unreliable plate only); [[Flumatinib (mesylate) (drug)]] 5 µM (1.49); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (1.47); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM (1.47); [[Fluvoxamine (drug)]] 0.5 µM (1.42)
- Weakest: [[Allantoin (drug)]] 0.05 µM (-0.440, ⚠ transcription drop); [[Pralsetinib (drug)]] 0.05 µM (-0.0695); [[Neratinib (drug)]] 0.05 µM (0.189); [[Verteporfin (drug)]] 0.5 µM (0.193); [[Naproxen (drug)]] 0.05 µM (0.225); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM (0.309); [[olaparib (drug)]] 0.05 µM (0.318, ⚠ unreliable plate only); [[Fluvoxamine (maleate) (drug)]] 0.5 µM (0.352); [[Carbamazepine (drug)]] 0.5 µM (0.353); [[Cytarabine (drug)]] 0.05 µM (0.387)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 2): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[FKBP5]] (22, 7 ⚠), [[CCND3]] (18), [[ZMYND8]] (17), [[ABLIM3]] (16), [[RPGR]] (14), [[AKAP13]] (14), [[HSPA4]] (14, 8 ⚠), [[SLC26A2]] (13), [[ABL2]] (13, 2 ⚠), [[MAP2K3]] (13, 4 ⚠), [[DNAJB1]] (13, 5 ⚠), [[SERTAD2]] (12, 1 ⚠), [[PCLO]] (12, 1 ⚠), [[HSP90AA1]] (12, 8 ⚠), [[TBC1D8]] (11)
- down: [[TGFA]] (27, 4 ⚠), [[ITGA3]] (26, 5 ⚠), [[ITGB5]] (26, 5 ⚠), [[NIHCOLE]] (26, 17 ⚠), [[MSRB3-AS1]] (25, 6 ⚠), [[NIBAN2]] (24, 6 ⚠), [[INPP5F]] (24, 8 ⚠), [[PLD1]] (24, 12 ⚠), [[NT5E]] (23, 2 ⚠), [[IL1RAP]] (23, 3 ⚠), [[PHC2]] (23, 4 ⚠), [[RAD51B]] (23, 12 ⚠), [[ACTN1]] (22, 3 ⚠), [[ITGB3]] (22, 5 ⚠), [[STX1A]] (20, 3 ⚠), [[MIR100HG]] (19, 2 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[NRG3]] (+8.2), [[ENSG00000241168]] (+7.9, ⚠ noise-class RNA), [[ENSG00000253500]] (+7.8, ⚠ noise-class RNA), [[LINC01320]] (+7.8), [[LINC00504]] (+7.6), [[MSRB3-AS1]] (+7.6), [[ENSG00000250954]] (+7.5, ⚠ noise-class RNA), [[ENSG00000234426]] (+7.4, ⚠ noise-class RNA), [[APOD]] (+7.2), [[LINC01205]] (+7.2), [[SOX10]] (+7.2), [[ENSG00000251574]] (+7.0, ⚠ noise-class RNA), [[ENSG00000232053]] (+7.0, ⚠ noise-class RNA), [[SAMMSON]] (+6.9), [[LINC02476]] (+6.9), [[LINC02377]] (+6.8), [[LINC00383]] (+6.8), [[PMEL]] (+6.8), [[DISC1FP1]] (+6.6), [[LINC02267]] (+6.6), [[LINC02566]] (+6.6) (1,794 genes, 233 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[SOX9]] (-3.7), [[TSPAN5]] (-3.7), [[TNFRSF10D]] (-3.6), [[TVP23C]] (-3.5), [[PARD3]] (-3.5), [[NHS]] (-3.4), [[CERS6]] (-3.3), [[ADM]] (-3.3), [[PRKCA]] (-3.3), [[H1-0]] (-3.3, ⚠ noise-class RNA), [[SERPINH1]] (-3.3), [[TVP23C-CDRT4]] (-3.2), [[TFCP2]] (-3.2), [[ETS2]] (-3.2), [[PRDX2]] (-3.2), [[MICU3]] (-3.2) (221 genes, 6 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 2): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.781 to 1.21).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 10 in all, 10 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 53 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[TERT]] | TERT gain of function (8 lines) vs not recorded (39) | 5 / 0 / 0 | C 5; 5 with an alert ⚠ | ⚠ tissue-confounded; across organs; TERT not expressed in 1 of the 8 altered lines |
| [[NRAS]] | NRAS gain of function (7 lines) vs not recorded (43) | 0 / 2 / 0 | C 2; 2 with an alert ⚠ | ⚠ within organs, on part of the lines |
| [[POLE]] | POLE altered (any record) (8 lines) vs not recorded (42) | 1 / 0 / 0 | A 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[SETD1B]] | SETD1B altered (any record) (11 lines) vs not recorded (39) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, ARID1A |
| [[EP300]] | EP300 altered (any record) (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, SETD1B |
| [[SETD1B]] | SETD1B loss of function (10 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, PRDM2, ARID1A |
| [[TERT]] | TERT altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; TERT not expressed in 2 of the 11 altered lines |
| [[ZFHX3]] | ZFHX3 altered (any record) (13 lines) vs not recorded (37) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B, PIK3CA |
| [[ZFHX3]] | ZFHX3 loss of function (8 lines) vs not recorded (37) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B, EP300, PIK3CA |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,638 in all, 1,638 with an alert ⚠; shown: the 15 strongest; 1,623 more line sets (1,623 of them with an alert ⚠) not shown; 1,664 genes; 1,492 of the sets gave arrows. Ranked by the number of arrows.*

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
| [[TC2N]] | 28 vs 22 | 3 / 163 / 5 | B 52, C 119; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 2; `tables/line_effects.parquet` — line == 2
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 2; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 2]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include SK-MEL-2

---
cell_line: "SW 1088"
type: "cell line"
cell_line_id: "CVCL_1715"
depmap_id: "ACH-000437"
organ: "CNS/Brain"
tp53_status: "altered"
drivers: ["CDKN2A(Deletion)", "CDKN2B(Deletion)", "NRAS(Missense)", "POLE(Missense)", "PTEN(Deletion)", "TP53(Missense)"]
n_dd_depleted: 5
median_response: 0.996
tags: ["cell-line", "organ/cns_brain"]
generated_by: "tahoemap"
---

# SW 1088

*CNS/Brain · TP53 altered · CVCL_1715 · ACH-000437*

|  |  |
|---|---|
| Organ | CNS/Brain |
| TP53 status | altered |
| Drivers | CDKN2A(Deletion); CDKN2B(Deletion); NRAS(Missense); POLE(Missense); PTEN(Deletion); TP53(Missense) |
| Driver changes | NRAS p.Q61K; POLE p.V1270F; TP53 p.R273C |
| Cells over all wells | 149,036 |
| Wells with usable expression | 1,235 (92.9%) |
| Median response strength (β) | 0.996 (1 = a typical line) |
| Drug-doses that deplete it | 5 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 4 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 15,448 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 44): the line loses cells relative to the other lines in the same wells. Drug-doses: 5 in all, 1 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.4 | -1.85 |
| [[Gallic acid (drug)]] 0.05 µM |  | -3.4 | -1.48 |
| [[Elimusertib hydrochloride (drug)]] 0.5 µM |  | -3.3 | -1.25 |
| [[Simotinib (drug)]] 0.5 µM |  | -3.3 | -1.94 |
| [[EX229 (drug)]] 0.5 µM |  | -3.3 | -1.23 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 435, 72 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Saquinavir (drug)]] 0.05 µM (2.57); [[Decitabine (drug)]] 0.5 µM (2.46); [[olaparib (drug)]] 0.05 µM (2.43, ⚠ unreliable plate only); [[Allantoin (drug)]] 0.05 µM (2.35, ⚠ transcription drop); [[Pimozide (drug)]] 0.5 µM (2.35, ⚠ transcription drop); [[Temsirolimus (drug)]] 0.5 µM (2.24); [[18β-Glycyrrhetinic acid (drug)]] 5 µM (2.20); [[Sunitinib (drug)]] 5 µM (2.12, ⚠ toxic); [[Citalopram (hydrobromide) (drug)]] 0.5 µM (2.08); [[NVP-BHG712 (drug)]] 0.05 µM (2.02); [[Saquinavir (drug)]] 5 µM (2.00); [[Oxaprozin (drug)]] 0.5 µM (1.92)
- Weakest: [[Simotinib (drug)]] 0.05 µM (-0.580); [[Benproperine (phosphate) (drug)]] 5 µM (-0.553); [[Glycyrrhizic acid (drug)]] 5 µM (-0.303); [[Tofacitinib (drug)]] 0.05 µM (-0.300); [[Cytarabine (hydrochloride) (drug)]] 0.05 µM (-0.271); [[Asciminib (drug)]] 0.05 µM (-0.152); [[Almonertinib (hydrochloride) (drug)]] 0.05 µM (0.0146); [[Hydroxyurea (drug)]] 5 µM (0.0392)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 44): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[KLF10]] (5), [[HSP90AA1]] (5, 1 ⚠), [[HSPD1]] (5, 1 ⚠), [[HSP90AB1]] (4), [[IRF1]] (3), [[ZSWIM6]] (3), [[SQSTM1]] (3), [[JUN]] (3), [[ENSG00000285744]] (3), [[HNRNPA2B1]] (3, 2 ⚠), [[HIVEP2]] (2), [[HDAC9]] (2), [[PPP1R15A]] (2)
- down: [[HMGA2]] (8), [[ZMYND8]] (7, 2 ⚠), [[ZNF395]] (7, 2 ⚠), [[ENSG00000259354]] (7, 2 ⚠), [[NAV1]] (7, 4 ⚠), [[VEGFC]] (6, 1 ⚠), [[DNAAF9]] (6, 2 ⚠), [[ITGA5]] (6, 2 ⚠), [[PRKN]] (6, 2 ⚠), [[BBS9]] (6, 4 ⚠), [[TFPI]] (5), [[CALU]] (5), [[MMP14]] (5), [[FNDC3B]] (5, 3 ⚠), [[ITGA3]] (4), [[LOX]] (4), [[GNB4]] (4)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[COL6A3]] (+7.7), [[MEG3]] (+7.5), [[PTN]] (+7.1), [[MEG8]] (+6.8), [[IL6]] (+6.6), [[TIMP3]] (+6.5), [[COL1A2]] (+6.4), [[THY1]] (+6.4), [[MIR493HG]] (+6.3), [[ROS1]] (+6.3), [[DKK3]] (+6.1), [[COL5A1]] (+6.0), [[NRXN3]] (+6.0), [[ENSG00000225649]] (+6.0, ⚠ noise-class RNA), [[SPARC]] (+5.9), [[WNT5A]] (+5.9) (1,240 genes, 98 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[TNFRSF10D]] (-2.6), [[PTEN]] (-2.5), [[PLAA]] (-2.5), [[RNF149]] (-2.5), [[MYO1B]] (-2.5), [[FZD6]] (-2.5), [[CAAP1]] (-2.5), [[PRKCZ]] (-2.4), [[CDCP1]] (-2.4), [[KLHL9]] (-2.4), [[IFT74]] (-2.4), [[MID2]] (-2.4), [[PTPN3]] (-2.3), [[MTAP]] (-2.3), [[RANBP17]] (-2.3) (125 genes, 1 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 44): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 42 (0.223; genes FHOD3, PMEPA1, LINC01505, CAPZB / STARD4, C4orf47, PRKCI, TCF4); component 39 (0.242; genes PVT1, RASAL2, PDP1, GNAI1 / TNIP1, ARHGAP31, MYO10, SYNM); component 22 (0.261; genes SLC9A1, LINC00910, NABP1, POLR2A / IQCJ, MIR4435-2HG, HIF1A, SH2B3); component 47 (0.274; genes EPIC1, LIMCH1, UGDH, VEGFA / LRMDA, NPC1, ITGB8, SUCO)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 7 in all, 7 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 57 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[CDKN2B]] | CDKN2B loss of function (13 lines) vs not recorded (37) | 4 / 2 / 0 | B 3, C 3; 6 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[NRAS]] | NRAS gain of function (7 lines) vs not recorded (43) | 0 / 2 / 0 | C 2; 2 with an alert ⚠ | ⚠ within organs, on part of the lines |
| [[POLE]] | POLE altered (any record) (8 lines) vs not recorded (42) | 1 / 0 / 0 | A 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[PTEN]] | PTEN loss of function (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; PTEN not expressed in 4 of the 9 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,163 in all, 1,163 with an alert ⚠; shown: the 15 strongest; 1,148 more line sets (1,148 of them with an alert ⚠) not shown; 1,182 genes; 1,008 of the sets gave arrows. Ranked by the number of arrows.*

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
| [[TOX3]] | 31 vs 19 | 4 / 168 / 1 | B 46, C 127; 173 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ITGB6]] | 32 vs 18 | 5 / 148 / 18 | B 47, C 124; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TC2N]] | 28 vs 22 | 3 / 163 / 5 | B 52, C 119; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 44; `tables/line_effects.parquet` — line == 44
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 44; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 44]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include SW 1088

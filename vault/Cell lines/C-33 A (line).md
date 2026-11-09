---
cell_line: "C-33 A"
type: "cell line"
cell_line_id: "CVCL_1094"
depmap_id: "ACH-001333"
organ: "Cervix"
tp53_status: "altered"
drivers: ["ARID1A(Frameshift)", "BRCA2(Missense)", "HNF1A(Frameshift)", "KMT2D(Frameshift)", "KMT2D(Missense)", "PIK3CA(Missense)", "PTEN(Stopgain)", "RB1(Splice_site)", "SETD1B(Frameshift)", "SETD1B(Missense)", "SMARCA4(Missense)", "SMARCA4(Stopgain)", "TP53(Missense)", "WNK2(Frameshift)", "WNK2(Missense)", "ZFHX3(Frameshift)"]
n_dd_depleted: 16
median_response: 0.89
tags: ["cell-line", "organ/cervix"]
generated_by: "tahoemap"
---

# C-33 A

*Cervix · TP53 altered · CVCL_1094 · ACH-001333*

|  |  |
|---|---|
| Organ | Cervix |
| TP53 status | altered |
| Drivers | ARID1A(Frameshift); BRCA2(Missense); HNF1A(Frameshift); KMT2D(Frameshift); KMT2D(Missense); PIK3CA(Missense); PTEN(Stopgain); RB1(Splice_site); SETD1B(Frameshift); SETD1B(Missense); SMARCA4(Missense); SMARCA4(Stopgain); TP53(Missense); WNK2(Frameshift); WNK2(Missense); ZFHX3(Frameshift) |
| Driver changes | ARID1A p.Q758fs; BRCA2 p.A3029T; HNF1A p.P291fs; KMT2D p.A2119fs; KMT2D p.R1614W; KMT2D p.R1617W; KMT2D p.V1244fs; PIK3CA p.R88Q; PTEN p.R130*; PTEN p.R233*; SETD1B p.H8fs; SETD1B p.R980W; SETD1B p.T482M; SMARCA4 p.M527T; SMARCA4 p.Q1248R; SMARCA4 p.Q1537*; TP53 p.R273C; WNK2 p.A678T; WNK2 p.D1638fs; ZFHX3 p.R1893fs |
| Cells over all wells | 1,483,079 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.890 (1 = a typical line) |
| Drug-doses that deplete it | 16 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 7 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 13,926 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 25): the line loses cells relative to the other lines in the same wells. Drug-doses: 16 in all, 9 with an alert ⚠; shown: the 12 strongest and the 2 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -11.1 | -1.79 |
| [[GSK1059615 (drug)]] 5 µM |  | -8.3 | -1.85 |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -8.2 | -2.19 |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.3 | -1.79 |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.0 | -1.89 |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.2 | -1.43 |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | -4.8 | -1.12 |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -0.99 |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.91 |
| [[Mebendazole (drug)]] 5 µM |  | -3.8 | -0.81 |
| [[Belumosudil (drug)]] 5 µM |  | -3.7 | -0.82 |
| [[Clopidogrel (drug)]] 0.05 µM |  | -3.5 | -0.74 |
| [[Cyclosporin A (drug)]] 0.05 µM |  | -3.4 | -0.72 |
| [[Atazanavir (sulfate) (drug)]] 0.5 µM |  | -3.3 | -0.74 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Futibatinib (drug)]] 0.05 µM (2.05); [[Glycyrrhizic acid (drug)]] 0.05 µM (2.01); [[Pitavastatin (Calcium) (drug)]] 0.05 µM (1.91); [[(S)-Crizotinib (drug)]] 0.05 µM (1.72); [[Tofacitinib (citrate) (drug)]] 0.05 µM (1.67); [[Neratinib (drug)]] 0.5 µM (1.65); [[Benproperine (phosphate) (drug)]] 5 µM (1.65); [[Pimozide (drug)]] 0.5 µM (1.60, ⚠ transcription drop); [[Flumatinib (mesylate) (drug)]] 0.5 µM (1.58)
- Weakest: [[Cyclosporin A (drug)]] 0.5 µM (-0.0800); [[palbociclib (drug)]] 0.5 µM (0.130, ⚠ cell-cycle shift); [[Mifepristone (drug)]] 5 µM (0.134); [[Menadione (drug)]] 5 µM (0.257); [[Econazole (drug)]] 5 µM (0.273); [[Betamethasone dipropionate (drug)]] 0.5 µM (0.275); [[palbociclib (drug)]] 5 µM (0.276); [[Regorafenib (drug)]] 5 µM (0.283); [[Cabozantinib (S-malate) (drug)]] 0.5 µM (0.367)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 25): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[HSPH1]] (14, 8 ⚠), [[DNAJB1]] (13, 5 ⚠), [[SNAPC1]] (11, 7 ⚠), [[SYDE2]] (9), [[RELCH]] (9, 1 ⚠), [[WAC]] (9, 2 ⚠), [[NFAT5]] (9, 2 ⚠), [[PAPOLA]] (9, 5 ⚠), [[SCD]] (8), [[TMEM41B]] (8, 1 ⚠), [[ARID4B]] (8, 2 ⚠), [[GPBP1]] (8, 2 ⚠), [[KLF6]] (8, 3 ⚠), [[ACSL3]] (7), [[NIPBL]] (7), [[UBE2H]] (7), [[HSPA5]] (7, 1 ⚠)
- down: [[EPIC1]] (23, 14 ⚠), [[GBE1]] (21, 9 ⚠), [[ENSG00000226965]] (21, 14 ⚠), [[IMMP2L]] (19, 13 ⚠), [[ATP11A]] (18, 12 ⚠), [[EIF2AK2]] (16, 2 ⚠), [[ERO1A]] (16, 7 ⚠), [[TENM3]] (16, 12 ⚠), [[NEBL]] (16, 14 ⚠), [[RAD51B]] (15, 8 ⚠), [[PRKAR1B]] (15, 9 ⚠), [[NR5A2]] (15, 13 ⚠), [[TRIM14]] (13, 1 ⚠), [[PARP9]] (13, 2 ⚠), [[ZNFX1]] (13, 4 ⚠), [[IFI6]] (12, 1 ⚠), [[RIGI]] (12, 2 ⚠), [[OAS3]] (12, 2 ⚠), [[PYGL]] (12, 3 ⚠), [[PARP14]] (11), [[DTX3L]] (10), [[IFIT1]] (10)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[ERBB4]] (+8.0), [[MIR99AHG]] (+7.6), [[LINC02240]] (+7.6), [[CTNNA2]] (+7.6), [[SEMA3D]] (+7.5), [[ENSG00000260126]] (+7.5, ⚠ noise-class RNA), [[CDH18]] (+7.4), [[NR5A2]] (+7.3), [[LINC02484]] (+7.3), [[SOX2]] (+7.2), [[TOX]] (+7.1), [[LINC01203]] (+6.9), [[ENSG00000229618]] (+6.9, ⚠ noise-class RNA), [[LINC02384]] (+6.8), [[HHIP]] (+6.7), [[LINC02008]] (+6.5), [[CASC15]] (+6.4) (1,691 genes, 144 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[NR3C1]] (-3.6), [[AHR]] (-3.4), [[SOX9]] (-3.4), [[UBB]] (-3.4), [[PLOD2]] (-3.4), [[TNFRSF10D]] (-3.4), [[CDCP1]] (-3.3), [[CPNE8]] (-3.3), [[ETS1]] (-3.3), [[TRIM38]] (-3.3), [[SMARCA2]] (-3.3), [[AXL]] (-3.3), [[CDK6]] (-3.3), [[GPD2]] (-3.3), [[PHLDA1]] (-3.2) (520 genes, 12 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 25): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 3 (0.510; genes MCL1, NABP1, DUSP6, EGR1 / KCTD3, TMEM123, XPO1, TNRC6A); component 14 (0.566; genes PNPT1, HILPDA, P4HB, ASCC3 / MBOAT2, SMARCA2, CSNK1G3, MACO1); component 13 (0.592; genes UGP2, KLF9, TSC22D3, SSBP2 / LUC7L3, PER3, TCP10L, SEMA3A); component 4 (0.616; genes LIMA1, JUNB, CENPF, TOP2A / NBR2, UQCC1, APTX, LRRC41)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 20 in all, 20 with an alert ⚠; shown: the 15 strongest; 5 more groups (5 of them with an alert ⚠) not shown. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 43 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[RB1]] | RB1 loss of function (3 lines) vs not recorded (46) | 2 / 1 / 0 | C 3; 3 with an alert ⚠ | ⚠ few lines (3 vs 46); tissue-confounded; across organs |
| [[RB1]] | RB1 altered (any record) (4 lines) vs not recorded (46) | 2 / 0 / 0 | C 2; 2 with an alert ⚠ | ⚠ few lines (4 vs 46); tissue-confounded; across organs; mechanism partly not recorded |
| [[KMT2D]] | KMT2D altered (any record) (15 lines) vs not recorded (35) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[SETD1B]] | SETD1B altered (any record) (11 lines) vs not recorded (39) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, ARID1A |
| [[ARID1A]] | ARID1A altered (any record) (15 lines) vs not recorded (35) | 0 / 0 / 1 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[HNF1A]] | HNF1A loss of function (6 lines) vs not recorded (44) | 1 / 0 / 0 | C 1; 1 with an alert ⚠ | ⚠ tissue-confounded; across organs |
| [[ARID1A]] | ARID1A loss of function (12 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[BRCA2]] | BRCA2 altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with WNK2, TGFBR2, PIK3CA |
| [[KMT2D]] | KMT2D loss of function (8 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[PIK3CA]] | PIK3CA altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3 |
| [[PIK3CA]] | PIK3CA gain of function (9 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, TGFBR2, ACVR2A |
| [[PTEN]] | PTEN loss of function (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; PTEN not expressed in 4 of the 9 altered lines |
| [[SETD1B]] | SETD1B loss of function (10 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, PRDM2, ARID1A |
| [[SMARCA4]] | SMARCA4 altered (any record) (12 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,606 in all, 2,606 with an alert ⚠; shown: the 15 strongest; 2,591 more line sets (2,591 of them with an alert ⚠) not shown; 2,657 genes; 2,320 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 25; `tables/line_effects.parquet` — line == 25
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 25; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 25]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include C-33 A

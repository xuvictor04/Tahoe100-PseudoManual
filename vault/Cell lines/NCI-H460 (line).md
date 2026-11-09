---
cell_line: "NCI-H460"
type: "cell line"
cell_line_id: "CVCL_0459"
depmap_id: "ACH-000463"
organ: "Lung"
tp53_status: "wild type"
drivers: ["ARID1A(Missense)", "CDKN2A(Deletion)", "CDKN2B(Deletion)", "KRAS(Missense)", "MAP2K1(Missense)", "MYC(Gain)", "PIK3CA(Missense)", "STK11(Stopgain)", "ZFHX3(Missense)"]
n_dd_depleted: 16
median_response: 0.998
tags: ["cell-line", "organ/lung"]
generated_by: "tahoemap"
---

# NCI-H460

*Lung · TP53 wild type · CVCL_0459 · ACH-000463*

|  |  |
|---|---|
| Organ | Lung |
| TP53 status | wild type |
| Drivers | ARID1A(Missense); CDKN2A(Deletion); CDKN2B(Deletion); KRAS(Missense); MAP2K1(Missense); MYC(Gain); PIK3CA(Missense); STK11(Stopgain); ZFHX3(Missense) |
| Driver changes | ARID1A p.LI1917del; KRAS p.Q61H; MAP2K1 p.Y134C; PIK3CA p.E545K; STK11 p.Q37*; ZFHX3 p.P3675Q |
| Cells over all wells | 5,735,623 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.998 (1 = a typical line) |
| Drug-doses that deplete it | 16 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 8 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,768 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 19): the line loses cells relative to the other lines in the same wells. Drug-doses: 16 in all, 8 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.6 | -1.17 |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.2 | -0.99 |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.1 | -0.96 |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -0.85 |
| [[Ipatasertib (drug)]] 0.5 µM |  | -5.1 | -0.81 |
| [[Alpelisib (drug)]] 5 µM |  | -5.1 | -0.82 |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | -4.9 | -0.89 |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | -0.78 |
| [[vincristine (drug)]] 5 µM |  | -4.7 | -0.77 |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -0.67 |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -4.2 | -0.69 |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.6 | -0.58 |
| [[PH-797804 (drug)]] 0.5 µM |  | -3.3 | -0.52 |
| [[Futibatinib (drug)]] 5 µM |  | -3.2 | -0.53 |
| [[Gemcitabine (drug)]] 5 µM |  | -3.2 | -0.37 |
| [[OTS514 (drug)]] 5 µM |  | -3.0 | -0.50 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Ouabain (Octahydrate) (drug)]] 0.05 µM (2.38, ⚠ cell-cycle shift); [[Amsacrine (drug)]] 0.5 µM (2.30); [[Gefitinib (drug)]] 5 µM (2.16); [[Digitoxin (drug)]] 0.05 µM (2.09, ⚠ cell-cycle shift); [[Chlorhexidine (diacetate) (drug)]] 5 µM (1.93); [[Homoharringtonine (drug)]] 0.05 µM (1.86); [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM (1.74); [[Pentamidine (isethionate) (drug)]] 5 µM (1.69); [[Peretinoin (drug)]] 0.05 µM (1.67); [[BI-3406 (drug)]] 5 µM (1.50)
- Weakest: [[Roxadustat (drug)]] 0.05 µM (-0.149); [[Neratinib (drug)]] 0.05 µM (-0.146); [[Monocrotaline (drug)]] 0.05 µM (0.0680); [[Tofacitinib (citrate) (drug)]] 0.5 µM (0.127); [[Tofacitinib (drug)]] 0.5 µM (0.131); [[Tofacitinib (citrate) (drug)]] 5 µM (0.138); [[Tofacitinib (drug)]] 5 µM (0.143); [[Naproxen (drug)]] 5 µM (0.189)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 19): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[CERS6]] (31, 19 ⚠), [[FKBP5]] (30, 10 ⚠), [[SAMD8]] (26, 1 ⚠), [[PISD]] (26, 1 ⚠), [[ZFAND5]] (24, 4 ⚠), [[ACSL1]] (24, 4 ⚠), [[ATP1A1]] (24, 8 ⚠), [[TMTC1]] (23, 1 ⚠), [[ATP2B4]] (23, 2 ⚠), [[ATP6V0A1]] (23, 5 ⚠), [[CPEB4]] (22, 2 ⚠), [[MAP1B]] (22, 7 ⚠), [[BACH2]] (21, 2 ⚠), [[NPHP4]] (19), [[WDFY2]] (19)
- down: [[BMPER]] (44, 17 ⚠), [[NPAS2]] (43, 11 ⚠), [[MBP]] (43, 15 ⚠), [[EFNA5]] (37, 17 ⚠), [[PITPNC1]] (36, 13 ⚠), [[MLKL]] (34, 9 ⚠), [[ITGB5]] (34, 10 ⚠), [[ESM1]] (33, 5 ⚠), [[NT5E]] (32, 3 ⚠), [[NTSR1]] (32, 7 ⚠), [[THSD4]] (31, 4 ⚠), [[DUSP4]] (31, 5 ⚠), [[KAT6B]] (31, 14 ⚠), [[ADAM19]] (29, 5 ⚠), [[CDCP1]] (27, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[LINC01035]] (+7.5), [[LINC03000]] (+7.4), [[LINC00824]] (+7.4), [[TBXT]] (+7.1), [[ENSG00000238054]] (+7.0, ⚠ noise-class RNA), [[ENSG00000260364]] (+7.0, ⚠ noise-class RNA), [[CHL1]] (+6.8), [[EPB41L3]] (+6.8), [[COL4A6]] (+6.8), [[ADGRD1]] (+6.8), [[GDA]] (+6.7), [[LINC02742]] (+6.6), [[CDH11]] (+6.6), [[DPP10]] (+6.6), [[GTF2I-AS1]] (+6.4), [[GREM2]] (+6.2), [[SCARA5]] (+6.2) (1,131 genes, 92 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[SCRN1]] (-3.3), [[TRPS1]] (-3.3), [[ZNF91]] (-3.2), [[CAT]] (-3.2), [[ZNF736]] (-3.1), [[ZNF700]] (-3.0), [[FRMD5]] (-3.0), [[IFITM1]] (-3.0), [[ZNF331]] (-2.9), [[THBS1]] (-2.9), [[ZNF44]] (-2.8), [[LSR]] (-2.8), [[MICAL2]] (-2.8), [[TGM2]] (-2.7), [[GRAMD2B]] (-2.7) (154 genes, 4 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 19): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Strong here (> 1.5): component 36 (1.78; genes MIR34AHG, POLH, STAT3, CCNG1 / PLCB1, LINGO2, SATB2, WDR76); component 19 (1.69; genes DIAPH3, ANLN, TES, HIF1A-AS3 / ETV1, NR4A2, FOSB, FOS); component 7 (1.60; genes ARCN1, GOLGB1, LYSMD3, HDLBP / UCK2, MEMO1, SRPK2, PLEKHA5); component 64 (1.56; genes FBXO17, PSD3, KCNQ1OT1, P3H2 / PMP22, ATP2B1, MIDN, HAS2)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 10 in all, 10 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 52 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[CDKN2B]] | CDKN2B loss of function (13 lines) vs not recorded (37) | 4 / 2 / 0 | B 3, C 3; 6 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[ARID1A]] | ARID1A altered (any record) (15 lines) vs not recorded (35) | 0 / 0 / 1 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[MYC]] | MYC gain of function (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[PIK3CA]] | PIK3CA altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3 |
| [[PIK3CA]] | PIK3CA gain of function (9 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, TGFBR2, ACVR2A |
| [[STK11]] | STK11 loss of function (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[ZFHX3]] | ZFHX3 altered (any record) (13 lines) vs not recorded (37) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B, PIK3CA |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,832 in all, 1,832 with an alert ⚠; shown: the 15 strongest; 1,817 more line sets (1,817 of them with an alert ⚠) not shown; 1,858 genes; 1,572 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 19; `tables/line_effects.parquet` — line == 19
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 19; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 19]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include NCI-H460

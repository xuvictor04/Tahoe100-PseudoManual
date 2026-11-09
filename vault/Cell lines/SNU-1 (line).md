---
cell_line: "SNU-1"
type: "cell line"
cell_line_id: "CVCL_0099"
depmap_id: "ACH-000932"
organ: "Esophagus/Stomach"
tp53_status: "wild type"
drivers: ["ARID1A(Frameshift)", "ARID1A(Missense)", "ATM(Frameshift)", "BRCA2(Frameshift)", "BRCA2(Missense)", "JAK1(Frameshift)", "KMT2D(Frameshift)", "KMT2D(Missense)", "KRAS(Missense)", "PRDM2(Missense)", "SETD1B(Frameshift)", "SMAD3(Frameshift)", "SMAD4(Missense)", "TGFBR2(Frameshift)", "WNK2(Missense)"]
n_dd_depleted: 27
median_response: 0.982
tags: ["cell-line", "organ/esophagus_stomach"]
generated_by: "tahoemap"
---

# SNU-1

*Esophagus/Stomach · TP53 wild type · CVCL_0099 · ACH-000932*

|  |  |
|---|---|
| Organ | Esophagus/Stomach |
| TP53 status | wild type |
| Drivers | ARID1A(Frameshift); ARID1A(Missense); ATM(Frameshift); BRCA2(Frameshift); BRCA2(Missense); JAK1(Frameshift); KMT2D(Frameshift); KMT2D(Missense); KRAS(Missense); PRDM2(Missense); SETD1B(Frameshift); SMAD3(Frameshift); SMAD4(Missense); TGFBR2(Frameshift); WNK2(Missense) |
| Driver changes | ARID1A p.D1633fs; ARID1A p.P121S; ARID1A p.Q372fs; ATM p.L1154fs; BRCA2 p.R1190W; BRCA2 p.S309fs; JAK1 p.K860fs; KMT2D p.A2119fs; KMT2D p.P2363del; KMT2D p.R5030C; KRAS p.G12D; PRDM2 p.S67F; SETD1B p.H8fs; SMAD3 p.V380fs; SMAD4 p.R265H; TGFBR2 p.S409fs; WNK2 p.G1850C; WNK2 p.W547C |
| Cells over all wells | 1,221,615 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.982 (1 = a typical line) |
| Drug-doses that deplete it | 27 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 9 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 13,198 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 3): the line loses cells relative to the other lines in the same wells. Drug-doses: 27 in all, 18 with an alert ⚠; shown: the 12 strongest and the 7 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -12.4 | -2.21 |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -11.4 | -2.07 |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -10.8 | -2.55 |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -10.1 | -2.78 |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.2 | -2.08 |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.7 | -1.72 |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.1 | -1.77 |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.9 | -1.49 |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.7 | -2.22 |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.4 | -1.92 |
| [[AT7519 (drug)]] 5 µM |  | -6.1 | -1.50 |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.9 | -1.17 |
| [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -1.32 |
| [[Infigratinib (drug)]] 5 µM |  | -4.5 | -1.07 |
| [[PH-797804 (drug)]] 5 µM |  | -3.9 | -0.97 |
| [[Brivudine (drug)]] 5 µM |  | -3.8 | -0.88 |
| [[Belumosudil (drug)]] 5 µM |  | -3.6 | -0.80 |
| [[HI-TOPK-032 (drug)]] 5 µM |  | -3.5 | -0.87 |
| [[Radotinib (drug)]] 5 µM |  | -3.5 | -0.55 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM (3.10); [[Amsacrine (drug)]] 0.5 µM (2.68); [[Allantoin (drug)]] 0.05 µM (2.33, ⚠ transcription drop); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM (2.02, ⚠ cell-cycle shift); [[Ivabradine (hydrochloride) (drug)]] 5 µM (1.99, ⚠ unreliable plate only); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM (1.97); [[Dihydroartemisinin (drug)]] 0.5 µM (1.94); [[Simotinib (drug)]] 0.05 µM (1.93); [[Futibatinib (drug)]] 0.05 µM (1.84); [[Cytarabine (drug)]] 0.05 µM (1.80); [[Anethole trithione (drug)]] 0.5 µM (1.79)
- Weakest: [[Crizotinib (hydrochloride) (drug)]] 0.5 µM (0.0306); [[Cyclosporin A (drug)]] 0.5 µM (0.0394); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM (0.0594); [[Vandetanib (drug)]] 5 µM (0.112); [[Elagolix sodium (drug)]] 0.5 µM (0.153); [[Menadione (drug)]] 5 µM (0.195); [[Fluvoxamine (maleate) (drug)]] 0.5 µM (0.200); [[DTP3 (drug)]] 5 µM (0.240)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 3): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[MDM2]] (14, 2 ⚠), [[ASCC3]] (14, 9 ⚠), [[HSPA9]] (13, 4 ⚠), [[MIR4435-2HG]] (13, 6 ⚠), [[BRD2]] (13, 7 ⚠), [[LINC01004]] (12, 2 ⚠), [[TOP1]] (12, 3 ⚠), [[MCL1]] (12, 5 ⚠), [[RSRC2]] (11, 2 ⚠), [[KDM6B]] (11, 2 ⚠), [[SON]] (11, 2 ⚠), [[GPATCH2L]] (11, 4 ⚠), [[CTNNAL1]] (11, 7 ⚠), [[ZC3H11A]] (10, 1 ⚠), [[AFF4]] (10, 1 ⚠), [[RAB7A]] (10, 1 ⚠), [[HIF1A]] (10, 1 ⚠), [[SUPT6H]] (10, 1 ⚠), [[NOCT]] (10, 1 ⚠)
- down: [[LOXL3]] (27, 12 ⚠), [[SH3TC2-DT]] (26, 9 ⚠), [[CAMK1D]] (26, 10 ⚠), [[ITGA10]] (25, 8 ⚠), [[FHIT]] (24, 16 ⚠), [[DUSP6]] (22, 6 ⚠), [[GCNT1]] (22, 10 ⚠), [[ENSG00000275649]] (22, 16 ⚠), [[SERPINB6]] (21, 7 ⚠), [[SMYD3]] (21, 7 ⚠), [[RIPOR2]] (21, 14 ⚠), [[TRERF1]] (20, 5 ⚠), [[MYO5C]] (20, 8 ⚠), [[ZMYND8]] (18, 5 ⚠), [[SPRY4]] (17, 3 ⚠), [[PARP9]] (15, 3 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[BMP10]] (+8.4), [[LINC02099]] (+8.1), [[ENSG00000275649]] (+8.0, ⚠ noise-class RNA), [[FENDRR]] (+7.7), [[CCK]] (+7.2), [[PIWIL1]] (+7.1), [[ENSG00000288098]] (+6.9, ⚠ noise-class RNA), [[FBLN2]] (+6.9), [[CPED1]] (+6.7), [[SOX6]] (+6.7), [[TNFRSF11B]] (+6.7), [[B3GALT1]] (+6.6), [[MIR99AHG]] (+6.6), [[LOXL3]] (+6.5), [[TTTY14]] (+6.3), [[ARHGAP25]] (+6.2), [[PDE4B]] (+6.2) (1,013 genes, 100 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[VIM]] (-3.6), [[SDC4]] (-3.6), [[JUNB]] (-3.6), [[PLOD2]] (-3.5), [[TRPS1]] (-3.4), [[MARCKS]] (-3.4), [[IGF2BP3]] (-3.4), [[CAVIN1]] (-3.4), [[AXL]] (-3.4), [[P4HA2]] (-3.4), [[ZNF516]] (-3.4), [[PLEKHA2]] (-3.4), [[CDK6]] (-3.4), [[FSCN1]] (-3.4), [[PRKCZ]] (-3.4) (594 genes, 14 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 3): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 3 (0.538; genes MCL1, NABP1, DUSP6, EGR1 / KCTD3, TMEM123, XPO1, TNRC6A); component 13 (0.547; genes UGP2, KLF9, TSC22D3, SSBP2 / LUC7L3, PER3, TCP10L, SEMA3A); component 59 (0.607; genes ZFP36L1, CHST11, ADAM19, PLK2 / KCNMA1, CSGALNACT1, STC1, BMERB1); component 54 (0.611; genes FDFT1, LPIN1, ACACA, MSMO1 / GLRX, DPY19L1, WWC1, NR4A3)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 18 in all, 18 with an alert ⚠; shown: the 15 strongest; 3 more groups (3 of them with an alert ⚠) not shown. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 45 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[BRCA2]] | BRCA2 loss of function (7 lines) vs not recorded (41) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, WNK2, ACVR2A |
| [[KMT2D]] | KMT2D altered (any record) (15 lines) vs not recorded (35) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[SETD1B]] | SETD1B altered (any record) (11 lines) vs not recorded (39) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, ARID1A |
| [[ARID1A]] | ARID1A altered (any record) (15 lines) vs not recorded (35) | 0 / 0 / 1 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[ARID1A]] | ARID1A loss of function (12 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[ATM]] | ATM altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[ATM]] | ATM loss of function (6 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[BRCA2]] | BRCA2 altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with WNK2, TGFBR2, PIK3CA |
| [[KMT2D]] | KMT2D loss of function (8 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[PRDM2]] | PRDM2 altered (any record) (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with TGFBR2, ACVR2A, SETD1B |
| [[PRDM2]] | PRDM2 loss of function (4 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ few lines (4 vs 44); within organs, on part of the lines; co-occurs with TGFBR2, WNK2 |
| [[SETD1B]] | SETD1B loss of function (10 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with ZFHX3, PRDM2, ARID1A |
| [[SMAD3]] | SMAD3 altered (any record) (3 lines) vs not recorded (47) | 0 / 0 / 0 | — | ⚠ few lines (3 vs 47); within organs, on part of the lines; mechanism partly not recorded; SMAD3 not expressed in 1 of the 3 altered lines |
| [[SMAD4]] | SMAD4 loss of function (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; SMAD4 not expressed in 2 of the 6 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 3,314 in all, 3,314 with an alert ⚠; shown: the 15 strongest; 3,299 more line sets (3,299 of them with an alert ⚠) not shown; 3,361 genes; 2,923 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 3; `tables/line_effects.parquet` — line == 3
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 3; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 3]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include SNU-1

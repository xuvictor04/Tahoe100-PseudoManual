---
cell_line: "RKO"
type: "cell line"
cell_line_id: "CVCL_0504"
depmap_id: "ACH-000943"
organ: "Bowel"
tp53_status: "wild type"
drivers: ["ACVR2A(Frameshift)", "ARID1A(Frameshift)", "B2M(Stopgain)", "BRAF(Missense)", "BRCA2(Frameshift)", "EP300(Frameshift)", "HNF1A(Frameshift)", "KMT2D(Frameshift)", "KMT2D(Missense)", "KMT2D(Stopgain)", "MSH6(Frameshift)", "NF1(Frameshift)", "NF1(Missense)", "NF2(Frameshift)", "PIK3CA(Missense)", "POLE(Missense)", "PRDM2(Missense)", "RNF43(Frameshift)", "RNF43(Missense)", "SETD1B(Frameshift)", "SETD1B(Missense)", "SMAD3(Missense)", "TGFBR2(Frameshift)", "TGFBR2(Missense)", "ZFHX3(Frameshift)", "ZFHX3(Missense)"]
n_dd_depleted: 36
median_response: 0.981
tags: ["cell-line", "organ/bowel"]
generated_by: "tahoemap"
---

# RKO

*Bowel · TP53 wild type · CVCL_0504 · ACH-000943*

|  |  |
|---|---|
| Organ | Bowel |
| TP53 status | wild type |
| Drivers | ACVR2A(Frameshift); ARID1A(Frameshift); B2M(Stopgain); BRAF(Missense); BRCA2(Frameshift); EP300(Frameshift); HNF1A(Frameshift); KMT2D(Frameshift); KMT2D(Missense); KMT2D(Stopgain); MSH6(Frameshift); NF1(Frameshift); NF1(Missense); NF2(Frameshift); PIK3CA(Missense); POLE(Missense); PRDM2(Missense); RNF43(Frameshift); RNF43(Missense); SETD1B(Frameshift); SETD1B(Missense); SMAD3(Missense); TGFBR2(Frameshift); TGFBR2(Missense); ZFHX3(Frameshift); ZFHX3(Missense) |
| Driver changes | ACVR2A p.K437fs; ARID1A p.D1633fs; ARID1A p.P1115fs; B2M p.R117*; BRAF p.V600E; BRCA2 p.N1784fs; EP300 p.K292fs; EP300 p.M1470fs; HNF1A p.P379fs; KMT2D p.G1960fs; KMT2D p.G3465*; KMT2D p.L1600P; KMT2D p.L5056P; KMT2D p.P2550fs; MSH6 p.Y1066fs; NF1 p.N2320fs; NF1 p.V2184A; NF1 p.Y628fs; NF2 p.P275fs; PIK3CA p.H1047R; POLE p.K995E; PRDM2 p.S876G; RNF43 p.G659fs; RNF43 p.H549N; SETD1B p.H8fs; SETD1B p.T1700A; SMAD3 p.A13T; TGFBR2 p.K128fs; TGFBR2 p.L452P; ZFHX3 p.F1596fs; ZFHX3 p.S112N |
| Cells over all wells | 2,182,105 |
| Wells with usable expression | 1,327 (99.8%) |
| Median response strength (β) | 0.981 (1 = a typical line) |
| Drug-doses that deplete it | 36 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 19 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 13,573 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 21): the line loses cells relative to the other lines in the same wells. Drug-doses: 37 in all, 18 with an alert ⚠; shown: the 12 strongest and the 12 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -23.6 | -2.88 |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -14.2 | -3.25 |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -13.9 | -1.47 |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -12.6 | -2.60 |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -11.6 | -1.72 |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -11.6 | -1.64 |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -11.6 | -1.74 |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -10.1 | -1.39 |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.8 | -2.52 |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -9.6 | -3.97 |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -9.6 | -1.52 |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.5 | -3.51 |
| [[Docetaxel (drug)]] 5 µM |  | -6.4 | -0.62 |
| [[venetoclax (drug)]] 5 µM |  | -6.3 | -0.97 |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | -6.3 | -0.95 |
| [[Belumosudil (drug)]] 5 µM |  | -6.1 | -0.88 |
| [[vincristine (drug)]] 5 µM |  | -5.3 | -0.82 |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | -5.0 | -0.67 |
| [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -0.65 |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.4 | -0.43 |
| [[Paclitaxel (drug)]] 5 µM |  | -4.4 | -0.59 |
| [[Peretinoin (drug)]] 0.05 µM |  | -4.3 | -0.59 |
| [[Mebendazole (drug)]] 5 µM |  | -4.1 | -0.55 |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -0.42 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 487, 83 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Futibatinib (drug)]] 0.05 µM (2.08); [[Amsacrine (drug)]] 0.5 µM (2.02); [[Docetaxel (Trihydrate) (drug)]] 5 µM (1.95); [[Glycyrrhizic acid (drug)]] 0.05 µM (1.78); [[Glycyrrhizic acid (drug)]] 5 µM (1.76); [[Idarubicin (hydrochloride) (drug)]] 0.05 µM (1.71); [[Pimozide (drug)]] 5 µM (1.67); [[Malotilate (drug)]] 0.05 µM (1.65)
- Weakest: [[Pentamidine (isethionate) (drug)]] 5 µM (0.0268); [[BI-3406 (drug)]] 5 µM (0.137); [[Econazole (drug)]] 5 µM (0.145); [[AZD-8055 (drug)]] 0.05 µM (0.164); [[Phenylephrine (hydrochloride) (drug)]] 5 µM (0.166); [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM (0.181, ⚠ unreliable plate only); [[Neratinib (drug)]] 0.05 µM (0.224); [[Finasteride (drug)]] 5 µM (0.260); [[Rosiglitazone (drug)]] 5 µM (0.269)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 21): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[MDM2]] (20, 2 ⚠), [[RRM2B]] (14, 2 ⚠), [[HSPA4L]] (13), [[TAF3]] (12, 1 ⚠), [[ZBTB11]] (12, 4 ⚠), [[DNAJC1]] (12, 5 ⚠), [[SON]] (11, 2 ⚠), [[CERS6]] (11, 3 ⚠), [[ZMAT3]] (11, 3 ⚠), [[ARID4B]] (10, 1 ⚠), [[RHOB]] (10, 1 ⚠), [[ZBTB43]] (10, 1 ⚠), [[GPBP1]] (10, 2 ⚠), [[BCLAF1]] (10, 3 ⚠), [[SORBS1]] (9), [[DAAM1]] (9), [[ZC2HC1A]] (9), [[RBM5]] (9, 1 ⚠)
- down: [[MAST4]] (37, 14 ⚠), [[ARHGAP22]] (35, 13 ⚠), [[NAV3]] (33, 8 ⚠), [[FRMD4A]] (33, 14 ⚠), [[DDX60]] (32, 10 ⚠), [[C2CD2]] (32, 14 ⚠), [[MX2]] (31, 8 ⚠), [[MX1]] (28, 7 ⚠), [[NEMP2]] (28, 10 ⚠), [[MAPKAP1]] (28, 11 ⚠), [[DLC1]] (28, 16 ⚠), [[GFPT2]] (27, 5 ⚠), [[TMEM156]] (26, 5 ⚠), [[FLNB]] (25, 4 ⚠), [[ITGB1-DT]] (25, 5 ⚠), [[RIGI]] (24, 4 ⚠), [[ASAP2]] (23, 3 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[MSRB3-AS1]] (+8.0), [[XIST]] (+7.5), [[LINC01592]] (+7.2), [[ENSG00000233491]] (+6.9, ⚠ noise-class RNA), [[ENSG00000242880]] (+6.6, ⚠ noise-class RNA), [[ENSG00000238178]] (+6.6, ⚠ noise-class RNA), [[TTN]] (+6.5), [[RDUR]] (+6.3), [[HGF]] (+6.3), [[ENSG00000235495]] (+6.1, ⚠ noise-class RNA), [[DGKI]] (+6.1), [[ADTRP]] (+6.1), [[CASC19]] (+6.0), [[RGS4]] (+6.0), [[ENSG00000287149]] (+6.0, ⚠ noise-class RNA), [[SHANK1]] (+5.9), [[LINC01812]] (+5.9), [[LCP1]] (+5.8), [[LINC01358]] (+5.6), [[CCND2]] (+5.6) (1,282 genes, 79 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[NR3C1]] (-3.9), [[QKI]] (-3.8), [[VIM]] (-3.7), [[PLOD2]] (-3.6), [[RBMS1]] (-3.6), [[FERMT2]] (-3.6), [[KLF7]] (-3.6), [[UBE2E2]] (-3.6), [[AHR]] (-3.6), [[OSMR-DT]] (-3.5), [[BNIP3]] (-3.5), [[CPNE8]] (-3.5), [[OSMR]] (-3.5), [[ZBTB10]] (-3.5), [[SMARCA1]] (-3.5) (388 genes, 11 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 21): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.759 to 1.30).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 32 in all, 32 with an alert ⚠; shown: the 15 strongest; 17 more groups (17 of them with an alert ⚠) not shown. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 31 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[POLE]] | POLE altered (any record) (8 lines) vs not recorded (42) | 1 / 0 / 0 | A 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[BRCA2]] | BRCA2 loss of function (7 lines) vs not recorded (41) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, WNK2, ACVR2A |
| [[KMT2D]] | KMT2D altered (any record) (15 lines) vs not recorded (35) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[SETD1B]] | SETD1B altered (any record) (11 lines) vs not recorded (39) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, ARID1A |
| [[ARID1A]] | ARID1A altered (any record) (15 lines) vs not recorded (35) | 0 / 0 / 1 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[HNF1A]] | HNF1A loss of function (6 lines) vs not recorded (44) | 1 / 0 / 0 | C 1; 1 with an alert ⚠ | ⚠ tissue-confounded; across organs |
| [[ACVR2A]] | ACVR2A altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with TGFBR2, SETD1B, PRDM2 |
| [[ACVR2A]] | ACVR2A loss of function (7 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B, PRDM2, EP300 |
| [[ARID1A]] | ARID1A loss of function (12 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[B2M]] | B2M altered (any record) (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[B2M]] | B2M loss of function (5 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, NF1, EP300 |
| [[BRAF]] | BRAF altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[BRAF]] | BRAF gain of function (7 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[BRCA2]] | BRCA2 altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with WNK2, TGFBR2, PIK3CA |
| [[EP300]] | EP300 altered (any record) (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, SETD1B |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,989 in all, 2,989 with an alert ⚠; shown: the 15 strongest; 2,974 more line sets (2,974 of them with an alert ⚠) not shown; 3,037 genes; 2,621 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 21; `tables/line_effects.parquet` — line == 21
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 21; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 21]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include RKO

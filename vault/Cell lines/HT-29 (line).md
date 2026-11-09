---
cell_line: "HT-29"
type: "cell line"
cell_line_id: "CVCL_0320"
depmap_id: "ACH-000552"
organ: "Bowel"
tp53_status: "altered"
drivers: ["APC(Frameshift)", "APC(Stopgain)", "BRAF(Missense)", "MYC(Gain)", "PIK3CA(Missense)", "SMAD4(Stopgain)", "TP53(Missense)", "ZFHX3(Missense)"]
n_dd_depleted: 10
median_response: 0.95
tags: ["cell-line", "organ/bowel"]
generated_by: "tahoemap"
---

# HT-29

*Bowel · TP53 altered · CVCL_0320 · ACH-000552*

|  |  |
|---|---|
| Organ | Bowel |
| TP53 status | altered |
| Drivers | APC(Frameshift); APC(Stopgain); BRAF(Missense); MYC(Gain); PIK3CA(Missense); SMAD4(Stopgain); TP53(Missense); ZFHX3(Missense) |
| Driver changes | APC p.E853*; APC p.T1556fs; BRAF p.V600E; PIK3CA p.P449T; SMAD4 p.Q311*; TP53 p.R273H; ZFHX3 p.I1217M |
| Cells over all wells | 2,170,790 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.950 (1 = a typical line) |
| Drug-doses that deplete it | 10 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 7 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,126 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 10): the line loses cells relative to the other lines in the same wells. Drug-doses: 11 in all, 4 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -13.5 | -1.52 |
| [[GSK1059615 (drug)]] 5 µM |  | -11.9 | -1.29 |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -8.9 | -1.80 |
| [[Bimiralisib (drug)]] 5 µM |  | -5.5 | -0.56 |
| [[PH-797804 (drug)]] 5 µM |  | -4.2 | -0.46 |
| [[Brivudine (drug)]] 5 µM |  | -4.1 | -0.42 |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -0.27 |
| [[Afatinib (drug)]] 5 µM |  | -3.5 | -0.25 |
| [[Afatinib (drug)]] 0.5 µM |  | -3.4 | -0.24 |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -0.33 |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | -3.1 | -0.24 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Raltitrexed (drug)]] 5 µM (1.95, ⚠ cell-cycle shift); [[Docetaxel (drug)]] 0.5 µM (1.90, ⚠ cell-cycle shift); [[Berbamine (drug)]] 0.5 µM (1.88); [[Trifluridine (drug)]] 5 µM (1.78, ⚠ cell-cycle shift); [[Auranofin (drug)]] 0.5 µM (1.74); [[Vinblastine (sulfate) (drug)]] 0.05 µM (1.74); [[Bexarotene (drug)]] 0.05 µM (1.66); [[Pentoxifylline (drug)]] 0.5 µM (1.65); [[Peretinoin (drug)]] 5 µM (1.62); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM (1.59); [[Raltitrexed (drug)]] 0.5 µM (1.58)
- Weakest: [[Naproxen (drug)]] 0.05 µM (0.0443); [[Flumatinib (mesylate) (drug)]] 0.5 µM (0.101); [[Vortioxetine (drug)]] 5 µM (0.162, ⚠ toxic); [[Lidocaine (hydrochloride) (drug)]] 5 µM (0.166); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM (0.180); [[Pentamidine (isethionate) (drug)]] 5 µM (0.190); [[Ciclopirox (drug)]] 5 µM (0.229); [[Ferulic acid (drug)]] 0.5 µM (0.234); [[Triamcinolone (drug)]] 0.05 µM (0.276)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 10): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[FRMD5]] (23, 6 ⚠), [[HSPA4]] (16, 8 ⚠), [[ABL2]] (15, 4 ⚠), [[GLS]] (15, 5 ⚠), [[DCBLD2]] (15, 7 ⚠), [[DAAM1]] (14, 2 ⚠), [[HSPA4L]] (13, 1 ⚠), [[LYST]] (13, 2 ⚠), [[TRIO]] (13, 4 ⚠), [[PVR]] (13, 4 ⚠), [[ETS1]] (13, 4 ⚠), [[HSPH1]] (13, 6 ⚠), [[OLA1]] (13, 6 ⚠), [[ATP6V1A]] (12), [[SORBS1]] (11), [[PCLO]] (11), [[SLMAP]] (11, 1 ⚠), [[ACSL3]] (10)
- down: [[HNF1A-AS1]] (28, 12 ⚠), [[HSD17B2]] (26, 13 ⚠), [[NIHCOLE]] (25, 17 ⚠), [[FAM114A1]] (23, 14 ⚠), [[TRERF1]] (21, 8 ⚠), [[TRIB3]] (21, 10 ⚠), [[NOL3]] (20, 4 ⚠), [[SNTB1]] (20, 8 ⚠), [[ZNF652]] (20, 8 ⚠), [[NAALADL2]] (20, 10 ⚠), [[GABRA2]] (20, 12 ⚠), [[FHL2]] (19, 7 ⚠), [[XPOT]] (17, 3 ⚠), [[SLC7A1]] (16, 3 ⚠), [[C1QTNF3-AMACR]] (15, 3 ⚠), [[ABCC3]] (14, 3 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[KRT20]] (+7.9), [[ENSG00000283380]] (+7.2, ⚠ noise-class RNA), [[LYZ]] (+7.2), [[TM4SF4]] (+7.0), [[XIST]] (+6.6), [[GCNT3]] (+6.3), [[CYP3A5]] (+6.2), [[BCAS1]] (+6.0), [[CAPN8]] (+5.9), [[POF1B]] (+5.9), [[SLC44A4]] (+5.8), [[MUC5AC]] (+5.8), [[LGALS4]] (+5.7), [[SULT2B1]] (+5.6), [[UGT1A6]] (+5.6), [[HHLA2]] (+5.5) (1,381 genes, 73 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[VIM]] (-3.5), [[NR3C1]] (-3.5), [[QKI]] (-3.5), [[KLF7]] (-3.4), [[CCDC88A]] (-3.3), [[HLTF]] (-3.3), [[BNIP3]] (-3.3), [[OSMR-DT]] (-3.3), [[FERMT2]] (-3.3), [[OSMR]] (-3.3), [[ARHGEF10]] (-3.2), [[MAP1B]] (-3.2), [[AKT3]] (-3.2), [[HDGFL3]] (-3.2), [[ELOVL5]] (-3.2) (345 genes, 6 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 10): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 58 (0.689; genes SDK1, WFDC3, WFDC10B, RUNX2 / TEAD1, ATP2C2, ARHGAP18, NFIB)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 9 in all, 9 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 53 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[APC]] | APC altered (any record) (10 lines) vs not recorded (40) | 7 / 0 / 0 | C 7; 7 with an alert ⚠ | ⚠ tissue-confounded; across organs; mechanism partly not recorded |
| [[APC]] | APC loss of function (7 lines) vs not recorded (40) | 5 / 0 / 0 | C 5; 5 with an alert ⚠ | ⚠ tissue-confounded; across organs |
| [[BRAF]] | BRAF altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[BRAF]] | BRAF gain of function (7 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[MYC]] | MYC gain of function (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[PIK3CA]] | PIK3CA altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3 |
| [[SMAD4]] | SMAD4 loss of function (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; SMAD4 not expressed in 2 of the 6 altered lines |
| [[ZFHX3]] | ZFHX3 altered (any record) (13 lines) vs not recorded (37) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B, PIK3CA |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,436 in all, 2,436 with an alert ⚠; shown: the 15 strongest; 2,421 more line sets (2,421 of them with an alert ⚠) not shown; 2,472 genes; 2,106 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[GBP4]] | 20 vs 30 | 13 / 118 / 0 | B 104, C 27; 131 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[OAS2]] | 14 vs 36 | 36 / 91 / 0 | B 111, C 16; 127 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MX1]] | 19 vs 31 | 17 / 103 / 0 | B 108, C 12; 120 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TRIM22]] | 18 vs 32 | 16 / 104 / 0 | B 94, C 26; 120 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[IFI6]] | 13 vs 37 | 39 / 72 / 0 | B 100, C 11; 111 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SPOCK1]] | 29 vs 21 | 1 / 62 / 45 | B 58, C 50; 108 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SAMD9L]] | 18 vs 32 | 11 / 90 / 1 | B 85, C 17; 102 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[APCDD1L]] | 34 vs 16 | 2 / 99 / 0 | B 16, C 85; 101 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC4]] | 41 vs 9 | 1 / 93 / 4 | B 25, C 73; 98 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ITGA11]] | 34 vs 16 | 2 / 95 / 0 | B 19, C 78; 97 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01411]] | 38 vs 12 | 0 / 97 / 0 | B 13, C 84; 97 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[EPSTI1]] | 25 vs 25 | 6 / 90 / 0 | B 79, C 17; 96 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PDGFRB]] | 36 vs 14 | 1 / 94 / 1 | B 21, C 75; 96 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC02474]] | 40 vs 10 | 1 / 94 / 0 | B 22, C 73; 95 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[KCNMA1]] | 26 vs 24 | 3 / 43 / 47 | B 70, C 23; 93 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 10; `tables/line_effects.parquet` — line == 10
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 10; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 10]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include HT-29

---
cell_line: "LoVo"
type: "cell line"
cell_line_id: "CVCL_0399"
depmap_id: "ACH-000950"
organ: "Bowel"
tp53_status: "wild type"
drivers: ["ACVR2A(Frameshift)", "APC(Frameshift)", "APC(Missense)", "APC(Stopgain)", "ARID1A(Frameshift)", "B2M(Frameshift)", "CHEK2(Frameshift)", "FBXW7(Missense)", "FGFR3(Missense)", "HNF1A(Missense)", "KMT2D(Frameshift)", "KRAS(Missense)", "NF1(Missense)", "PIK3CB(Missense)", "PRDM2(Frameshift)", "PRDM2(Missense)", "RAF1(Missense)", "SETD1B(Frameshift)", "SETD1B(Missense)", "SMAD2(Missense)", "TGFBR2(Frameshift)", "WNK2(Missense)"]
n_dd_depleted: 19
median_response: 0.918
tags: ["cell-line", "organ/bowel"]
generated_by: "tahoemap"
---

# LoVo

*Bowel · TP53 wild type · CVCL_0399 · ACH-000950*

|  |  |
|---|---|
| Organ | Bowel |
| TP53 status | wild type |
| Drivers | ACVR2A(Frameshift); APC(Frameshift); APC(Missense); APC(Stopgain); ARID1A(Frameshift); B2M(Frameshift); CHEK2(Frameshift); FBXW7(Missense); FGFR3(Missense); HNF1A(Missense); KMT2D(Frameshift); KRAS(Missense); NF1(Missense); PIK3CB(Missense); PRDM2(Frameshift); PRDM2(Missense); RAF1(Missense); SETD1B(Frameshift); SETD1B(Missense); SMAD2(Missense); TGFBR2(Frameshift); WNK2(Missense) |
| Driver changes | ACVR2A p.K437fs; APC p.M1431fs; APC p.R1114*; APC p.R2816Q; ARID1A p.F1924fs; B2M p.L15fs; CHEK2 p.T389fs; FBXW7 p.R425C; FGFR3 p.I533V; HNF1A p.V446M; KMT2D p.H77fs; KRAS p.G13D; NF1 p.R1674Q; PIK3CB p.E1051K; PRDM2 p.S1618G; PRDM2 p.V1490fs; RAF1 p.V98A; SETD1B p.H8fs; SETD1B p.V1447I; SMAD2 p.A292V; TGFBR2 p.K128fs; WNK2 p.R2073C; WNK2 p.V1544A |
| Cells over all wells | 3,012,852 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.918 (1 = a typical line) |
| Drug-doses that deplete it | 19 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 14 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,613 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 17): the line loses cells relative to the other lines in the same wells. Drug-doses: 19 in all, 5 with an alert ⚠; shown: the 12 strongest and the 4 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | -8.5 | -1.04 |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.4 | -1.00 |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.7 | -1.14 |
| [[GSK1059615 (drug)]] 0.5 µM |  | -5.3 | -0.63 |
| [[Trametinib (drug)]] 0.5 µM |  | -4.5 | -0.37 |
| [[Ipatasertib (drug)]] 0.5 µM |  | -4.5 | -0.53 |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.33 |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -0.32 |
| [[MK-3903 (drug)]] 5 µM |  | -3.8 | -0.46 |
| [[Binimetinib (drug)]] 0.05 µM |  | -3.7 | -0.30 |
| [[AZD-8055 (drug)]] 5 µM |  | -3.7 | -0.44 |
| [[Brivudine (drug)]] 5 µM |  | -3.7 | -0.43 |
| [[GSK1059615 (drug)]] 5 µM |  | -3.7 | -0.43 |
| [[4EGI-1 (drug)]] 5 µM |  | -3.7 | -0.46 |
| [[Binimetinib (drug)]] 5 µM |  | -3.6 | -0.31 |
| [[Celecoxib (drug)]] 0.5 µM |  | -3.2 | -0.38 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Berbamine (drug)]] 0.5 µM (2.02); [[Berbamine (drug)]] 5 µM (1.72); [[EX229 (drug)]] 0.05 µM (1.68); [[Bexarotene (drug)]] 0.05 µM (1.59); [[Everolimus (drug)]] 5 µM (1.59); [[Tofacitinib (citrate) (drug)]] 0.5 µM (1.55); [[Tofacitinib (citrate) (drug)]] 5 µM (1.54); [[Tofacitinib (drug)]] 5 µM (1.52)
- Weakest: [[Vortioxetine (drug)]] 5 µM (0.0330, ⚠ toxic); [[Imiquimod (maleate) (drug)]] 0.5 µM (0.0878); [[Carbamazepine (drug)]] 0.5 µM (0.133); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM (0.163); [[Pentamidine (isethionate) (drug)]] 5 µM (0.194); [[Hydroxyurea (drug)]] 0.05 µM (0.200); [[Roxadustat (drug)]] 0.05 µM (0.240); [[Orlistat (drug)]] 0.05 µM (0.295); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM (0.296)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 17): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[PON2]] (20, 2 ⚠), [[DAAM1]] (19, 4 ⚠), [[SORBS1]] (18, 1 ⚠), [[ARID5B]] (16), [[LARP4]] (15, 2 ⚠), [[TNPO1]] (15, 7 ⚠), [[HSPA4]] (15, 7 ⚠), [[CTNNAL1]] (15, 13 ⚠), [[ACSL3]] (14, 1 ⚠), [[BIRC3]] (14, 4 ⚠), [[RSRC2]] (14, 6 ⚠), [[HNRNPM]] (14, 8 ⚠), [[WAPL]] (13, 1 ⚠), [[PPHLN1]] (13, 2 ⚠), [[SUPT6H]] (12, 1 ⚠), [[PCLO]] (12, 1 ⚠), [[SPAG9]] (12, 2 ⚠), [[ELOVL5]] (12, 2 ⚠)
- down: [[SEMA4B]] (30, 5 ⚠), [[ITGB4]] (28, 5 ⚠), [[FLNB]] (28, 6 ⚠), [[FERMT1]] (27, 2 ⚠), [[ENSG00000260877]] (27, 2 ⚠), [[NAB1]] (26, 5 ⚠), [[IFI44L]] (26, 6 ⚠), [[THSD4]] (26, 6 ⚠), [[OAS2]] (25, 5 ⚠), [[MX2]] (25, 5 ⚠), [[PARP9]] (25, 7 ⚠), [[ANTXR2]] (25, 7 ⚠), [[IFI44]] (25, 9 ⚠), [[EPSTI1]] (24, 5 ⚠), [[MX1]] (24, 5 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[ENSG00000230975]] (+7.8, ⚠ noise-class RNA), [[CALB1]] (+7.4), [[DSG3]] (+7.2), [[LGR5]] (+7.1), [[SPINK13]] (+6.9), [[MARCOL]] (+6.8), [[CLIC5]] (+6.6), [[GCNT3]] (+6.5), [[TSPAN8]] (+6.4), [[ENSG00000224322]] (+6.4, ⚠ noise-class RNA), [[SPON1]] (+6.4), [[SERPINB5]] (+6.4), [[TPTEP1-1]] (+6.4), [[PTPRR]] (+6.3), [[ENSG00000283633]] (+6.3, ⚠ noise-class RNA), [[LINC02582]] (+6.3), [[MUC13]] (+6.3), [[SLC6A20]] (+6.2) (1,455 genes, 109 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[VIM]] (-3.9), [[ZNF264]] (-3.7), [[LGALS1]] (-3.7), [[SMARCA1]] (-3.6), [[OSMR-DT]] (-3.5), [[ENSG00000214265]] (-3.5, ⚠ noise-class RNA), [[HDGFL3]] (-3.5), [[OSMR]] (-3.5), [[MPDZ]] (-3.5), [[LIFR]] (-3.5), [[LINC00662]] (-3.5), [[FKBP10]] (-3.5), [[MAP1B]] (-3.5), [[ZNF875]] (-3.5), [[TUSC3]] (-3.4), [[MAGED1]] (-3.4) (221 genes, 3 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 17): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Strong here (> 1.5): component 43 (1.57; genes MYO5B, TRPS1, FGD6, OCLN / LIMK2, TGFBR1, CYB5B, ITPK1); component 14 (1.53; genes PNPT1, HILPDA, P4HB, ASCC3 / MBOAT2, SMARCA2, CSNK1G3, MACO1); component 9 (1.52; genes PCNT, YWHAH, KLC1, HP1BP3 / MAP3K8, EGLN3, RAB20, IVNS1ABP)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 21 in all, 21 with an alert ⚠; shown: the 15 strongest; 6 more groups (6 of them with an alert ⚠) not shown. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 41 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[APC]] | APC altered (any record) (10 lines) vs not recorded (40) | 7 / 0 / 0 | C 7; 7 with an alert ⚠ | ⚠ tissue-confounded; across organs; mechanism partly not recorded |
| [[APC]] | APC loss of function (7 lines) vs not recorded (40) | 5 / 0 / 0 | C 5; 5 with an alert ⚠ | ⚠ tissue-confounded; across organs |
| [[KMT2D]] | KMT2D altered (any record) (15 lines) vs not recorded (35) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[SETD1B]] | SETD1B altered (any record) (11 lines) vs not recorded (39) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, ARID1A |
| [[ARID1A]] | ARID1A altered (any record) (15 lines) vs not recorded (35) | 0 / 0 / 1 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[FBXW7]] | FBXW7 loss of function (5 lines) vs not recorded (45) | 0 / 1 / 0 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines |
| [[HNF1A]] | HNF1A loss of function (6 lines) vs not recorded (44) | 1 / 0 / 0 | C 1; 1 with an alert ⚠ | ⚠ tissue-confounded; across organs |
| [[ACVR2A]] | ACVR2A altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with TGFBR2, SETD1B, PRDM2 |
| [[ACVR2A]] | ACVR2A loss of function (7 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B, PRDM2, EP300 |
| [[ARID1A]] | ARID1A loss of function (12 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[B2M]] | B2M altered (any record) (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[B2M]] | B2M loss of function (5 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, NF1, EP300 |
| [[KMT2D]] | KMT2D loss of function (8 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[NF1]] | NF1 altered (any record) (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with B2M |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,980 in all, 1,980 with an alert ⚠; shown: the 15 strongest; 1,965 more line sets (1,965 of them with an alert ⚠) not shown; 2,010 genes; 1,699 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[MUC5B]] | 37 vs 13 | 2 / 135 / 2 | B 33, C 106; 139 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[DAPP1]] | 39 vs 11 | 3 / 101 / 10 | B 37, C 77; 114 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SLC6A14]] | 39 vs 11 | 3 / 101 / 4 | B 29, C 79; 108 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SPOCK1]] | 29 vs 21 | 1 / 62 / 45 | B 58, C 50; 108 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MMP7]] | 39 vs 11 | 5 / 97 / 0 | B 39, C 63; 102 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[APCDD1L]] | 34 vs 16 | 2 / 99 / 0 | B 16, C 85; 101 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PDZK1IP1]] | 32 vs 18 | 7 / 92 / 1 | B 41, C 59; 100 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ITGA11]] | 34 vs 16 | 2 / 95 / 0 | B 19, C 78; 97 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01411]] | 38 vs 12 | 0 / 97 / 0 | B 13, C 84; 97 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TACSTD2]] | 34 vs 16 | 2 / 94 / 1 | B 17, C 80; 97 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PDGFRB]] | 36 vs 14 | 1 / 94 / 1 | B 21, C 75; 96 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[KCNMA1]] | 26 vs 24 | 3 / 43 / 47 | B 70, C 23; 93 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SLC28A3]] | 34 vs 16 | 4 / 89 / 0 | B 31, C 62; 93 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[INSYN2B]] | 31 vs 19 | 0 / 92 / 0 | B 18, C 74; 92 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[RORC]] | 30 vs 20 | 5 / 87 / 0 | B 32, C 60; 92 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 17; `tables/line_effects.parquet` — line == 17
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 17; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 17]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include LoVo

---
cell_line: "NCI-H2347"
type: "cell line"
cell_line_id: "CVCL_1550"
depmap_id: "ACH-000875"
organ: "Lung"
tp53_status: "altered"
drivers: ["B2M(Stopgain)", "EP300(Missense)", "KRAS(Missense)", "NF1(Missense)", "NRAS(Missense)", "TP53(Splice_site)", "TP53(Synonymous_splicing)"]
n_dd_depleted: 7
median_response: 0.811
tags: ["cell-line", "organ/lung"]
generated_by: "tahoemap"
---

# NCI-H2347

*Lung · TP53 altered · CVCL_1550 · ACH-000875*

|  |  |
|---|---|
| Organ | Lung |
| TP53 status | altered |
| Drivers | B2M(Stopgain); EP300(Missense); KRAS(Missense); NF1(Missense); NRAS(Missense); TP53(Splice_site); TP53(Synonymous_splicing) |
| Driver changes | B2M p.Q28*; EP300 p.V5L; KRAS p.L19F; NF1 p.H31L; NRAS p.Q61R; TP53 p.T125T; TP53 p.Thr125Thr |
| Cells over all wells | 2,227,532 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.811 (1 = a typical line) |
| Drug-doses that deplete it | 7 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 5 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,283 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 38): the line loses cells relative to the other lines in the same wells. Drug-doses: 7 in all, 2 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Dabrafenib (drug)]] 5 µM |  | -3.7 | -0.72 |
| [[Artesunate (drug)]] 0.5 µM |  | -3.6 | -0.72 |
| [[BAY1125976 (drug)]] 5 µM |  | -3.3 | -0.65 |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -3.2 | -0.68 |
| [[Encorafenib (drug)]] 5 µM |  | -3.2 | -0.63 |
| [[Anethole trithione (drug)]] 0.5 µM |  | -3.1 | -0.60 |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.48 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Phenylephrine (hydrochloride) (drug)]] 5 µM (1.59); [[TAK-901 (drug)]] 0.05 µM (1.48); [[Decitabine (drug)]] 0.05 µM (1.46); [[Medroxyprogesterone acetate (drug)]] 5 µM (1.42); [[Econazole (drug)]] 5 µM (1.41); [[Tofacitinib (drug)]] 5 µM (1.41); [[Tucidinostat (drug)]] 0.05 µM (1.39); [[Triamcinolone (drug)]] 0.05 µM (1.39)
- Weakest: [[Crizotinib (hydrochloride) (drug)]] 0.5 µM (-0.309); [[Allantoin (drug)]] 0.05 µM (-0.238, ⚠ transcription drop); [[Naproxen (drug)]] 0.05 µM (-0.0351); [[Monocrotaline (drug)]] 0.05 µM (-0.0267); [[Pimozide (drug)]] 0.5 µM (0.0816, ⚠ transcription drop); [[Vilanterol (drug)]] 0.05 µM (0.0940); [[Tazarotene (drug)]] 0.5 µM (0.162); [[Ferulic acid (drug)]] 0.5 µM (0.210); [[Rapamycin (drug)]] 0.05 µM (0.219); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM (0.227)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 38): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[BIRC3]] (33, 4 ⚠), [[FKBP5]] (30, 7 ⚠), [[CPD]] (22), [[ATP1A1]] (21, 3 ⚠), [[ACSL1]] (20, 4 ⚠), [[KLF9]] (19), [[TFCP2L1]] (19, 4 ⚠), [[MT1E]] (18), [[PYGB]] (15), [[UGP2]] (15), [[TSC22D3]] (14), [[ARHGAP26]] (14, 1 ⚠), [[AGPAT5]] (14, 4 ⚠)
- down: [[MRPS6]] (26, 4 ⚠), [[SLC5A3]] (20, 4 ⚠), [[WASF2]] (20, 11 ⚠), [[GFPT1]] (19, 9 ⚠), [[GPRC5A]] (19, 13 ⚠), [[IRF9]] (18, 4 ⚠), [[SEC23A]] (18, 5 ⚠), [[CBLB]] (18, 9 ⚠), [[KCNK1]] (18, 10 ⚠), [[MXI1]] (18, 12 ⚠), [[FAM13A]] (18, 12 ⚠), [[ETV5]] (17, 3 ⚠), [[DUSP6]] (17, 4 ⚠), [[MX1]] (17, 4 ⚠), [[FAM107B]] (17, 7 ⚠), [[SPRED2]] (16, 3 ⚠), [[GBP4]] (16, 4 ⚠), [[SPRY4]] (15, 2 ⚠), [[IFI44L]] (14, 2 ⚠), [[ADAR]] (14, 2 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[SLC34A2]] (+6.7), [[STEAP4]] (+6.6), [[TACSTD2]] (+6.4), [[ARHGAP20]] (+6.4), [[IRF6]] (+6.1), [[XIST]] (+6.1), [[CST6]] (+6.0), [[VGLL3]] (+5.9), [[PGBD5]] (+5.9), [[DAPP1]] (+5.9), [[SFTPA2]] (+5.9), [[FAM83A]] (+5.8), [[G0S2]] (+5.8), [[WFDC2]] (+5.7), [[KRT7]] (+5.6) (1,164 genes, 26 with an alert ⚠; shown: the 15 strongest)
- Lacks: [[IGF2BP3]] (-3.8), [[RASA3]] (-3.6), [[ANGPTL4]] (-3.5), [[ZEB1]] (-3.3), [[NFIA]] (-3.3), [[UACA]] (-3.2), [[TMLHE]] (-3.2), [[OSBPL6]] (-3.1), [[MSRB3]] (-3.1), [[XKR6]] (-3.1), [[GP6-AS1]] (-3.0), [[LINC01138]] (-3.0), [[LHFPL6]] (-3.0), [[CACHD1]] (-3.0), [[CHPT1]] (-3.0) (223 genes, 11 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 38): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Strong here (> 1.5): component 13 (1.50; genes UGP2, KLF9, TSC22D3, SSBP2 / LUC7L3, PER3, TCP10L, SEMA3A)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 8 in all, 8 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 55 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[NRAS]] | NRAS gain of function (7 lines) vs not recorded (43) | 0 / 2 / 0 | C 2; 2 with an alert ⚠ | ⚠ within organs, on part of the lines |
| [[B2M]] | B2M altered (any record) (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[B2M]] | B2M loss of function (5 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, NF1, EP300 |
| [[EP300]] | EP300 altered (any record) (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, SETD1B |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[NF1]] | NF1 altered (any record) (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with B2M |
| [[NF1]] | NF1 loss of function (3 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ few lines (3 vs 43); within organs, on part of the lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,172 in all, 2,172 with an alert ⚠; shown: the 15 strongest; 2,157 more line sets (2,157 of them with an alert ⚠) not shown; 2,207 genes; 1,825 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[TMEM45B]] | 32 vs 18 | 3 / 199 / 12 | B 58, C 156; 214 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[EPS8L3]] | 35 vs 15 | 0 / 196 / 1 | B 46, C 151; 197 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ARHGEF38]] | 36 vs 14 | 5 / 172 / 9 | B 49, C 137; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GCNT3]] | 38 vs 12 | 2 / 184 / 0 | B 43, C 143; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01559]] | 38 vs 12 | 0 / 182 / 0 | B 36, C 146; 182 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TOX3]] | 31 vs 19 | 4 / 168 / 1 | B 46, C 127; 173 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PRR15]] | 28 vs 22 | 1 / 138 / 9 | B 36, C 112; 148 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[HNF4A]] | 34 vs 16 | 0 / 145 / 0 | B 29, C 116; 145 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01819]] | 29 vs 21 | 2 / 141 / 1 | B 27, C 117; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[NPSR1]] | 42 vs 8 | 2 / 142 / 0 | B 26, C 118; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GPX2]] | 36 vs 14 | 2 / 139 / 0 | B 23, C 118; 141 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[KLK10]] | 34 vs 16 | 2 / 131 / 8 | B 43, C 98; 141 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ATP10B]] | 40 vs 10 | 0 / 140 / 0 | B 27, C 113; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC13]] | 40 vs 10 | 2 / 138 / 0 | B 33, C 107; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PROM1]] | 37 vs 13 | 0 / 137 / 0 | B 32, C 105; 137 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 38; `tables/line_effects.parquet` — line == 38
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 38; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 38]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include NCI-H2347

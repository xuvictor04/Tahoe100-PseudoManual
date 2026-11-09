---
cell_line: "MIA PaCa-2"
type: "cell line"
cell_line_id: "CVCL_0428"
depmap_id: "ACH-000601"
organ: "Pancreas"
tp53_status: "altered"
drivers: ["ARID1A(Missense)", "ARID1A(Stopgain)", "CDKN2A(Deletion)", "CDKN2B(Deletion)", "KRAS(Missense)", "TP53(Missense)"]
n_dd_depleted: 18
median_response: 1.043
tags: ["cell-line", "organ/pancreas"]
generated_by: "tahoemap"
---

# MIA PaCa-2

*Pancreas · TP53 altered · CVCL_0428 · ACH-000601*

|  |  |
|---|---|
| Organ | Pancreas |
| TP53 status | altered |
| Drivers | ARID1A(Missense); ARID1A(Stopgain); CDKN2A(Deletion); CDKN2B(Deletion); KRAS(Missense); TP53(Missense) |
| Driver changes | ARID1A p.P1723L; ARID1A p.Q321*; KRAS p.G12C; TP53 p.R248W |
| Cells over all wells | 2,432,607 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 1.04 (1 = a typical line) |
| Drug-doses that deplete it | 18 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 10 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 13,724 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 18): the line loses cells relative to the other lines in the same wells. Drug-doses: 18 in all, 8 with an alert ⚠; shown: the 12 strongest and the 5 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -18.2 | -2.42 |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -16.4 | -2.47 |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -14.2 | -2.71 |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -12.4 | -1.81 |
| [[Belumosudil (drug)]] 5 µM |  | -10.2 | -1.56 |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -9.1 | -1.49 |
| [[GSK1059615 (drug)]] 5 µM |  | -6.0 | -0.90 |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -0.85 |
| [[Bimiralisib (drug)]] 5 µM |  | -5.5 | -0.82 |
| [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -0.71 |
| [[Auranofin (drug)]] 5 µM |  | -4.1 | -0.60 |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -0.57 |
| [[Pralsetinib (drug)]] 5 µM |  | -3.7 | -0.66 |
| [[XRK3F2 (drug)]] 5 µM |  | -3.5 | -0.53 |
| [[palbociclib (drug)]] 5 µM |  | -3.5 | -0.56 |
| [[Vemurafenib (drug)]] 5 µM |  | -3.2 | -0.48 |
| [[Posaconazole (drug)]] 5 µM |  | -3.1 | -0.45 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Norepinephrine (hydrochloride) (drug)]] 5 µM (1.96); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM (1.88); [[Irinotecan (drug)]] 0.5 µM (1.82); [[Everolimus (drug)]] 5 µM (1.81); [[Tofacitinib (drug)]] 5 µM (1.79); [[Vilanterol (drug)]] 0.05 µM (1.79); [[Binimetinib (drug)]] 0.5 µM (1.75); [[vincristine (drug)]] 0.05 µM (1.74)
- Weakest: [[Monocrotaline (drug)]] 0.05 µM (-0.0931); [[Menadione (drug)]] 5 µM (0.0440); [[Allantoin (drug)]] 0.05 µM (0.143, ⚠ transcription drop); [[Roxadustat (drug)]] 0.05 µM (0.150); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM (0.258); [[Citalopram (hydrobromide) (drug)]] 0.5 µM (0.268); [[Cyclosporin A (drug)]] 0.5 µM (0.296); [[Hydroxyurea (drug)]] 0.05 µM (0.399); [[Pimozide (drug)]] 0.05 µM (0.446)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 18): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[FKBP5]] (21, 6 ⚠), [[EGFR]] (18, 4 ⚠), [[HSPA4]] (17, 8 ⚠), [[CFB]] (15, 1 ⚠), [[DDX5]] (15, 6 ⚠), [[HSPH1]] (14, 6 ⚠), [[CHD1]] (13, 3 ⚠), [[COL5A2]] (13, 3 ⚠), [[TEAD1]] (13, 5 ⚠), [[LIMA1]] (13, 8 ⚠), [[UBR3]] (12, 2 ⚠), [[ZBTB11]] (12, 3 ⚠), [[ZSWIM6]] (12, 3 ⚠), [[CPEB4]] (11), [[MED13]] (10), [[ARID4A]] (10, 1 ⚠), [[MED29]] (10, 1 ⚠), [[ATP6V0A1]] (9)
- down: [[NTSR1]] (34, 11 ⚠), [[SPRY4-AS1]] (33, 9 ⚠), [[TRIB2]] (29, 6 ⚠), [[SPRY4]] (29, 8 ⚠), [[WT1-AS]] (28, 8 ⚠), [[ZMYND8]] (28, 11 ⚠), [[CDCP1]] (27, 4 ⚠), [[NT5E]] (25, 1 ⚠), [[STX1A]] (25, 6 ⚠), [[TM4SF1]] (25, 8 ⚠), [[CAPRIN2]] (25, 9 ⚠), [[INSR]] (25, 12 ⚠), [[LINC01844]] (24, 3 ⚠), [[SH3TC2-DT]] (24, 4 ⚠), [[PYGL]] (22, 4 ⚠), [[ETV1]] (21, 2 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[TP63]] (+8.1), [[LINC02154]] (+7.6), [[ENSG00000286853]] (+6.7, ⚠ noise-class RNA), [[RGS4]] (+6.6), [[PKD1L1-AS1]] (+6.6), [[TNFRSF6B]] (+6.5), [[CSMD3]] (+6.4), [[ENSG00000287158]] (+6.4, ⚠ noise-class RNA), [[WT1-AS]] (+5.9), [[ENSG00000287023]] (+5.9, ⚠ noise-class RNA), [[ENSG00000289850]] (+5.9, ⚠ noise-class RNA), [[CFAP299]] (+5.8), [[ROR1-AS1]] (+5.8), [[LINC02509]] (+5.7), [[ENSG00000243486]] (+5.7, ⚠ noise-class RNA), [[CCDC190]] (+5.7), [[SRGN]] (+5.6), [[LINC01010]] (+5.6), [[BRINP3]] (+5.6), [[UCA1]] (+5.6) (1,142 genes, 93 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[ARID1B]] (-4.1), [[DIAPH2]] (-4.0), [[MLLT3]] (-3.9), [[KLF7]] (-3.9), [[KDM6A]] (-3.9), [[TRPS1]] (-3.9), [[PLOD2]] (-3.9), [[ARHGEF10]] (-3.8), [[FOCAD]] (-3.8), [[ARID5B]] (-3.8), [[TUSC3]] (-3.8), [[BNIP3]] (-3.8), [[ALCAM]] (-3.8), [[ITGA2]] (-3.8), [[TGFBR2]] (-3.7) (441 genes, 6 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 18): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Strong here (> 1.5): component 56 (1.53; genes PARVA, PARP8, MME, LIMS1 / ATP2B4, NAV3, PLCXD1, MIR31HG)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 7 in all, 7 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 57 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[CDKN2B]] | CDKN2B loss of function (13 lines) vs not recorded (37) | 4 / 2 / 0 | B 3, C 3; 6 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[ARID1A]] | ARID1A altered (any record) (15 lines) vs not recorded (35) | 0 / 0 / 1 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[ARID1A]] | ARID1A loss of function (12 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,816 in all, 2,816 with an alert ⚠; shown: the 15 strongest; 2,801 more line sets (2,801 of them with an alert ⚠) not shown; 2,860 genes; 2,461 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 18; `tables/line_effects.parquet` — line == 18
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 18; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 18]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include MIA PaCa-2

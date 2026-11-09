---
cell_line: "SNU-423"
type: "cell line"
cell_line_id: "CVCL_0366"
depmap_id: "ACH-000493"
organ: "Liver"
tp53_status: "altered"
drivers: ["ARID1A(Stopgain)", "RNF43(Missense)", "TERT(Promoter)", "TP53(Splice_site)"]
n_dd_depleted: 21
median_response: 1.015
tags: ["cell-line", "organ/liver"]
generated_by: "tahoemap"
---

# SNU-423

*Liver · TP53 altered · CVCL_0366 · ACH-000493*

|  |  |
|---|---|
| Organ | Liver |
| TP53 status | altered |
| Drivers | ARID1A(Stopgain); RNF43(Missense); TERT(Promoter); TP53(Splice_site) |
| Driver changes | ARID1A p.G623*; RNF43 p.I485V |
| Cells over all wells | 1,501,592 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 1.01 (1 = a typical line) |
| Drug-doses that deplete it | 21 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 17 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,969 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 14): the line loses cells relative to the other lines in the same wells. Drug-doses: 21 in all, 4 with an alert ⚠; shown: the 12 strongest and the 2 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -5.7 | -1.45 |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -0.91 |
| [[Penfluridol (drug)]] 0.5 µM |  | -4.2 | -1.02 |
| [[Pemetrexed (drug)]] 0.5 µM |  | -4.1 | -0.99 |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -0.98 |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | -3.9 | -0.93 |
| [[Mozavaptan (drug)]] 0.5 µM |  | -3.9 | -0.92 |
| [[Hydroxyurea (drug)]] 0.5 µM |  | -3.7 | -0.88 |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.7 | -0.90 |
| [[Vismodegib (drug)]] 5 µM |  | -3.6 | -0.84 |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -3.5 | -0.83 |
| [[Celecoxib (drug)]] 0.05 µM |  | -3.5 | -0.82 |
| [[Peretinoin (drug)]] 0.5 µM |  | -3.4 | -0.81 |
| [[Ferulic acid (drug)]] 0.5 µM |  | -3.3 | -0.81 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Neratinib (drug)]] 0.05 µM (1.98); [[LJI308 (drug)]] 0.05 µM (1.95); [[Sonidegib (drug)]] 0.05 µM (1.79, ⚠ unreliable plate only); [[Budesonide (drug)]] 5 µM (1.73); [[(S)-Crizotinib (drug)]] 5 µM (1.73); [[Econazole (drug)]] 5 µM (1.73); [[Dexamethasone (drug)]] 5 µM (1.70); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM (1.69); [[Clobetasol propionate (drug)]] 5 µM (1.69)
- Weakest: [[Allantoin (drug)]] 0.05 µM (0.0535, ⚠ transcription drop); [[Vilanterol (drug)]] 0.05 µM (0.137); [[Pralsetinib (drug)]] 0.05 µM (0.207); [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM (0.244); [[Vandetanib (drug)]] 5 µM (0.340); [[Verteporfin (drug)]] 0.5 µM (0.373); [[Idarubicin (hydrochloride) (drug)]] 0.05 µM (0.428); [[Bimatoprost (drug)]] 0.5 µM (0.445); [[Orlistat (drug)]] 0.05 µM (0.457)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 14): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[FKBP5]] (29, 9 ⚠), [[HSPA4]] (20, 12 ⚠), [[ACSL1]] (19, 3 ⚠), [[ERRFI1]] (18), [[KLF9]] (18), [[TSC22D3]] (18), [[CPD]] (17), [[LDLRAD3]] (17), [[HIPK2]] (17, 2 ⚠), [[CCND3]] (16), [[TMTC1]] (15, 1 ⚠), [[TOP1]] (15, 2 ⚠), [[ATP2B4]] (14, 1 ⚠)
- down: [[IFIT3]] (26, 8 ⚠), [[IFI44L]] (25, 7 ⚠), [[INSR]] (24, 15 ⚠), [[PHF21A]] (24, 18 ⚠), [[SYNJ2]] (23, 2 ⚠), [[DDX60]] (23, 6 ⚠), [[MX1]] (23, 7 ⚠), [[PLSCR1]] (23, 7 ⚠), [[ZMYND8]] (23, 9 ⚠), [[FRMD5]] (22, 5 ⚠), [[IFITM1]] (22, 6 ⚠), [[TRIM22]] (22, 7 ⚠), [[IGFBP3]] (22, 10 ⚠), [[PARP9]] (21, 5 ⚠), [[IFIT1]] (21, 5 ⚠), [[CTPS2]] (17, 2 ⚠), [[EIF2AK2]] (17, 2 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[GRIN2A]] (+7.8), [[SFRP1]] (+6.8), [[ENSG00000259560]] (+6.6, ⚠ noise-class RNA), [[LINC02506]] (+6.5), [[PLPP4]] (+6.5), [[TMEM132D]] (+6.4), [[TRIM55]] (+6.4), [[IGFN1]] (+6.4), [[ENSG00000233358]] (+6.3, ⚠ noise-class RNA), [[LINC01435]] (+6.2), [[PSG9]] (+6.2), [[PSG1]] (+6.1), [[NGF]] (+6.0), [[COL6A3]] (+6.0), [[VCAN]] (+6.0), [[THBS2]] (+6.0), [[SPARC]] (+5.9) (1,366 genes, 119 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[LDHB]] (-3.3), [[GSTP1]] (-3.1), [[LAMA5]] (-2.9), [[DAB2IP]] (-2.7), [[NQO1]] (-2.7), [[ULK2]] (-2.7), [[TSPAN13]] (-2.7), [[LRRC8B]] (-2.7), [[CGAS]] (-2.6), [[PPP1R9A]] (-2.6), [[LIPE-AS1]] (-2.6), [[NUP210]] (-2.6), [[NEBL]] (-2.6), [[CYBA]] (-2.6), [[PTK7]] (-2.6) (116 genes, 2 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 14): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Strong here (> 1.5): component 13 (1.61; genes UGP2, KLF9, TSC22D3, SSBP2 / LUC7L3, PER3, TCP10L, SEMA3A)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 6 in all, 6 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 57 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[TERT]] | TERT gain of function (8 lines) vs not recorded (39) | 5 / 0 / 0 | C 5; 5 with an alert ⚠ | ⚠ tissue-confounded; across organs; TERT not expressed in 1 of the 8 altered lines |
| [[ARID1A]] | ARID1A altered (any record) (15 lines) vs not recorded (35) | 0 / 0 / 1 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[ARID1A]] | ARID1A loss of function (12 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[RNF43]] | RNF43 altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with EP300, ACVR2A |
| [[TERT]] | TERT altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; TERT not expressed in 2 of the 11 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,634 in all, 1,634 with an alert ⚠; shown: the 15 strongest; 1,619 more line sets (1,619 of them with an alert ⚠) not shown; 1,653 genes; 1,419 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 14; `tables/line_effects.parquet` — line == 14
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 14; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 14]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include SNU-423

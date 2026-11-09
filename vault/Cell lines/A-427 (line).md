---
cell_line: "A-427"
type: "cell line"
cell_line_id: "CVCL_1055"
depmap_id: "ACH-000757"
organ: "Lung"
tp53_status: "wild type"
drivers: ["CDKN2A(Deletion)", "CDKN2B(Deletion)", "CTNNB1(Missense)", "KRAS(Missense)", "POLE(Missense)", "SMARCA4(Missense)"]
n_dd_depleted: 30
median_response: 0.8
tags: ["cell-line", "organ/lung"]
generated_by: "tahoemap"
---

# A-427

*Lung · TP53 wild type · CVCL_1055 · ACH-000757*

|  |  |
|---|---|
| Organ | Lung |
| TP53 status | wild type |
| Drivers | CDKN2A(Deletion); CDKN2B(Deletion); CTNNB1(Missense); KRAS(Missense); POLE(Missense); SMARCA4(Missense) |
| Driver changes | CTNNB1 p.T41A; KRAS p.G12D; POLE p.R37L; SMARCA4 p.A1307D |
| Cells over all wells | 1,430,066 |
| Wells with usable expression | 1,328 (99.9%) |
| Median response strength (β) | 0.800 (1 = a typical line) |
| Drug-doses that deplete it | 30 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 15 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,435 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 23): the line loses cells relative to the other lines in the same wells. Drug-doses: 31 in all, 16 with an alert ⚠; shown: the 12 strongest and the 8 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -20.4 | -4.09 |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -17.7 | -3.89 |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -15.5 | -4.21 |
| [[GSK1059615 (drug)]] 5 µM |  | -13.3 | -3.06 |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -11.9 | -2.78 |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -10.6 | -2.31 |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -10.2 | -2.30 |
| [[PH-797804 (drug)]] 5 µM |  | -9.1 | -2.10 |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -8.8 | -1.86 |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -8.3 | -1.58 |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.9 | -1.97 |
| [[Homoharringtonine (drug)]] 0.05 µM |  | -6.7 | -1.41 |
| [[venetoclax (drug)]] 5 µM |  | -5.5 | -1.24 |
| [[Brivudine (drug)]] 5 µM |  | -4.9 | -1.04 |
| [[Ponatinib (drug)]] 5 µM |  | -4.7 | -0.98 |
| [[ERK5-IN-2 (drug)]] 5 µM |  | -4.1 | -0.86 |
| [[Mebendazole (drug)]] 5 µM |  | -3.9 | -0.81 |
| [[Tofacitinib (drug)]] 0.05 µM |  | -3.5 | -0.74 |
| [[Infigratinib (drug)]] 5 µM |  | -3.4 | -0.72 |
| [[Clopidogrel (drug)]] 0.05 µM |  | -3.3 | -0.67 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Amsacrine (drug)]] 0.5 µM (1.84); [[palbociclib (drug)]] 5 µM (1.65); [[Benproperine (phosphate) (drug)]] 5 µM (1.56); [[Cytarabine (hydrochloride) (drug)]] 0.05 µM (1.55); [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM (1.54); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM (1.47, ⚠ cell-cycle shift); [[Neratinib (drug)]] 0.5 µM (1.47); [[Gemcitabine (drug)]] 0.05 µM (1.47); [[Glycyrrhizic acid (drug)]] 5 µM (1.46)
- Weakest: [[Allantoin (drug)]] 0.05 µM (-0.691, ⚠ transcription drop); [[Tazarotene (drug)]] 0.5 µM (-0.685); [[Imiquimod (maleate) (drug)]] 0.5 µM (-0.476); [[Neratinib (drug)]] 0.05 µM (-0.304); [[Monocrotaline (drug)]] 0.05 µM (-0.221); [[Verteporfin (drug)]] 0.5 µM (0.103); [[Econazole (drug)]] 5 µM (0.175); [[Pimozide (drug)]] 0.5 µM (0.241, ⚠ transcription drop); [[Aprepitant (drug)]] 0.05 µM (0.257); [[Budesonide (drug)]] 0.5 µM (0.290)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 23): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[GBF1]] (15, 3 ⚠), [[SQSTM1]] (13, 1 ⚠), [[ARL13B]] (13, 3 ⚠), [[GLS]] (13, 4 ⚠), [[ATP6V1A]] (12, 2 ⚠), [[SPAG9]] (12, 3 ⚠), [[EPS8]] (12, 4 ⚠), [[RIOK3]] (12, 5 ⚠), [[KLF6]] (11, 4 ⚠), [[CPEB4]] (10, 1 ⚠), [[GULP1]] (10, 1 ⚠), [[PARD6B]] (10, 2 ⚠), [[MDM2]] (9), [[SYDE2]] (8), [[RSRC2]] (8)
- down: [[ST6GAL1]] (20, 9 ⚠), [[R3HDM2]] (20, 12 ⚠), [[ETV5]] (19, 4 ⚠), [[NHSL1]] (19, 7 ⚠), [[CCN2]] (18, 6 ⚠), [[WWOX]] (18, 6 ⚠), [[IMMP2L]] (18, 14 ⚠), [[LINC00466]] (17, 9 ⚠), [[ZBTB20]] (17, 10 ⚠), [[MTAP]] (17, 14 ⚠), [[EGR1]] (16, 1 ⚠), [[NEBL]] (16, 14 ⚠), [[HMGA2]] (14, 1 ⚠), [[XPOT]] (14, 2 ⚠), [[ETV4]] (13), [[ASPH]] (13), [[DCBLD2]] (13, 1 ⚠), [[DUSP6]] (11)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[BCHE]] (+7.7), [[ALDH1A1]] (+7.6), [[GCG]] (+7.4), [[OLR1]] (+7.4), [[SERPINB2]] (+7.3), [[PTPRZ1]] (+7.2), [[ENSG00000253500]] (+7.0, ⚠ noise-class RNA), [[NLGN1]] (+6.9), [[MGAT4C]] (+6.8), [[LINC01322]] (+6.8), [[MME]] (+6.7), [[LRRTM4]] (+6.7), [[FGF20]] (+6.6), [[NR5A2]] (+6.5), [[EPHA5]] (+6.4), [[CRISPLD1]] (+6.3) (1,850 genes, 144 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[TXNIP]] (-4.1), [[PRKCSH]] (-3.8), [[CD44]] (-3.8), [[LGALS3BP]] (-3.8), [[PARVA]] (-3.8), [[ZNF532]] (-3.7), [[TRIM38]] (-3.7), [[ZNF462]] (-3.7), [[ATP2B4]] (-3.6), [[TENT5A]] (-3.6), [[TIMP1]] (-3.6), [[SOX9]] (-3.6), [[MIR100HG]] (-3.6), [[MBNL2]] (-3.6), [[EMP1]] (-3.6) (340 genes, 11 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 23): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.700 to 1.36).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 9 in all, 9 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 55 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[CDKN2B]] | CDKN2B loss of function (13 lines) vs not recorded (37) | 4 / 2 / 0 | B 3, C 3; 6 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[POLE]] | POLE altered (any record) (8 lines) vs not recorded (42) | 1 / 0 / 0 | A 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[CTNNB1]] | CTNNB1 altered (any record) (5 lines) vs not recorded (45) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[CTNNB1]] | CTNNB1 gain of function (4 lines) vs not recorded (45) | 0 / 0 / 0 | — | ⚠ few lines (4 vs 45); within organs, on part of the lines |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[SMARCA4]] | SMARCA4 altered (any record) (12 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[SMARCA4]] | SMARCA4 loss of function (10 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,137 in all, 2,137 with an alert ⚠; shown: the 15 strongest; 2,122 more line sets (2,122 of them with an alert ⚠) not shown; 2,166 genes; 1,872 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 23; `tables/line_effects.parquet` — line == 23
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 23; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 23]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include A-427

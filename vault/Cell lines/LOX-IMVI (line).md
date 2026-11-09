---
cell_line: "LOX-IMVI"
type: "cell line"
cell_line_id: "CVCL_1381"
depmap_id: "ACH-000750"
organ: "Skin"
tp53_status: "wild type"
drivers: ["ARID1A(Stopgain)", "BRAF(Missense)", "CDKN2A(Deletion)", "NF1(Stopgain)", "TERT(Promoter)"]
n_dd_depleted: 43
median_response: 1.018
tags: ["cell-line", "organ/skin"]
generated_by: "tahoemap"
---

# LOX-IMVI

*Skin · TP53 wild type · CVCL_1381 · ACH-000750*

|  |  |
|---|---|
| Organ | Skin |
| TP53 status | wild type |
| Drivers | ARID1A(Stopgain); BRAF(Missense); CDKN2A(Deletion); NF1(Stopgain); TERT(Promoter) |
| Driver changes | ARID1A p.Q1212*; BRAF p.V600E; NF1 p.Q1174* |
| Cells over all wells | 2,208,086 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 1.02 (1 = a typical line) |
| Drug-doses that deplete it | 43 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 23 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,015 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 32): the line loses cells relative to the other lines in the same wells. Drug-doses: 43 in all, 20 with an alert ⚠; shown: the 12 strongest and the 10 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -13.9 | -1.26 |
| [[PH-797804 (drug)]] 5 µM |  | -13.1 | -1.80 |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -12.4 | -1.50 |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -10.9 | -1.39 |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -9.8 | -1.15 |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -9.2 | -1.12 |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.1 | -0.96 |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -0.59 |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | -0.69 |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -5.8 | -1.01 |
| [[TAK-901 (drug)]] 0.05 µM |  | -5.8 | -0.73 |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -0.66 |
| [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -0.65 |
| [[ERK5-IN-2 (drug)]] 5 µM |  | -4.7 | -0.54 |
| [[Abemaciclib (drug)]] 5 µM |  | -4.7 | -0.57 |
| [[Paclitaxel (drug)]] 5 µM |  | -4.6 | -0.53 |
| [[Brivudine (drug)]] 5 µM |  | -4.5 | -0.52 |
| [[BAY1125976 (drug)]] 5 µM |  | -4.4 | -0.51 |
| [[Sapanisertib (drug)]] 5 µM |  | -4.3 | -0.49 |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -0.39 |
| [[GSK1059615 (drug)]] 5 µM |  | -4.2 | -0.49 |
| [[Encorafenib (drug)]] 5 µM |  | -4.1 | -0.47 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM (1.85); [[Ritonavir (drug)]] 0.5 µM (1.71); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (1.53, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM (1.53, ⚠ cell-cycle shift); [[palbociclib (drug)]] 0.5 µM (1.50, ⚠ cell-cycle shift); [[18β-Glycyrrhetinic acid (drug)]] 5 µM (1.50); [[Flumatinib (mesylate) (drug)]] 0.5 µM (1.49); [[Idarubicin (hydrochloride) (drug)]] 0.05 µM (1.46); [[palbociclib (drug)]] 5 µM (1.45); [[Naproxen (drug)]] 5 µM (1.44); [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM (1.44)
- Weakest: [[Monocrotaline (drug)]] 0.05 µM (-0.155); [[Citalopram (hydrobromide) (drug)]] 0.5 µM (0.0637); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM (0.170); [[BI-3406 (drug)]] 5 µM (0.245); [[Canagliflozin (drug)]] 0.05 µM (0.413); [[Vilanterol (drug)]] 0.05 µM (0.415); [[Saquinavir (drug)]] 0.5 µM (0.422); [[Silodosin (drug)]] 5 µM (0.424)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 32): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[PTPN1]] (24), [[FKBP5]] (21, 6 ⚠), [[PEG10]] (21, 12 ⚠), [[HIPK2]] (19, 1 ⚠), [[ZMYND8]] (17), [[FN1]] (17), [[TANC2]] (17), [[UBR3]] (16, 3 ⚠), [[UGP2]] (15), [[HSPA9]] (15, 6 ⚠), [[NOLC1]] (15, 12 ⚠), [[KLF9]] (14), [[MDM2]] (14, 1 ⚠), [[CPEB4]] (12), [[TSC22D3]] (12)
- down: [[KIAA1549L]] (30, 10 ⚠), [[NAV1]] (28, 14 ⚠), [[SIPA1L3]] (27, 15 ⚠), [[SAMD3]] (23, 13 ⚠), [[DNAAF9]] (23, 14 ⚠), [[C2CD2]] (23, 16 ⚠), [[EPIC1]] (22, 12 ⚠), [[C4orf47]] (21, 7 ⚠), [[PTPRD]] (21, 10 ⚠), [[KDM2B]] (21, 11 ⚠), [[EFNA5]] (21, 12 ⚠), [[PPP2R2C]] (21, 17 ⚠), [[MAP3K20]] (20, 6 ⚠), [[TBC1D32]] (20, 6 ⚠), [[PRMT2]] (18, 5 ⚠), [[AKAP12]] (18, 6 ⚠), [[LOXL2]] (17, 4 ⚠), [[SEMA4B]] (17, 4 ⚠), [[NT5E]] (14), [[HMGA2]] (14, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[TMPRSS15]] (+7.9), [[NETO1]] (+7.5), [[ENSG00000275016]] (+7.0, ⚠ noise-class RNA), [[SAMD3]] (+7.0), [[NTM]] (+6.9), [[DSCAM]] (+6.9), [[MSR1]] (+6.9), [[LINC02945]] (+6.8), [[LINC01687]] (+6.8), [[PAX3]] (+6.6), [[PHACTR1]] (+6.6), [[UBBP4-1]] (+6.5), [[ENSG00000258081]] (+6.4, ⚠ noise-class RNA), [[ENSG00000230972]] (+6.4, ⚠ noise-class RNA), [[MME]] (+6.2), [[MIR4527HG]] (+6.1), [[LINC02267]] (+6.1), [[KISS1]] (+6.1) (1,003 genes, 105 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[ZNF254]] (-3.3), [[ZNF91]] (-3.2), [[CPNE8]] (-3.2), [[TNFRSF10D]] (-3.1), [[PPP6R2]] (-3.1), [[CDCP1]] (-3.1), [[DANT2]] (-3.1), [[ABCA5]] (-3.1), [[LITAF]] (-3.1), [[PTPN3]] (-3.0), [[TVP23C-CDRT4]] (-3.0), [[FOXN3]] (-3.0), [[TVP23C]] (-3.0), [[ZNF611]] (-3.0), [[IL13RA1]] (-3.0) (368 genes, 7 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 32): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 56 (0.347; genes PARVA, PARP8, MME, LIMS1 / ATP2B4, NAV3, PLCXD1, MIR31HG)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 10 in all, 10 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 54 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TERT]] | TERT gain of function (8 lines) vs not recorded (39) | 5 / 0 / 0 | C 5; 5 with an alert ⚠ | ⚠ tissue-confounded; across organs; TERT not expressed in 1 of the 8 altered lines |
| [[ARID1A]] | ARID1A altered (any record) (15 lines) vs not recorded (35) | 0 / 0 / 1 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[ARID1A]] | ARID1A loss of function (12 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[BRAF]] | BRAF altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[BRAF]] | BRAF gain of function (7 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[NF1]] | NF1 altered (any record) (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with B2M |
| [[NF1]] | NF1 loss of function (3 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ few lines (3 vs 43); within organs, on part of the lines |
| [[TERT]] | TERT altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; TERT not expressed in 2 of the 11 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,489 in all, 2,489 with an alert ⚠; shown: the 15 strongest; 2,474 more line sets (2,474 of them with an alert ⚠) not shown; 2,535 genes; 2,213 of the sets gave arrows. Ranked by the number of arrows.*

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
| [[GCNT3]] | 38 vs 12 | 2 / 184 / 0 | B 43, C 143; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01559]] | 38 vs 12 | 0 / 182 / 0 | B 36, C 146; 182 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TOX3]] | 31 vs 19 | 4 / 168 / 1 | B 46, C 127; 173 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ITGB6]] | 32 vs 18 | 5 / 148 / 18 | B 47, C 124; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TC2N]] | 28 vs 22 | 3 / 163 / 5 | B 52, C 119; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 32; `tables/line_effects.parquet` — line == 32
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 32; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 32]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include LOX-IMVI

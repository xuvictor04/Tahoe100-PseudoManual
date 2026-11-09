---
cell_line: "A549"
type: "cell line"
cell_line_id: "CVCL_0023"
depmap_id: "ACH-000681"
organ: "Lung"
tp53_status: "wild type"
drivers: ["CDKN2A(Deletion)", "CDKN2B(Deletion)", "KRAS(Missense)", "SMARCA4(Frameshift)", "STK11(Stopgain)", "ZFHX3(Missense)"]
n_dd_depleted: 22
median_response: 1.043
tags: ["cell-line", "organ/lung"]
generated_by: "tahoemap"
---

# A549

*Lung · TP53 wild type · CVCL_0023 · ACH-000681*

|  |  |
|---|---|
| Organ | Lung |
| TP53 status | wild type |
| Drivers | CDKN2A(Deletion); CDKN2B(Deletion); KRAS(Missense); SMARCA4(Frameshift); STK11(Stopgain); ZFHX3(Missense) |
| Driver changes | KRAS p.G12S; SMARCA4 p.Q729fs; STK11 p.Q37*; ZFHX3 p.L1473F |
| Cells over all wells | 2,567,712 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 1.04 (1 = a typical line) |
| Drug-doses that deplete it | 22 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 17 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,841 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 0): the line loses cells relative to the other lines in the same wells. Drug-doses: 22 in all, 5 with an alert ⚠; shown: the 12 strongest and the 3 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.7 | -0.64 |
| [[Abemaciclib (drug)]] 5 µM |  | -6.5 | -0.66 |
| [[Hydroxyurea (drug)]] 0.5 µM |  | -4.8 | -0.48 |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -0.35 |
| [[venetoclax (drug)]] 5 µM |  | -4.2 | -0.44 |
| [[Fluvoxamine (drug)]] 0.5 µM |  | -4.2 | -0.40 |
| [[Cobimetinib (drug)]] 0.5 µM |  | -3.9 | -0.39 |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | -3.8 | -0.49 |
| [[Amsacrine (drug)]] 5 µM |  | -3.7 | -0.25 |
| [[OTS514 (drug)]] 5 µM |  | -3.5 | -0.39 |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.5 | -0.32 |
| [[Procainamide (hydrochloride) (drug)]] 0.5 µM |  | -3.5 | -0.34 |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.5 | -0.36 |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -3.4 | -0.35 |
| [[Clofarabine (drug)]] 0.5 µM |  | -3.3 | -0.32 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Amsacrine (drug)]] 5 µM (2.38); [[Amsacrine (drug)]] 0.5 µM (2.21); [[Medroxyprogesterone acetate (drug)]] 5 µM (2.09); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM (2.00, ⚠ cell-cycle shift); [[Citalopram (hydrobromide) (drug)]] 0.05 µM (1.99); [[Phenylephrine (hydrochloride) (drug)]] 5 µM (1.96); [[Triamcinolone (drug)]] 0.05 µM (1.94); [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM (1.93); [[Econazole (drug)]] 5 µM (1.92)
- Weakest: [[Allantoin (drug)]] 0.05 µM (-0.267, ⚠ transcription drop); [[Citalopram (hydrobromide) (drug)]] 0.5 µM (0.142); [[Orlistat (drug)]] 0.05 µM (0.281); [[Hydroxyurea (drug)]] 0.05 µM (0.289); [[Auranofin (drug)]] 5 µM (0.333); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM (0.353); [[Vilanterol (drug)]] 0.05 µM (0.419); [[Auranofin (drug)]] 0.5 µM (0.443); [[Verteporfin (drug)]] 0.5 µM (0.449)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 0): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[SLC26A2]] (23, 2 ⚠), [[ATP1A1]] (23, 3 ⚠), [[FKBP5]] (23, 4 ⚠), [[PACSIN2]] (19), [[FGD4]] (19), [[STOM]] (19), [[SLC45A4]] (18), [[ABHD2]] (18), [[ABLIM2]] (16), [[DIP2C]] (16, 1 ⚠), [[SCD]] (14), [[ACSL1]] (14, 4 ⚠), [[ENSG00000286153]] (13)
- down: [[WNT7B]] (32, 8 ⚠), [[ARHGAP26]] (29, 17 ⚠), [[CMPK2]] (27, 6 ⚠), [[RIGI]] (25, 6 ⚠), [[MX1]] (25, 7 ⚠), [[MAP7]] (23, 6 ⚠), [[PARP9]] (23, 8 ⚠), [[SYNJ2]] (21, 1 ⚠), [[LTBP4]] (21, 4 ⚠), [[ENSG00000259354]] (21, 8 ⚠), [[IFIT3]] (20, 3 ⚠), [[EIF2AK2]] (20, 4 ⚠), [[HMGA2]] (19), [[ITGB5]] (19, 2 ⚠), [[NAV3]] (18)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[KRT81]] (+7.5), [[RHCG]] (+6.8), [[KIRREL3]] (+6.6), [[ST6GAL2]] (+6.5), [[FYB1]] (+6.4), [[AKR1C2]] (+6.2), [[CXCL5]] (+6.1), [[RSPO3]] (+6.1), [[CYP24A1]] (+6.0), [[PAPPA]] (+6.0), [[AADACP1]] (+6.0), [[NTRK3]] (+5.9), [[CA12]] (+5.8), [[IGSF1]] (+5.8), [[ALDH1A1]] (+5.7) (1,064 genes, 54 with an alert ⚠; shown: the 15 strongest)
- Lacks: [[TXNIP]] (-3.7), [[TRPS1]] (-3.7), [[PRDX2]] (-3.6), [[HDAC9]] (-3.5), [[ZNF91]] (-3.5), [[ZNF83]] (-3.2), [[PARP8]] (-3.2), [[ZNF736]] (-3.1), [[PCDH7]] (-3.1), [[OXCT1]] (-3.0), [[EPIC1]] (-2.9), [[ENSG00000290199]] (-2.8, ⚠ noise-class RNA), [[CDKN2A]] (-2.8), [[MCTP2]] (-2.8), [[ZNF808]] (-2.7), [[ZNF345]] (-2.6) (110 genes, 3 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 0): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.755 to 1.36).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 8 in all, 8 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 55 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[CDKN2B]] | CDKN2B loss of function (13 lines) vs not recorded (37) | 4 / 2 / 0 | B 3, C 3; 6 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[SMARCA4]] | SMARCA4 altered (any record) (12 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[SMARCA4]] | SMARCA4 loss of function (10 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[STK11]] | STK11 loss of function (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[ZFHX3]] | ZFHX3 altered (any record) (13 lines) vs not recorded (37) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B, PIK3CA |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,759 in all, 1,759 with an alert ⚠; shown: the 15 strongest; 1,744 more line sets (1,744 of them with an alert ⚠) not shown; 1,787 genes; 1,490 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[TMPRSS4]], [[OVOL1]] | 33 vs 17 | 14 / 223 / 24 | B 115, C 146; 261 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[IRF6]], [[C1orf116]] | 31 vs 19 | 18 / 216 / 24 | B 128, C 130; 258 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ST14]] | 32 vs 18 | 11 / 196 / 21 | B 88, C 140; 228 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TMPRSS2]] | 35 vs 15 | 6 / 197 / 18 | B 77, C 144; 221 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TMEM45B]] | 32 vs 18 | 3 / 199 / 12 | B 58, C 156; 214 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SLC44A4]] | 37 vs 13 | 9 / 186 / 9 | B 57, C 147; 204 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[EPS8L3]] | 35 vs 15 | 0 / 196 / 1 | B 46, C 151; 197 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CLIC5]] | 37 vs 13 | 4 / 185 / 7 | B 59, C 137; 196 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ARHGEF38]] | 36 vs 14 | 5 / 172 / 9 | B 49, C 137; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01559]] | 38 vs 12 | 0 / 182 / 0 | B 36, C 146; 182 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ITGB6]] | 32 vs 18 | 5 / 148 / 18 | B 47, C 124; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TJP3]] | 29 vs 21 | 7 / 155 / 9 | B 61, C 110; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ADGRF1]] | 35 vs 15 | 14 / 138 / 16 | B 64, C 104; 168 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[C6orf132]] | 27 vs 23 | 3 / 151 / 2 | B 41, C 115; 156 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC03040]] | 31 vs 19 | 3 / 147 / 4 | B 38, C 116; 154 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 0; `tables/line_effects.parquet` — line == 0
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 0; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 0]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include A549

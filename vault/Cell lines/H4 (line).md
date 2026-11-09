---
cell_line: "H4"
type: "cell line"
cell_line_id: "CVCL_1239"
depmap_id: "ACH-000389"
organ: "CNS/Brain"
tp53_status: "wild type"
drivers: ["CDKN2A(Deletion)", "CDKN2B(Deletion)", "PTEN(Deletion)", "TERT(Promoter)"]
n_dd_depleted: 47
median_response: 1.096
tags: ["cell-line", "organ/cns_brain"]
generated_by: "tahoemap"
---

# H4

*CNS/Brain · TP53 wild type · CVCL_1239 · ACH-000389*

|  |  |
|---|---|
| Organ | CNS/Brain |
| TP53 status | wild type |
| Drivers | CDKN2A(Deletion); CDKN2B(Deletion); PTEN(Deletion); TERT(Promoter) |
| Driver changes | — |
| Cells over all wells | 1,041,998 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 1.10 (1 = a typical line) |
| Drug-doses that deplete it | 47 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 22 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 15,137 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 30): the line loses cells relative to the other lines in the same wells. Drug-doses: 49 in all, 27 with an alert ⚠; shown: the 12 strongest and the 10 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -15.0 | -2.97 |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -12.8 | -1.86 |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -9.7 | -1.71 |
| [[Peretinoin (drug)]] 0.5 µM |  | -8.4 | -1.54 |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.8 | -1.80 |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -7.8 | -1.37 |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -7.6 | -1.42 |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.5 | -1.04 |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -7.4 | -1.32 |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | -1.17 |
| [[Bimiralisib (drug)]] 5 µM |  | -6.3 | -1.12 |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.3 | -1.10 |
| [[GSK1059615 (drug)]] 5 µM |  | -5.7 | -1.04 |
| [[AT7519 (drug)]] 5 µM |  | -5.3 | -1.02 |
| [[DTP3 (drug)]] 5 µM |  | -5.2 | -1.11 |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | -5.0 | -0.89 |
| [[Alpelisib (drug)]] 5 µM |  | -4.8 | -0.98 |
| [[Peretinoin (drug)]] 5 µM |  | -4.7 | -0.87 |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.3 | -0.73 |
| [[Infigratinib (drug)]] 5 µM |  | -4.3 | -0.80 |
| [[Amsacrine (drug)]] 5 µM |  | -4.1 | -0.52 |
| [[Sonidegib (drug)]] 5 µM |  | -4.0 | -0.97 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[olaparib (drug)]] 0.05 µM (3.45, ⚠ unreliable plate only); [[Dexamethasone (drug)]] 0.05 µM (2.41); [[Econazole (drug)]] 5 µM (2.41); [[Dexamethasone (drug)]] 5 µM (2.32); [[Sonidegib (drug)]] 0.05 µM (2.30, ⚠ unreliable plate only); [[Budesonide (drug)]] 5 µM (2.30); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (2.27, ⚠ cell-cycle shift); [[Clobetasol propionate (drug)]] 5 µM (2.27); [[Triamcinolone (drug)]] 0.05 µM (2.23); [[Phenylephrine (hydrochloride) (drug)]] 5 µM (2.15); [[Triamcinolone (drug)]] 0.5 µM (2.10)
- Weakest: [[Tofacitinib (citrate) (drug)]] 0.05 µM (0.0261); [[Verteporfin (drug)]] 0.5 µM (0.176); [[Tofacitinib (drug)]] 0.5 µM (0.214); [[Tofacitinib (citrate) (drug)]] 5 µM (0.221); [[Tofacitinib (drug)]] 5 µM (0.239); [[Tazarotene (drug)]] 0.5 µM (0.294); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM (0.296); [[Lopinavir (drug)]] 5 µM (0.318)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 30): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[SLC7A2]] (20), [[DNER]] (19), [[HIPK2]] (18), [[TSC22D3]] (18), [[FKBP5]] (18, 3 ⚠), [[CPD]] (17), [[MBOAT2]] (16, 1 ⚠), [[PDZD2]] (15), [[ATP1A1]] (14, 1 ⚠), [[HSPA4]] (14, 7 ⚠), [[ACSL1]] (13, 4 ⚠), [[RB1CC1]] (12, 3 ⚠), [[PACSIN2]] (11), [[RBMS3]] (11), [[MED13]] (11, 1 ⚠)
- down: [[ITGA2]] (43, 8 ⚠), [[IGFBP3]] (37, 12 ⚠), [[MAST4]] (33, 10 ⚠), [[LUCAT1]] (30, 12 ⚠), [[MYLK]] (29, 6 ⚠), [[RFX8]] (29, 7 ⚠), [[PRSS23]] (26, 2 ⚠), [[FAM114A1]] (26, 16 ⚠), [[LOX]] (25, 9 ⚠), [[GPR173]] (25, 11 ⚠), [[NR2F2-AS1]] (25, 11 ⚠), [[ZMYND8]] (23, 8 ⚠), [[EXT1]] (22, 2 ⚠), [[SEMA3A]] (21, 2 ⚠), [[SMAD3]] (21, 3 ⚠), [[SYTL2]] (20, 1 ⚠), [[CXCL8]] (19, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[ANKRD20A8P]] (+7.7), [[ENSG00000287474]] (+7.7, ⚠ noise-class RNA), [[COL6A3]] (+7.3), [[ENSG00000291025]] (+7.3, ⚠ noise-class RNA), [[ENSG00000250038]] (+7.1, ⚠ noise-class RNA), [[UBBP4-1]] (+7.1), [[FAM95A]] (+7.0), [[ENSG00000287598]] (+6.9, ⚠ noise-class RNA), [[ENSG00000285822]] (+6.9, ⚠ noise-class RNA), [[LINC01411]] (+6.7), [[ENSG00000288098]] (+6.5, ⚠ noise-class RNA), [[SLC14A1]] (+6.5), [[TPTE]] (+6.4), [[LINC02476]] (+6.4), [[LINC02055]] (+6.4), [[LINC01029]] (+6.3), [[LINC01684]] (+6.3), [[ANKRD20A9P]] (+6.2), [[GLYATL2]] (+6.0), [[ANKRD20A7P]] (+6.0), [[AJAP1]] (+6.0) (1,563 genes, 161 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[PTEN]] (-3.5), [[TNFRSF10D]] (-3.4), [[H1-0]] (-3.4, ⚠ noise-class RNA), [[CPNE8]] (-3.3), [[LRIF1]] (-3.3), [[MTAP]] (-3.2), [[KLHL9]] (-3.2), [[PRDX2]] (-3.2), [[MIPOL1]] (-3.2), [[ADGRG6]] (-3.2), [[MBP]] (-3.2), [[CDCP1]] (-3.2), [[ANGPTL4]] (-3.1), [[ZNF544]] (-3.1), [[RANBP17]] (-3.1), [[ATAD1]] (-3.0) (159 genes, 6 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 30): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.771 to 1.36).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 6 in all, 6 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 58 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[CDKN2B]] | CDKN2B loss of function (13 lines) vs not recorded (37) | 4 / 2 / 0 | B 3, C 3; 6 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[TERT]] | TERT gain of function (8 lines) vs not recorded (39) | 5 / 0 / 0 | C 5; 5 with an alert ⚠ | ⚠ tissue-confounded; across organs; TERT not expressed in 1 of the 8 altered lines |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[PTEN]] | PTEN loss of function (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; PTEN not expressed in 4 of the 9 altered lines |
| [[TERT]] | TERT altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; TERT not expressed in 2 of the 11 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,472 in all, 1,472 with an alert ⚠; shown: the 15 strongest; 1,457 more line sets (1,457 of them with an alert ⚠) not shown; 1,494 genes; 1,281 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 30; `tables/line_effects.parquet` — line == 30
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 30; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 30]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include H4

---
cell_line: "A498"
type: "cell line"
cell_line_id: "CVCL_1056"
depmap_id: "ACH-000555"
organ: "Kidney"
tp53_status: "wild type"
drivers: ["APC(Missense)", "CDKN2A(Deletion)", "CDKN2B(Deletion)", "PIK3CB(Missense)", "SMARCA4(Missense)", "VHL(Frameshift)"]
n_dd_depleted: 26
median_response: 0.945
tags: ["cell-line", "organ/kidney"]
generated_by: "tahoemap"
---

# A498

*Kidney · TP53 wild type · CVCL_1056 · ACH-000555*

|  |  |
|---|---|
| Organ | Kidney |
| TP53 status | wild type |
| Drivers | APC(Missense); CDKN2A(Deletion); CDKN2B(Deletion); PIK3CB(Missense); SMARCA4(Missense); VHL(Frameshift) |
| Driver changes | APC p.C1270R; PIK3CB p.D1067V; SMARCA4 p.A923P; VHL p.G144fs |
| Cells over all wells | 2,737,641 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.945 (1 = a typical line) |
| Drug-doses that deplete it | 26 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 19 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,575 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 24): the line loses cells relative to the other lines in the same wells. Drug-doses: 27 in all, 8 with an alert ⚠; shown: the 12 strongest and the 4 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.4 | -1.04 |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.8 | -1.33 |
| [[Abemaciclib (drug)]] 5 µM |  | -5.0 | -0.99 |
| [[Penfluridol (drug)]] 0.5 µM |  | -4.7 | -0.92 |
| [[Fluvoxamine (drug)]] 0.5 µM |  | -4.4 | -0.84 |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -0.82 |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | -0.91 |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | -4.2 | -0.82 |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.2 | -0.83 |
| [[Pemetrexed (drug)]] 0.5 µM |  | -4.0 | -0.78 |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -3.9 | -0.76 |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.9 | -0.80 |
| [[Ixazomib (drug)]] 0.05 µM |  | -3.8 | -0.76 |
| [[Hydroxyurea (drug)]] 0.5 µM |  | -3.7 | -0.73 |
| [[Ferulic acid (drug)]] 0.5 µM |  | -3.6 | -0.70 |
| [[Vismodegib (drug)]] 5 µM |  | -3.5 | -0.67 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Amsacrine (drug)]] 5 µM (1.89); [[Flumatinib (mesylate) (drug)]] 0.5 µM (1.65); [[Econazole (drug)]] 5 µM (1.65); [[Dexamethasone (drug)]] 0.05 µM (1.64); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM (1.63, ⚠ cell-cycle shift); [[Amsacrine (drug)]] 0.5 µM (1.61); [[Pimitespib (drug)]] 0.05 µM (1.60); [[Diphenhydramine (drug)]] 5 µM (1.60); [[Menadione (drug)]] 5 µM (1.58)
- Weakest: [[Allantoin (drug)]] 0.05 µM (0.0759, ⚠ transcription drop); [[Pimozide (drug)]] 0.5 µM (0.105, ⚠ transcription drop); [[Roxadustat (drug)]] 0.05 µM (0.151); [[Saquinavir (drug)]] 0.05 µM (0.278); [[Drospirenone (drug)]] 0.5 µM (0.332); [[Saquinavir (drug)]] 5 µM (0.345); [[Roxadustat (drug)]] 5 µM (0.346); [[Orlistat (drug)]] 0.05 µM (0.347); [[Pemetrexed (drug)]] 0.5 µM (0.364); [[Glycyrrhizic acid (drug)]] 0.05 µM (0.371)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 24): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[HIPK2]] (31, 5 ⚠), [[BIRC3]] (30, 2 ⚠), [[FKBP5]] (29, 7 ⚠), [[PPM1L]] (25), [[ZFAND5]] (24), [[IL6ST]] (24, 2 ⚠), [[TSC22D3]] (23), [[TOP1]] (23, 2 ⚠), [[CPD]] (20), [[ACSL1]] (20, 3 ⚠), [[FGD4]] (19), [[MT1X]] (19), [[KLF9]] (19, 1 ⚠)
- down: [[IGFBP3]] (27, 3 ⚠), [[SLC1A1]] (23, 11 ⚠), [[GBP4]] (21, 5 ⚠), [[OAS2]] (21, 6 ⚠), [[IFI44L]] (21, 6 ⚠), [[MX1]] (21, 6 ⚠), [[MINDY2]] (20, 9 ⚠), [[ETV6]] (20, 9 ⚠), [[FRMD5]] (19, 2 ⚠), [[CADM1]] (19, 2 ⚠), [[IFITM1]] (19, 2 ⚠), [[TRIM22]] (19, 5 ⚠), [[FAM107B]] (19, 7 ⚠), [[MRPS6]] (18), [[ENSG00000259354]] (18), [[SLC5A3]] (16), [[BARX2]] (16, 1 ⚠), [[CD82]] (16, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[VCAM1]] (+7.7), [[CCL2]] (+7.1), [[AKR1B10]] (+6.7), [[LINC01508]] (+6.5), [[PREX2]] (+6.5), [[XIST]] (+6.4), [[SPP1]] (+6.3), [[ITIH5]] (+6.0), [[RHEX]] (+5.9), [[MSR1]] (+5.9), [[TNFAIP6]] (+5.8), [[PTH2R]] (+5.7), [[CP]] (+5.6), [[SLC4A4]] (+5.6), [[APBB1IP]] (+5.5) (1,711 genes, 87 with an alert ⚠; shown: the 15 strongest)
- Lacks: [[ZNF655]] (-3.8), [[H1-0]] (-3.7, ⚠ noise-class RNA), [[ZNF160]] (-3.7), [[CRADD]] (-3.7), [[ENSG00000214265]] (-3.7, ⚠ noise-class RNA), [[RANBP17]] (-3.6), [[GSTP1]] (-3.6), [[NNT]] (-3.4), [[OXCT1]] (-3.4), [[MYEF2]] (-3.3), [[ZNF714]] (-3.3), [[RIN3]] (-3.3), [[SNRPN]] (-3.2), [[CD9]] (-3.2), [[CXADR]] (-3.2), [[ZNF431]] (-3.2), [[MID2]] (-3.2) (162 genes, 5 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 24): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.895 to 1.49).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 7 in all, 7 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 57 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[APC]] | APC altered (any record) (10 lines) vs not recorded (40) | 7 / 0 / 0 | C 7; 7 with an alert ⚠ | ⚠ tissue-confounded; across organs; mechanism partly not recorded |
| [[CDKN2B]] | CDKN2B loss of function (13 lines) vs not recorded (37) | 4 / 2 / 0 | B 3, C 3; 6 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[APC]] | APC loss of function (7 lines) vs not recorded (40) | 5 / 0 / 0 | C 5; 5 with an alert ⚠ | ⚠ tissue-confounded; across organs |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[SMARCA4]] | SMARCA4 altered (any record) (12 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[SMARCA4]] | SMARCA4 loss of function (10 lines) vs not recorded (38) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,985 in all, 1,985 with an alert ⚠; shown: the 15 strongest; 1,970 more line sets (1,970 of them with an alert ⚠) not shown; 2,022 genes; 1,683 of the sets gave arrows. Ranked by the number of arrows.*

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
| [[B3GNT3]] | 31 vs 19 | 6 / 174 / 6 | B 72, C 114; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GCNT3]] | 38 vs 12 | 2 / 184 / 0 | B 43, C 143; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01559]] | 38 vs 12 | 0 / 182 / 0 | B 36, C 146; 182 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TOX3]] | 31 vs 19 | 4 / 168 / 1 | B 46, C 127; 173 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TC2N]] | 28 vs 22 | 3 / 163 / 5 | B 52, C 119; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TJP3]] | 29 vs 21 | 7 / 155 / 9 | B 61, C 110; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 24; `tables/line_effects.parquet` — line == 24
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 24; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 24]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include A498

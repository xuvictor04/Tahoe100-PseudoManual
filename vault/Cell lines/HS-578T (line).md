---
cell_line: "HS-578T"
type: "cell line"
cell_line_id: "CVCL_0332"
depmap_id: "ACH-000148"
organ: "Breast"
tp53_status: "altered"
drivers: ["CDKN2A(Deletion)", "HNF1A(Missense)", "HRAS(Missense)", "NF1(Missense)", "PIK3R1(Missense)", "TP53(Missense)"]
n_dd_depleted: 19
median_response: 1.008
tags: ["cell-line", "organ/breast"]
generated_by: "tahoemap"
---

# HS-578T

*Breast · TP53 altered · CVCL_0332 · ACH-000148*

|  |  |
|---|---|
| Organ | Breast |
| TP53 status | altered |
| Drivers | CDKN2A(Deletion); HNF1A(Missense); HRAS(Missense); NF1(Missense); PIK3R1(Missense); TP53(Missense) |
| Driver changes | HNF1A p.K273E; HRAS p.G12D; NF1 p.G2724R; PIK3R1 p.89_90insN; TP53 p.V157F |
| Cells over all wells | 1,725,207 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 1.01 (1 = a typical line) |
| Drug-doses that deplete it | 19 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 13 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,627 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 11): the line loses cells relative to the other lines in the same wells. Drug-doses: 20 in all, 7 with an alert ⚠; shown: the 12 strongest and the 5 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.8 | -1.10 |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | -1.02 |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -0.93 |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.1 | -1.06 |
| [[Peretinoin (drug)]] 0.5 µM |  | -4.9 | -0.83 |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.8 | -0.82 |
| [[Pemetrexed (drug)]] 0.5 µM |  | -4.1 | -0.69 |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -4.0 | -0.69 |
| [[Ferulic acid (drug)]] 0.5 µM |  | -4.0 | -0.69 |
| [[Fluvoxamine (drug)]] 0.5 µM |  | -3.7 | -0.61 |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.5 | -0.61 |
| [[Hydroxyurea (drug)]] 0.5 µM |  | -3.4 | -0.57 |
| [[Mozavaptan (drug)]] 0.5 µM |  | -3.3 | -0.55 |
| [[Vismodegib (drug)]] 5 µM |  | -3.2 | -0.53 |
| [[Dihydroartemisinin (drug)]] 5 µM |  | -3.1 | -0.52 |
| [[PH-797804 (drug)]] 5 µM |  | -3.1 | -0.53 |
| [[Penfluridol (drug)]] 0.5 µM |  | -3.0 | -0.52 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM (1.96, ⚠ unreliable plate only); [[Econazole (drug)]] 5 µM (1.96); [[Triamcinolone (drug)]] 0.05 µM (1.96); [[olaparib (drug)]] 0.05 µM (1.94, ⚠ unreliable plate only); [[Citalopram (hydrobromide) (drug)]] 0.05 µM (1.92); [[Sonidegib (drug)]] 0.05 µM (1.89, ⚠ unreliable plate only); [[Budesonide (drug)]] 5 µM (1.83); [[Triamcinolone (drug)]] 0.5 µM (1.83); [[Betamethasone dipropionate (drug)]] 0.05 µM (1.83); [[Phenylephrine (hydrochloride) (drug)]] 5 µM (1.83); [[Dexamethasone (drug)]] 0.05 µM (1.82)
- Weakest: [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM (0.219); [[Carbamazepine (drug)]] 0.5 µM (0.247); [[Roxadustat (drug)]] 0.05 µM (0.328); [[Monocrotaline (drug)]] 0.05 µM (0.339); [[Elagolix sodium (drug)]] 0.5 µM (0.408); [[Finasteride (drug)]] 5 µM (0.409); [[Pimozide (drug)]] 0.05 µM (0.427); [[Pimozide (drug)]] 0.5 µM (0.433, ⚠ transcription drop); [[18β-Glycyrrhetinic acid (drug)]] 5 µM (0.434)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 11): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[BIRC3]] (30, 2 ⚠), [[PPM1L]] (25), [[TOP1]] (25, 2 ⚠), [[HIPK2]] (24), [[PID1]] (20), [[KLF9]] (20, 2 ⚠), [[FKBP5]] (20, 3 ⚠), [[IL1R1]] (20, 4 ⚠), [[ENSG00000285744]] (20, 4 ⚠), [[TGFBR3]] (19), [[DNER]] (19), [[DCLK1]] (18), [[TSC22D3]] (18), [[TBC1D8]] (18), [[SLC7A2]] (17)
- down: [[MRPS6]] (39, 10 ⚠), [[CLMP]] (27, 7 ⚠), [[ENSG00000259753]] (26, 12 ⚠), [[SLC5A3]] (25, 9 ⚠), [[GPR173]] (25, 12 ⚠), [[PDE10A]] (24, 10 ⚠), [[IGFBP3]] (23, 7 ⚠), [[STC1]] (23, 8 ⚠), [[GDNF]] (23, 11 ⚠), [[ZNF395]] (22, 10 ⚠), [[ITGB3]] (21, 8 ⚠), [[ITGA2]] (20, 4 ⚠), [[DNAAF9]] (20, 13 ⚠), [[HMGA2]] (19, 2 ⚠), [[OAS2]] (19, 5 ⚠), [[IL33]] (18, 2 ⚠), [[SYNJ2]] (17), [[PTGS2]] (17, 1 ⚠), [[ITGB5]] (15)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[NKAIN3]] (+7.7), [[COL6A3]] (+7.6), [[POSTN]] (+7.6), [[COL1A2]] (+7.4), [[ENSG00000249174]] (+7.2, ⚠ noise-class RNA), [[COL1A1]] (+7.2), [[CARMN]] (+7.1), [[SPARC]] (+6.7), [[LINC01060]] (+6.7), [[LINC02476]] (+6.5), [[THY1]] (+6.4), [[COL3A1]] (+6.4), [[TIMP3]] (+6.3), [[LINC00879]] (+6.3), [[ENSG00000280241]] (+6.1, ⚠ noise-class RNA), [[ADAM12]] (+6.1), [[ITGA11]] (+6.0) (1,293 genes, 99 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[CDCP1]] (-3.3), [[ADGRG6]] (-3.3), [[ALDOC]] (-3.3), [[PRKCZ]] (-3.3), [[MBP]] (-3.2), [[IRS2]] (-3.2), [[SLC25A33]] (-3.1), [[PPP1R9A]] (-3.1), [[ZNF516]] (-3.1), [[MID2]] (-3.1), [[TGFA]] (-3.0), [[CXADR]] (-3.0), [[NEO1]] (-3.0), [[INSR]] (-2.9), [[SEZ6L2]] (-2.9) (207 genes, 3 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 11): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.895 to 1.47).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 6 in all, 6 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 57 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[HNF1A]] | HNF1A loss of function (6 lines) vs not recorded (44) | 1 / 0 / 0 | C 1; 1 with an alert ⚠ | ⚠ tissue-confounded; across organs |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[NF1]] | NF1 altered (any record) (7 lines) vs not recorded (43) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with B2M |
| [[PIK3R1]] | PIK3R1 altered (any record) (5 lines) vs not recorded (45) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; PIK3R1 not expressed in 1 of the 5 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,952 in all, 1,952 with an alert ⚠; shown: the 15 strongest; 1,937 more line sets (1,937 of them with an alert ⚠) not shown; 1,983 genes; 1,681 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 11; `tables/line_effects.parquet` — line == 11
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 11; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 11]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include HS-578T

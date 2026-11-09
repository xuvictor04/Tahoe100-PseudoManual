---
cell_line: "J82"
type: "cell line"
cell_line_id: "CVCL_0359"
depmap_id: "ACH-000396"
organ: "Bladder/Urinary Tract"
tp53_status: "altered"
drivers: ["APC(Missense)", "ERBB2(Missense)", "FGFR3(Missense)", "PIK3CA(Missense)", "PTEN(Frameshift)", "RB1(Splice_site)", "TERT(Promoter)", "TP53(Missense)"]
n_dd_depleted: 22
median_response: 0.911
tags: ["cell-line", "organ/bladder_urinary-tract"]
generated_by: "tahoemap"
---

# J82

*Bladder/Urinary Tract · TP53 altered · CVCL_0359 · ACH-000396*

|  |  |
|---|---|
| Organ | Bladder/Urinary Tract |
| TP53 status | altered |
| Drivers | APC(Missense); ERBB2(Missense); FGFR3(Missense); PIK3CA(Missense); PTEN(Frameshift); RB1(Splice_site); TERT(Promoter); TP53(Missense) |
| Driver changes | APC p.S770P; ERBB2 p.R678Q; FGFR3 p.K651E; PIK3CA p.P124L; PTEN p.N212fs; TP53 p.E271K; TP53 p.K320N |
| Cells over all wells | 2,342,899 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.911 (1 = a typical line) |
| Drug-doses that deplete it | 22 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 17 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,687 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 13): the line loses cells relative to the other lines in the same wells. Drug-doses: 22 in all, 5 with an alert ⚠; shown: the 12 strongest and the 5 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -1.05 |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.3 | -1.11 |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -0.68 |
| [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -0.80 |
| [[Torkinib (drug)]] 5 µM | ⚠ toxic | -4.2 | -0.85 |
| [[Terfenadine (drug)]] 0.5 µM |  | -4.1 | -0.77 |
| [[Ixazomib (drug)]] 0.05 µM |  | -4.1 | -0.80 |
| [[PH-797804 (drug)]] 5 µM |  | -4.0 | -0.75 |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.8 | -0.77 |
| [[BAY1125976 (drug)]] 5 µM |  | -3.8 | -0.70 |
| [[EX229 (drug)]] 0.05 µM |  | -3.6 | -0.70 |
| [[Fluvoxamine (drug)]] 0.5 µM |  | -3.5 | -0.65 |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -3.4 | -0.66 |
| [[Aliskiren (drug)]] 0.5 µM |  | -3.4 | -0.64 |
| [[BI-78D3 (drug)]] 5 µM |  | -3.4 | -0.64 |
| [[Celecoxib (drug)]] 0.05 µM |  | -3.2 | -0.62 |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -0.60 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[olaparib (drug)]] 0.05 µM (2.08, ⚠ unreliable plate only); [[LJI308 (drug)]] 0.05 µM (1.65); [[Sonidegib (drug)]] 0.05 µM (1.62, ⚠ unreliable plate only); [[Citalopram (hydrobromide) (drug)]] 0.5 µM (1.49); [[Pimozide (drug)]] 5 µM (1.43); [[Belinostat (drug)]] 0.05 µM (1.38); [[Fluvoxamine (drug)]] 0.5 µM (1.38); [[Lopinavir (drug)]] 5 µM (1.38); [[Entecavir (monohydrate) (drug)]] 0.5 µM (1.37); [[Sulfatinib (drug)]] 5 µM (1.32)
- Weakest: [[Allantoin (drug)]] 0.05 µM (-0.218, ⚠ transcription drop); [[palbociclib (drug)]] 0.5 µM (0.0909, ⚠ cell-cycle shift); [[palbociclib (drug)]] 5 µM (0.216); [[Neratinib (drug)]] 0.05 µM (0.224); [[Vortioxetine (drug)]] 5 µM (0.279, ⚠ toxic); [[Almonertinib (hydrochloride) (drug)]] 5 µM (0.287); [[18β-Glycyrrhetinic acid (drug)]] 5 µM (0.362); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM (0.381); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM (0.385); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM (0.418); [[Pyridoxine (drug)]] 0.5 µM (0.431)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 13): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[FKBP5]] (22, 6 ⚠), [[ADAMTS9]] (17), [[ENSG00000285744]] (15, 2 ⚠), [[PMAIP1]] (15, 7 ⚠), [[ARHGAP26]] (14, 3 ⚠), [[PEG10]] (14, 5 ⚠), [[CPEB4]] (13, 1 ⚠), [[ARL15]] (13, 4 ⚠), [[ALCAM]] (13, 6 ⚠), [[HELLS]] (13, 9 ⚠), [[TBC1D8]] (12), [[DAAM1]] (12, 1 ⚠), [[BIRC3]] (12, 3 ⚠), [[PALLD]] (11, 1 ⚠), [[SORBS1]] (10), [[EIF5]] (10, 1 ⚠), [[PLA2G4C]] (10, 1 ⚠)
- down: [[SIPA1L3]] (27, 14 ⚠), [[NAV1]] (24, 13 ⚠), [[DNAAF9]] (22, 12 ⚠), [[FLNB]] (21, 6 ⚠), [[ZMYND8]] (20, 10 ⚠), [[ENSG00000251314]] (20, 13 ⚠), [[BCKDHB]] (19, 7 ⚠), [[GBE1]] (19, 10 ⚠), [[ITGA2]] (18, 4 ⚠), [[NR2F2-AS1]] (18, 9 ⚠), [[TEX41]] (18, 10 ⚠), [[ZFYVE9]] (18, 13 ⚠), [[PODXL]] (17, 3 ⚠), [[CDCP1]] (17, 5 ⚠), [[ELK3]] (16, 2 ⚠), [[AFAP1L1]] (16, 3 ⚠), [[RHBDF2]] (16, 5 ⚠), [[SERPINB6]] (14, 3 ⚠), [[CD44]] (13, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[PHACTR1]] (+7.0), [[NPPB]] (+6.5), [[PSG9]] (+6.3), [[POSTN]] (+6.3), [[OLR1]] (+6.3), [[TEX41]] (+6.3), [[SULF1]] (+6.0), [[LCP1]] (+5.9), [[PSG1]] (+5.9), [[CCBE1]] (+5.8), [[ENSG00000254337]] (+5.8, ⚠ noise-class RNA), [[ANO4]] (+5.7), [[ZNF732]] (+5.6), [[PSG5]] (+5.6), [[VGLL3]] (+5.5), [[COL5A1]] (+5.5) (1,319 genes, 86 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[CPNE8]] (-3.8), [[STARD4]] (-3.4), [[NF2]] (-3.4), [[ZDBF2]] (-3.4), [[DUXAP10]] (-3.4), [[FKBP10]] (-3.4), [[OAT]] (-3.4), [[COMT]] (-3.3), [[ALDH7A1]] (-3.2), [[MICU3]] (-3.1), [[RNF144A]] (-3.1), [[TCEAL9]] (-3.0), [[DUXAP9]] (-3.0), [[RPS6KA2]] (-3.0), [[APBA2]] (-2.9) (149 genes, 6 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 13): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.777 to 1.45).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 9 in all, 9 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 53 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[APC]] | APC altered (any record) (10 lines) vs not recorded (40) | 7 / 0 / 0 | C 7; 7 with an alert ⚠ | ⚠ tissue-confounded; across organs; mechanism partly not recorded |
| [[TERT]] | TERT gain of function (8 lines) vs not recorded (39) | 5 / 0 / 0 | C 5; 5 with an alert ⚠ | ⚠ tissue-confounded; across organs; TERT not expressed in 1 of the 8 altered lines |
| [[RB1]] | RB1 loss of function (3 lines) vs not recorded (46) | 2 / 1 / 0 | C 3; 3 with an alert ⚠ | ⚠ few lines (3 vs 46); tissue-confounded; across organs |
| [[RB1]] | RB1 altered (any record) (4 lines) vs not recorded (46) | 2 / 0 / 0 | C 2; 2 with an alert ⚠ | ⚠ few lines (4 vs 46); tissue-confounded; across organs; mechanism partly not recorded |
| [[ERBB2]] | ERBB2 gain of function (3 lines) vs not recorded (47) | 0 / 0 / 0 | — | ⚠ few lines (3 vs 47); tissue-confounded; across organs |
| [[PIK3CA]] | PIK3CA altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3 |
| [[PTEN]] | PTEN loss of function (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; PTEN not expressed in 4 of the 9 altered lines |
| [[TERT]] | TERT altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; TERT not expressed in 2 of the 11 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,907 in all, 1,907 with an alert ⚠; shown: the 15 strongest; 1,892 more line sets (1,892 of them with an alert ⚠) not shown; 1,934 genes; 1,630 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 13; `tables/line_effects.parquet` — line == 13
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 13; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 13]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include J82

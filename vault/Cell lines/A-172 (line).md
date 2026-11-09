---
cell_line: "A-172"
type: "cell line"
cell_line_id: "CVCL_0131"
depmap_id: "ACH-000558"
organ: "CNS/Brain"
tp53_status: "wild type"
drivers: ["ABL1(Fusion)", "CDKN2A(Deletion)", "CDKN2B(Deletion)", "PTEN(Deletion)", "RB1(Missense)"]
n_dd_depleted: 24
median_response: 0.975
tags: ["cell-line", "organ/cns_brain"]
generated_by: "tahoemap"
---

# A-172

*CNS/Brain · TP53 wild type · CVCL_0131 · ACH-000558*

|  |  |
|---|---|
| Organ | CNS/Brain |
| TP53 status | wild type |
| Drivers | ABL1(Fusion); CDKN2A(Deletion); CDKN2B(Deletion); PTEN(Deletion); RB1(Missense) |
| Driver changes | RB1 p.V852L |
| Cells over all wells | 2,314,002 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.975 (1 = a typical line) |
| Drug-doses that deplete it | 24 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 12 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,805 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 4): the line loses cells relative to the other lines in the same wells. Drug-doses: 24 in all, 12 with an alert ⚠; shown: the 12 strongest and the 8 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.6 | -0.91 |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | -0.84 |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.8 | -0.77 |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -6.7 | -0.77 |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.7 | -0.88 |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.3 | -0.72 |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.1 | -0.52 |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -0.63 |
| [[Aliskiren (drug)]] 0.5 µM |  | -5.4 | -0.60 |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -4.6 | -0.58 |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | -4.5 | -0.56 |
| [[Ixazomib (drug)]] 0.05 µM |  | -4.2 | -0.50 |
| [[Adenosine (drug)]] 5 µM |  | -4.1 | -0.33 |
| [[ERK5-IN-2 (drug)]] 0.5 µM |  | -3.9 | -0.46 |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.8 | -0.43 |
| [[olaparib (drug)]] 5 µM |  | -3.5 | -0.41 |
| [[Irinotecan (drug)]] 0.5 µM |  | -3.4 | -0.38 |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | -3.2 | -0.25 |
| [[Ixazomib (drug)]] 5 µM |  | -3.2 | -0.37 |
| [[PF-06260933 (drug)]] 5 µM |  | -3.1 | -0.37 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[olaparib (drug)]] 0.05 µM (2.24, ⚠ unreliable plate only); [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM (2.20, ⚠ cell-cycle shift); [[Sonidegib (drug)]] 0.05 µM (2.06, ⚠ unreliable plate only); [[Amsacrine (drug)]] 5 µM (1.84); [[Pitavastatin (Calcium) (drug)]] 0.05 µM (1.79); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (1.75); [[TAK-901 (drug)]] 0.05 µM (1.68); [[Homoharringtonine (drug)]] 0.05 µM (1.66); [[Malotilate (drug)]] 0.5 µM (1.61); [[Amsacrine (drug)]] 0.5 µM (1.61); [[Megestrol (drug)]] 5 µM (1.56)
- Weakest: [[Monocrotaline (drug)]] 0.05 µM (-0.0228); [[Allantoin (drug)]] 0.05 µM (0.00208, ⚠ transcription drop); [[Imiquimod (maleate) (drug)]] 0.5 µM (0.157); [[Menadione (drug)]] 5 µM (0.167); [[Finasteride (drug)]] 5 µM (0.276); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM (0.292); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM (0.329); [[Isocorydine (drug)]] 0.5 µM (0.330); [[RMC-6236 (drug)]] 0.05 µM (0.341)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 4): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[FKBP5]] (23, 7 ⚠), [[DNER]] (21, 4 ⚠), [[HSPA4]] (20, 12 ⚠), [[HIPK2]] (19), [[NEBL]] (19), [[SEMA3C]] (18, 5 ⚠), [[ZMYND8]] (17), [[PHLDB2]] (17, 4 ⚠), [[CREB5]] (17, 5 ⚠), [[TOP1]] (17, 7 ⚠), [[ATP6V1A]] (16, 2 ⚠), [[EPB41L2]] (16, 10 ⚠), [[TUSC3]] (14, 2 ⚠), [[SAA1]] (13), [[NIBAN1]] (13, 1 ⚠)
- down: [[MANCR]] (32, 11 ⚠), [[IFI44L]] (25, 6 ⚠), [[IFITM1]] (25, 6 ⚠), [[DGKG]] (24, 8 ⚠), [[MRPS6]] (24, 9 ⚠), [[PDGFB]] (24, 10 ⚠), [[DNAAF9]] (24, 14 ⚠), [[SERPINB6]] (23, 6 ⚠), [[ITGA2]] (22, 4 ⚠), [[ENSG00000260877]] (22, 4 ⚠), [[CHD1L]] (22, 7 ⚠), [[FAM114A1]] (22, 11 ⚠), [[OAS2]] (21, 5 ⚠), [[HIVEP3]] (20, 5 ⚠), [[NTSR1]] (18, 3 ⚠), [[NT5E]] (17, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[SUCNR1]] (+7.8), [[SPARC]] (+7.6), [[THBS2]] (+7.6), [[LINC01411]] (+7.4), [[COL3A1]] (+7.3), [[DIRAS3]] (+7.1), [[ENSG00000230258]] (+7.0, ⚠ noise-class RNA), [[PLAT]] (+6.5), [[COL5A1]] (+6.3), [[THY1]] (+6.3), [[LINC02476]] (+6.3), [[DKK3]] (+6.3), [[LOX]] (+6.3), [[ENSG00000224865]] (+6.3, ⚠ noise-class RNA), [[HS3ST3A1]] (+6.2), [[SOX11]] (+6.2), [[LRRC17]] (+6.2) (1,744 genes, 129 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[FUBP3]] (-3.7), [[TNFRSF10D]] (-3.6), [[ABCA5]] (-3.5), [[H1-0]] (-3.5, ⚠ noise-class RNA), [[MYO1B]] (-3.5), [[CDCP1]] (-3.4), [[RANBP17]] (-3.3), [[MBP]] (-3.3), [[TES]] (-3.3), [[PRDX2]] (-3.3), [[CPNE8]] (-3.3), [[MIPOL1]] (-3.3), [[MTAP]] (-3.2), [[PTER]] (-3.2), [[NFIA]] (-3.2), [[AHR]] (-3.2) (188 genes, 5 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 4): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.720 to 1.47).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 5 in all, 5 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 58 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[CDKN2B]] | CDKN2B loss of function (13 lines) vs not recorded (37) | 4 / 2 / 0 | B 3, C 3; 6 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[RB1]] | RB1 altered (any record) (4 lines) vs not recorded (46) | 2 / 0 / 0 | C 2; 2 with an alert ⚠ | ⚠ few lines (4 vs 46); tissue-confounded; across organs; mechanism partly not recorded |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[PTEN]] | PTEN loss of function (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; PTEN not expressed in 4 of the 9 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 1,771 in all, 1,771 with an alert ⚠; shown: the 15 strongest; 1,756 more line sets (1,756 of them with an alert ⚠) not shown; 1,797 genes; 1,532 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 4; `tables/line_effects.parquet` — line == 4
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 4; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 4]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include A-172

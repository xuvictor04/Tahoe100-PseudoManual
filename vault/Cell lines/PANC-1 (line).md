---
cell_line: "PANC-1"
type: "cell line"
cell_line_id: "CVCL_0480"
depmap_id: "ACH-000164"
organ: "Pancreas"
tp53_status: "altered"
drivers: ["AKT2(Gain)", "CDKN2A(Deletion)", "CDKN2B(Deletion)", "KRAS(Missense)", "TP53(Missense)"]
n_dd_depleted: 16
median_response: 0.955
tags: ["cell-line", "organ/pancreas"]
generated_by: "tahoemap"
---

# PANC-1

*Pancreas · TP53 altered · CVCL_0480 · ACH-000164*

|  |  |
|---|---|
| Organ | Pancreas |
| TP53 status | altered |
| Drivers | AKT2(Gain); CDKN2A(Deletion); CDKN2B(Deletion); KRAS(Missense); TP53(Missense) |
| Driver changes | KRAS p.G12D; TP53 p.R273H |
| Cells over all wells | 4,089,464 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.955 (1 = a typical line) |
| Drug-doses that deplete it | 16 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 12 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,270 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 20): the line loses cells relative to the other lines in the same wells. Drug-doses: 16 in all, 4 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | -6.0 | -0.77 |
| [[Pralsetinib (drug)]] 5 µM |  | -5.5 | -0.72 |
| [[Belumosudil (drug)]] 5 µM |  | -4.7 | -0.54 |
| [[AZD2858 (drug)]] 5 µM | ⚠ toxic | -4.3 | -0.57 |
| [[olaparib (drug)]] 5 µM |  | -4.1 | -0.50 |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -0.49 |
| [[Volasertib (drug)]] 5 µM |  | -3.9 | -0.49 |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.8 | -0.51 |
| [[vincristine (drug)]] 0.05 µM |  | -3.7 | -0.43 |
| [[Pemetrexed (drug)]] 0.5 µM |  | -3.6 | -0.40 |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -0.40 |
| [[Abemaciclib (drug)]] 5 µM |  | -3.4 | -0.39 |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.3 | -0.27 |
| [[Penfluridol (drug)]] 0.5 µM |  | -3.2 | -0.36 |
| [[Celecoxib (drug)]] 0.05 µM |  | -3.2 | -0.37 |
| [[ERK5-IN-2 (drug)]] 0.5 µM |  | -3.2 | -0.38 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Pentamidine (isethionate) (drug)]] 5 µM (1.79); [[Ouabain (Octahydrate) (drug)]] 0.05 µM (1.69, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (1.62, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (1.49, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (1.48, ⚠ cell-cycle shift); [[Chlorhexidine (diacetate) (drug)]] 5 µM (1.43); [[Decitabine (drug)]] 5 µM (1.41); [[Ouabain (Octahydrate) (drug)]] 5 µM (1.41, ⚠ cell-cycle shift); [[Bentamapimod (drug)]] 5 µM (1.39); [[XRK3F2 (drug)]] 5 µM (1.38); [[Ritonavir (drug)]] 5 µM (1.33); [[RMC-6236 (drug)]] 0.5 µM (1.32); [[BI-3406 (drug)]] 0.5 µM (1.32)
- Weakest: [[Roxadustat (drug)]] 0.05 µM (-0.0449); [[Hydroxyurea (drug)]] 0.05 µM (0.0295); [[Orlistat (drug)]] 0.05 µM (0.0411); [[Belumosudil (mesylate) (drug)]] 5 µM (0.123); [[Pimozide (drug)]] 0.5 µM (0.139, ⚠ transcription drop); [[Allantoin (drug)]] 0.05 µM (0.170, ⚠ transcription drop); [[Saquinavir (drug)]] 0.05 µM (0.270); [[Citalopram (hydrobromide) (drug)]] 0.5 µM (0.278); [[Oxaprozin (drug)]] 0.5 µM (0.282); [[Neratinib (drug)]] 0.5 µM (0.285)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 20): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[FKBP5]] (26, 9 ⚠), [[FGD4]] (24, 6 ⚠), [[CCND3]] (21, 1 ⚠), [[PSMD11]] (18, 6 ⚠), [[ATP6V1D]] (18, 7 ⚠), [[HSPA4]] (18, 9 ⚠), [[ATP6V1A]] (17, 2 ⚠), [[LARP4]] (17, 3 ⚠), [[UBE2H]] (17, 3 ⚠), [[SUPT6H]] (16, 2 ⚠), [[NEDD4L]] (16, 3 ⚠), [[SLMAP]] (16, 3 ⚠), [[NAA50]] (16, 6 ⚠), [[CPEB4]] (15, 1 ⚠), [[PIP5K1A]] (15, 1 ⚠), [[ATP6V0A1]] (14, 1 ⚠)
- down: [[SPRY4-AS1]] (39, 10 ⚠), [[DANT2]] (27, 11 ⚠), [[DHX32]] (27, 15 ⚠), [[ENSG00000260877]] (26, 1 ⚠), [[ZNF652]] (26, 9 ⚠), [[THSD4]] (25, 5 ⚠), [[NT5E]] (24, 1 ⚠), [[ETV1]] (24, 3 ⚠), [[ZMYND8]] (24, 7 ⚠), [[AFAP1]] (24, 9 ⚠), [[RNF220]] (23, 12 ⚠), [[BCAS3]] (23, 13 ⚠), [[CDCP1]] (20, 3 ⚠), [[FOSL1]] (19), [[ENSG00000230615]] (18, 2 ⚠), [[ITGB5]] (17)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[CARD18]] (+7.1), [[MEG8]] (+5.9), [[COL11A1]] (+5.9), [[ENSG00000291105]] (+5.8, ⚠ noise-class RNA), [[MEG3]] (+5.5), [[PPP1R14A]] (+5.3), [[DDX43]] (+5.2), [[CHD5]] (+5.2), [[DLL3]] (+5.1), [[LRFN5]] (+5.1), [[FBXO27]] (+5.0), [[ELOVL2]] (+4.9), [[CA8]] (+4.9), [[WT1]] (+4.8), [[ONECUT3]] (+4.8), [[ANKRD20A21P]] (+4.7) (1,167 genes, 64 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[TUSC3]] (-3.8), [[TMEM168]] (-3.7), [[RANBP17]] (-3.7), [[CNTLN]] (-3.6), [[SLC2A3]] (-3.3), [[AASS]] (-3.2), [[C1orf21]] (-3.2), [[COBLL1]] (-3.1), [[KIF13B]] (-3.1), [[SLC1A1]] (-3.1), [[LTBR]] (-3.1), [[APBA2]] (-3.0), [[DUSP4]] (-3.0), [[IFI16]] (-3.0), [[IFI44]] (-3.0) (229 genes, 6 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 20): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Strong here (> 1.5): component 42 (1.57; genes FHOD3, PMEPA1, LINC01505, CAPZB / STARD4, C4orf47, PRKCI, TCF4); component 24 (1.52; genes GOT1, YARS1, DDIT3, AARS1 / ASCC3, ADAM32, GPRC5D-AS1, LUC7L3); component 52 (1.51; genes CHST15, PHLDB2, TNS4, SNTB1 / SH3RF3, LTBP1, FUT8, NRG2)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 5 in all, 5 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 59 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[CDKN2B]] | CDKN2B loss of function (13 lines) vs not recorded (37) | 4 / 2 / 0 | B 3, C 3; 6 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,311 in all, 2,311 with an alert ⚠; shown: the 15 strongest; 2,296 more line sets (2,296 of them with an alert ⚠) not shown; 2,342 genes; 1,981 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 20; `tables/line_effects.parquet` — line == 20
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 20; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 20]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include PANC-1

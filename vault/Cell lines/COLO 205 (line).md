---
cell_line: "COLO 205"
type: "cell line"
cell_line_id: "CVCL_0218"
depmap_id: "ACH-001039"
organ: "Bowel"
tp53_status: "altered"
drivers: ["APC(Frameshift)", "BRAF(Missense)", "CTNNB1(Missense)", "GNAS(Missense)", "MTOR(Missense)", "PMS2(Missense)", "TP53(Frameshift)"]
n_dd_depleted: 30
median_response: 0.984
tags: ["cell-line", "organ/bowel"]
generated_by: "tahoemap"
---

# COLO 205

*Bowel · TP53 altered · CVCL_0218 · ACH-001039*

|  |  |
|---|---|
| Organ | Bowel |
| TP53 status | altered |
| Drivers | APC(Frameshift); BRAF(Missense); CTNNB1(Missense); GNAS(Missense); MTOR(Missense); PMS2(Missense); TP53(Frameshift) |
| Driver changes | APC p.T1556fs; BRAF p.V600E; CTNNB1 p.N287S; GNAS p.S95I; MTOR p.P1193L; PMS2 p.E504Q; TP53 p.Y103fs; TP53 p.Y107fs |
| Cells over all wells | 1,456,534 |
| Wells with usable expression | 1,326 (99.8%) |
| Median response strength (β) | 0.984 (1 = a typical line) |
| Drug-doses that deplete it | 30 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 21 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 13,995 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 7): the line loses cells relative to the other lines in the same wells. Drug-doses: 30 in all, 9 with an alert ⚠; shown: the 12 strongest and the 5 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.7 | -2.57 |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.6 | -2.80 |
| [[AT7519 (drug)]] 5 µM |  | -7.4 | -1.66 |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.2 | -2.38 |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -7.0 | -3.56 |
| [[Bimiralisib (drug)]] 5 µM |  | -6.9 | -1.44 |
| [[Ipatasertib (drug)]] 0.5 µM |  | -6.2 | -1.34 |
| [[GSK1059615 (drug)]] 5 µM |  | -5.4 | -1.12 |
| [[BAY1125976 (drug)]] 5 µM |  | -5.3 | -1.09 |
| [[venetoclax (drug)]] 5 µM |  | -5.3 | -1.23 |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -0.73 |
| [[Trametinib (drug)]] 0.5 µM |  | -4.9 | -0.72 |
| [[MK-3903 (drug)]] 5 µM |  | -4.8 | -1.07 |
| [[Capmatinib (drug)]] 5 µM |  | -4.3 | -0.98 |
| [[Binimetinib (drug)]] 5 µM |  | -4.0 | -0.63 |
| [[BAY1125976 (drug)]] 0.5 µM |  | -3.9 | -0.82 |
| [[Afatinib (drug)]] 5 µM |  | -3.8 | -0.55 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 486, 82 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Raltitrexed (drug)]] 5 µM (1.98, ⚠ cell-cycle shift); [[Bexarotene (drug)]] 0.05 µM (1.87); [[Monocrotaline (drug)]] 0.05 µM (1.81); [[Tofacitinib (citrate) (drug)]] 5 µM (1.78); [[palbociclib (drug)]] 0.5 µM (1.76, ⚠ cell-cycle shift); [[Tofacitinib (drug)]] 5 µM (1.75); [[Artesunate (drug)]] 5 µM (1.72, ⚠ cell-cycle shift); [[Bexarotene (drug)]] 0.5 µM (1.69); [[Saquinavir (drug)]] 0.5 µM (1.66); [[Berbamine (drug)]] 0.5 µM (1.65); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM (1.59)
- Weakest: [[Decitabine (drug)]] 0.05 µM (-0.215); [[Verteporfin (drug)]] 0.05 µM (-0.189); [[BI-3406 (drug)]] 5 µM (0.0415); [[Norepinephrine (hydrochloride) (drug)]] 5 µM (0.0982); [[Ranolazine (drug)]] 0.5 µM (0.103); [[Allantoin (drug)]] 5 µM (0.122); [[Econazole (drug)]] 5 µM (0.174); [[Triamcinolone (drug)]] 0.05 µM (0.215)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 7): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[DST]] (16, 6 ⚠), [[HSPA4]] (14, 8 ⚠), [[SCD]] (13), [[YWHAG]] (13, 2 ⚠), [[CLIP1]] (13, 3 ⚠), [[TXNRD1]] (13, 3 ⚠), [[MIR4435-2HG]] (12, 5 ⚠), [[G3BP1]] (12, 8 ⚠), [[GULP1]] (11, 3 ⚠), [[NUP58]] (11, 6 ⚠), [[RABEP1]] (10, 1 ⚠), [[ZFPM2-AS1]] (10, 1 ⚠), [[DAAM1]] (10, 2 ⚠), [[CD44]] (10, 5 ⚠), [[GPATCH2L]] (9), [[PSME4]] (9, 1 ⚠), [[ATP6V1A]] (8), [[ACSL3]] (8)
- down: [[HNF1A-AS1]] (31, 14 ⚠), [[LINC01091]] (23, 9 ⚠), [[STS]] (23, 10 ⚠), [[BMP4]] (22, 10 ⚠), [[PLCB1]] (21, 15 ⚠), [[CFB]] (20, 9 ⚠), [[LINC01876]] (20, 12 ⚠), [[ZMYND8]] (19, 8 ⚠), [[MEIS2]] (19, 8 ⚠), [[XDH]] (19, 8 ⚠), [[SNTB1]] (19, 8 ⚠), [[ATP10B]] (19, 13 ⚠), [[CMPK2]] (17, 3 ⚠), [[OAS2]] (16), [[EPSTI1]] (16, 3 ⚠), [[DDX60]] (15, 2 ⚠), [[OAS3]] (14), [[CASC19]] (14), [[TRIM22]] (14, 1 ⚠), [[PARP9]] (14, 1 ⚠), [[EIF2AK2]] (13, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[SMIM2-AS1]] (+8.2), [[LINC01559]] (+7.4), [[HCN1]] (+7.4), [[TMPRSS4]] (+7.1), [[LCN2]] (+7.1), [[ENSG00000266976]] (+6.9, ⚠ noise-class RNA), [[ENSG00000257831]] (+6.8, ⚠ noise-class RNA), [[LINC00540]] (+6.7), [[PADI1]] (+6.7), [[IGFL2-AS1]] (+6.6), [[DSCAML1]] (+6.5), [[PLA2G2A]] (+6.5), [[EPSTI1]] (+6.5), [[ENSG00000227400]] (+6.5, ⚠ noise-class RNA), [[IL20RA]] (+6.4), [[NPSR1-AS1]] (+6.4), [[HNF1A-AS1]] (+6.4), [[ARHGEF38]] (+6.3) (1,681 genes, 162 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[NR3C1]] (-3.9), [[VIM]] (-3.9), [[QKI]] (-3.8), [[SMAD4]] (-3.8), [[FERMT2]] (-3.6), [[UBE2E2]] (-3.6), [[OSMR-DT]] (-3.6), [[KIRREL1]] (-3.6), [[OSMR]] (-3.6), [[CPLANE1]] (-3.6), [[BNIP3]] (-3.6), [[CPNE8]] (-3.5), [[HLTF]] (-3.5), [[AKT3]] (-3.5), [[LDHB]] (-3.5) (435 genes, 7 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 7): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 42 (0.654; genes FHOD3, PMEPA1, LINC01505, CAPZB / STARD4, C4orf47, PRKCI, TCF4); component 13 (0.697; genes UGP2, KLF9, TSC22D3, SSBP2 / LUC7L3, PER3, TCP10L, SEMA3A)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 7 in all, 7 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 56 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[APC]] | APC altered (any record) (10 lines) vs not recorded (40) | 7 / 0 / 0 | C 7; 7 with an alert ⚠ | ⚠ tissue-confounded; across organs; mechanism partly not recorded |
| [[APC]] | APC loss of function (7 lines) vs not recorded (40) | 5 / 0 / 0 | C 5; 5 with an alert ⚠ | ⚠ tissue-confounded; across organs |
| [[BRAF]] | BRAF altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[BRAF]] | BRAF gain of function (7 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[CTNNB1]] | CTNNB1 altered (any record) (5 lines) vs not recorded (45) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[PMS2]] | PMS2 altered (any record) (4 lines) vs not recorded (46) | 0 / 0 / 0 | — | ⚠ few lines (4 vs 46); within organs, on part of the lines; mechanism partly not recorded |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,494 in all, 2,494 with an alert ⚠; shown: the 15 strongest; 2,479 more line sets (2,479 of them with an alert ⚠) not shown; 2,537 genes; 2,183 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[PBK]] | 4 vs 46 | 1 / 138 / 0 | C 139; 139 with an alert ⚠ | within organs | ⚠ few lines (4 vs 46); within organs, on part of the lines |
| [[CEACAM6]] | 37 vs 13 | 2 / 113 / 2 | B 27, C 90; 117 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[DAPP1]] | 39 vs 11 | 3 / 101 / 10 | B 37, C 77; 114 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SLC6A14]] | 39 vs 11 | 3 / 101 / 4 | B 29, C 79; 108 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SPOCK1]] | 29 vs 21 | 1 / 62 / 45 | B 58, C 50; 108 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[APCDD1L]] | 34 vs 16 | 2 / 99 / 0 | B 16, C 85; 101 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC4]] | 41 vs 9 | 1 / 93 / 4 | B 25, C 73; 98 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ITGA11]] | 34 vs 16 | 2 / 95 / 0 | B 19, C 78; 97 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01411]] | 38 vs 12 | 0 / 97 / 0 | B 13, C 84; 97 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PIMREG]] | 6 vs 44 | 3 / 94 / 0 | B 91, C 6; 97 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PDGFRB]] | 36 vs 14 | 1 / 94 / 1 | B 21, C 75; 96 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[KCNMA1]] | 26 vs 24 | 3 / 43 / 47 | B 70, C 23; 93 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[INSYN2B]] | 31 vs 19 | 0 / 92 / 0 | B 18, C 74; 92 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[PTPRR]] | 32 vs 18 | 3 / 86 / 0 | B 21, C 68; 89 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[FRMD4A]] | 24 vs 26 | 2 / 85 / 1 | B 28, C 60; 88 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 7; `tables/line_effects.parquet` — line == 7
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 7; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 7]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include COLO 205

---
cell_line: "SHP-77"
type: "cell line"
cell_line_id: "CVCL_1693"
depmap_id: "ACH-000790"
organ: "Lung"
tp53_status: "altered"
drivers: ["ABL1(Missense)", "ACVR2A(Missense)", "ARID1A(Missense)", "EGFR(Missense)", "KMT2D(Missense)", "KRAS(Missense)", "RAC1(Missense)", "SETD1B(Missense)", "TP53(Missense)"]
n_dd_depleted: 10
median_response: 0.794
tags: ["cell-line", "organ/lung"]
generated_by: "tahoemap"
---

# SHP-77

*Lung · TP53 altered · CVCL_1693 · ACH-000790*

|  |  |
|---|---|
| Organ | Lung |
| TP53 status | altered |
| Drivers | ABL1(Missense); ACVR2A(Missense); ARID1A(Missense); EGFR(Missense); KMT2D(Missense); KRAS(Missense); RAC1(Missense); SETD1B(Missense); TP53(Missense) |
| Driver changes | ABL1 p.V1128E; ACVR2A p.L147R; ARID1A p.P253S; EGFR p.Q656R; KMT2D p.Q3950R; KRAS p.G12V; RAC1 p.Y32C; SETD1B p.T482M; TP53 p.C176W |
| Cells over all wells | 2,282,350 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 0.794 (1 = a typical line) |
| Drug-doses that deplete it | 10 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 4 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,349 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 43): the line loses cells relative to the other lines in the same wells. Drug-doses: 10 in all, 6 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.0 | -2.25 |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.2 | -2.07 |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | -1.29 |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.9 | -1.19 |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.5 | -1.07 |
| [[AT7519 (drug)]] 5 µM |  | -4.4 | -1.08 |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -0.66 |
| [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -0.89 |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | -3.4 | -0.81 |
| [[Tucatinib (drug)]] 5 µM |  | -3.2 | -0.76 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Futibatinib (drug)]] 0.05 µM (1.95); [[Dihydroartemisinin (drug)]] 0.5 µM (1.83); [[Allantoin (drug)]] 0.5 µM (1.59); [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM (1.43); [[Neratinib (drug)]] 0.5 µM (1.42); [[Arbutin (drug)]] 0.5 µM (1.40); [[Tofacitinib (citrate) (drug)]] 0.05 µM (1.38); [[Tofacitinib (citrate) (drug)]] 5 µM (1.38)
- Weakest: [[Elagolix sodium (drug)]] 0.5 µM (-0.0805); [[Imiquimod (maleate) (drug)]] 0.5 µM (-0.0529); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM (0.0357); [[palbociclib (drug)]] 0.5 µM (0.173, ⚠ cell-cycle shift); [[Berbamine (drug)]] 5 µM (0.181); [[Berbamine (dihydrochloride) (drug)]] 5 µM (0.203); [[Lonafarnib (drug)]] 5 µM (0.241, ⚠ toxic); [[Daptomycin (drug)]] 0.05 µM (0.246, ⚠ unreliable plate only); [[Ritonavir (drug)]] 5 µM (0.254); [[PH-797804 (drug)]] 5 µM (0.258); [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM (0.261)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 43): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[TACC2]] (18), [[ARHGAP26]] (18), [[RALGAPA2]] (18), [[DNAH5]] (17), [[OTULINL]] (15), [[SPIDR]] (13), [[MBOAT2]] (12), [[NEBL]] (11), [[HSP90AA1]] (11, 6 ⚠), [[ZFPM2-AS1]] (10, 2 ⚠), [[RIPOR2]] (9), [[HSPA5]] (9, 1 ⚠), [[ATP6V0A1]] (8)
- down: [[SLCO3A1]] (32, 12 ⚠), [[CNKSR3]] (31, 11 ⚠), [[PITPNC1]] (30, 11 ⚠), [[CLDN10-AS1]] (28, 4 ⚠), [[CACNA1A]] (28, 10 ⚠), [[MAN1C1]] (25, 6 ⚠), [[SASH1]] (23, 11 ⚠), [[PITPNM2]] (22, 7 ⚠), [[ETV1]] (21, 3 ⚠), [[OAS3]] (21, 4 ⚠), [[PAM]] (21, 7 ⚠), [[MX2]] (20, 5 ⚠), [[DNAH5]] (20, 12 ⚠), [[DOCK5]] (19, 4 ⚠), [[NCKAP5]] (19, 4 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[CALCA]] (+8.3), [[PCSK1]] (+7.8), [[ENSG00000285534]] (+7.6, ⚠ noise-class RNA), [[RIT2]] (+7.5), [[KCNB2]] (+7.5), [[SNTG1]] (+7.4), [[SYT4]] (+7.4), [[ENSG00000253642]] (+7.4, ⚠ noise-class RNA), [[GRIK1]] (+7.3), [[CGA]] (+7.3), [[ENSG00000189229]] (+7.3, ⚠ noise-class RNA), [[KCND2]] (+7.3), [[MIR3667HG]] (+7.2), [[ADARB2]] (+7.2), [[CHGB]] (+7.2), [[ASCL1]] (+7.1), [[MIR646HG]] (+7.1), [[NKAIN2]] (+7.1) (2,157 genes, 183 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[VIM]] (-4.0), [[SDC4]] (-4.0), [[ZFP36L1]] (-3.9), [[AHNAK]] (-3.9), [[SOX9]] (-3.8), [[USP25]] (-3.8), [[ATXN1]] (-3.8), [[AXL]] (-3.8), [[ARHGAP10]] (-3.8), [[IGF2BP2]] (-3.8), [[HSPA13]] (-3.7), [[HLA-E]] (-3.7), [[DIAPH2]] (-3.7), [[ATL3]] (-3.7), [[UBE2E2]] (-3.7) (449 genes, 13 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 43): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 64 (0.403; genes FBXO17, PSD3, KCNQ1OT1, P3H2 / PMP22, ATP2B1, MIDN, HAS2); component 50 (0.588; genes TNFRSF19, ALDH1A3, ERRFI1, TNFAIP3 / PTPRB, SCD, MECOM, GALNT1); component 40 (0.611; genes MYOF, IFNAR2, ABCC3, HSPA8 / AP3B1, HERC6, CDC20, WDR59); component 2 (0.624; genes PRKDC, NUP155, POLA1, TFDP1 / CIR1, PNRC1, AKAP9, RSRP1)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 8 in all, 8 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 53 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TP53]] | TP53 loss of function (33 lines) vs not recorded (17) | 106 / 13 / 0 | A 24, B 9, C 86; 119 with an alert ⚠ | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[KMT2D]] | KMT2D altered (any record) (15 lines) vs not recorded (35) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[SETD1B]] | SETD1B altered (any record) (11 lines) vs not recorded (39) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, ARID1A |
| [[ARID1A]] | ARID1A altered (any record) (15 lines) vs not recorded (35) | 0 / 0 / 1 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[ACVR2A]] | ACVR2A altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with TGFBR2, SETD1B, PRDM2 |
| [[ACVR2A]] | ACVR2A loss of function (7 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B, PRDM2, EP300 |
| [[EGFR]] | EGFR altered (any record) (4 lines) vs not recorded (46) | 0 / 0 / 0 | — | ⚠ few lines (4 vs 46); within organs, on part of the lines; mechanism partly not recorded; EGFR not expressed in 1 of the 4 altered lines |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,105 in all, 2,105 with an alert ⚠; shown: the 15 strongest; 2,090 more line sets (2,090 of them with an alert ⚠) not shown; 2,147 genes; 1,889 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[TMPRSS4]], [[OVOL1]] | 33 vs 17 | 14 / 223 / 24 | B 115, C 146; 261 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[IRF6]], [[C1orf116]] | 31 vs 19 | 18 / 216 / 24 | B 128, C 130; 258 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ST14]] | 32 vs 18 | 11 / 196 / 21 | B 88, C 140; 228 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[INAVA]], [[MROH3P]] | 29 vs 21 | 11 / 194 / 19 | B 109, C 115; 224 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TMPRSS2]] | 35 vs 15 | 6 / 197 / 18 | B 77, C 144; 221 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SLC44A4]] | 37 vs 13 | 9 / 186 / 9 | B 57, C 147; 204 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[EPS8L3]] | 35 vs 15 | 0 / 196 / 1 | B 46, C 151; 197 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[CLIC5]] | 37 vs 13 | 4 / 185 / 7 | B 59, C 137; 196 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ARHGEF38]] | 36 vs 14 | 5 / 172 / 9 | B 49, C 137; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[B3GNT3]] | 31 vs 19 | 6 / 174 / 6 | B 72, C 114; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GCNT3]] | 38 vs 12 | 2 / 184 / 0 | B 43, C 143; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01559]] | 38 vs 12 | 0 / 182 / 0 | B 36, C 146; 182 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ITGB6]] | 32 vs 18 | 5 / 148 / 18 | B 47, C 124; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TC2N]] | 28 vs 22 | 3 / 163 / 5 | B 52, C 119; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TJP3]] | 29 vs 21 | 7 / 155 / 9 | B 61, C 110; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 43; `tables/line_effects.parquet` — line == 43
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 43; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 43]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include SHP-77

---
cell_line: "SW48"
type: "cell line"
cell_line_id: "CVCL_1724"
depmap_id: "ACH-000958"
organ: "Bowel"
tp53_status: "wild type"
drivers: ["ACVR2A(Frameshift)", "APC(Missense)", "ARID1A(Frameshift)", "B2M(Frameshift)", "B2M(Stopgain)", "BRCA2(Frameshift)", "CTNNB1(Missense)", "EGFR(Missense)", "EP300(Frameshift)", "EP300(Missense)", "FBXW7(Frameshift)", "KMT2D(Frameshift)", "KMT2D(Stopgain)", "MAP2K1(Missense)", "PIK3CA(Missense)", "RNF43(Frameshift)", "SETD1B(Frameshift)", "SMARCA4(Missense)", "TGFBR2(Frameshift)", "ZFHX3(Frameshift)"]
n_dd_depleted: 8
median_response: 1.006
tags: ["cell-line", "organ/bowel"]
generated_by: "tahoemap"
---

# SW48

*Bowel · TP53 wild type · CVCL_1724 · ACH-000958*

|  |  |
|---|---|
| Organ | Bowel |
| TP53 status | wild type |
| Drivers | ACVR2A(Frameshift); APC(Missense); ARID1A(Frameshift); B2M(Frameshift); B2M(Stopgain); BRCA2(Frameshift); CTNNB1(Missense); EGFR(Missense); EP300(Frameshift); EP300(Missense); FBXW7(Frameshift); KMT2D(Frameshift); KMT2D(Stopgain); MAP2K1(Missense); PIK3CA(Missense); RNF43(Frameshift); SETD1B(Frameshift); SMARCA4(Missense); TGFBR2(Frameshift); ZFHX3(Frameshift) |
| Driver changes | ACVR2A p.K437fs; APC p.R2714C; ARID1A p.A339fs; B2M p.Q22*; B2M p.V69fs; BRCA2 p.K1691fs; BRCA2 p.N1784fs; CTNNB1 p.S33Y; EGFR p.G674S; EP300 p.M1470fs; EP300 p.T594M; FBXW7 p.S588fs; KMT2D p.R4904*; KMT2D p.R755fs; MAP2K1 p.D175G; MAP2K1 p.Q56P; PIK3CA p.G914R; RNF43 p.G659fs; RNF43 p.V299fs; SETD1B p.H8fs; SMARCA4 p.A703V; TGFBR2 p.K128fs; ZFHX3 p.A3407fs |
| Cells over all wells | 954,083 |
| Wells with usable expression | 1,328 (99.9%) |
| Median response strength (β) | 1.01 (1 = a typical line) |
| Drug-doses that deplete it | 8 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 3 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,089 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 47): the line loses cells relative to the other lines in the same wells. Drug-doses: 9 in all, 6 with an alert ⚠. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -6.4 | -2.95 |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | -0.85 |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.05 |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -0.96 |
| [[TAK-901 (drug)]] 0.05 µM |  | -4.1 | -0.81 |
| [[Infigratinib (drug)]] 5 µM |  | -3.3 | -0.66 |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | -3.1 | -0.63 |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -0.59 |
| [[Ipatasertib (drug)]] 0.5 µM |  | -3.0 | -0.60 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 488, 84 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Amsacrine (drug)]] 0.5 µM (2.40); [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM (1.86); [[Imiquimod (maleate) (drug)]] 0.5 µM (1.84); [[EX229 (drug)]] 0.05 µM (1.84); [[Amsacrine (drug)]] 5 µM (1.82); [[TAK-733 (drug)]] 0.05 µM (1.81); [[Trifluridine (drug)]] 5 µM (1.80, ⚠ cell-cycle shift); [[Cytarabine (drug)]] 0.05 µM (1.73); [[Citalopram (hydrobromide) (drug)]] 0.5 µM (1.73)
- Weakest: [[Ponatinib (drug)]] 5 µM (0.102); [[BI-3406 (drug)]] 5 µM (0.177); [[Regorafenib (drug)]] 5 µM (0.193); [[BI-3406 (drug)]] 0.5 µM (0.221); [[Tofacitinib (drug)]] 5 µM (0.312); [[Verteporfin (drug)]] 0.05 µM (0.330); [[Gallic acid (hydrate) (drug)]] 0.5 µM (0.342); [[Tofacitinib (citrate) (drug)]] 5 µM (0.360)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 47): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[MDM2]] (17, 2 ⚠), [[ARRDC4]] (12, 1 ⚠), [[KLF6]] (12, 3 ⚠), [[ABL2]] (11), [[ARHGAP26]] (11, 2 ⚠), [[JUN]] (11, 3 ⚠), [[NR1D2]] (10, 1 ⚠), [[ARID4A]] (10, 2 ⚠), [[XPO1]] (10, 2 ⚠), [[ADNP2]] (10, 2 ⚠), [[GADD45B]] (10, 5 ⚠), [[DDX5]] (10, 5 ⚠), [[APLP2]] (10, 8 ⚠), [[DAAM1]] (9), [[SIRT1]] (9, 1 ⚠), [[SUPT6H]] (9, 1 ⚠)
- down: [[FERMT1]] (36, 7 ⚠), [[KIAA0040]] (30, 8 ⚠), [[HMGA2]] (29, 5 ⚠), [[NT5E]] (23, 2 ⚠), [[CDCP1]] (22, 3 ⚠), [[FHIT]] (22, 10 ⚠), [[BAMBI]] (22, 11 ⚠), [[CCSER1]] (20, 13 ⚠), [[ITGA2]] (19, 1 ⚠), [[NTSR1]] (19, 7 ⚠), [[SKAP1]] (19, 9 ⚠), [[LMO7]] (19, 14 ⚠), [[PHLDA1]] (18, 1 ⚠), [[MET]] (18, 4 ⚠), [[MIR100HG]] (17, 3 ⚠), [[SERPINB1]] (17, 4 ⚠), [[PLAUR]] (16, 2 ⚠), [[LAMC2]] (15, 2 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[CD36]] (+8.0), [[ENSG00000289850]] (+7.3, ⚠ noise-class RNA), [[GNAT3]] (+7.1), [[HPGD]] (+7.0), [[KLK7]] (+6.7), [[GPR15]] (+6.7), [[EDAR]] (+6.3), [[SLC30A10]] (+6.3), [[LINC01956]] (+6.3), [[KLK10]] (+6.2), [[MAOB]] (+5.8), [[BMP4]] (+5.7), [[ENSG00000239498]] (+5.7, ⚠ noise-class RNA), [[ENSG00000285635]] (+5.7, ⚠ noise-class RNA), [[XIST]] (+5.6), [[SGPP2]] (+5.6), [[VSNL1]] (+5.4), [[RNF43]] (+5.3) (1,364 genes, 110 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)
- Lacks: [[NR3C1]] (-3.6), [[QKI]] (-3.5), [[VIM]] (-3.5), [[KLF7]] (-3.5), [[RBMS1]] (-3.4), [[ZNF264]] (-3.4), [[PLOD2]] (-3.4), [[ZNF254]] (-3.3), [[UBE2E2]] (-3.3), [[KIRREL1]] (-3.3), [[OSMR-DT]] (-3.3), [[OSMR]] (-3.3), [[BNIP3]] (-3.3), [[ATRN]] (-3.3), [[HLTF]] (-3.3) (319 genes, 6 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 47): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Weak here (< 0.7): component 13 (0.534; genes UGP2, KLF9, TSC22D3, SSBP2 / LUC7L3, PER3, TCP10L, SEMA3A); component 56 (0.560; genes PARVA, PARP8, MME, LIMS1 / ATP2B4, NAV3, PLCXD1, MIR31HG); component 54 (0.570; genes FDFT1, LPIN1, ACACA, MSMO1 / GLRX, DPY19L1, WWC1, NR4A3); component 48 (0.656; genes LINC01876, RNF19A, PDE4D, NEBL / CYP51A1, LPIN1, INSIG1, LYST)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 28 in all, 28 with an alert ⚠; shown: the 15 strongest; 13 more groups (13 of them with an alert ⚠) not shown. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 34 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[APC]] | APC altered (any record) (10 lines) vs not recorded (40) | 7 / 0 / 0 | C 7; 7 with an alert ⚠ | ⚠ tissue-confounded; across organs; mechanism partly not recorded |
| [[BRCA2]] | BRCA2 loss of function (7 lines) vs not recorded (41) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, WNK2, ACVR2A |
| [[KMT2D]] | KMT2D altered (any record) (15 lines) vs not recorded (35) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[SETD1B]] | SETD1B altered (any record) (11 lines) vs not recorded (39) | 1 / 0 / 0 | B 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with ZFHX3, ACVR2A, ARID1A |
| [[ARID1A]] | ARID1A altered (any record) (15 lines) vs not recorded (35) | 0 / 0 / 1 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[FBXW7]] | FBXW7 loss of function (5 lines) vs not recorded (45) | 0 / 1 / 0 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines |
| [[ACVR2A]] | ACVR2A altered (any record) (8 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with TGFBR2, SETD1B, PRDM2 |
| [[ACVR2A]] | ACVR2A loss of function (7 lines) vs not recorded (42) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B, PRDM2, EP300 |
| [[ARID1A]] | ARID1A loss of function (12 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[B2M]] | B2M altered (any record) (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[B2M]] | B2M loss of function (5 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, NF1, EP300 |
| [[BRCA2]] | BRCA2 altered (any record) (9 lines) vs not recorded (41) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with WNK2, TGFBR2, PIK3CA |
| [[CTNNB1]] | CTNNB1 altered (any record) (5 lines) vs not recorded (45) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded |
| [[CTNNB1]] | CTNNB1 gain of function (4 lines) vs not recorded (45) | 0 / 0 / 0 | — | ⚠ few lines (4 vs 45); within organs, on part of the lines |
| [[EGFR]] | EGFR altered (any record) (4 lines) vs not recorded (46) | 0 / 0 / 0 | — | ⚠ few lines (4 vs 46); within organs, on part of the lines; mechanism partly not recorded; EGFR not expressed in 1 of the 4 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,477 in all, 2,477 with an alert ⚠; shown: the 15 strongest; 2,462 more line sets (2,462 of them with an alert ⚠) not shown; 2,528 genes; 2,163 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[TMPRSS2]] | 35 vs 15 | 6 / 197 / 18 | B 77, C 144; 221 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[SLC44A4]] | 37 vs 13 | 9 / 186 / 9 | B 57, C 147; 204 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ARHGEF38]] | 36 vs 14 | 5 / 172 / 9 | B 49, C 137; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[B3GNT3]] | 31 vs 19 | 6 / 174 / 6 | B 72, C 114; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GCNT3]] | 38 vs 12 | 2 / 184 / 0 | B 43, C 143; 186 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC01559]] | 38 vs 12 | 0 / 182 / 0 | B 36, C 146; 182 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TOX3]] | 31 vs 19 | 4 / 168 / 1 | B 46, C 127; 173 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[TJP3]] | 29 vs 21 | 7 / 155 / 9 | B 61, C 110; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ADGRF1]] | 35 vs 15 | 14 / 138 / 16 | B 64, C 104; 168 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[LINC03040]] | 31 vs 19 | 3 / 147 / 4 | B 38, C 116; 154 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[NPSR1]] | 42 vs 8 | 2 / 142 / 0 | B 26, C 118; 144 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[GPX2]] | 36 vs 14 | 2 / 139 / 0 | B 23, C 118; 141 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[ATP10B]] | 40 vs 10 | 0 / 140 / 0 | B 27, C 113; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC13]] | 40 vs 10 | 2 / 138 / 0 | B 33, C 107; 140 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
| [[MUC5B]] | 37 vs 13 | 2 / 135 / 2 | B 33, C 106; 139 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 47; `tables/line_effects.parquet` — line == 47
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 47; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 47]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include SW48

---
cell_line: "hTERT-HPNE"
type: "cell line"
cell_line_id: "CVCL_C466"
depmap_id: ""
organ: "Pancreas"
tp53_status: "wild type"
drivers: ["TERT(Transgene)"]
n_dd_depleted: 15
median_response: 1.047
tags: ["cell-line", "organ/pancreas"]
generated_by: "tahoemap"
---

# hTERT-HPNE

*Pancreas · TP53 wild type · CVCL_C466 · *

|  |  |
|---|---|
| Organ | Pancreas |
| TP53 status | wild type |
| Drivers | TERT(Transgene) |
| Driver changes | — |
| Cells over all wells | 1,682,091 |
| Wells with usable expression | 1,329 (100%) |
| Median response strength (β) | 1.05 (1 = a typical line) |
| Drug-doses that deplete it | 15 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 10 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,476 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 49): the line loses cells relative to the other lines in the same wells. Drug-doses: 15 in all, 5 with an alert ⚠; shown: the 12 strongest and the 2 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[vincristine (drug)]] 5 µM |  | -6.3 | -1.45 |
| [[Peretinoin (drug)]] 0.5 µM |  | -6.1 | -1.24 |
| [[Ipatasertib (drug)]] 0.5 µM |  | -5.9 | -1.21 |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -5.8 | -1.27 |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | -5.0 | -1.03 |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -4.5 | -1.16 |
| [[PH-797804 (drug)]] 0.5 µM |  | -4.4 | -0.90 |
| [[Neratinib (drug)]] 5 µM |  | -3.5 | -0.70 |
| [[Penfluridol (drug)]] 0.5 µM |  | -3.4 | -0.69 |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -0.68 |
| [[Sonidegib (drug)]] 5 µM |  | -3.2 | -0.73 |
| [[DTP3 (drug)]] 5 µM |  | -3.1 | -0.65 |
| [[Celecoxib (drug)]] 0.5 µM |  | -3.0 | -0.60 |
| [[Pimitespib (drug)]] 5 µM |  | -3.0 | -0.67 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 489, 85 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Econazole (drug)]] 5 µM (1.81); [[Dexamethasone (drug)]] 5 µM (1.72); [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM (1.68, ⚠ unreliable plate only); [[Ritonavir (drug)]] 0.5 µM (1.67); [[Clobetasol propionate (drug)]] 5 µM (1.67); [[(S)-Crizotinib (drug)]] 5 µM (1.67); [[Medroxyprogesterone acetate (drug)]] 5 µM (1.64); [[Budesonide (drug)]] 5 µM (1.62); [[Rifaximin (drug)]] 5 µM (1.61)
- Weakest: [[Tofacitinib (citrate) (drug)]] 0.05 µM (0.0875); [[Citalopram (hydrobromide) (drug)]] 0.5 µM (0.169); [[Tofacitinib (citrate) (drug)]] 5 µM (0.176); [[Tofacitinib (drug)]] 5 µM (0.219); [[Bicalutamide (drug)]] 0.5 µM (0.240); [[Elagolix sodium (drug)]] 0.5 µM (0.248); [[Tofacitinib (citrate) (drug)]] 0.5 µM (0.258); [[Tofacitinib (drug)]] 0.5 µM (0.261)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 49): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[FKBP5]] (22, 5 ⚠), [[UGP2]] (18), [[TANC2]] (18), [[SLC44A1]] (16), [[MAP2]] (16), [[CERS6]] (16), [[SORT1]] (16, 1 ⚠), [[HIPK2]] (15), [[STXBP5]] (15), [[SSBP2]] (14), [[TMEM87A]] (13), [[HSP90AA1]] (13, 8 ⚠), [[MED13]] (12, 1 ⚠)
- down: [[HMGA2]] (25, 9 ⚠), [[ADAMTS6]] (25, 10 ⚠), [[SYNJ2]] (23, 2 ⚠), [[ITGA2]] (23, 6 ⚠), [[NAV1]] (23, 13 ⚠), [[PITPNC1]] (22, 10 ⚠), [[SIPA1L3]] (20, 12 ⚠), [[DNAAF9]] (20, 13 ⚠), [[PLD1]] (19, 10 ⚠), [[STC1]] (18, 5 ⚠), [[AFF3]] (18, 7 ⚠), [[CBLB]] (18, 11 ⚠), [[TTC3]] (17, 5 ⚠), [[CHD1L]] (16, 4 ⚠), [[LOXL2]] (16, 4 ⚠), [[KIAA1549L]] (14, 3 ⚠), [[SEC23A]] (13, 2 ⚠), [[LAMA4]] (12, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[GREM1]] (+7.8), [[MMP1]] (+7.7), [[COL6A3]] (+7.4), [[MEG3]] (+7.2), [[ADAMTS12]] (+7.0), [[MEG8]] (+7.0), [[COL1A2]] (+6.9), [[PDGFRB]] (+6.8), [[INHBA]] (+6.8), [[SGIP1]] (+6.8), [[ADGRB3]] (+6.7), [[PRRX1]] (+6.6), [[WNT5A]] (+6.5), [[CARMN]] (+6.5), [[PAPPA]] (+6.5) (1,120 genes, 81 with an alert ⚠; shown: the 15 strongest)
- Lacks: [[BACE2]] (-3.1), [[PRKCZ]] (-3.1), [[CDCP1]] (-3.0), [[CHD7]] (-3.0), [[KIF16B]] (-2.9), [[NFIB]] (-2.9), [[PTPN3]] (-2.9), [[KIAA1671]] (-2.9), [[TPD52]] (-2.9), [[SLCO4A1]] (-2.9), [[RNF144A]] (-2.9), [[MGMT]] (-2.8), [[PPP1R9A]] (-2.8), [[CMTM8]] (-2.8), [[DHRS3]] (-2.8) (248 genes, 5 with an alert ⚠; shown: the 15 strongest)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 49): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Every component responds within 0.7–1.5 of a typical line (range 0.702 to 1.28).

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 1 in all, 1 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 62 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[TERT]] | TERT altered (any record) (11 lines) vs not recorded (39) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; TERT not expressed in 2 of the 11 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,082 in all, 2,082 with an alert ⚠; shown: the 15 strongest; 2,067 more line sets (2,067 of them with an alert ⚠) not shown; 2,120 genes; 1,821 of the sets gave arrows. Ranked by the number of arrows.*

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

- `tables/lines.parquet` — line == 49; `tables/line_effects.parquet` — line == 49
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 49; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 49]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include hTERT-HPNE

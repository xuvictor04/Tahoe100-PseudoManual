---
cell_line: "Hs 766T"
type: "cell line"
cell_line_id: "CVCL_0334"
depmap_id: "ACH-000178"
organ: "Pancreas"
tp53_status: "wild type"
drivers: ["ARID1A(Stopgain)", "CDKN2A(Splice_site)", "KRAS(Missense)", "SMAD4(Deletion)"]
n_dd_depleted: 28
median_response: 1.023
tags: ["cell-line", "organ/pancreas"]
generated_by: "tahoemap"
---

# Hs 766T

*Pancreas · TP53 wild type · CVCL_0334 · ACH-000178*

|  |  |
|---|---|
| Organ | Pancreas |
| TP53 status | wild type |
| Drivers | ARID1A(Stopgain); CDKN2A(Splice_site); KRAS(Missense); SMAD4(Deletion) |
| Driver changes | ARID1A p.Q538*; KRAS p.Q61H |
| Cells over all wells | 2,535,670 |
| Wells with usable expression | 1,328 (99.9%) |
| Median response strength (β) | 1.02 (1 = a typical line) |
| Drug-doses that deplete it | 28 (abundance z ≤ −3; drug-doses whose flags make abundance untrustworthy left out); 22 without any artifact flag |
| Genes it measures (expresses above the ambient level) | 14,400 of 16,643 |

## Drug-doses that deplete it

*Drug-doses with relative-abundance z ≤ −3 (`atlas/effects/DD_Az.npy`, column 12): the line loses cells relative to the other lines in the same wells. Drug-doses: 29 in all, 7 with an alert ⚠; shown: the 12 strongest and the 6 next strongest without an alert. ⚠ = the drug-dose's artifact flags. Of them `unreliable plate only`, `position not correctable` and `wells disagree` make its cell counts untrustworthy: the count in the table above leaves such drug-doses out, this list shows them.*

| Drug-dose | Alert | Abundance z | log2 relative abundance |
|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.5 | -0.99 |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.0 | -1.39 |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.7 | -0.71 |
| [[Pentoxifylline (drug)]] 0.5 µM |  | -6.5 | -0.63 |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -6.4 | -0.70 |
| [[EX229 (drug)]] 5 µM |  | -6.3 | -0.85 |
| [[venetoclax (drug)]] 5 µM |  | -6.2 | -0.91 |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | -6.2 | -0.62 |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -5.9 | -1.73 |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | -0.70 |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.5 | -0.54 |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.1 | -0.72 |
| [[Sulfisoxazole (drug)]] 0.5 µM |  | -4.9 | -0.55 |
| [[Verteporfin (drug)]] 5 µM |  | -4.3 | -0.43 |
| [[Ipatasertib (drug)]] 0.5 µM |  | -4.3 | -0.51 |
| [[4EGI-1 (drug)]] 5 µM |  | -4.2 | -0.59 |
| [[TAK-733 (drug)]] 5 µM |  | -4.0 | -0.51 |
| [[Penfluridol (drug)]] 0.5 µM |  | -3.9 | -0.38 |

## How strongly it responds

*β = slope of the line's changes on the drug-dose's consensus (`atlas/effects/DD_beta.npy`; 1 = typical, 0 = no response), drug-doses with ≥ 20 significant genes: 488, 84 with an alert ⚠. The 8 strongest and weakest, and any of the 8 strongest and weakest without an alert beyond them; ⚠ = the drug-dose's artifact flags.*

- Strongest: [[Dexamethasone (drug)]] 0.05 µM (2.05); [[Budesonide (drug)]] 0.5 µM (2.02); [[AZD-8055 (drug)]] 0.5 µM (1.99); [[Betamethasone dipropionate (drug)]] 5 µM (1.97); [[Econazole (drug)]] 5 µM (1.97); [[Betamethasone dipropionate (drug)]] 0.5 µM (1.94); [[Pemetrexed (drug)]] 0.5 µM (1.93); [[Dexamethasone (drug)]] 5 µM (1.93)
- Weakest: [[Norepinephrine (hydrochloride) (drug)]] 5 µM (-0.390); [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM (0.128); [[Monocrotaline (drug)]] 0.05 µM (0.135); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM (0.176); [[Canagliflozin (drug)]] 0.05 µM (0.332); [[Decitabine (drug)]] 0.05 µM (0.337); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM (0.349); [[Malotilate (drug)]] 0.5 µM (0.372)

## Genes it moves most

*Genes with the most drug-doses moving them ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses) in this line (`tables/line_effects.parquet`, line == 12): in brackets the number of drug-doses, and how many of them carry an alert (⚠); the 12 with the most, and any of the 12 with the most drug-doses without an alert beyond them.*

- up: [[BIRC3]] (28, 2 ⚠), [[FKBP5]] (25, 4 ⚠), [[TOP1]] (23, 4 ⚠), [[ATP1A1]] (22, 2 ⚠), [[GLUL]] (20), [[TXNIP]] (20, 2 ⚠), [[KLF9]] (19), [[FGD4]] (19), [[PID1]] (19, 1 ⚠), [[UBE2E2]] (19, 1 ⚠), [[ZMYND8]] (18), [[ZFHX3]] (18)
- down: [[NHS]] (29, 7 ⚠), [[CPOX]] (28, 8 ⚠), [[DOK5]] (28, 9 ⚠), [[ADAM19]] (27, 8 ⚠), [[ADAMTS16]] (26, 7 ⚠), [[PDGFB]] (26, 12 ⚠), [[NRG1]] (25, 2 ⚠), [[BBOX1-AS1]] (25, 9 ⚠), [[ATP8B1]] (23, 8 ⚠), [[LIMA1]] (22, 4 ⚠), [[DUSP6]] (22, 6 ⚠), [[SYNJ2]] (21, 3 ⚠), [[GPRC5B]] (21, 4 ⚠), [[LGR6]] (20, 2 ⚠), [[ITGA2]] (19, 1 ⚠)

## Its own level

*Baseline CPM in this line vs the median line (`tables/line_effects.parquet` baseline_cpm; log2 ratio). Highest = at least 2× the median line and ≥ 10 CPM here. Lacks = expressed at ≥ 20 CPM in the median line, not measured here (below 25% of the median line, or below 0.25 × the gene's pooled level, where the line reads only ambient RNA; deletion, silencing or lineage). ⚠ = a noise-class RNA, or a level here that is only ambient RNA (kept in its rank).*

- Highest relative to other lines: [[KRT6A]] (+7.7), [[SULF1]] (+7.6), [[KRT14]] (+7.4), [[DOK5]] (+7.1), [[KRT17]] (+7.1), [[TIMP3]] (+6.9), [[HSD17B2]] (+6.8), [[LINC01133]] (+6.6), [[C4BPB]] (+6.5), [[SOX7]] (+6.5), [[LINC02725]] (+6.4), [[ALDH3A1]] (+6.4), [[MXRA5]] (+6.3), [[COL17A1]] (+6.1), [[ECSCR]] (+6.1) (1,251 genes, 88 with an alert ⚠; shown: the 15 strongest)
- Lacks: [[SMAD4]] (-4.1), [[BNIP3]] (-3.7), [[ENSG00000214265]] (-3.6, ⚠ noise-class RNA), [[PRKCZ]] (-3.6), [[RANBP17]] (-3.6), [[VIM]] (-3.5), [[SPART]] (-3.4), [[ZNF462]] (-3.4), [[ZDBF2]] (-3.4), [[MPDZ]] (-3.4), [[PCNX2]] (-3.4), [[PLOD2]] (-3.4), [[CERS6]] (-3.3), [[DANT2]] (-3.3), [[RGS17]] (-3.3), [[NETO2]] (-3.3) (232 genes, 8 with an alert ⚠; shown: the 15 strongest and the next strongest without an alert)

## In the vector space

*Response sensitivity per component of the space (`embed/line_response_vectors.npy` row 12): 1 = the programme responds as in a typical line, 0 = it does not respond here. Genes = the component's top + / − genes.*

- Strong here (> 1.5): component 13 (1.56; genes UGP2, KLF9, TSC22D3, SSBP2 / LUC7L3, PER3, TCP10L, SEMA3A)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Its recorded alterations

*The comparison groups that count this line as altered (Tahoe's cell-line genetics; `direction/groups.parquet`): 6 in all, 6 with an alert ⚠. Each group is its gene's recorded loss of function, gain of function, or any record (some records carry no mechanism), against the lines with no record of the gene. Arrows = the arrows that came out of the group, by target: a gene's drug response / its level / the cells under a drug-dose. In 58 other groups this line is on the 'not recorded' side.*

| Gene | Group | Arrows (response / level / cells) | Grades | Alerts |
|---|---|---|---|---|
| [[ARID1A]] | ARID1A altered (any record) (15 lines) vs not recorded (35) | 0 / 0 / 1 | C 1; 1 with an alert ⚠ | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with SETD1B |
| [[ARID1A]] | ARID1A loss of function (12 lines) vs not recorded (35) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with SETD1B |
| [[CDKN2A]] | CDKN2A altered (any record) (22 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; mechanism partly not recorded; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 22 altered lines |
| [[CDKN2A]] | CDKN2A loss of function (20 lines) vs not recorded (28) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; CDKN2A not expressed in 13 of the 20 altered lines |
| [[KRAS]] | KRAS gain of function (24 lines) vs not recorded (26) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines |
| [[SMAD4]] | SMAD4 loss of function (6 lines) vs not recorded (44) | 0 / 0 / 0 | — | ⚠ within organs, on part of the lines; SMAD4 not expressed in 2 of the 6 altered lines |

### Genes it does not express (natural knockouts)

*Genes this line does not express (it reads only the ambient RNA of the well) while at least 3 other lines do: the stage compared the lines lacking each gene with the lines expressing it (genes absent from exactly the same lines share one test). Line sets that include this line: 2,166 in all, 2,166 with an alert ⚠; shown: the 15 strongest; 2,151 more line sets (2,151 of them with an alert ⚠) not shown; 2,207 genes; 1,877 of the sets gave arrows. Ranked by the number of arrows.*

| Gene(s) | Lines without vs expressing | Arrows (response / level / cells) | Grades | Compared | Alerts |
|---|---|---|---|---|---|
| [[TMPRSS4]], [[OVOL1]] | 33 vs 17 | 14 / 223 / 24 | B 115, C 146; 261 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |
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
| [[TC2N]] | 28 vs 22 | 3 / 163 / 5 | B 52, C 119; 171 with an alert ⚠ | within organs | ⚠ within organs, on part of the lines |

## Data

- `tables/lines.parquet` — line == 12; `tables/line_effects.parquet` — line == 12
- `atlas/effects/DD_A.npy`, `DD_Az.npy`, `DD_beta.npy`, `line_cpm.npy` — column / row 12; `tensor/DDL_lfc.npy`, `DDL_z.npy` — [:, :, 12]
- `direction/groups.parquet` — the genotype and natural-knockout groups whose altered_lines include Hs 766T

---
symbol: "SNHG11"
type: "gene"
col: 10486
ensembl_id: "ENSG00000174365"
name: "small nucleolar RNA host gene 11"
location: "20q11.23"
module: 12
arm: "+"
pooled_cpm: 3.15
n_lines_expressing: 48
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# SNHG11

*small nucleolar RNA host gene 11* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.38× (z +9.2, q 3e-17, up in 28 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.451× (z -6.3, q 2e-07, down in 21 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STK16]] (+0.78, fdr 7e-06), [[WASHC1]] (+0.78, fdr 7e-06), [[RP9]] (+0.78, fdr 7e-06); moves opposite to [[BCAP31]] (-0.70, fdr 7e-06), [[BANF1]] (-0.66, fdr 1e-05), [[CRTAP]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF264]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10486.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.38×** | +9.2 | 3e-17 | 28/34 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.91×** | +8.3 | 2e-14 | 29/32 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.39×** | +6.5 | 1e-08 | 1/5 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.71×** | +5.6 | 2e-06 | 10/43 (NCI-H2030, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +5.6 | 2e-06 | 24/40 (Panc 03.27, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +5.3 | 1e-05 | 4/16 (Hs 766T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.97×** | +5.3 | 1e-05 | 10/20 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +4.6 | 3e-04 | 8/22 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.94×** | +4.4 | 7e-04 | 4/7 (SW1417, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.73×** | +4.3 | 0.001 | 13/43 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.65×** | +3.9 | 0.005 | 7/30 (Hs 766T, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.65×** | +3.9 | 0.005 | 14/39 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.43×** | +3.8 | 0.007 | 5/17 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10486.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.451×** | -6.3 | 2e-07 | 21/39 (A-172, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.472×** | -5.9 | 7e-07 | 20/38 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.473×** | -5.9 | 7e-07 | 24/45 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | 0.662× | -3.3 | 0.16 | 13/40 (SW 900, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.405× | -3.1 | 0.20 | 10/36 (PANC-1, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.678× | -3.1 | 0.20 | 6/44 (SW 900, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.683× | -3.0 | 0.20 | 5/43 (COLO 205, PANC-1, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10486. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10486), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK16]] | +0.78 | +0.83 / +0.71 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.78 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[RP9]] | +0.78 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.77 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[AMZ2P1-1]] | +0.76 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[EBAG9]] | +0.76 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[ZNF579]] | +0.74 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.74 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[NFKBIL1]] | +0.74 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[PEX12]] | +0.74 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[TMEM42]] | +0.74 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[FBXL6]] | +0.73 | +0.76 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | -0.70 | -0.72 / -0.67 | both halves | 7e-06 |  |
| [[BANF1]] | -0.66 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[CRTAP]] | -0.64 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[TXNDC5]] | -0.64 | -0.59 / -0.72 | both halves | 7e-06 |  |
| [[ADAM15]] | -0.63 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[CDK2]] | -0.63 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[PPT1]] | -0.62 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.62 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[CMPK1]] | -0.62 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[ZNF731P]] | -0.62 | -0.65 / -0.55 | both halves | 1e-05 |  |
| [[TXN]] | -0.61 | -0.67 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF264]] | B | ZNF264 activity lowers SNHG11's level | lines that do not express ZNF264 (5) vs lines expressing it (45) | 1.29× higher at baseline in the lines without ZNF264 | 0.098 | ⚠ within organs, on part of the lines; also absent: ZNF548, ZNF550, ZNF419 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.853). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-34.1, 1.4); signed map (0.5, -12.4). **Vector** length 54.6, 9.02% of its response variance represented; |z| ≥ 3 in 667 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mRNA Splicing - Major Pathway* (reactome, mean cos +0.51 to 17); *mRNA Splicing* (reactome, mean cos +0.51 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.1 | +8.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.2 | +5.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.8 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.7 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.9 | +3.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -5.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.9 | -1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | +0.8 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 11 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q11.23 — chr20:38,446,343-38,450,940 (+) |
| Ensembl biotype | lncRNA |
| Also known as | LINC00101; previously C20orf198 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [128439](https://www.ncbi.nlm.nih.gov/gene/128439):

> This gene is a member of the non-protein-coding multiple snoRNA host gene family. Two snoRNAs are derived from the introns of this host gene. Although many alternative splice variants have been observed, the gene is thought to have no protein-coding potential. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:25046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25046) · Entrez [128439](https://www.ncbi.nlm.nih.gov/gene/128439) · Ensembl [ENSG00000174365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174365)

## Data

Gene col 10486: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10486); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10486, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10486]; `tensor/DDL_lfc|DDL_z.npy` [10486]; `embed/gene_vectors.npy` [10486]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10486 or target_col == 10486). Every well: [[SNHG11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

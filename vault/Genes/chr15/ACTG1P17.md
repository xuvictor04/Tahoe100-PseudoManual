---
symbol: "ACTG1P17"
type: "gene"
col: 15183
ensembl_id: "ENSG00000259315"
name: "actin gamma 1 pseudogene 17"
location: "15q25.2"
module: 35
arm: "+"
pooled_cpm: 2.31
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# ACTG1P17

*actin gamma 1 pseudogene 17* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.31× (z +10.3, q 5e-22, up in 23 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.532× (z -5.5, q 2e-05, down in 18 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.145×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Erdafitinib (drug)]] 0.05 µM in 1 line (A498 0.0599×); [[NG25 (drug)]] 0.05 µM in 1 line (NCI-H460 0.0649×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSMCE1-DT]] (+0.71, fdr 7e-06), [[GTF2IP5]] (+0.71, fdr 7e-06), [[KDM4D]] (+0.69, fdr 7e-06); moves opposite to [[POLR2E]] (-0.54, fdr 8e-04, ⚠ not reproduced).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[ZNF12]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15183.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +10.3 | 5e-22 | 23/29 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.02×** | +9.6 | 2e-19 | 24/38 (SW480, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.76×** | +6.9 | 9e-10 | 12/43 (PANC-1, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +5.9 | 5e-07 | 8/12 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +5.8 | 8e-07 | 1/2 (A498) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +5.7 | 1e-06 | 12/24 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +5.5 | 3e-06 | 19/45 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.75×** | +4.9 | 8e-05 | 5/43 (KATO III, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +4.7 | 1e-04 | 9/30 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +4.4 | 7e-04 | 11/43 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +4.2 | 0.001 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.61×** | +4.1 | 0.002 | 4/43 (NCI-H460, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +4.1 | 0.002 | 7/31 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.002 | 10/43 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +3.5 | 0.017 | 7/39 (C-33 A, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +3.0 | 0.093 | 5/45 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Monocrotaline (drug)]] 0.05 µM |  | **1.45×** | +3.0 | 0.094 | 2/24 (COLO 205, HOP62) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15183.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.145×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Erdafitinib (drug)]] 0.05 µM in 1 line (A498 0.0599×); [[NG25 (drug)]] 0.05 µM in 1 line (NCI-H460 0.0649×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.532×** | -5.5 | 2e-05 | 18/41 (SW480, HT-29, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.559×** | -5.1 | 1e-04 | 19/46 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.665×** | -3.6 | 0.070 | 13/38 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | 0.688× | -3.3 | 0.15 | 7/19 (PANC-1, HOP62, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | 0.692× | -3.1 | 0.22 | 11/17 (PANC-1, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15183. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 4.58 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A498 (line)]] | wt | 2.43 | 0 | 1 | — | [[Erdafitinib (drug)]] 0.05 µM 0.0599× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 1.93 | 0 | 1 | — | [[NG25 (drug)]] 0.05 µM 0.0649× (z -8.8) |
| [[A-172 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.825 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.915 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.930 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15183), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSMCE1-DT]] | +0.71 | +0.79 / +0.64 | both halves | 7e-06 |  |
| [[GTF2IP5]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[KDM4D]] | +0.69 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[TAS2R4]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ZNF529-AS1]] | +0.64 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[DDX59-AS1]] | +0.64 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[THBS4]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[DMXL1-DT]] | +0.64 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[TMEM30A-DT]] | +0.63 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[GOT1-DT]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ATE1OSP]] | +0.62 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[PSMD14-DT]] | +0.62 | +0.69 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2E]] | -0.54 | -0.20 / -0.46 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF12]] | C | ACTG1P17's natural level strengthens ZNF12's drug response | ACTG1P17's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.07; direction not clear | 0.060 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (5.1, 21.9); signed map (31.9, -6.9). **Vector** length 40.1, 4.28% of its response variance represented; |z| ≥ 3 in 1,031 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.4 | +9.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.7 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.1 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | -0.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.6 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.4 | +4.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.4 | +3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -0.9 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | actin gamma 1 pseudogene 17 |
| Locus type | pseudogene |
| Location | 15q25.2 — chr15:82,726,307-82,727,425 (-) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51497](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51497) · Entrez [283693](https://www.ncbi.nlm.nih.gov/gene/283693) · Ensembl [ENSG00000259315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259315)

## Data

Gene col 15183: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15183); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15183, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15183]; `tensor/DDL_lfc|DDL_z.npy` [15183]; `embed/gene_vectors.npy` [15183]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15183 or target_col == 15183). Every well: [[ACTG1P17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTG1P17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

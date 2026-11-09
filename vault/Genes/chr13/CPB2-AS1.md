---
symbol: "CPB2-AS1"
type: "gene"
col: 14047
ensembl_id: "ENSG00000235903"
name: "CPB2 antisense RNA 1"
location: "13q14.13"
module: 35
arm: "+"
pooled_cpm: 3.58
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# CPB2-AS1

*CPB2 antisense RNA 1* — 13q14.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.06× (z +17.1, q 0e+00, up in 31 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.177×; ⚠ toxic; transcription drop); [[Vitamin K4 (drug)]] 0.5 µM in 1 line (A-427 0.0722×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0835×); [[Talc (drug)]] 0.5 µM in 1 line (LoVo 0.0716×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX19A-DT]] (+0.63, fdr 2e-05), [[ANKHD1-DT]] (+0.63, fdr 1e-05), [[DNAJC9-AS1-1]] (+0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14047.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.06×** | +17.1 | 0e+00 | 31/35 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.80×** | +10.8 | 9e-25 | 3/7 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +10.7 | 2e-24 | 25/38 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.55×** | +10.6 | 3e-24 | 32/47 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +10.3 | 7e-23 | 3/5 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +10.1 | 5e-22 | 10/16 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.43×** | +9.7 | 3e-20 | 15/32 (SW480, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +8.5 | 1e-15 | 9/17 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +7.9 | 1e-13 | 17/36 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +7.9 | 1e-13 | 26/47 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.94×** | +7.5 | 2e-12 | 20/42 (SW480, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +7.2 | 2e-11 | 14/36 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.76×** | +6.4 | 7e-09 | 23/44 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.3 | 5e-06 | 11/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +5.0 | 2e-05 | 5/46 (NCI-H460, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +4.3 | 7e-04 | 11/42 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.001 | 10/46 (SW480, C-33 A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +4.1 | 0.001 | 9/45 (LoVo, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belzutifan (drug)]] 5 µM |  | **1.94×** | +3.9 | 0.003 | 1/24 (LoVo) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.003 | 5/42 (LoVo, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14047.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 0.177×; ⚠ toxic; transcription drop); [[Vitamin K4 (drug)]] 0.5 µM in 1 line (A-427 0.0722×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0835×); [[Talc (drug)]] 0.5 µM in 1 line (LoVo 0.0716×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.721× | -3.7 | 0.10 | 16/43 (NCI-H1573, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.755× | -3.2 | 0.38 | 11/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14047. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 8.24 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 3.33 | 0 | 1 | — | [[Vitamin K4 (drug)]] 0.5 µM 0.0722× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 3.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.33× (z +8.8) | — |
| [[LoVo (line)]] | wt | 2.66 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.0716× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 4.35 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0835× (z -9.0) |
| [[A-172 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14047), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX19A-DT]] | +0.63 | +0.70 / +0.47 | both halves | 2e-05 |  |
| [[ANKHD1-DT]] | +0.63 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[DNAJC9-AS1-1]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 | same gene group |
| [[LINC01618]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[RAD9B]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[DNAH10]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[PPP1R42]] | +0.62 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[PSMD14-DT]] | +0.62 | +0.70 / +0.50 | both halves | 1e-05 |  |
| [[CFAP20DC-AS1]] | +0.62 | +0.46 / +0.48 | both halves | 3e-05 | same gene group |
| [[ESR2]] | +0.61 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[PECAM1]] | +0.61 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[KCNAB1]] | +0.61 | +0.68 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CPB2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.565). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (12.1, 22.4); signed map (29.2, 0.7). **Vector** length 40.9, 4.04% of its response variance represented; |z| ≥ 3 in 1,062 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +17.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +7.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +10.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +3.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.4 | +3.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.1 | -3.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | +1.6 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.9 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -0.8 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | CPB2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q14.13 — chr13:46,052,497-46,161,379 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100509894](https://www.ncbi.nlm.nih.gov/gene/100509894):

> Predicted to be involved in miRNA-mediated post-transcriptional gene silencing. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:39898](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39898) · Entrez [100509894](https://www.ncbi.nlm.nih.gov/gene/100509894) · Ensembl [ENSG00000235903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235903)

## Data

Gene col 14047: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14047); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14047, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14047]; `tensor/DDL_lfc|DDL_z.npy` [14047]; `embed/gene_vectors.npy` [14047]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14047 or target_col == 14047). Every well: [[CPB2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPB2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

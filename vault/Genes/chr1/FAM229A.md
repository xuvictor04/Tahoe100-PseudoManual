---
symbol: "FAM229A"
type: "gene"
col: 13489
ensembl_id: "ENSG00000225828"
name: "family with sequence similarity 229 member A"
location: "1p35.1"
module: 37
arm: "+"
pooled_cpm: 2.25
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# FAM229A

*family with sequence similarity 229 member A* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +8.7, q 1e-15, up in 21 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.463× (z -6.2, q 4e-07, down in 23 of 43 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.605× (z -4.0, q 0.017, down in 14 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0564×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC17]] (+0.65, fdr 1e-05), [[ECT2L]] (+0.63, fdr 9e-06), [[TNXB]] (+0.62, fdr 1e-05); moves opposite to [[AGGF1]] (-0.58, fdr 3e-05), [[SERBP1]] (-0.57, fdr 1e-05), [[PAK1IP1]] (-0.57, fdr 3e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13489.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +8.7 | 1e-15 | 21/31 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +7.0 | 7e-10 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +6.2 | 1e-07 | 2/12 (NCI-H2347, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.97×** | +4.7 | 3e-04 | 3/4 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +4.4 | 0.001 | 7/27 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.7 | 0.017 | 3/18 (NCI-H2030, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +3.7 | 0.017 | 6/43 (SW48, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.072 | 5/26 (PANC-1, CFPAC-1, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.084 | 7/33 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.084 | 2/42 (HEC-1-A, NCI-H1573) | two highest doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13489.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0564×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.463×** | -6.2 | 4e-07 | 23/43 (MIA PaCa-2, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.605×** | -4.0 | 0.017 | 14/43 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.617×** | -3.7 | 0.041 | 11/39 (SNU-423, Hs 766T, …) | rises with dose | composition shift; position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | 0.561× | -3.3 | 0.13 | 3/43 (H4, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.465× | -3.2 | 0.13 | 11/37 (COLO 205, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.670× | -3.2 | 0.13 | 7/43 (LoVo, SW 900, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13489. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 3.14 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0564× (z -8.7) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13489), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC17]] | +0.65 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[ECT2L]] | +0.63 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[TNXB]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[RNF44]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ADCY10]] | +0.61 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[PAQR6]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TEPSIN]] | +0.60 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[LENG8]] | +0.58 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[EFCAB12]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[MTCH1]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CFAP410]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[RAB5B]] | +0.57 | +0.48 / +0.63 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGGF1]] | -0.58 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[SERBP1]] | -0.57 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[PAK1IP1]] | -0.57 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[EID1]] | -0.54 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[TAF1B]] | -0.53 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[SLX4IP]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[TIGD2]] | -0.53 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[KLHL9]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[MAGEF1]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[COMMD8]] | -0.52 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[UTP14A]] | -0.51 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[CFAP298]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FAM229A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.5, -23.0); signed map (8.3, 2.8). **Vector** length 48.2, 5.95% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +6.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +2.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +2.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.1 | -3.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -6.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -0.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 229 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:32,361,270-32,364,278 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [H3BQW9](https://www.uniprot.org/uniprotkb/H3BQW9) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44652) · Entrez [100128071](https://www.ncbi.nlm.nih.gov/gene/100128071) · UniProt [H3BQW9](https://www.uniprot.org/uniprotkb/H3BQW9) · Ensembl [ENSG00000225828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225828)

## Data

Gene col 13489: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13489); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13489, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13489]; `tensor/DDL_lfc|DDL_z.npy` [13489]; `embed/gene_vectors.npy` [13489]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13489 or target_col == 13489). Every well: [[FAM229A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM229A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

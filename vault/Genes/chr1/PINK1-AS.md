---
symbol: "PINK1-AS"
type: "gene"
col: 3887
ensembl_id: "ENSG00000117242"
name: "PINK1 antisense RNA"
location: "1p36.12"
module: 15
arm: "+"
pooled_cpm: 3.21
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PINK1-AS

*PINK1 antisense RNA* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +12.4, q 1e-32, up in 29 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.593× (z -6.1, q 7e-07, down in 17 of 45 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF213-AS1]] (+0.62, fdr 1e-05), [[FAM184B]] (+0.61, fdr 1e-05), [[CNPY2-AS1]] (+0.61, fdr 2e-05); moves opposite to [[SSNA1]] (-0.51, fdr 3e-04), [[RPUSD3]] (-0.50, fdr 3e-04), [[MRPL12]] (-0.50, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3887.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +12.4 | 1e-32 | 29/39 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.10×** | +12.1 | 5e-31 | 6/6 (HS-578T, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.86×** | +11.7 | 3e-29 | 4/6 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +10.2 | 3e-22 | 13/17 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +6.3 | 3e-08 | 14/37 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +6.1 | 9e-08 | 12/47 (LS 180, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +4.5 | 5e-04 | 8/43 (RPMI-7951, AN3 CA, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +4.3 | 0.001 | 5/39 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.1 | 0.003 | 4/20 (NCI-H1792, KATO III, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.0 | 0.003 | 6/45 (HS-578T, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.005 | 4/31 (RPMI-7951, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.007 | 11/38 (HS-578T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.007 | 8/35 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.3 | 0.034 | 0/7 | top dose only | noisy plate (z scaled); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.034 | 0/47 | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.081 | 8/43 (SNU-423, A549, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.084 | 1/45 (C32) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3887.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.593×** | -6.1 | 7e-07 | 17/45 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.604×** | -5.6 | 5e-06 | 14/43 (RPMI-7951, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.697×** | -4.2 | 0.005 | 10/42 (SW1417, AsPC-1, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -3.8 | 0.019 | 11/48 (A549, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3887. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 4.60 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.94× (z +9.9) | [[Verteporfin (drug)]] 5 µM 0.0749× (z -9.8) |
| [[J82 (line)]] | alt | 2.52 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.05 µM 0.0594× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 2.27 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 3.56 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0846× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 2.30 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0722× (z -10.2) |
| [[A-172 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.98 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3887), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF213-AS1]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 | same gene group |
| [[FAM184B]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CNPY2-AS1]] | +0.61 | +0.61 / +0.48 | both halves | 2e-05 | same gene group |
| [[LAMTOR5-AS1]] | +0.60 | +0.46 / +0.57 | both halves | 3e-05 | same gene group |
| [[DDX19A-DT]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ZNF596]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[GTF3C2-AS2]] | +0.57 | +0.42 / +0.62 | both halves | 4e-05 | same gene group |
| [[SNHG10]] | +0.57 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[SARM1]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[LMAN2]] | +0.56 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[PEBP4]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[RBM15-AS1]] | +0.56 | +0.43 / +0.50 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSNA1]] | -0.51 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[RPUSD3]] | -0.50 | -0.29 / -0.41 | both halves | 3e-04 |  |
| [[MRPL12]] | -0.50 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[KRI1]] | -0.49 | -0.13 / -0.51 | ⚠ one half (not replicated) | 0.002 |  |
| [[TUBG2]] | -0.49 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[PUSL1]] | -0.48 | -0.40 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PINK1-AS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.475). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (11.4, 23.5); signed map (30.0, -0.4). **Vector** length 44.2, 4.47% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +12.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +12.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.2 | +0.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -6.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.1 | -2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Busulfan (drug)]] 5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | PINK1 antisense RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p36.12 — chr1:20,642,657-20,652,193 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ00387, PINK1AS, naPINK1; previously PINK1-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:38872](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:38872) · Entrez [100861548](https://www.ncbi.nlm.nih.gov/gene/100861548) · Ensembl [ENSG00000117242](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117242)

## Data

Gene col 3887: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3887); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3887, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3887]; `tensor/DDL_lfc|DDL_z.npy` [3887]; `embed/gene_vectors.npy` [3887]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3887 or target_col == 3887). Every well: [[PINK1-AS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PINK1-AS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

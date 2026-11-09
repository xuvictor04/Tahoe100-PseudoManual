---
symbol: "MPHOSPH8"
type: "gene"
col: 12152
ensembl_id: "ENSG00000196199"
name: "M-phase phosphoprotein 8"
location: "13q12.11"
module: 12
arm: "+"
pooled_cpm: 96.84
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MPHOSPH8

*M-phase phosphoprotein 8* — 13q12.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.40× (z +6.3, q 2e-07, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.529× (z -8.3, q 4e-14, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIR1]] (+0.77, fdr 7e-06), [[FRG1]] (+0.75, fdr 7e-06), [[ZMYM5]] (+0.73, fdr 7e-06); moves opposite to [[EIF5A]] (-0.70, fdr 7e-06), [[NUP188]] (-0.68, fdr 1e-05), [[VMA21]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZMYM5]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12152.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +6.3 | 2e-07 | 36/49 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.9 | 3e-04 | 39/47 (NCI-H1573, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +4.6 | 1e-03 | 36/48 (KATO III, Hs 766T, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.013 | 33/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.28× | +3.3 | 0.12 | 26/49 (PANC-1, J82, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.27× | +3.2 | 0.15 | 30/48 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12152.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.529×** | -8.3 | 4e-14 | 46/48 (SNU-423, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.608×** | -6.5 | 2e-08 | 42/48 (SNU-423, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.639×** | -5.9 | 9e-07 | 43/48 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.689×** | -4.9 | 1e-04 | 37/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.690×** | -4.8 | 1e-04 | 35/48 (SNU-423, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.726×** | -4.2 | 0.003 | 34/47 (SW480, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12152. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 353 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.350× (z -10.4) |
| [[SNU-423 (line)]] | alt | 103 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 88.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.375× (z -9.6) |
| [[HT-29 (line)]] | alt | 212 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +9.0) | [[Digitoxin (drug)]] 0.5 µM 0.469× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 84.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.311× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.336× (z -8.8) |
| [[SW 1088 (line)]] | alt | 101 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0714× (z -10.4) |
| [[HOP62 (line)]] | alt | 86.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.416× (z -9.4) |
| [[Hs 766T (line)]] | wt | 174 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.450× (z -8.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 113 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 40.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.6) | — |
| [[NCI-H596 (line)]] | alt | 104 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.143× (z -10.7) |
| [[PANC-1 (line)]] | alt | 63.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +11.4) | — |
| [[A-172 (line)]] | wt | 91.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 72.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 99.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 64.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 119 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 103 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 60.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 123 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 97.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 131 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 100 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 65.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 63.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 120 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 85.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 98.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 157 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12152), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIR1]] | +0.77 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[FRG1]] | +0.75 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[ZMYM5]] | +0.73 | +0.72 / +0.75 | both halves | 7e-06 |  |
| [[SYF2]] | +0.71 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[CWC15]] | +0.71 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[EAPP]] | +0.70 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.70 | +0.61 / +0.81 | both halves | 7e-06 |  |
| [[TRIM23]] | +0.67 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[PPIG]] | +0.67 | +0.71 / +0.63 | both halves | 7e-06 | STRING 442 |
| [[ANKRD49]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 | same gene group |
| [[RBMX2]] | +0.66 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[SNHG32]] | +0.65 | +0.70 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF5A]] | -0.70 | -0.68 / -0.67 | both halves | 7e-06 |  |
| [[NUP188]] | -0.68 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[VMA21]] | -0.68 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[SIGMAR1]] | -0.67 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[PRKDC]] | -0.64 | -0.53 / -0.68 | both halves | 1e-05 |  |
| [[PRPS2]] | -0.64 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[FAM91A1]] | -0.63 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[UBE2G2]] | -0.62 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[GLB1L2]] | -0.62 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[MDH2]] | -0.62 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[AHCY]] | -0.60 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[PSME3]] | -0.60 | -0.47 / -0.72 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZMYM5]] | C | ZMYM5's natural level strengthens MPHOSPH8's drug response | ZMYM5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.44; direction not clear | 0.084 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-34.1, -29.0); signed map (-14.4, -5.5). **Vector** length 117, 39.3% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +2.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.6 | +3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.3 | +1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.0 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +2.0 |
|  | [[MK-3903 (drug)]] 5 µM |  | +2.8 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.1 | -5.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.5 | -8.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.4 | -6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.9 | -4.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.5 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -1.7 |
|  | [[Volasertib (drug)]] 0.5 µM |  | -2.9 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.5 µM |  | -2.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | M-phase phosphoprotein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.11 — chr13:19,633,659-19,673,441 (+) |
| Ensembl biotype | protein_coding |
| Also known as | mpp8, HSMPP8 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; HUSH complex |
| Reactome | 12 pathways, smallest: Regulation of endogenous retroelements by the Human Silencing Hub (HUSH) complex; Negative Regulation of CDH1 Gene Transcription; Regulation of CDH1 Gene Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99549](https://www.uniprot.org/uniprotkb/Q99549) (M-phase phosphoprotein 8):

> Heterochromatin component that specifically recognizes and binds methylated 'Lys-9' of histone H3 (H3K9me) and promotes recruitment of proteins that mediate epigenetic repression. As part of the HUSH complex, promotes epigenetic repression of mobile genetic elements, such as retroviruses and transposable elements: the HUSH complex mainly represses LINE-1 (L1) retrotransposons that are still capable of transposition. Silencing events often occur within introns of transcriptionally active genes, …

**Summary**, from NCBI Gene [54737](https://www.ncbi.nlm.nih.gov/gene/54737):

> Enables chromatin binding activity and histone H3K9me2/3 reader activity. Involved in negative regulation of gene expression via chromosomal CpG island methylation; negative regulation of type I interferon production; and transposable element silencing by heterochromatin formation. Located in cytoplasm; heterochromatin; and nucleoplasm. Part of HUSH complex; HUSH2 complex; and nucleosome. Is active in chromatin and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29810](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29810) · Entrez [54737](https://www.ncbi.nlm.nih.gov/gene/54737) · UniProt [Q99549](https://www.uniprot.org/uniprotkb/Q99549) · Ensembl [ENSG00000196199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196199)

## Data

Gene col 12152: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12152); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12152, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12152]; `tensor/DDL_lfc|DDL_z.npy` [12152]; `embed/gene_vectors.npy` [12152]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12152 or target_col == 12152). Every well: [[MPHOSPH8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MPHOSPH8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

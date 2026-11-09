---
symbol: "KLHL17"
type: "gene"
col: 11962
ensembl_id: "ENSG00000187961"
name: "kelch like family member 17"
location: "1p36.33"
module: 2
arm: "+"
pooled_cpm: 2.55
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# KLHL17

*kelch like family member 17* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.75× (z +4.6, q 0.002, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bosentan (hydrate) (drug)]] 5 µM: 1.64× (z +4.1, q 0.013, up in 7 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.514× (z -5.5, q 2e-05, down in 14 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC8]] (+0.78, fdr 7e-06), [[ABHD17A]] (+0.73, fdr 7e-06), [[CPSF1]] (+0.72, fdr 7e-06); moves opposite to [[TRIP11]] (-0.56, fdr 1e-05), [[BCL2L13]] (-0.55, fdr 3e-05), [[MCTS1]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[OSBPL7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11962.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +4.6 | 0.002 | 1/3 (HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.64×** | +4.1 | 0.013 | 7/27 (SW48, LOX-IMVI, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +3.8 | 0.032 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.047 | 11/46 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11962.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.514×** | -5.5 | 2e-05 | 14/33 (HEC-1-A, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.515×** | -5.4 | 2e-05 | 19/40 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.543×** | -5.2 | 4e-05 | 15/45 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.572×** | -4.8 | 3e-04 | 13/32 (PANC-1, LS 180, …) | two highest doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.581×** | -4.6 | 4e-04 | 12/43 (C-33 A, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -3.8 | 0.017 | 11/34 (MIA PaCa-2, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11962. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.25 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0562× (z -8.8) |
| [[HS-578T (line)]] | alt | 3.65 | 0 | 1 (1 ⚠) | — | [[Edoxaban (tosylate monohydrate) (drug)]] 0.5 µM 0.0632× (z -8.6) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 5.38 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.100× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.822 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11962), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC8]] | +0.78 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[ABHD17A]] | +0.73 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[CPSF1]] | +0.72 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[TUBGCP6]] | +0.72 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[UCKL1]] | +0.72 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[ABCA2]] | +0.71 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[INTS11]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[NBEAL2]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[TRABD]] | +0.68 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[JAG2]] | +0.68 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[LLGL1]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[TCF3]] | +0.67 | +0.64 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIP11]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[BCL2L13]] | -0.55 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[MCTS1]] | -0.55 | -0.55 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL7]] | B | OSBPL7 activity lowers KLHL17's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.46× higher at baseline in the lines without OSBPL7 | 0.086 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |
| [[SEPTIN5]] | B | SEPTIN5 activity raises KLHL17's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.37× lower at baseline in the lines without SEPTIN5 | 0.098 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[ARHGEF19]] | C | ARHGEF19 activity weakens KLHL17's drug response | lines that do not express ARHGEF19 (3) vs lines expressing it (43) | the lines without ARHGEF19 respond 1.31× as strongly (z diff -0.38); strongest at Harringtonine 0.5 µM: 0.24x vs 0.55x (z diff -2.4) | 0.088 | ⚠ few lines (3 vs 47); across organs; also absent: SLC35F2, ENSG00000274213; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.816). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.4, -23.8); signed map (-44.7, -10.7). **Vector** length 48.5, 5.61% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +2.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.2 | +2.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.2 | -5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -5.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.0 | -4.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -1.8 | -5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:960,584-965,719 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6TDP4](https://www.uniprot.org/uniprotkb/Q6TDP4) (Kelch-like protein 17):

> Substrate-recognition component of some cullin-RING-based BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complexes. The BCR(KLHL17) complex mediates the ubiquitination and subsequent degradation of GLUR6. May play a role in the actin-based neuronal function (By similarity).

**Summary**, from NCBI Gene [339451](https://www.ncbi.nlm.nih.gov/gene/339451):

> The protein encoded by this gene is expressed in neurons of most regions of the brain. It contains an N-terminal BTB domain, which mediates dimerization of the protein, and a C-terminal Kelch domain, which mediates binding to F-actin. This protein may play a key role in the regulation of actin-based neuronal function. [provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:24023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24023) · Entrez [339451](https://www.ncbi.nlm.nih.gov/gene/339451) · UniProt [Q6TDP4](https://www.uniprot.org/uniprotkb/Q6TDP4) · Ensembl [ENSG00000187961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187961)

## Data

Gene col 11962: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11962); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11962, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11962]; `tensor/DDL_lfc|DDL_z.npy` [11962]; `embed/gene_vectors.npy` [11962]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11962 or target_col == 11962). Every well: [[KLHL17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

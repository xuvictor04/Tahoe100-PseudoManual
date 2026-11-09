---
symbol: "HAPSTR1"
type: "gene"
col: 11331
ensembl_id: "ENSG00000182831"
name: "HUWE1 associated protein modifying stress responses"
location: "16p13.2"
module: 54
arm: "-"
pooled_cpm: 104.19
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# HAPSTR1

*HUWE1 associated protein modifying stress responses* — 16p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.64× (z +8.1, q 4e-13, up in 41 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Isocorydine (drug)]] 0.5 µM in 1 line (SW 1271 0.0720×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRAS]] (+0.65, fdr 7e-06), [[FLNA]] (+0.64, fdr 1e-05), [[UBA1]] (+0.63, fdr 7e-06); moves opposite to [[NDUFB1]] (-0.60, fdr 1e-05), [[SELENOH]] (-0.60, fdr 1e-04), [[LSM2]] (-0.60, fdr 2e-05).
> It sits in the **-** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11331.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +8.1 | 4e-13 | 41/48 (AsPC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.92×** | +6.4 | 3e-08 | 45/49 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +5.7 | 2e-06 | 38/48 (C32, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.44×** | +5.4 | 1e-05 | 44/48 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +4.4 | 0.001 | 37/48 (SW480, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.2 | 0.003 | 31/48 (SW480, SW1417, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.017 | 34/48 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +3.2 | 0.088 | 29/48 (NCI-H1792, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11331.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (C-33 A 0.149×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Isocorydine (drug)]] 0.5 µM in 1 line (SW 1271 0.0720×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.816× | -3.3 | 0.27 | 27/48 (SW480, SW 900, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.752× | -3.3 | 0.27 | 29/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.828× | -3.1 | 0.35 | 25/49 (Hs 766T, SK-MEL-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11331. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 83.8 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.53× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 255 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +14.7) | — |
| [[C32 (line)]] | wt | 90.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +13.0) | — |
| [[NCI-H460 (line)]] | wt | 76.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +8.6) | — |
| [[A498 (line)]] | wt | 146 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +12.9) | — |
| [[C-33 A (line)]] | alt | 80.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 97.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.3) | — |
| [[HOP62 (line)]] | alt | 89.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 79.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.6) | — |
| [[LoVo (line)]] | wt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 121 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 81.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 122 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 90.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.2) | — |
| [[SW 1271 (line)]] | alt | 76.3 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0720× (z -10.7) |
| [[SW1417 (line)]] | alt | 112 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.2) | — |
| [[A-172 (line)]] | wt | 117 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 107 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 98.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 106 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 109 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 136 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 101 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 95.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 124 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11331), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRAS]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[FLNA]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[UBA1]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[NORAD]] | +0.61 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[ACADVL]] | +0.60 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[G6PD]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ZNF460]] | +0.58 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CDC42]] | +0.58 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[ARF1]] | +0.58 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[MAPRE1]] | +0.58 | +0.33 / +0.69 | both halves | 1e-04 |  |
| [[LIN7C]] | +0.57 | +0.37 / +0.65 | both halves | 8e-05 |  |
| [[CDK9]] | +0.57 | +0.47 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 8 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFB1]] | -0.60 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[SELENOH]] | -0.60 | -0.36 / -0.68 | both halves | 1e-04 |  |
| [[LSM2]] | -0.60 | -0.48 / -0.69 | both halves | 2e-05 |  |
| [[MRPL23]] | -0.58 | -0.34 / -0.66 | both halves | 1e-04 |  |
| [[YBEY]] | -0.56 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[CHCHD1]] | -0.55 | -0.30 / -0.64 | both halves | 2e-04 |  |
| [[C15orf61]] ⚠ | -0.55 | -0.38 / -0.64 | both halves | 7e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COX5A]] ⚠ | -0.55 | -0.45 / -0.63 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CCDC66]] | -0.55 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[TUT4]] | -0.54 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[FDX2]] | -0.54 | -0.34 / -0.64 | both halves | 1e-04 |  |
| [[TRIM52-AS1]] | -0.54 | -0.31 / -0.61 | both halves | 2e-04 |  |
| [[KRTCAP2]] | -0.54 | -0.29 / -0.66 | both halves | 3e-04 |  |
| [[MZT2A]] | -0.53 | -0.35 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **-** arm (projection on the module's main direction -0.580). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.3, -20.2); signed map (-8.3, 33.4). **Vector** length 90.8, 28.9% of its response variance represented; |z| ≥ 3 in 700 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.9 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.6 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.5 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.2 | -1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.0 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.8 | +1.5 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | +1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | +1.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | +4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | +1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | +3.7 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.0 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.9 | -3.3 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.9 | -1.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | +0.1 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | HUWE1 associated protein modifying stress responses |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.2 — chr16:9,091,644-9,121,635 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ41272, PRO0149, TAPR1; previously C16orf72 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14CZ0](https://www.uniprot.org/uniprotkb/Q14CZ0) (HUWE1-associated protein modifying stress responses 1):

> Acts as a central player within a network of stress response pathways promoting cellular adaptability. The E3 ligase HUWE1 assists HAPSTR1 in controlling stress signaling and in turn, HUWE1 feeds back to promote the degradation of HAPSTR1. HAPSTR1 represents a central coordination mechanism for stress response programs. Functions as a negative regulator of TP53/P53 in the cellular response to telomere erosion and probably also DNA damage. May attenuate p53/TP53 activation through the E3 …

**Summary**, from NCBI Gene [29035](https://www.ncbi.nlm.nih.gov/gene/29035):

> Enables ubiquitin protein ligase binding activity. Involved in negative regulation of signal transduction by p53 class mediator and regulation of cellular response to stress. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30103](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30103) · Entrez [29035](https://www.ncbi.nlm.nih.gov/gene/29035) · UniProt [Q14CZ0](https://www.uniprot.org/uniprotkb/Q14CZ0) · Ensembl [ENSG00000182831](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182831)

## Data

Gene col 11331: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11331); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11331, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11331]; `tensor/DDL_lfc|DDL_z.npy` [11331]; `embed/gene_vectors.npy` [11331]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11331 or target_col == 11331). Every well: [[HAPSTR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAPSTR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

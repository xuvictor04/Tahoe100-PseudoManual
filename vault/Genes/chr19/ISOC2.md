---
symbol: "ISOC2"
type: "gene"
col: 724
ensembl_id: "ENSG00000063241"
name: "isochorismatase domain containing 2"
location: "19q13.42"
module: 40
arm: "+"
pooled_cpm: 11.02
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 7
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# ISOC2

*isochorismatase domain containing 2* — 19q13.42

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.87× (z +6.0, q 1e-06, up in 22 of 33 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.387× (z -12.8, q 8e-35, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDF2L1]] (+0.71, fdr 7e-06), [[SNHG18]] (+0.70, fdr 7e-06), [[TMEM243]] (+0.69, fdr 7e-06); moves opposite to [[CCDC50]] (-0.58, fdr 3e-05), [[CFLAR]] (-0.58, fdr 3e-05), [[SEPTIN7-DT]] (-0.56, fdr 9e-04, ⚠ one half only (not replicated)), [[LRRC37A3]] (-0.56, fdr 4e-04).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 724.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.87×** | +6.0 | 1e-06 | 22/33 (NCI-H460, J82, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.82×** | +5.7 | 4e-06 | 25/41 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.63×** | +4.5 | 0.002 | 7/17 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.40× | +3.2 | 0.21 | 14/43 (KATO III, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Arbutin (drug)]] 5 µM |  | 1.39× | +3.0 | 0.29 | 6/44 (HOP62, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 724.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.387×** | -12.8 | 8e-35 | 38/45 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.486×** | -6.9 | 2e-09 | 28/42 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.507×** | -6.2 | 9e-08 | 32/46 (KATO III, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.582×** | -5.2 | 3e-05 | 26/45 (A-427, H4, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.622×** | -4.5 | 6e-04 | 25/46 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.647×** | -3.4 | 0.070 | 15/46 (A-172, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.709×** | -3.3 | 0.080 | 18/48 (KATO III, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.793× | -3.2 | 0.11 | 22/43 (H4, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.793× | -3.1 | 0.11 | 13/48 (HCT15, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 724. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 17.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -14.8) |
| [[A498 (line)]] | wt | 42.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -11.9) |
| [[HT-29 (line)]] | alt | 18.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -12.8) |
| [[PANC-1 (line)]] | alt | 22.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 6.23 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -10.7) |
| [[HOP62 (line)]] | alt | 7.92 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -8.7) |
| [[J82 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 8.53 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -8.8) |
| [[SW480 (line)]] | alt | 9.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -9.2) |
| [[A-172 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 724), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDF2L1]] | +0.71 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SNHG18]] | +0.70 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[TMEM243]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[MRPL55]] | +0.67 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[SEC13]] | +0.66 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[COG5]] | +0.66 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[SIVA1]] | +0.66 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[SSR2]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.65 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[COX14]] | +0.64 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[CYB561D2]] | +0.64 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[COG6]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC50]] | -0.58 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[CFLAR]] | -0.58 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[SEPTIN7-DT]] | -0.56 | -0.62 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[LRRC37A3]] | -0.56 | -0.55 / -0.26 | both halves | 4e-04 |  |
| [[IL6ST]] | -0.56 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[ANKLE2]] | -0.55 | -0.48 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (15.9, -34.4); signed map (-47.9, 9.3). **Vector** length 65.9, 13.3% of its response variance represented; |z| ≥ 3 in 621 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.3 | +1.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +1.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +2.8 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.0 | +3.2 |
|  | [[Arbutin (drug)]] 5 µM |  | +0.9 | +3.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +0.9 | +1.8 |
|  | [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | +0.9 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -12.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -6.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | isochorismatase domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.42 — chr19:55,452,985-55,462,343 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23469 |
| Matched by | ensembl_id |

UniProt [Q96AB3](https://www.uniprot.org/uniprotkb/Q96AB3) carries no function annotation.

**Summary**, from NCBI Gene [79763](https://www.ncbi.nlm.nih.gov/gene/79763):

> Involved in protein destabilization. Located in cytosol and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26278](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26278) · Entrez [79763](https://www.ncbi.nlm.nih.gov/gene/79763) · UniProt [Q96AB3](https://www.uniprot.org/uniprotkb/Q96AB3) · Ensembl [ENSG00000063241](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000063241)

## Data

Gene col 724: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 724); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 724, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 724]; `tensor/DDL_lfc|DDL_z.npy` [724]; `embed/gene_vectors.npy` [724]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 724 or target_col == 724). Every well: [[ISOC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ISOC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

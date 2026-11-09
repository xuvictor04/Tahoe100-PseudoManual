---
symbol: "SPATA24"
type: "gene"
col: 9958
ensembl_id: "ENSG00000170469"
name: "spermatogenesis associated 24"
location: "5q31.2"
module: 23
arm: "+"
pooled_cpm: 2.31
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# SPATA24

*spermatogenesis associated 24* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.45× (z +9.1, q 5e-17, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Temsirolimus (drug)]] 0.5 µM: 1.43× (z +4.0, q 0.007, up in 8 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.652× (z -4.7, q 0.002, down in 8 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEN1]] (+0.57, fdr 4e-05), [[TSC1]] (+0.57, fdr 2e-05), [[GPRASP3]] (+0.55, fdr 1e-05); moves opposite to [[SRPK1]] (-0.53, fdr 4e-05), [[TEX2]] (-0.50, fdr 1e-04), [[CDYL2]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9958.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.45×** | +9.1 | 5e-17 | 1/3 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +8.7 | 9e-16 | 1/3 (A498) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +5.9 | 9e-07 | 5/13 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.49×** | +4.4 | 0.001 | 2/39 (C32, Panc 03.27) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.4 | 0.001 | 5/48 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.007 | 8/25 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.009 | 4/40 (A498, HT-29, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.018 | 2/34 (SW480, SW1417) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.24× | +3.2 | 0.10 | 3/44 (SW480, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.26× | +3.1 | 0.11 | 5/41 (A-427, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.22× | +3.1 | 0.11 | 1/44 (C-33 A) | two highest doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9958.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.652×** | -4.7 | 0.002 | 8/42 (LOX-IMVI, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.695×** | -4.0 | 0.018 | 6/29 (LoVo, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.719×** | -3.5 | 0.080 | 8/25 (SW480, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.733×** | -3.4 | 0.080 | 9/40 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[8-Hydroxyquinoline (drug)]] 5 µM |  | **0.807×** | -3.3 | 0.080 | 5/46 (SW 1271, RKO, …) | top dose only |  |
| [[Bexarotene (drug)]] 0.5 µM |  | **0.739×** | -3.3 | 0.080 | 4/43 (NCI-H1792, H4, …) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | **0.740×** | -3.3 | 0.080 | 3/41 (KATO III, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9958. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 2.14 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0512× (z -9.0) ⚠ cell-cycle shift, explains ~67% of this change |
| [[A-172 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.896 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.876 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9958), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEN1]] | +0.57 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[TSC1]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[GPRASP3]] | +0.55 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[CDK3]] | +0.54 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[CFAP410]] | +0.54 | +0.39 / +0.47 | both halves | 6e-05 |  |
| [[NAPA-AS1]] | +0.53 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[UFC1]] | +0.53 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[CD72]] | +0.53 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[DAZAP2]] | +0.52 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[KCP]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[PNISR]] | +0.52 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[NRL]] | +0.51 | +0.65 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPK1]] | -0.53 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[TEX2]] | -0.50 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[CDYL2]] | -0.49 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[BRI3BP]] | -0.49 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[SNTB2]] | -0.49 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[KIF2A]] | -0.48 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[ASAP2]] | -0.48 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[TTC13]] | -0.47 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[RALB]] | -0.47 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[MCM6]] | -0.46 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[ABTB3]] | -0.46 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[ACTL6A]] | -0.46 | -0.39 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.437). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-3.6, 29.8); signed map (-1.1, -5.8). **Vector** length 30.7, 2.40% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +2.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.7 | +5.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +1.5 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.0 | +2.6 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +0.8 | +3.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.7 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.7 | -4.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.2 | -3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.7 | -0.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -0.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | spermatogenesis associated 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:139,396,563-139,404,089 (-) |
| Ensembl biotype | protein_coding |
| Also known as | T6441, CCDC161 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86W54](https://www.uniprot.org/uniprotkb/Q86W54) (Spermatogenesis-associated protein 24):

> Binds DNA with high affinity but does not bind to TATA boxes. Synergises with GMNN and TBP in activation of TATA box-containing promoters and with GMNN and TBPL1 in activation of the NF1 TATA-less promoter. May play a role in cytoplasm movement and removal during spermiogenesis (By similarity).

**Summary**, from NCBI Gene [202051](https://www.ncbi.nlm.nih.gov/gene/202051):

> Predicted to enable DNA binding activity. Predicted to be involved in DNA-templated transcription; cell differentiation; and spermatogenesis. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27322](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27322) · Entrez [202051](https://www.ncbi.nlm.nih.gov/gene/202051) · UniProt [Q86W54](https://www.uniprot.org/uniprotkb/Q86W54) · Ensembl [ENSG00000170469](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170469)

## Data

Gene col 9958: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9958); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9958, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9958]; `tensor/DDL_lfc|DDL_z.npy` [9958]; `embed/gene_vectors.npy` [9958]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9958 or target_col == 9958). Every well: [[SPATA24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPATA24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

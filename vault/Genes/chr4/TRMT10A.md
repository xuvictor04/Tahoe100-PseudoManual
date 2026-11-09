---
symbol: "TRMT10A"
type: "gene"
col: 6974
ensembl_id: "ENSG00000145331"
name: "tRNA methyltransferase 10A"
location: "4q23"
module: 83
arm: "+"
pooled_cpm: 6.64
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# TRMT10A

*tRNA methyltransferase 10A* — 4q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.29× (z +15.9, q 0e+00, up in 29 of 30 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +8.3, q 1e-14, up in 28 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (A549 0.0896×; ⚠ toxic); [[Clofarabine (drug)]] 5 µM in 1 line (BT-474 0.0676×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP16]] (+0.68, fdr 1e-05), [[RABL3]] (+0.64, fdr 2e-05), [[SON]] (+0.60, fdr 5e-05); moves opposite to [[GRAMD4]] (-0.52, fdr 5e-04), [[NTAQ1]] (-0.51, fdr 9e-05), [[TSFM]] (-0.51, fdr 1e-04).
> It sits in the **+** arm of [[Module 083]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6974.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.29×** | +15.9 | 0e+00 | 29/30 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.86×** | +13.5 | 4e-39 | 7/9 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.51×** | +10.7 | 2e-24 | 16/19 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +8.3 | 1e-14 | 28/43 (NCI-H1792, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +7.1 | 1e-10 | 19/45 (A-427, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.41×** | +6.5 | 5e-09 | 21/42 (LS 180, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.53×** | +5.7 | 1e-06 | 20/47 (LS 180, NCI-H1573, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.50×** | +5.4 | 4e-06 | 21/43 (LoVo, RKO, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.49×** | +5.3 | 7e-06 | 19/45 (LS 180, A-427, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.43×** | +4.8 | 1e-04 | 16/42 (LS 180, RKO, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.40×** | +4.5 | 4e-04 | 12/45 (SNU-1, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.1 | 0.002 | 11/33 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +3.8 | 0.008 | 11/45 (HEC-1-A, KATO III, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.008 | 8/44 (CFPAC-1, LS 180, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.32×** | +3.6 | 0.013 | 14/45 (RKO, NCI-H2347, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +3.5 | 0.017 | 9/44 (LS 180, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.039 | 6/45 (KATO III, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (A549 0.0896×; ⚠ toxic); [[Clofarabine (drug)]] 5 µM in 1 line (BT-474 0.0676×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6974. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 5.68 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0896× (z -10.2) ⚠ toxic |
| [[BT-474 (line)]] | alt | 7.00 | 0 | 1 | — | [[Clofarabine (drug)]] 5 µM 0.0676× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 9.16 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 7.72 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6974), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP16]] | +0.68 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[RABL3]] | +0.64 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[SON]] | +0.60 | +0.68 / +0.40 | both halves | 5e-05 |  |
| [[FBXL19-AS1]] | +0.59 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[ZC3H11A]] | +0.59 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[C11orf58]] | +0.59 | +0.66 / +0.33 | both halves | 1e-04 |  |
| [[ATRX]] | +0.59 | +0.67 / +0.41 | both halves | 4e-05 |  |
| [[NQO1-DT]] | +0.58 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[ZC2HC1C]] | +0.58 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[PPP4R3B]] | +0.57 | +0.60 / +0.37 | both halves | 8e-05 |  |
| [[ZBTB40]] | +0.57 | +0.67 / +0.26 | both halves | 3e-04 |  |
| [[LINC02307]] | +0.56 | +0.59 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRAMD4]] | -0.52 | -0.59 / -0.24 | both halves | 5e-04 |  |
| [[NTAQ1]] | -0.51 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[TSFM]] | -0.51 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[SLC15A4]] | -0.51 | -0.53 / -0.36 | both halves | 1e-04 |  |
| [[TMEM120B]] | -0.49 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[MFSD14CP]] | -0.49 | -0.56 / -0.38 | both halves | 7e-05 |  |
| [[WASF3]] | -0.49 | -0.52 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[RNF4]] | -0.49 | -0.59 / -0.29 | both halves | 2e-04 |  |
| [[TRIM35]] | -0.49 | -0.41 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.285). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-23.0, 10.9); signed map (12.9, -29.1). **Vector** length 51.9, 6.53% of its response variance represented; |z| ≥ 3 in 840 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +15.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +13.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +10.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +3.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +1.9 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | +1.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.3 | -2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[NVP-BHG712 (drug)]] 0.05 µM |  | -1.1 | -0.3 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -1.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase 10A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q23 — chr4:99,546,709-99,564,039 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC27034, TRM10; previously RG9MTD2 |
| Gene groups (HGNC) | SPOUT methyltransferase domain containing; DNA/RNA methyltransferases |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBZ6](https://www.uniprot.org/uniprotkb/Q8TBZ6) (tRNA methyltransferase 10 homolog A):

> S-adenosyl-L-methionine-dependent guanine N(1)-methyltransferase that catalyzes the formation of N(1)-methylguanine at position 9 (m1G9) in tRNAs. Probably not able to catalyze formation of N(1)-methyladenine at position 9 (m1A9) in tRNAs.

**Summary**, from NCBI Gene [93587](https://www.ncbi.nlm.nih.gov/gene/93587):

> This gene encodes a protein that belongs to the tRNA (Guanine-1)-methyltransferase family. A similar gene in yeast modifies several different tRNA species. Mutations in this gene are associated with microcephaly, short stature, and impaired glucose metabolism. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2014]

**Accessions** — [HGNC:28403](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28403) · Entrez [93587](https://www.ncbi.nlm.nih.gov/gene/93587) · UniProt [Q8TBZ6](https://www.uniprot.org/uniprotkb/Q8TBZ6) · Ensembl [ENSG00000145331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145331)

## Data

Gene col 6974: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6974); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6974, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6974]; `tensor/DDL_lfc|DDL_z.npy` [6974]; `embed/gene_vectors.npy` [6974]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6974 or target_col == 6974). Every well: [[TRMT10A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT10A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

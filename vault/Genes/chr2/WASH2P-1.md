---
symbol: "WASH2P-1"
type: "gene"
col: 16597
ensembl_id: "ENSG00000291134"
name: ""
location: ""
module: 15
arm: "+"
pooled_cpm: 3.31
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# WASH2P-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.76× (z +8.7, q 2e-15, up in 5 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +6.7, q 7e-09, up in 21 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.631× (z -4.3, q 0.011, down in 17 of 45 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Furosemide (drug)]] 0.5 µM: 0.659× (z -3.9, q 0.016, down in 16 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSSK3]] (+0.70, fdr 8e-06), [[SPRYD4]] (+0.68, fdr 7e-06), [[GTF3C2-AS2]] (+0.68, fdr 1e-05); moves opposite to [[SLC9A3R1]] (-0.55, fdr 1e-04), [[MAPRE2]] (-0.53, fdr 1e-04), [[USP2]] (-0.53, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16597.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +8.7 | 2e-15 | 5/7 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.7 | 7e-09 | 21/36 (LOX-IMVI, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +6.1 | 2e-07 | 11/17 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.53×** | +5.6 | 4e-06 | 7/44 (PANC-1, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.4 | 6e-06 | 2/4 (PANC-1, HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.67×** | +4.7 | 2e-04 | 9/34 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.009 | 5/44 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +3.7 | 0.014 | 4/18 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.5 | 0.030 | 5/48 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.41× | +3.1 | 0.12 | 8/31 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pentagastrin (drug)]] 5 µM |  | 1.26× | +3.0 | 0.12 | 1/48 (HEC-1-A) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16597.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.631×** | -4.3 | 0.011 | 17/45 (SW480, SHP-77, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.633×** | -4.1 | 0.011 | 19/43 (Panc 03.27, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.647×** | -4.0 | 0.011 | 15/44 (HepG2/C3A, NCI-H1792, …) | all doses, flat |  |
| [[Furosemide (drug)]] 0.5 µM |  | **0.659×** | -3.9 | 0.016 | 16/41 (PANC-1, A549, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.665×** | -3.8 | 0.019 | 11/45 (SW480, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.690×** | -3.4 | 0.058 | 5/44 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Esmolol (hydrochloride) (drug)]] 0.5 µM |  | **0.700×** | -3.3 | 0.080 | 13/41 (HT-29, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Cysteamine (hydrochloride) (drug)]] 0.5 µM |  | 0.712× | -3.1 | 0.12 | 15/38 (RKO, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.717× | -3.1 | 0.13 | 7/44 (PANC-1, NCI-H1792, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16597. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 8.21 | 0 | 1 | — | [[Larotrectinib (drug)]] 0.5 µM 0.0705× (z -8.9) |
| [[LS 180 (line)]] | wt | 3.89 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.05 µM 0.0536× (z -8.9) |
| [[SHP-77 (line)]] | alt | 5.14 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0800× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16597), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSSK3]] | +0.70 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[SPRYD4]] | +0.68 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[GTF3C2-AS2]] | +0.68 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[MIR762HG]] | +0.67 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[CNPY2-AS1]] | +0.66 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[ZNF596]] | +0.65 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[ZBTB26]] | +0.65 | +0.37 / +0.57 | both halves | 7e-05 |  |
| [[ZNF236-DT]] | +0.65 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R42]] | +0.63 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[DNAJC30]] | +0.62 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[STARD7-AS1]] | +0.62 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[ZNF213-AS1]] | +0.62 | +0.47 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A3R1]] | -0.55 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[MAPRE2]] | -0.53 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[USP2]] | -0.53 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[PPP1CC]] | -0.52 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.693). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-7.4, 21.1); signed map (29.2, -18.6). **Vector** length 45.3, 5.01% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +3.6 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +6.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.7 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +3.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.2 | +2.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.1 | +4.7 |
|  | [[Carbamazepine (drug)]] 0.5 µM |  | +1.0 | +1.1 |
|  | [[Belzutifan (drug)]] 5 µM |  | +0.9 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.2 | -3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -1.6 | -4.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -1.6 | -4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -1.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.1 | -1.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

> [!warning] No registry record
> WASH2P-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16597: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16597); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16597, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16597]; `tensor/DDL_lfc|DDL_z.npy` [16597]; `embed/gene_vectors.npy` [16597]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16597 or target_col == 16597). Every well: [[WASH2P-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WASH2P-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

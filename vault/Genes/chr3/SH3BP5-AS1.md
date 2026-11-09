---
symbol: "SH3BP5-AS1"
type: "gene"
col: 13414
ensembl_id: "ENSG00000224660"
name: "SH3BP5 antisense RNA 1"
location: "3p25.1"
module: 39
arm: "+"
pooled_cpm: 7.44
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# SH3BP5-AS1

*SH3BP5 antisense RNA 1* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.35× (z +4.9, q 6e-04, up in 18 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.526× (z -7.4, q 8e-11, down in 28 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.562× (z -3.5, q 0.099, down in 12 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.0886×, NCI-H23 0.134×; ⚠ cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 0.148×, J82 0.104×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H2030 0.131×, LoVo 0.241×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Valdecoxib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0823×); [[Zileuton (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0416×); [[Vandetanib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0789×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED6]] (+0.70, fdr 7e-06), [[CHRNA10]] (+0.69, fdr 7e-06), [[RNF32-AS1]] (+0.67, fdr 7e-06); moves opposite to [[MTF2]] (-0.58, fdr 1e-05), [[TMEM14A]] (-0.55, fdr 4e-05), [[ORC4]] (-0.53, fdr 4e-05).
> It is in [[Module 039]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13414.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +4.9 | 6e-04 | 18/44 (SW480, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.6 | 0.001 | 3/48 (NCI-H23, AsPC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +3.7 | 0.035 | 8/47 (C32, J82, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.36×** | +3.6 | 0.051 | 4/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.34×** | +3.3 | 0.095 | 9/47 (NCI-H2030, LS 180, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.69× | +3.1 | 0.15 | 2/46 (SW480, HOP62) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13414.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 0.0886×, NCI-H23 0.134×; ⚠ cell-cycle shift, explains ~28% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 0.148×, J82 0.104×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H2030 0.131×, LoVo 0.241×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Valdecoxib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0823×); [[Zileuton (drug)]] 0.05 µM in 1 line (hTERT-HPNE 0.0416×); [[Vandetanib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0789×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.526×** | -7.4 | 8e-11 | 28/44 (NCI-H2030, LoVo, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.729×** | -3.5 | 0.099 | 14/46 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.562×** | -3.5 | 0.099 | 12/46 (PANC-1, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.822× | -3.2 | 0.20 | 10/48 (CHP-212, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13414. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 6.32 | 0 | 4 (2 ⚠) | — | [[Valdecoxib (drug)]] 0.05 µM 0.0823× (z -10.7) |
| [[C32 (line)]] | wt | 8.76 | 0 | 2 | — | [[Mozavaptan (drug)]] 0.05 µM 0.1000× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 7.82 | 0 | 1 | — | [[Zileuton (drug)]] 0.05 µM 0.0416× (z -10.6) |
| [[J82 (line)]] | alt | 5.71 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 9.16 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H460 (line)]] | wt | 6.35 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 6.90 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0986× (z -8.5) |
| [[RKO (line)]] | wt | 11.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0886× (z -11.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 8.09 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0789× (z -9.8) |
| [[A-172 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13414), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED6]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[CHRNA10]] | +0.69 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[RNF32-AS1]] | +0.67 | +0.70 / +0.60 | both halves | 7e-06 | same gene group |
| [[TMEM236]] | +0.64 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[CCDC17]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.62 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[GABRR2]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[CLDN15]] | +0.62 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[APRG1]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[NLGN3]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.61 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[YIPF7]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTF2]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[TMEM14A]] | -0.55 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[ORC4]] | -0.53 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[FNBP1L]] | -0.49 | -0.51 / -0.37 | both halves | 7e-05 |  |
| [[PGAP1]] | -0.49 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[MINDY3]] | -0.49 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[MLLT3]] | -0.49 | -0.49 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.597). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.3, -14.2); signed map (18.6, 6.0). **Vector** length 49.9, 5.77% of its response variance represented; |z| ≥ 3 in 876 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.6 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.5 | +4.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.4 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +0.2 |
| fall | [[Verteporfin (drug)]] 5 µM |  | -2.0 | +0.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.7 | -1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.7 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | SH3BP5 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p25.1 — chr3:15,254,184-15,264,515 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44501](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44501) · Entrez [100505696](https://www.ncbi.nlm.nih.gov/gene/100505696) · Ensembl [ENSG00000224660](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224660)

## Data

Gene col 13414: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13414); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13414, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13414]; `tensor/DDL_lfc|DDL_z.npy` [13414]; `embed/gene_vectors.npy` [13414]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13414 or target_col == 13414). Every well: [[SH3BP5-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3BP5-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

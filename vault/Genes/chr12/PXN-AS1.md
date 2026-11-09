---
symbol: "PXN-AS1"
type: "gene"
col: 14960
ensembl_id: "ENSG00000255857"
name: "PXN antisense RNA 1"
location: "12q24.23"
module: 21
arm: "+"
pooled_cpm: 3.78
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# PXN-AS1

*PXN antisense RNA 1* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.42× (z +16.1, q 0e+00, up in 20 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tomivosertib (drug)]] 0.05 µM: 2.18× (z +8.0, q 3e-13, up in 30 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.898× (z -4.4, q 0.007, down in 11 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Lucanthone (drug)]] 0.05 µM: 0.661× (z -4.2, q 0.008, down in 10 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[5-Azacytidine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0662×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPK-AS1]] (+0.65, fdr 1e-05), [[HSPE1-MOB4]] (+0.64, fdr 3e-05), [[TICAM2-AS1]] (+0.64, fdr 1e-05); moves opposite to [[SETX]] (-0.48, fdr 5e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14960.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.42×** | +16.1 | 0e+00 | 20/20 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.44×** | +15.5 | 0e+00 | 4/5 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.03×** | +11.1 | 3e-26 | 7/7 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tomivosertib (drug)]] 0.05 µM |  | **2.18×** | +8.0 | 3e-13 | 30/43 (PANC-1, SW480, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.96×** | +7.3 | 4e-11 | 14/24 (A498, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.9 | 3e-07 | 17/37 (J82, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +5.8 | 4e-07 | 9/25 (NCI-H1573, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Temuterkib (drug)]] 0.05 µM |  | **1.67×** | +5.2 | 1e-05 | 8/44 (A498, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +4.7 | 2e-04 | 11/35 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.48×** | +4.0 | 0.004 | 3/42 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.7 | 0.013 | 7/25 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.013 | 7/44 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.40×** | +3.6 | 0.014 | 4/37 (AsPC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.55×** | +3.4 | 0.030 | 1/31 (MIA PaCa-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.3 | 0.040 | 1/8 (NCI-H23) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.057 | 8/46 (HepG2/C3A, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14960.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[5-Azacytidine (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0662×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -4.4 | 0.007 | 11/48 (A-172, NCI-H661, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.661×** | -4.2 | 0.008 | 10/47 (SHP-77, A-427, …) | inconsistent across doses | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.668×** | -4.1 | 0.008 | 6/45 (HT-29, KATO III, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14960. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 3.39 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0662× (z -9.5) |
| [[A-172 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14960), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPK-AS1]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 | same gene group |
| [[HSPE1-MOB4]] | +0.64 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[TICAM2-AS1]] | +0.64 | +0.49 / +0.57 | both halves | 1e-05 | same gene group |
| [[GEMIN7-AS1]] | +0.61 | +0.42 / +0.67 | both halves | 4e-05 | same gene group |
| [[MIR762HG]] | +0.61 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[HOXB-AS3]] | +0.60 | +0.48 / +0.62 | both halves | 2e-05 | same gene group |
| [[GOT1-DT]] | +0.60 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ZNF236-DT]] | +0.60 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[FAM217A]] | +0.60 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[C12orf73]] | +0.59 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[AQP11]] | +0.59 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[ZRANB2-AS1]] | +0.58 | +0.41 / +0.60 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETX]] | -0.48 | -0.40 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.578). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.0, 26.6); signed map (33.8, -17.0). **Vector** length 36.6, 3.48% of its response variance represented; |z| ≥ 3 in 710 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +11.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +5.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +3.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -2.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -4.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | PXN antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q24.23 — chr12:120,201,274-120,213,233 (+) |
| Ensembl biotype | lncRNA |
| Also known as | EyeLinc4 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44123](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44123) · Entrez [100506649](https://www.ncbi.nlm.nih.gov/gene/100506649) · Ensembl [ENSG00000255857](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255857)

## Data

Gene col 14960: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14960); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14960, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14960]; `tensor/DDL_lfc|DDL_z.npy` [14960]; `embed/gene_vectors.npy` [14960]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14960 or target_col == 14960). Every well: [[PXN-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PXN-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

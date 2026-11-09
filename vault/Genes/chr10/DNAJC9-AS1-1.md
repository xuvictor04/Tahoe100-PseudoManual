---
symbol: "DNAJC9-AS1-1"
type: "gene"
col: 14097
ensembl_id: "ENSG00000236756"
name: "DNAJC9 and MRPS16 antisense RNA 1"
location: "10q22.2"
module: 21
arm: "+"
pooled_cpm: 2.71
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# DNAJC9-AS1-1

*DNAJC9 and MRPS16 antisense RNA 1* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.14× (z +10.6, q 2e-23, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +9.3, q 4e-18, up in 24 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 0.05 µM in 1 line (LoVo 0.0840×); [[Allantoin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0895×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (A498 0.0827×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKD2L2]] (+0.79, fdr 7e-06), [[HRG-AS1]] (+0.77, fdr 7e-06), [[TOMM20L-DT]] (+0.76, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14097.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.14×** | +10.6 | 2e-23 | 3/4 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.16×** | +10.2 | 3e-22 | 3/6 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +9.3 | 4e-18 | 24/33 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.58×** | +9.1 | 9e-18 | 12/16 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.90×** | +6.2 | 6e-08 | 8/13 (HEC-1-A, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.87×** | +6.0 | 2e-07 | 20/42 (SW480, HT-29, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.3 | 0.001 | 8/36 (C32, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.3 | 0.001 | 2/14 (A498, Hs 766T) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.027 | 5/43 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.061 | 4/44 (PANC-1, NCI-H2030, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14097.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 0.05 µM in 1 line (LoVo 0.0840×); [[Allantoin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0895×); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (A498 0.0827×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.885× | -4.1 | 0.024 | 18/46 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14097. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.44 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0827× (z -9.4) |
| [[LoVo (line)]] | wt | 3.65 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0840× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 2.54 | 0 | 1 (1 ⚠) | — | [[Carbidopa (monohydrate) (drug)]] 0.5 µM 0.0650× (z -9.0) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 2.55 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0895× (z -9.6) |
| [[A-172 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14097), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKD2L2]] | +0.79 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[HRG-AS1]] | +0.77 | +0.71 / +0.70 | both halves | 7e-06 | same gene group |
| [[TOMM20L-DT]] | +0.76 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[TP53TG5]] | +0.76 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.76 | +0.69 / +0.73 | both halves | 7e-06 | same gene group |
| [[UBOX5-AS1]] | +0.75 | +0.62 / +0.67 | both halves | 7e-06 | same gene group |
| [[CTDSPL2-DT]] | +0.75 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[CNPY2-AS1]] | +0.75 | +0.61 / +0.73 | both halves | 7e-06 | same gene group |
| [[SPATA1]] | +0.75 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[MASP2]] | +0.74 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.74 | +0.72 / +0.68 | both halves | 7e-06 | same gene group |
| [[SLC13A4]] | +0.73 | +0.60 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.792). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.9, 25.7); signed map (31.5, 4.8). **Vector** length 30.6, 2.26% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.9 | +1.5 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -0.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.8 | -1.2 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | DNAJC9 and MRPS16 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q22.2 — chr10:73,247,360-73,276,984 (+) |
| Ensembl biotype | lncRNA |
| Also known as | bA537A6.3; previously C10orf103 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [A6NH13](https://www.uniprot.org/uniprotkb/A6NH13) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31432) · Entrez [414245](https://www.ncbi.nlm.nih.gov/gene/414245) · UniProt [A6NH13](https://www.uniprot.org/uniprotkb/A6NH13) · Ensembl [ENSG00000236756](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236756)

## Data

Gene col 14097: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14097); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14097, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14097]; `tensor/DDL_lfc|DDL_z.npy` [14097]; `embed/gene_vectors.npy` [14097]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14097 or target_col == 14097). Every well: [[DNAJC9-AS1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJC9-AS1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

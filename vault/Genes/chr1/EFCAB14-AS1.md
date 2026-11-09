---
symbol: "EFCAB14-AS1"
type: "gene"
col: 13631
ensembl_id: "ENSG00000228237"
name: "EFCAB14 antisense RNA 1"
location: "1p33"
module: 21
arm: "+"
pooled_cpm: 3.87
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# EFCAB14-AS1

*EFCAB14 antisense RNA 1* — 1p33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.60× (z +9.5, q 1e-18, up in 23 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +3.8, q 0.017, up in 12 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.836× (z -6.2, q 2e-07, down in 28 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.665× (z -4.0, q 0.015, down in 8 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (LS 180 0.0808×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM in 1 line (HS-578T 0.0858×); [[Bestatin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0857×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RN7SL2]] (+0.84, fdr 7e-06), [[FAM217A]] (+0.83, fdr 7e-06), [[BIRC6-AS2-1]] (+0.83, fdr 7e-06); moves opposite to [[DCLRE1A]] (-0.67, fdr 3e-05), [[ZBTB33]] (-0.67, fdr 2e-05), [[ALG10]] (-0.67, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13631.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +9.5 | 1e-18 | 23/24 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.67×** | +9.4 | 2e-18 | 5/7 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +6.4 | 3e-08 | 4/9 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +5.2 | 3e-05 | 10/24 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.017 | 12/39 (HEC-1-A, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +3.3 | 0.070 | 3/32 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.3 | 0.070 | 10/39 (LOX-IMVI, HS-578T, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.2 | 0.089 | 8/28 (SW 900, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.39× | +3.1 | 0.12 | 8/26 (LOX-IMVI, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Decitabine (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.12 | 5/41 (HS-578T, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13631.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (LS 180 0.0808×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM in 1 line (HS-578T 0.0858×); [[Bestatin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0857×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.836× | -6.2 | 2e-07 | 28/48 (SNU-1, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.665×** | -4.0 | 0.015 | 8/44 (SW1417, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | 0.720× | -3.1 | 0.27 | 9/44 (NCI-H23, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.713× | -3.1 | 0.27 | 2/46 (CFPAC-1, HCT15) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13631. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 4.26 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM 0.0858× (z -8.7) |
| [[LS 180 (line)]] | wt | 4.21 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0808× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 3.92 | 0 | 1 | — | [[Bestatin (drug)]] 0.05 µM 0.0857× (z -8.6) |
| [[A-172 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13631), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RN7SL2]] | +0.84 | +0.81 / +0.81 | both halves | 7e-06 |  |
| [[FAM217A]] | +0.83 | +0.77 / +0.84 | both halves | 7e-06 |  |
| [[BIRC6-AS2-1]] | +0.83 | +0.72 / +0.90 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.80 | +0.78 / +0.84 | both halves | 7e-06 | same gene group |
| [[KIZ-AS1]] ⚠ | +0.80 | +0.63 / +0.79 | both halves | 7e-06 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[RN7SL1]] | +0.79 | +0.73 / +0.82 | both halves | 7e-06 |  |
| [[VPS39-DT]] | +0.79 | +0.72 / +0.82 | both halves | 7e-06 |  |
| [[NFATC2IP-AS1]] | +0.79 | +0.66 / +0.83 | both halves | 7e-06 | same gene group |
| [[CCDC65]] | +0.78 | +0.63 / +0.82 | both halves | 7e-06 |  |
| [[MAL2-AS1]] | +0.78 | +0.71 / +0.81 | both halves | 7e-06 | same gene group |
| [[CCDC39]] | +0.78 | +0.54 / +0.83 | both halves | 1e-05 |  |
| [[UBOX5-AS1]] | +0.77 | +0.72 / +0.80 | both halves | 7e-06 | same gene group |
| [[RHOQ-AS1]] | +0.77 | +0.62 / +0.74 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCLRE1A]] | -0.67 | -0.44 / -0.66 | both halves | 3e-05 |  |
| [[ZBTB33]] | -0.67 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[ALG10]] | -0.67 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[ZNF816]] | -0.64 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[BBS10]] | -0.64 | -0.41 / -0.65 | both halves | 4e-05 |  |
| [[AKAP11]] | -0.63 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[ZNF770]] | -0.62 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[VEZF1]] | -0.62 | -0.33 / -0.68 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.770). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.6, 29.1); signed map (34.8, 5.7). **Vector** length 32.7, 2.74% of its response variance represented; |z| ≥ 3 in 741 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +6.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +1.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.0 | +1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +1.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +0.9 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.9 | -4.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -0.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -6.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -2.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | EFCAB14 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p33 — chr1:46,674,036-46,692,098 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously KIAA0494-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44108) · Entrez [100130197](https://www.ncbi.nlm.nih.gov/gene/100130197) · Ensembl [ENSG00000228237](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228237)

## Data

Gene col 13631: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13631); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13631, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13631]; `tensor/DDL_lfc|DDL_z.npy` [13631]; `embed/gene_vectors.npy` [13631]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13631 or target_col == 13631). Every well: [[EFCAB14-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EFCAB14-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

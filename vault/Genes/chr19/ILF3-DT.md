---
symbol: "ILF3-DT"
type: "gene"
col: 15521
ensembl_id: "ENSG00000267100"
name: "ILF3 divergent transcript"
location: "19p13.2"
module: 24
arm: "+"
pooled_cpm: 9.31
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ILF3-DT

*ILF3 divergent transcript* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.30× (z +7.1, q 5e-10, up in 30 of 37 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +7.0, q 5e-10, up in 27 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 5 µM in 1 line (LoVo 0.0342×; ⚠ toxic; cell-cycle shift, explains ~34% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.204×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM7-AS2]] (+0.68, fdr 7e-06), [[RSL1D1-DT]] (+0.67, fdr 1e-05), [[DCTN6-DT]] (+0.64, fdr 1e-05); moves opposite to [[CEP170B]] (-0.59, fdr 1e-05), [[UBR4]] (-0.56, fdr 5e-05), [[MACROH2A1]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15521.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.30×** | +7.1 | 5e-10 | 30/37 (SW1417, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +7.0 | 5e-10 | 27/44 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +6.3 | 5e-08 | 27/48 (Hs 766T, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.25×** | +5.8 | 1e-06 | 27/43 (HOP62, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +5.3 | 1e-05 | 8/18 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.92×** | +5.2 | 2e-05 | 31/46 (NCI-H23, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.59×** | +3.6 | 0.023 | 16/34 (LoVo, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.46×** | +3.5 | 0.032 | 17/46 (RPMI-7951, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | 1.40× | +3.1 | 0.11 | 8/40 (MIA PaCa-2, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 1.38× | +3.0 | 0.14 | 10/47 (A-172, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15521.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 5 µM in 1 line (LoVo 0.0342×; ⚠ toxic; cell-cycle shift, explains ~34% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.204×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.702× | -3.3 | 0.26 | 17/46 (LoVo, J82, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.705× | -3.3 | 0.26 | 12/47 (NCI-H661, NCI-H460, …) | inconsistent across doses |  |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 0.791× | -3.1 | 0.26 | 9/48 (MIA PaCa-2, RKO, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.719× | -3.1 | 0.26 | 20/47 (HS-578T, MIA PaCa-2, …) | rises with dose |  |
| [[Tadalafil (drug)]] 5 µM |  | 0.700× | -3.1 | 0.26 | 14/45 (KATO III, SW1417, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15521. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 4.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 15.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +8.7) | — |
| [[LoVo (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0342× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[SK-MEL-2 (line)]] | alt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.204× (z -9.1) |
| [[A-172 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15521), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM7-AS2]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[RSL1D1-DT]] | +0.67 | +0.53 / +0.64 | both halves | 1e-05 | same gene group |
| [[DCTN6-DT]] | +0.64 | +0.53 / +0.71 | both halves | 1e-05 | same gene group |
| [[TRAPPC6A]] | +0.63 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[TBC1D22A-DT]] | +0.62 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[MINCR]] | +0.60 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[TVP23B]] | +0.59 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[EID2B]] | +0.59 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[FMC1]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[KLHL28]] | +0.57 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[DNAJC4]] | +0.57 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[MBTD1]] | +0.57 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP170B]] | -0.59 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[UBR4]] | -0.56 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[MACROH2A1]] | -0.56 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[ELAC2]] | -0.56 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[TTL]] | -0.55 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | -0.54 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[PRPS1]] | -0.53 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[HERC2P9-1]] | -0.52 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[NPIPB4]] | -0.52 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[CCT5]] | -0.52 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[PSMD11]] | -0.50 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[MAPK9]] | -0.50 | -0.45 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.525). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.0, -22.4); signed map (-2.0, -0.8). **Vector** length 67.9, 12.8% of its response variance represented; |z| ≥ 3 in 622 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +5.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.5 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +7.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.8 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +5.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +1.8 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.9 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ILF3 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19p13.2 — chr19:10,651,862-10,653,875 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously ILF3-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27115](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27115) · Entrez [147727](https://www.ncbi.nlm.nih.gov/gene/147727) · Ensembl [ENSG00000267100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267100)

## Data

Gene col 15521: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15521); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15521, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15521]; `tensor/DDL_lfc|DDL_z.npy` [15521]; `embed/gene_vectors.npy` [15521]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15521 or target_col == 15521). Every well: [[ILF3-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ILF3-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

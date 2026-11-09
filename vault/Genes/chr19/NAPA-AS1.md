---
symbol: "NAPA-AS1"
type: "gene"
col: 15588
ensembl_id: "ENSG00000268061"
name: "NAPA antisense RNA 1"
location: "19q13.32-q13.33"
module: 35
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# NAPA-AS1

*NAPA antisense RNA 1* — 19q13.32-q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.85× (z +11.7, q 6e-29, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.59× (z +7.6, q 3e-12, up in 11 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0796×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC2HC1C]] (+0.70, fdr 7e-06), [[C1orf56]] (+0.69, fdr 7e-06), [[PAXBP1-AS1]] (+0.69, fdr 7e-06); moves opposite to [[GPR180]] (-0.56, fdr 1e-04), [[LYPLA1]] (-0.55, fdr 4e-05), [[GGCT]] (-0.55, fdr 2e-04).
> It sits in the **+** arm of [[Module 035]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15588.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +11.7 | 6e-29 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +11.2 | 9e-27 | 10/15 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +7.8 | 1e-12 | 1/3 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +7.6 | 3e-12 | 11/35 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +6.0 | 2e-07 | 6/44 (SW480, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.0 | 2e-07 | 11/33 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +5.5 | 3e-06 | 3/14 (LoVo, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +5.5 | 3e-06 | 12/45 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.59×** | +3.9 | 0.007 | 3/15 (HS-578T, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +3.8 | 0.008 | 8/31 (LoVo, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.8 | 0.008 | 1/15 (HEC-1-A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.37×** | +3.6 | 0.014 | 3/28 (A498, LS 180, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.54×** | +3.6 | 0.016 | 2/37 (C32, PANC-1) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.5 | 0.018 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.030 | 12/40 (SW 900, RKO, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.030 | 0/28 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.030 | 2/32 (SW480, NCI-H460) | inconsistent across doses | low cells (technical?); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +3.1 | 0.051 | 2/38 (HT-29, RPMI-7951) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.30×** | +3.0 | 0.075 | 3/42 (KATO III, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15588.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0796×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Thymol (drug)]] 0.05 µM |  | 0.742× | -3.5 | 0.29 | 11/40 (LS 180, HOP62, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.928× | -3.2 | 0.36 | 8/46 (NCI-H1573, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15588. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 2.94 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0796× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15588), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC2HC1C]] | +0.70 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[C1orf56]] | +0.69 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[PAXBP1-AS1]] | +0.69 | +0.63 / +0.59 | both halves | 7e-06 | same gene group |
| [[HNRNPK-AS1]] | +0.68 | +0.55 / +0.50 | both halves | 1e-05 | same gene group |
| [[C11orf71]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SLC23A1]] | +0.67 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PLA2G6]] | +0.66 | +0.70 / +0.43 | both halves | 3e-05 |  |
| [[CES3]] | +0.66 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[CHMP3-AS1]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 | same gene group |
| [[LRIG2-DT]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ZBTB20-AS5]] | +0.64 | +0.55 / +0.50 | both halves | 1e-05 | same gene group |
| [[MYL5]] | +0.63 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR180]] | -0.56 | -0.47 / -0.32 | both halves | 1e-04 |  |
| [[LYPLA1]] | -0.55 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[GGCT]] | -0.55 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[RALB]] | -0.54 | -0.56 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (8.7, 25.2); signed map (33.7, -1.7). **Vector** length 27.7, 1.89% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.5 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +7.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.0 | +3.6 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.0 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | +0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.0 | +0.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.8 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | NAPA antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.32-q13.33 — chr19:47,484,282-47,502,399 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44118](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44118) · Entrez [100505681](https://www.ncbi.nlm.nih.gov/gene/100505681) · Ensembl [ENSG00000268061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000268061)

## Data

Gene col 15588: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15588); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15588, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15588]; `tensor/DDL_lfc|DDL_z.npy` [15588]; `embed/gene_vectors.npy` [15588]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15588 or target_col == 15588). Every well: [[NAPA-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAPA-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

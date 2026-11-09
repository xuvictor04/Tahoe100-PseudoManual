---
symbol: "WASL-DT"
type: "gene"
col: 15736
ensembl_id: "ENSG00000272686"
name: "WASL divergent transcript"
location: "7q31.32"
module: 21
arm: "+"
pooled_cpm: 2.02
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# WASL-DT

*WASL divergent transcript* — 7q31.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.14× (z +13.2, q 5e-37, up in 25 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0653×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (A549 0.0597×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ETFBKMT]] (+0.69, fdr 7e-06), [[PAXIP1-DT]] (+0.62, fdr 8e-06), [[PPM1N]] (+0.62, fdr 4e-05); moves opposite to [[IDE]] (-0.57, fdr 1e-05), [[MFN2]] (-0.51, fdr 4e-05), [[MTA1]] (-0.50, fdr 1e-04).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15736.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.14×** | +13.2 | 5e-37 | 25/27 (CFPAC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.66×** | +9.8 | 3e-20 | 2/2 (A498, SW1417) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +8.1 | 8e-14 | 0/0 | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.56×** | +7.7 | 2e-12 | 6/11 (KATO III, PANC-1, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.42×** | +7.2 | 5e-11 | 27/40 (C32, SW480, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.73×** | +6.3 | 3e-08 | 20/40 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.67×** | +5.9 | 3e-07 | 12/43 (SW480, NCI-H2030, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +5.6 | 1e-06 | 18/44 (KATO III, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.98×** | +5.3 | 6e-06 | 3/10 (KATO III, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +5.2 | 1e-05 | 19/41 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.86×** | +5.0 | 2e-05 | 11/34 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +4.6 | 2e-04 | 15/45 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.45×** | +4.3 | 7e-04 | 10/31 (A-172, SW1417, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.66×** | +4.1 | 0.002 | 3/12 (SW1417, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +4.0 | 0.002 | 7/35 (SK-MEL-2, Panc 03.27, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.62×** | +3.9 | 0.003 | 6/25 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.84×** | +3.6 | 0.012 | 2/25 (SW480, NCI-H1573) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +3.3 | 0.025 | 4/23 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.70×** | +3.1 | 0.052 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15736.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0653×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (A549 0.0597×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.655× | -3.5 | 0.23 | 10/45 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Malotilate (drug)]] 0.05 µM |  | 0.665× | -3.4 | 0.23 | 12/36 (NCI-H23, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15736. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 3.04 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0597× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 3.20 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0653× (z -9.7) |
| [[A-172 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.710 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.546 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.872 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.955 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15736), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ETFBKMT]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[PAXIP1-DT]] | +0.62 | +0.58 / +0.66 | both halves | 8e-06 | same gene group |
| [[PPM1N]] | +0.62 | +0.41 / +0.74 | both halves | 4e-05 |  |
| [[SDAD1P1]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[NPW]] | +0.58 | +0.40 / +0.63 | both halves | 4e-05 |  |
| [[SP2-DT]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[COL26A1]] | +0.56 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[ZNF232-AS1]] | +0.55 | +0.22 / +0.63 | both halves | 6e-04 |  |
| [[EXOC3-AS1]] | +0.54 | +0.31 / +0.67 | both halves | 2e-04 |  |
| [[KDM5B]] | +0.54 | +0.36 / +0.64 | both halves | 1e-04 |  |
| [[HERPUD2-AS1]] | +0.54 | +0.57 / +0.59 | both halves | 8e-06 |  |
| [[PLCL1]] | +0.53 | +0.53 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IDE]] | -0.57 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[MFN2]] | -0.51 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[MTA1]] | -0.50 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[MTOR]] | -0.50 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[HERC2P9-1]] | -0.49 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[HERC2]] | -0.49 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[MACROH2A1]] | -0.48 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[FANCG]] | -0.47 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[GCN1]] | -0.46 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[DNA2]] | -0.46 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[DROSHA]] | -0.46 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[MCM3AP]] | -0.46 | -0.32 / -0.53 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.410). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.8, 32.2); signed map (37.9, 3.0). **Vector** length 38.8, 4.23% of its response variance represented; |z| ≥ 3 in 914 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +13.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +2.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -0.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -1.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.7 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | WASL divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q31.32 — chr7:123,749,068-123,751,166 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54820](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54820) · Entrez [116435299](https://www.ncbi.nlm.nih.gov/gene/116435299) · Ensembl [ENSG00000272686](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272686)

## Data

Gene col 15736: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15736); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15736, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15736]; `tensor/DDL_lfc|DDL_z.npy` [15736]; `embed/gene_vectors.npy` [15736]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15736 or target_col == 15736). Every well: [[WASL-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WASL-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

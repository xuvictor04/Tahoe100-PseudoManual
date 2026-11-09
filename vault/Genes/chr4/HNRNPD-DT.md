---
symbol: "HNRNPD-DT"
type: "gene"
col: 15735
ensembl_id: "ENSG00000272677"
name: "HNRNPD divergent transcript"
location: "4q21.22"
module: 21
arm: "+"
pooled_cpm: 2.62
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# HNRNPD-DT

*HNRNPD divergent transcript* — 4q21.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.19× (z +20.9, q 0e+00, up in 29 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNBD2]] (+0.71, fdr 7e-06), [[BTG1-DT]] (+0.71, fdr 7e-06), [[RSPH9]] (+0.65, fdr 7e-06); moves opposite to [[MYCBP2]] (-0.55, fdr 1e-04), [[PRKDC]] (-0.52, fdr 4e-05), [[HERC2]] (-0.52, fdr 4e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15735.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.19×** | +20.9 | 0e+00 | 29/31 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.52×** | +18.4 | 0e+00 | 29/37 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.81×** | +13.3 | 7e-38 | 11/13 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.03×** | +11.4 | 4e-28 | 35/46 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.18×** | +11.0 | 3e-26 | 2/4 (PANC-1, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.66×** | +10.1 | 5e-22 | 27/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +9.7 | 2e-20 | 0/2 | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.51×** | +9.5 | 1e-19 | 30/45 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.80×** | +8.5 | 1e-15 | 14/44 (SW480, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.20×** | +8.1 | 2e-14 | 6/11 (HEC-1-A, HOP62, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.2 | 2e-11 | 14/44 (SW480, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +7.2 | 2e-11 | 18/43 (SW480, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.89×** | +6.6 | 2e-09 | 14/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +5.7 | 4e-07 | 15/33 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +3.7 | 0.009 | 8/37 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.011 | 5/41 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.016 | 4/46 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.047 | 7/42 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.047 | 3/45 (MIA PaCa-2, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15735.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Busulfan (drug)]] 0.05 µM |  | 0.720× | -3.4 | 0.37 | 5/42 (COLO 205, LS 180, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | 0.749× | -3.0 | 0.55 | 4/44 (SW1417, NCI-H661, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15735. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 1.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.25× (z +9.1) | — |
| [[LoVo (line)]] | wt | 2.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.85× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 1.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +10.3) | — |
| [[SW480 (line)]] | alt | 3.28 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +8.8) | — |
| [[A-172 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.984 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.950 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15735), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNBD2]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[BTG1-DT]] | +0.71 | +0.65 / +0.69 | both halves | 7e-06 | same gene group |
| [[RSPH9]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[CHMP3-AS1]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[PKD2L2]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[ELAVL3]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[LINC02603]] | +0.61 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[RYR1]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[SPATA1]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[PTPRT]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[KIAA2012]] | +0.59 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYCBP2]] | -0.55 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[PRKDC]] | -0.52 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[HERC2]] | -0.52 | -0.54 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.4, 31.0); signed map (37.1, 6.0). **Vector** length 43.8, 4.91% of its response variance represented; |z| ≥ 3 in 1,084 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +20.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +11.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +7.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.9 | +2.4 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | +0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | +0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -0.9 | -2.3 |
|  | [[Busulfan (drug)]] 5 µM |  | -0.9 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | HNRNPD divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q21.22 — chr4:82,374,142-82,384,027 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55205) · Entrez [101928963](https://www.ncbi.nlm.nih.gov/gene/101928963) · Ensembl [ENSG00000272677](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272677)

## Data

Gene col 15735: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15735); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15735, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15735]; `tensor/DDL_lfc|DDL_z.npy` [15735]; `embed/gene_vectors.npy` [15735]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15735 or target_col == 15735). Every well: [[HNRNPD-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPD-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

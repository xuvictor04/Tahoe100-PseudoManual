---
symbol: "EOGT-DT"
type: "gene"
col: 14408
ensembl_id: "ENSG00000244513"
name: "EOGT divergent transcript"
location: "3p14.1"
module: 21
arm: "+"
pooled_cpm: 8.89
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# EOGT-DT

*EOGT divergent transcript* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +9.9, q 3e-20, up in 33 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.822× (z -8.1, q 2e-13, down in 32 of 48 measured lines) ⚠ position not correctable.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.101×); [[Pentamidine (isethionate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0623×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TICAM2-AS1]] (+0.90, fdr 7e-06), [[ZRANB2-AS1]] (+0.89, fdr 7e-06), [[PP2D1]] (+0.87, fdr 7e-06); moves opposite to [[PRKDC]] (-0.64, fdr 7e-06), [[RUVBL1]] (-0.62, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14408.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +9.9 | 3e-20 | 33/43 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +9.8 | 3e-20 | 28/33 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +9.0 | 3e-17 | 17/20 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +6.4 | 3e-08 | 27/42 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +5.3 | 1e-05 | 15/26 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +4.2 | 0.002 | 14/39 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.39×** | +4.0 | 0.006 | 16/45 (SNU-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.006 | 14/43 (LOX-IMVI, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.014 | 8/45 (HT-29, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.017 | 8/45 (H4, NCI-H460, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.025 | 6/46 (A-172, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.084 | 11/46 (SNU-423, NCI-H2347, …) | top dose only |  |
| [[Bicalutamide (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.089 | 3/46 (BT-474, CFPAC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14408.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.101×); [[Pentamidine (isethionate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0623×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.822×** | -8.1 | 2e-13 | 32/48 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.818× | -3.4 | 0.21 | 13/48 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | 0.834× | -3.0 | 0.30 | 6/48 (MIA PaCa-2, A498, …) | top dose only | position effect removed |
| [[Trifluridine (drug)]] 0.5 µM |  | 0.776× | -3.0 | 0.30 | 10/47 (HCT15, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.836× | -3.0 | 0.30 | 9/48 (LOX-IMVI, HCT15, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14408. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 11.0 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.101× (z -9.6) |
| [[SNU-1 (line)]] | wt | 9.54 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 0.5 µM 0.0623× (z -9.3) |
| [[A-172 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14408), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TICAM2-AS1]] | +0.90 | +0.78 / +0.90 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.89 | +0.80 / +0.85 | both halves | 7e-06 |  |
| [[PP2D1]] | +0.87 | +0.82 / +0.81 | both halves | 7e-06 |  |
| [[LRRC37A16P]] | +0.87 | +0.73 / +0.88 | both halves | 7e-06 |  |
| [[FAM217A]] | +0.86 | +0.76 / +0.83 | both halves | 7e-06 |  |
| [[C12orf73]] | +0.85 | +0.77 / +0.85 | both halves | 7e-06 |  |
| [[FLJ40194]] | +0.84 | +0.71 / +0.81 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.83 | +0.66 / +0.81 | both halves | 7e-06 |  |
| [[BIRC6-AS2-1]] | +0.82 | +0.71 / +0.81 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.82 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.81 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[MAL2-AS1]] | +0.81 | +0.75 / +0.81 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.64 | -0.68 / -0.58 | both halves | 7e-06 |  |
| [[RUVBL1]] | -0.62 | -0.55 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.884). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.8, 28.0); signed map (34.2, 5.1). **Vector** length 52.7, 7.30% of its response variance represented; |z| ≥ 3 in 667 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +3.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.0 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -1.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -8.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -2.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.4 | -0.6 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | -1.3 | -2.2 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | EOGT divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p14.1 — chr3:69,013,941-69,056,622 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [121676928](https://www.ncbi.nlm.nih.gov/gene/121676928):

> Predicted to be involved in SRP-dependent cotranslational protein targeting to membrane, signal sequence recognition. Predicted to be part of signal recognition particle, endoplasmic reticulum targeting. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:55605](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55605) · Entrez [121676928](https://www.ncbi.nlm.nih.gov/gene/121676928) · Ensembl [ENSG00000244513](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244513)

## Data

Gene col 14408: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14408); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14408, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14408]; `tensor/DDL_lfc|DDL_z.npy` [14408]; `embed/gene_vectors.npy` [14408]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14408 or target_col == 14408). Every well: [[EOGT-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EOGT-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

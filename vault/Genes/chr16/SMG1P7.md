---
symbol: "SMG1P7"
type: "gene"
col: 15353
ensembl_id: "ENSG00000261556"
name: "SMG1 pseudogene 7"
location: "16q22.1"
module: 37
arm: "+"
pooled_cpm: 8.24
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# SMG1P7

*SMG1 pseudogene 7* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.87× (z +8.3, q 7e-14, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.538× (z -4.9, q 6e-04, down in 23 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 2 lines (A-172 0.114×, A498 0.186×; ⚠ cell-cycle shift, explains ~70% of this change); [[Imiquimod (maleate) (drug)]] 0.05 µM in 1 line (A-172 0.0583×); [[Digitoxin (drug)]] 5 µM in 1 line (HT-29 0.0458×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Terfenadine (drug)]] 0.5 µM in 1 line (A549 0.0654×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLRA1P]] (+0.72, fdr 7e-06), [[PLAC8L1]] (+0.72, fdr 7e-06), [[MOCOS]] (+0.68, fdr 7e-06); moves opposite to [[TUBG2]] (-0.52, fdr 4e-05), [[MICU2]] (-0.51, fdr 5e-05).
> It is in [[Module 037]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15353.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.87×** | +8.3 | 7e-14 | 39/47 (SW480, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.7 | 3e-06 | 30/43 (HOP62, SW1417, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.04×** | +5.6 | 4e-06 | 31/47 (NCI-H2030, NCI-H460, …) | all doses, flat | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +4.7 | 4e-04 | 19/40 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.4 | 0.001 | 16/33 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +4.0 | 0.005 | 8/22 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.66×** | +4.0 | 0.005 | 17/47 (LOX-IMVI, HEC-1-A, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.007 | 12/48 (HCT15, COLO 205, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.56×** | +3.5 | 0.032 | 12/47 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.48× | +3.1 | 0.12 | 14/43 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15353.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 5 µM in 2 lines (A-172 0.114×, A498 0.186×; ⚠ cell-cycle shift, explains ~70% of this change); [[Imiquimod (maleate) (drug)]] 0.05 µM in 1 line (A-172 0.0583×); [[Digitoxin (drug)]] 5 µM in 1 line (HT-29 0.0458×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Terfenadine (drug)]] 0.5 µM in 1 line (A549 0.0654×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.538×** | -4.9 | 6e-04 | 23/46 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.620×** | -3.6 | 0.062 | 16/46 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.636×** | -3.6 | 0.062 | 16/42 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.491×** | -3.5 | 0.062 | 12/35 (LOX-IMVI, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.453× | -3.3 | 0.13 | 12/36 (HepG2/C3A, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.666× | -3.2 | 0.14 | 15/47 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | 0.675× | -3.1 | 0.16 | 18/43 (KATO III, HOP62, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Rapamycin (drug)]] 5 µM |  | 0.762× | -3.0 | 0.18 | 14/48 (C32, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15353. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 12.5 | 0 | 3 (2 ⚠) | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0583× (z -11.7) |
| [[A498 (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.186× (z -8.8) ⚠ cell-cycle shift, explains ~70% of this change |
| [[A549 (line)]] | wt | 4.90 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.0654× (z -9.1) |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0458× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.123× (z -8.6) ⚠ cell-cycle shift, explains ~63% of this change |
| [[SNU-423 (line)]] | alt | 4.30 | 0 | 1 (1 ⚠) | — | [[Plicamycin (drug)]] 0.5 µM 0.0498× (z -8.8) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.98 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15353), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLRA1P]] | +0.72 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[PLAC8L1]] | +0.72 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[MOCOS]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[GABRR2]] | +0.67 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[NBR2]] | +0.67 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[IARS1]] | +0.66 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[RRH]] | +0.66 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[LINC01355]] | +0.66 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ARL9]] | +0.65 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[CCDC62]] | +0.64 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[PPIEL]] | +0.64 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[VLDLR-AS1]] | +0.63 | +0.51 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBG2]] | -0.52 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[MICU2]] | -0.51 | -0.41 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.539). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.7, -16.4); signed map (14.8, 5.8). **Vector** length 90.3, 18.0% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.2 | +8.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.9 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.2 | +4.4 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -3.9 | -3.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.6 | -3.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.6 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.5 | -3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -2.6 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | -2.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | SMG1 pseudogene 7 |
| Locus type | pseudogene |
| Location | 16q22.1 — chr16:70,219,870-70,246,610 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49864](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49864) · Entrez [100506060](https://www.ncbi.nlm.nih.gov/gene/100506060) · Ensembl [ENSG00000261556](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261556)

## Data

Gene col 15353: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15353); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15353, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15353]; `tensor/DDL_lfc|DDL_z.npy` [15353]; `embed/gene_vectors.npy` [15353]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15353 or target_col == 15353). Every well: [[SMG1P7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMG1P7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

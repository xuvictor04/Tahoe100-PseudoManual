---
symbol: "CRYBB2P1"
type: "gene"
col: 1855
ensembl_id: "ENSG00000100058"
name: "crystallin beta B2 pseudogene 1"
location: "22q11.2-q12.1"
module: 105
arm: "+"
pooled_cpm: 3.22
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# CRYBB2P1

*crystallin beta B2 pseudogene 1* — 22q11.2-q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.23× (z +4.8, q 8e-04, up in 17 of 46 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.68× (z +3.7, q 0.029, up in 18 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.382× (z -6.7, q 1e-08, down in 25 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 0.0409×, NCI-H460 0.179×, SNU-423 0.164×; ⚠ cell-cycle shift, explains ~25% of this change); [[Cobimetinib (drug)]] 0.5 µM in 1 line (C32 0.0568×); [[Sodium Salicylate (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0600×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMS2P3-1]] (+0.78, fdr 7e-06), [[EOLA2]] (+0.75, fdr 7e-06), [[EOLA1]] (+0.74, fdr 7e-06); moves opposite to [[GPATCH8]] (-0.65, fdr 7e-06), [[BPTF]] (-0.61, fdr 1e-05), [[CUX1]] (-0.58, fdr 1e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1855.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +4.8 | 8e-04 | 17/46 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +4.6 | 0.001 | 5/9 (PANC-1, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.78×** | +4.1 | 0.007 | 15/44 (Hs 766T, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.68×** | +3.7 | 0.029 | 18/45 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +3.6 | 0.041 | 12/43 (LoVo, SHP-77, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +3.4 | 0.061 | 16/44 (HCT15, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.45×** | +3.4 | 0.061 | 8/38 (NCI-H2030, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.063 | 5/43 (SW1417, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~18% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.53× | +3.1 | 0.14 | 14/41 (HCT15, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Roxadustat (drug)]] 5 µM |  | 1.55× | +3.0 | 0.14 | 2/43 (HS-578T, J82) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1855.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (C32 0.0409×, NCI-H460 0.179×, SNU-423 0.164×; ⚠ cell-cycle shift, explains ~25% of this change); [[Cobimetinib (drug)]] 0.5 µM in 1 line (C32 0.0568×); [[Sodium Salicylate (drug)]] 0.5 µM in 1 line (NCI-H2030 0.0600×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.382×** | -6.7 | 1e-08 | 25/40 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.491×** | -5.2 | 7e-05 | 20/44 (HepG2/C3A, COLO 205, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.717× | -3.4 | 0.11 | 23/36 (C32, NCI-H460, …) | rises with dose | composition shift |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.611× | -3.3 | 0.13 | 14/43 (NCI-H1573, HCT15, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | 0.707× | -3.2 | 0.13 | 5/45 (COLO 205, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.645× | -3.2 | 0.13 | 8/44 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | 0.653× | -3.1 | 0.15 | 4/44 (H4, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1855. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 5.70 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0409× (z -14.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.0568× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 3.45 | 0 | 1 | — | [[Sodium Salicylate (drug)]] 0.5 µM 0.0600× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 3.07 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 4.88 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1855), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P3-1]] | +0.78 | +0.78 / +0.74 | both halves | 7e-06 |  |
| [[EOLA2]] | +0.75 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[EOLA1]] | +0.74 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[CRYBB2P1-1]] | +0.72 | +0.75 / +0.65 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of CRYBB2P1-1 on the same strand (can correlate by spillover, not regulation) |
| [[BTAF1]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[PDK1]] | +0.66 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[TIMM10B]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[HK2]] | +0.65 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[PMS2P3]] | +0.65 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[NAPB]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[LINC03009]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[BCL2L2]] | +0.65 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[SEPTIN7P13]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH8]] | -0.65 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[BPTF]] | -0.61 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[CUX1]] | -0.58 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[LARP7]] | -0.55 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[ZNF518A]] | -0.55 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[ZNF75A]] | -0.55 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[R3HDM2]] | -0.55 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[KMT5B]] | -0.55 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[SVIL]] | -0.54 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[NFE2L2]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[POGZ]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[ROCK2]] | -0.53 | -0.58 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.0, -23.1); signed map (-40.5, 24.9). **Vector** length 56.9, 8.25% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.6 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | +0.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.6 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +3.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | -0.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +3.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.1 | -6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.7 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +0.5 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.6 | -3.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.5 | -2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | -1.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.4 | -2.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | crystallin beta B2 pseudogene 1 |
| Locus type | pseudogene |
| Location | 22q11.2-q12.1 — chr22:25,455,712-25,459,681 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously CRYB2B |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:2399](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2399) · Entrez [1416](https://www.ncbi.nlm.nih.gov/gene/1416) · Ensembl [ENSG00000100058](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100058)

## Data

Gene col 1855: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1855); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1855, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1855]; `tensor/DDL_lfc|DDL_z.npy` [1855]; `embed/gene_vectors.npy` [1855]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1855 or target_col == 1855). Every well: [[CRYBB2P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRYBB2P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

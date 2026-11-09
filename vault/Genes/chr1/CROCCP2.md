---
symbol: "CROCCP2"
type: "gene"
col: 13280
ensembl_id: "ENSG00000215908"
name: "CROCC pseudogene 2"
location: "1p36.13"
module: 209
arm: "+"
pooled_cpm: 17.56
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/209"]
generated_by: "tahoemap"
---

# CROCCP2

*CROCC pseudogene 2* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.54× (z +5.3, q 7e-05, up in 27 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.855× (z -7.0, q 1e-09, down in 18 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.725× (z -5.4, q 1e-05, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NISCH]] (+0.65, fdr 7e-06), [[ZNF341]] (+0.63, fdr 1e-05), [[BCL7C]] (+0.58, fdr 2e-05); moves opposite to [[ZSWIM6]] (-0.49, fdr 1e-05), [[TRIM69]] (-0.47, fdr 3e-05), [[EHBP1]] (-0.46, fdr 4e-04).
> It is in [[Module 209]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13280.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.54×** | +5.3 | 7e-05 | 27/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.34×** | +4.9 | 2e-04 | 27/48 (LS 180, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +4.6 | 7e-04 | 26/46 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +4.5 | 7e-04 | 23/46 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.44×** | +4.5 | 7e-04 | 21/47 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +3.9 | 0.010 | 19/46 (H4, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.073 | 10/48 (J82, SNU-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | 1.29× | +3.1 | 0.11 | 13/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | 1.30× | +3.1 | 0.11 | 13/48 (A-427, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.12 | 14/48 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | 1.28× | +3.0 | 0.12 | 15/47 (LoVo, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13280.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.855× | -7.0 | 1e-09 | 18/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.639×** | -5.5 | 1e-05 | 22/42 (Panc 03.27, A549, …) | inconsistent across doses | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -5.4 | 1e-05 | 27/47 (H4, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | **0.722×** | -3.7 | 0.031 | 12/37 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.740×** | -3.6 | 0.041 | 18/47 (SW 1088, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.753×** | -3.5 | 0.046 | 17/48 (SW 1271, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.823×** | -3.3 | 0.072 | 17/48 (NCI-H661, C32, …) | top dose only | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | 0.625× | -3.0 | 0.16 | 13/47 (A-427, C-33 A, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13280. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 14.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.140× (z -11.3) |
| [[A-172 (line)]] | wt | 5.68 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0775× (z -9.5) |
| [[A549 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.159× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[C32 (line)]] | wt | 16.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 54.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[Hs 766T (line)]] | wt | 15.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -9.7) |
| [[J82 (line)]] | alt | 13.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -9.1) |
| [[KATO III (line)]] | alt | 12.1 | 0 | 1 | — | [[Futibatinib (drug)]] 0.05 µM 0.187× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -9.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0914× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[SW480 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13280), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NISCH]] | +0.65 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ZNF341]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[BCL7C]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[VPS16]] | +0.58 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[CTC1]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ZNF594-DT]] | +0.56 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[ACTR5]] | +0.55 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[TMEM242]] | +0.54 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[STEEP1]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[ZNF852]] | +0.53 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[CDK5RAP1]] | +0.53 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[E4F1]] | +0.53 | +0.65 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM6]] | -0.49 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TRIM69]] | -0.47 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[EHBP1]] | -0.46 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[MEIS2]] | -0.45 | -0.27 / -0.52 | both halves | 3e-04 |  |
| [[BZW2]] | -0.44 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[SLCO1B3-SLCO1B7]] | -0.44 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[KDM4C]] | -0.44 | -0.36 / -0.41 | both halves | 9e-05 |  |
| [[C19orf38]] | -0.44 | -0.51 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 209]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-6.8, -0.6); signed map (-39.8, -15.4). **Vector** length 72.8, 13.4% of its response variance represented; |z| ≥ 3 in 777 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.8 | +2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.0 | +4.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +2.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.1 | +0.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.8 | +1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.7 | -0.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -3.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Thymol (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | CROCC pseudogene 2 |
| Locus type | pseudogene |
| Location | 1p36.13 — chr1:16,618,969-16,657,232 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | MGC12760; previously CROCCL1 |
| Hallmark sets | HEME_METABOLISM |
| Matched by | ensembl_id |

UniProt [Q86T23](https://www.uniprot.org/uniprotkb/Q86T23) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:28170](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28170) · Entrez [84809](https://www.ncbi.nlm.nih.gov/gene/84809) · UniProt [Q86T23](https://www.uniprot.org/uniprotkb/Q86T23) · Ensembl [ENSG00000215908](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215908)

## Data

Gene col 13280: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13280); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13280, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13280]; `tensor/DDL_lfc|DDL_z.npy` [13280]; `embed/gene_vectors.npy` [13280]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13280 or target_col == 13280). Every well: [[CROCCP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CROCCP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

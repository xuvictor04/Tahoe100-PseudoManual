---
symbol: "FAM3A"
type: "gene"
col: 994
ensembl_id: "ENSG00000071889"
name: "FAM3 metabolism regulating signaling molecule A"
location: "Xq28"
module: 2
arm: "+"
pooled_cpm: 8.31
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# FAM3A

*FAM3 metabolism regulating signaling molecule A* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.59× (z +6.7, q 2e-08, up in 24 of 40 measured lines) ⚠ transcription drop. The strongest without an alert is [[GSK1059615 (drug)]] 0.5 µM: 1.48× (z +4.0, q 0.007, up in 9 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.832× (z -3.7, q 0.084, down in 12 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SNU-423 0.123×; ⚠ toxic); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (A-427 0.143×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS6KB2]] (+0.71, fdr 7e-06), [[CORO1B]] (+0.61, fdr 2e-05), [[SLC2A8]] (+0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 994.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +6.7 | 2e-08 | 24/40 (Hs 766T, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +6.5 | 2e-08 | 13/23 (KATO III, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +6.5 | 2e-08 | 20/29 (KATO III, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +5.5 | 5e-06 | 7/15 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.48×** | +4.0 | 0.007 | 9/44 (HCT15, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.041 | 3/38 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.078 | 8/36 (SNU-423, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.38×** | +3.2 | 0.083 | 7/31 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 994.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SNU-423 0.123×; ⚠ toxic); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (A-427 0.143×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.832×** | -3.7 | 0.084 | 12/48 (Panc 03.27, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.778×** | -3.6 | 0.084 | 11/47 (SW480, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.794× | -3.3 | 0.17 | 11/45 (KATO III, C32, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Pentoxifylline (drug)]] 0.05 µM | ⚠ transcription drop | 0.806× | -3.1 | 0.23 | 5/46 (NCI-H1792, KATO III, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.800× | -3.1 | 0.23 | 12/37 (SNU-423, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 994. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 7.36 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.143× (z -9.0) |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -10.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 994), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS6KB2]] | +0.71 | +0.59 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CORO1B]] | +0.61 | +0.48 / +0.66 | both halves | 2e-05 | **novel candidate** |
| [[SLC2A8]] | +0.60 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[IPO13]] | +0.59 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[ATG4D]] | +0.57 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[CIC]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ATG9A]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[DGAT1]] | +0.53 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[MAPK7]] | +0.53 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[CRAT]] | +0.53 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[NAA80]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[ZNF446]] | +0.53 | +0.53 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.416). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-6.5, -20.4); signed map (-24.7, 2.1). **Vector** length 41.0, 4.17% of its response variance represented; |z| ≥ 3 in 724 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.5 | +6.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +6.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.2 | +4.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +2.9 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +2.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.9 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | FAM3 metabolism regulating signaling molecule A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:154,506,159-154,516,242 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DXS560S, 2-19, XAP-7 |
| Matched by | ensembl_id |

**Function**, from UniProt [P98173](https://www.uniprot.org/uniprotkb/P98173) (Protein FAM3A):

> May act as a defensin against invading fungal microorganisms.

**Summary**, from NCBI Gene [60343](https://www.ncbi.nlm.nih.gov/gene/60343):

> This gene encodes a cytokine-like protein. The expression of this gene may be regulated by peroxisome proliferator-activated receptor gamma, and the encoded protein may be involved in the regulation of glucose and lipid metabolism. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:13749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13749) · Entrez [60343](https://www.ncbi.nlm.nih.gov/gene/60343) · UniProt [P98173](https://www.uniprot.org/uniprotkb/P98173) · Ensembl [ENSG00000071889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071889)

## Data

Gene col 994: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 994); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 994, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 994]; `tensor/DDL_lfc|DDL_z.npy` [994]; `embed/gene_vectors.npy` [994]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 994 or target_col == 994). Every well: [[FAM3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

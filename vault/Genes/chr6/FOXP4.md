---
symbol: "FOXP4"
type: "gene"
col: 5977
ensembl_id: "ENSG00000137166"
name: "forkhead box P4"
location: "6p21.1"
module: 138
arm: "+"
pooled_cpm: 25.17
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# FOXP4

*forkhead box P4* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +9.3, q 9e-18, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.822× (z -4.4, q 0.005, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (COLO 205 0.279×, SW 900 0.224×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.311×); [[Digitoxin (drug)]] 5 µM in 1 line (SK-MEL-2 0.177×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (SNU-1 0.141×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.221×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAMA5]] (+0.60, fdr 1e-05), [[NOTCH1]] (+0.57, fdr 1e-05), [[RIPOR1]] (+0.56, fdr 2e-05); moves opposite to [[ODR4]] (-0.46, fdr 1e-04), [[DHX36]] (-0.43, fdr 2e-04), [[ATP5PD]] (-0.43, fdr 6e-05).
> It is in [[Module 138]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5977.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +9.3 | 9e-18 | 30/48 (CFPAC-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.6 | 5e-06 | 21/47 (A498, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.9 | 2e-04 | 1/48 (HOP62) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.015 | 17/47 (HEC-1-A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.26×** | +3.3 | 0.092 | 12/47 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.22× | +3.1 | 0.16 | 17/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5977.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (COLO 205 0.279×, SW 900 0.224×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.311×); [[Digitoxin (drug)]] 5 µM in 1 line (SK-MEL-2 0.177×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (SNU-1 0.141×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.221×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.822×** | -4.4 | 0.005 | 21/48 (A-427, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.768×** | -4.2 | 0.007 | 20/48 (A-427, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Thymol (drug)]] 5 µM |  | 0.860× | -3.4 | 0.12 | 11/48 (LS 180, NCI-H23, …) | top dose only | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | 0.817× | -3.2 | 0.17 | 10/48 (LoVo, HOP62, …) | inconsistent across doses | position effect removed |
| [[Trimetrexate (drug)]] 0.05 µM |  | 0.821× | -3.2 | 0.18 | 13/48 (H4, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5977. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 19.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.221× (z -8.9) |
| [[PANC-1 (line)]] | alt | 13.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +12.2) | — |
| [[A-427 (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -8.8) ⚠ cell-cycle shift, explains ~61% of this change |
| [[AN3 CA (line)]] | alt | 64.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 54.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +17.5) | — |
| [[COLO 205 (line)]] | alt | 94.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 11.3 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.44× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 24.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 39.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.0) | — |
| [[RKO (line)]] | wt | 30.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.258× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 20.5 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.141× (z -9.2) |
| [[SNU-423 (line)]] | alt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.0) | — |
| [[SW 900 (line)]] | alt | 23.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 32.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5977), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAMA5]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 | same gene group |
| [[NOTCH1]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 | same gene group |
| [[RIPOR1]] | +0.56 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[CRTC2]] | +0.56 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[FURIN]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[PITPNM1]] | +0.55 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[GRK2]] | +0.55 | +0.40 / +0.58 | both halves | 4e-05 |  |
| [[RHBDF1]] | +0.55 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[TESK1]] | +0.53 | +0.38 / +0.64 | both halves | 7e-05 | same gene group |
| [[AKT1]] | +0.51 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[PLEKHO2]] | +0.51 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[IQSEC1]] | +0.51 | +0.38 / +0.60 | both halves | 6e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ODR4]] | -0.46 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[DHX36]] | -0.43 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[ATP5PD]] | -0.43 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[TMEM87A]] | -0.42 | -0.40 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.571). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.6, -6.3); signed map (-9.8, 30.5). **Vector** length 87.0, 16.8% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +9.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.6 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.2 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.7 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +1.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +0.8 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.4 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.9 | -4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -1.1 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -2.0 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -0.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box P4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:41,546,381-41,602,384 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40908 |
| Gene groups (HGNC) | Forkhead boxes; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVH2](https://www.uniprot.org/uniprotkb/Q8IVH2) (Forkhead box protein P4):

> Transcriptional repressor that represses lung-specific expression.

**Summary**, from NCBI Gene [116113](https://www.ncbi.nlm.nih.gov/gene/116113):

> This gene belongs to subfamily P of the forkhead box (FOX) transcription factor family. Forkhead box transcription factors play important roles in the regulation of tissue- and cell type-specific gene transcription during both development and adulthood. Many members of the forkhead box gene family, including members of subfamily P, have roles in mammalian oncogenesis. This gene may play a role in the development of tumors of the kidney and larynx. Alternative splicing of this gene produces …

**Accessions** — [HGNC:20842](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20842) · Entrez [116113](https://www.ncbi.nlm.nih.gov/gene/116113) · UniProt [Q8IVH2](https://www.uniprot.org/uniprotkb/Q8IVH2) · Ensembl [ENSG00000137166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137166)

## Data

Gene col 5977: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5977); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5977, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5977]; `tensor/DDL_lfc|DDL_z.npy` [5977]; `embed/gene_vectors.npy` [5977]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5977 or target_col == 5977). Every well: [[FOXP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

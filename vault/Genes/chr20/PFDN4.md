---
symbol: "PFDN4"
type: "gene"
col: 2074
ensembl_id: "ENSG00000101132"
name: "prefoldin subunit 4"
location: "20q13.2"
module: 64
arm: "+"
pooled_cpm: 55.63
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# PFDN4

*prefoldin subunit 4* — 20q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 2.56× (z +8.9, q 3e-16, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.175×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASP6]] (+0.64, fdr 1e-05), [[NSA2]] (+0.64, fdr 7e-06), [[TBCA]] (+0.63, fdr 1e-05); moves opposite to [[PTBP1]] (-0.57, fdr 1e-05), [[RECQL4]] (-0.55, fdr 4e-05), [[GPAA1]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2074.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.56×** | +8.9 | 3e-16 | 46/48 (KATO III, HOP62, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.89×** | +8.7 | 9e-16 | 45/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.41×** | +8.3 | 1e-14 | 46/48 (KATO III, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +7.6 | 5e-12 | 36/43 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.21×** | +6.6 | 4e-09 | 45/48 (KATO III, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +6.5 | 7e-09 | 40/45 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.69×** | +4.3 | 0.001 | 39/48 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~45% of this change | **1.58×** | +4.3 | 0.001 | 34/47 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +3.9 | 0.006 | 33/48 (C32, LS 180, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.55×** | +3.7 | 0.014 | 29/48 (BT-474, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.4 | 0.034 | 27/47 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.3 | 0.043 | 27/47 (H4, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.3 | 0.043 | 27/42 (Panc 03.27, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.1 | 0.070 | 28/47 (CFPAC-1, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2074.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.175×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | 0.719× | -3.1 | 0.55 | 26/48 (H4, Hs 766T, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.718× | -3.1 | 0.55 | 22/48 (HEC-1-A, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2074. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 40.2 | 3 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.83× (z +9.2) | — |
| [[KATO III (line)]] | alt | 59.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.17× (z +11.1) | — |
| [[A549 (line)]] | wt | 49.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.28× (z +8.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 348 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.78× (z +8.9) | — |
| [[COLO 205 (line)]] | alt | 28.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.57× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -14.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 41.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +9.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 41.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.81× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 56.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 78.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 99.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 67.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 96.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2074), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASP6]] | +0.64 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[NSA2]] | +0.64 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[TBCA]] | +0.63 | +0.55 / +0.67 | both halves | 1e-05 | pathway: Protein folding; STRING 466 |
| [[PSMA7]] | +0.61 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[FAM241B]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[EAPP]] | +0.59 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[DCTN6]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[RUFY2]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[NDUFB9]] | +0.57 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[MRPL45]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PLEKHM3]] | +0.57 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[NACA]] ⚠ | +0.57 | +0.48 / +0.62 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PSMC1]] | +0.57 | +0.64 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTBP1]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[RECQL4]] | -0.55 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[GPAA1]] | -0.54 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[CFL1]] | -0.53 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[PYGO2]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[NCAPG2]] | -0.52 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[RRM2]] | -0.52 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[TK1]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[KIFC1]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.51 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[C4orf46]] | -0.51 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[MCM8]] | -0.51 | -0.36 / -0.60 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.627). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-48.5, -4.8); signed map (-19.2, -5.4). **Vector** length 82.5, 27.7% of its response variance represented; |z| ≥ 3 in 612 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.7 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.8 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.4 | +8.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.7 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.7 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | -0.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.3 | -3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -1.1 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.6 | -0.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.5 | +0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.4 | -0.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | prefoldin subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.2 — chr20:54,208,087-54,228,052 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PFD4, C-1, C1 |
| Gene groups (HGNC) | Prefoldin subunits |
| Reactome | 4 pathways, smallest: Prefoldin mediated transfer of substrate  to CCT/TriC; Cooperation of Prefoldin and TriC/CCT  in actin and tubulin folding; Chaperonin-mediated protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQP4](https://www.uniprot.org/uniprotkb/Q9NQP4) (Prefoldin subunit 4):

> Binds specifically to cytosolic chaperonin (c-CPN) and transfers target proteins to it. Binds to nascent polypeptide chain and promotes folding in an environment in which there are many competing pathways for nonnative proteins.

**Summary**, from NCBI Gene [5203](https://www.ncbi.nlm.nih.gov/gene/5203):

> This gene encodes a member of the prefoldin beta subunit family. The encoded protein is one of six subunits of prefoldin, a molecular chaperone complex that binds and stabilizes newly synthesized polypeptides, thereby allowing them to fold correctly. The complex, consisting of two alpha and four beta subunits, forms a double beta barrel assembly with six protruding coiled-coils. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8868) · Entrez [5203](https://www.ncbi.nlm.nih.gov/gene/5203) · UniProt [Q9NQP4](https://www.uniprot.org/uniprotkb/Q9NQP4) · Ensembl [ENSG00000101132](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101132)

## Data

Gene col 2074: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2074); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2074, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2074]; `tensor/DDL_lfc|DDL_z.npy` [2074]; `embed/gene_vectors.npy` [2074]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2074 or target_col == 2074). Every well: [[PFDN4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PFDN4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

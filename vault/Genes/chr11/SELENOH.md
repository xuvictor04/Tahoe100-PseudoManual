---
symbol: "SELENOH"
type: "gene"
col: 13061
ensembl_id: "ENSG00000211450"
name: "selenoprotein H"
location: "11q12.1"
module: 24
arm: "+"
pooled_cpm: 33.38
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# SELENOH

*selenoprotein H* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.23× (z +5.8, q 4e-06, up in 40 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.665× (z -4.2, q 0.013, down in 37 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.271×, A-427 0.334×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.162×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COX6B1]] (+0.75, fdr 7e-06), [[SMIM26]] (+0.74, fdr 2e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[MINCR]] (+0.73, fdr 7e-06), [[SNHG9]] (+0.72, fdr 1e-05); moves opposite to [[MAPRE1]] (-0.70, fdr 3e-05), [[LIN7C]] (-0.68, fdr 4e-05), [[DYNC1H1]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13061.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.23×** | +5.8 | 4e-06 | 40/43 (LoVo, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.92×** | +4.5 | 0.002 | 29/35 (LOX-IMVI, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.70×** | +3.5 | 0.076 | 30/42 (C-33 A, LOX-IMVI, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.4 | 0.076 | 31/45 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.40×** | +3.4 | 0.076 | 35/47 (RKO, A-427, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | 1.55× | +3.2 | 0.15 | 27/45 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13061.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.271×, A-427 0.334×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.162×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.665×** | -4.2 | 0.013 | 37/46 (SNU-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | 0.640× | -3.3 | 0.21 | 26/47 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.620× | -3.2 | 0.21 | 38/47 (LS 180, NCI-H2347, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | 0.648× | -3.2 | 0.21 | 24/47 (hTERT-HPNE, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13061. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 42.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -8.9) |
| [[C-33 A (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SNU-1 (line)]] | wt | 44.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -9.2) |
| [[A-172 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.54 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 48.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13061), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 18 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX6B1]] | +0.75 | +0.58 / +0.81 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.74 | +0.48 / +0.80 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MINCR]] | +0.73 | +0.60 / +0.76 | both halves | 7e-06 |  |
| [[SNHG9]] | +0.72 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[TMEM258]] | +0.72 | +0.53 / +0.78 | both halves | 1e-05 |  |
| [[NCBP2AS2]] | +0.72 | +0.52 / +0.77 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | +0.71 | +0.46 / +0.78 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL23]] | +0.71 | +0.49 / +0.76 | both halves | 1e-05 |  |
| [[SNHG19]] | +0.69 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[CHCHD1]] | +0.69 | +0.46 / +0.75 | both halves | 3e-05 |  |
| [[TOMM7]] | +0.69 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[SCAND1]] | +0.69 | +0.45 / +0.73 | both halves | 3e-05 |  |
| [[ATP5PD]] | +0.68 | +0.49 / +0.77 | both halves | 2e-05 |  |
| [[NDUFA1]] | +0.68 | +0.56 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE1]] | -0.70 | -0.44 / -0.79 | both halves | 3e-05 |  |
| [[LIN7C]] | -0.68 | -0.40 / -0.76 | both halves | 4e-05 |  |
| [[DYNC1H1]] | -0.64 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[PRELID3B]] | -0.64 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[YWHAQ]] | -0.64 | -0.44 / -0.73 | both halves | 3e-05 |  |
| [[STIP1]] | -0.62 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[SPTBN1]] | -0.62 | -0.34 / -0.64 | both halves | 1e-04 |  |
| [[TWF1]] | -0.62 | -0.47 / -0.65 | both halves | 2e-05 |  |
| [[YWHAZ]] | -0.61 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ZNF664]] | -0.60 | -0.32 / -0.63 | both halves | 2e-04 |  |
| [[MOB1A]] | -0.60 | -0.42 / -0.68 | both halves | 4e-05 |  |
| [[AP2M1]] | -0.60 | -0.45 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.6, -21.3); signed map (-30.4, 7.1). **Vector** length 57.4, 16.0% of its response variance represented; |z| ≥ 3 in 455 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.8 | +2.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.6 | +1.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +1.3 | +1.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -3.7 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -3.4 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -2.7 | +3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -2.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.6 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | selenoprotein H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:57,741,491-57,743,554 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SELH; previously C11orf31 |
| Gene groups (HGNC) | Selenoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZQ5](https://www.uniprot.org/uniprotkb/Q8IZQ5) (Selenoprotein H):

> May be involved in a redox-related process.

**Summary**, from NCBI Gene [280636](https://www.ncbi.nlm.nih.gov/gene/280636):

> This gene encodes a nucleolar protein, which belongs to the SelWTH family. It functions as an oxidoreductase, and has been shown to protect neurons against UVB-induced damage by inhibiting apoptotic cell death pathways, promote mitochondrial biogenesis and mitochondrial function, and suppress cellular senescence through genome maintenance and redox regulation. This protein is a selenoprotein, containing the rare amino acid selenocysteine (Sec) at its active site. Sec is encoded by the UGA …

**Accessions** — [HGNC:18251](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18251) · Entrez [280636](https://www.ncbi.nlm.nih.gov/gene/280636) · UniProt [Q8IZQ5](https://www.uniprot.org/uniprotkb/Q8IZQ5) · Ensembl [ENSG00000211450](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000211450)

## Data

Gene col 13061: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13061); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13061, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13061]; `tensor/DDL_lfc|DDL_z.npy` [13061]; `embed/gene_vectors.npy` [13061]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13061 or target_col == 13061). Every well: [[SELENOH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SELENOH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

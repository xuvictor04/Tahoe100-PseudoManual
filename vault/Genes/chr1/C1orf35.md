---
symbol: "C1orf35"
type: "gene"
col: 6804
ensembl_id: "ENSG00000143793"
name: "chromosome 1 open reading frame 35"
location: "1q42.13"
module: 24
arm: "+"
pooled_cpm: 18.82
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# C1orf35

*chromosome 1 open reading frame 35* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.81× (z +4.6, q 0.002, up in 30 of 43 measured lines) ⚠ toxic. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.592× (z -4.3, q 0.011, down in 27 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (BT-474 0.101×, SW 900 0.206×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 0.258×, J82 0.346×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.149×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCGF1]] (+0.75, fdr 7e-06, ⚠ PCGF1 in the vector space only through flagged drug-doses), [[ENKD1]] (+0.73, fdr 1e-05), [[C16orf91]] (+0.73, fdr 2e-05), [[POP7]] (+0.72, fdr 3e-05); moves opposite to [[LIN7C]] (-0.67, fdr 7e-05), [[DHFR]] (-0.67, fdr 4e-05), [[MOB1A]] (-0.67, fdr 2e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6804.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +4.6 | 0.002 | 30/43 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.56×** | +3.6 | 0.092 | 27/44 (BT-474, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6804.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (BT-474 0.101×, SW 900 0.206×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 0.258×, J82 0.346×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.149×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.592×** | -4.3 | 0.011 | 27/48 (SW 900, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.631×** | -3.8 | 0.048 | 26/46 (NCI-H460, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.742× | -3.4 | 0.11 | 24/47 (LOX-IMVI, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.652× | -3.2 | 0.18 | 15/47 (BT-474, SW480, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.688× | -3.0 | 0.26 | 19/48 (Hs 766T, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6804. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.101× (z -11.2) |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 12.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 28.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.206× (z -8.5) |
| [[A-172 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6804), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 10 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCGF1]] ⚠ | +0.75 | +0.62 / +0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ENKD1]] | +0.73 | +0.54 / +0.77 | both halves | 1e-05 | STRING 439 |
| [[C16orf91]] | +0.73 | +0.48 / +0.78 | both halves | 2e-05 |  |
| [[SMIM26]] ⚠ | +0.72 | +0.52 / +0.80 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[POP7]] | +0.72 | +0.46 / +0.78 | both halves | 3e-05 |  |
| [[RNF113A]] | +0.72 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[LEO1]] | +0.72 | +0.52 / +0.75 | both halves | 1e-05 |  |
| [[NCBP2AS2]] | +0.71 | +0.41 / +0.80 | both halves | 4e-05 |  |
| [[SCNM1]] | +0.70 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[MTIF3]] | +0.69 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[MRPS26]] | +0.69 | +0.48 / +0.73 | both halves | 2e-05 |  |
| [[TIMM29]] | +0.69 | +0.45 / +0.78 | both halves | 3e-05 |  |
| [[MPHOSPH10]] | +0.68 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[ING2]] | +0.68 | +0.41 / +0.78 | both halves | 4e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7C]] | -0.67 | -0.38 / -0.79 | both halves | 7e-05 |  |
| [[DHFR]] | -0.67 | -0.41 / -0.76 | both halves | 4e-05 |  |
| [[MOB1A]] | -0.67 | -0.48 / -0.72 | both halves | 2e-05 |  |
| [[MAPRE1]] | -0.65 | -0.40 / -0.74 | both halves | 5e-05 |  |
| [[UBE2V1]] | -0.64 | -0.42 / -0.68 | both halves | 4e-05 |  |
| [[GALC]] | -0.61 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[VMA21]] | -0.60 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[GNG12]] | -0.60 | -0.32 / -0.69 | both halves | 1e-04 |  |
| [[ERLIN2]] | -0.60 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[PAPOLA]] | -0.60 | -0.32 / -0.70 | both halves | 1e-04 |  |
| [[IPO5]] | -0.59 | -0.35 / -0.69 | both halves | 1e-04 |  |
| [[SRP9]] | -0.59 | -0.33 / -0.67 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.673). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.1, -13.2); signed map (-14.3, -7.1). **Vector** length 75.7, 20.7% of its response variance represented; |z| ≥ 3 in 393 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -0.7 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.4 | +1.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -8.2 | -0.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.8 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -7.5 | -0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.2 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[Adenine (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.8 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 1 open reading frame 35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:228,100,726-228,105,411 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4174, MMTAG2 |
| Matched by | ensembl_id |

UniProt [Q9BU76](https://www.uniprot.org/uniprotkb/Q9BU76) carries no function annotation.

**Summary**, from NCBI Gene [79169](https://www.ncbi.nlm.nih.gov/gene/79169):

> Enables RNA binding activity. Predicted to be located in extracellular region; ficolin-1-rich granule lumen; and secretory granule lumen. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19032](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19032) · Entrez [79169](https://www.ncbi.nlm.nih.gov/gene/79169) · UniProt [Q9BU76](https://www.uniprot.org/uniprotkb/Q9BU76) · Ensembl [ENSG00000143793](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143793)

## Data

Gene col 6804: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6804); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6804, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6804]; `tensor/DDL_lfc|DDL_z.npy` [6804]; `embed/gene_vectors.npy` [6804]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6804 or target_col == 6804). Every well: [[C1orf35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1orf35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

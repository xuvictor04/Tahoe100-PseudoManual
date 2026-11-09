---
symbol: "AARSD1"
type: "gene"
col: 15508
ensembl_id: "ENSG00000266967"
name: "alanyl-tRNA synthetase domain containing 1"
location: "17q21.31"
module: 12
arm: "+"
pooled_cpm: 27.4
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# AARSD1

*alanyl-tRNA synthetase domain containing 1* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.03× (z +11.1, q 5e-26, up in 36 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 0.186×, MIA PaCa-2 0.236×, C32 0.305×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.114×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cepharanthine (drug)]] 5 µM in 1 line (H4 0.271×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RINT1]] (+0.74, fdr 7e-06), [[PARL]] (+0.72, fdr 7e-06), [[DRG1]] (+0.64, fdr 7e-06); moves opposite to [[MAPRE1]] (-0.56, fdr 1e-05), [[LINC02035]] (-0.54, fdr 4e-05), [[YWHAZ]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15508.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +11.1 | 5e-26 | 36/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.75×** | +8.8 | 3e-16 | 41/48 (LS 180, SNU-423, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +8.2 | 4e-14 | 41/48 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +7.7 | 2e-12 | 31/45 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +7.6 | 3e-12 | 38/48 (A-427, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +6.9 | 4e-10 | 28/47 (LS 180, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.46×** | +5.6 | 1e-06 | 26/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +4.9 | 6e-05 | 21/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +4.9 | 7e-05 | 24/48 (KATO III, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +4.8 | 1e-04 | 22/48 (KATO III, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.35×** | +4.7 | 1e-04 | 23/46 (PANC-1, NCI-H23, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +4.6 | 2e-04 | 20/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.31×** | +4.1 | 0.002 | 23/48 (NCI-H1573, SW480, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.25×** | +3.4 | 0.023 | 16/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.042 | 13/46 (RPMI-7951, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.066 | 13/48 (LoVo, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.072 | 11/46 (HT-29, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.30×** | +3.0 | 0.093 | 8/48 (PANC-1, A-427, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15508.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (LS 180 0.186×, MIA PaCa-2 0.236×, C32 0.305×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW48 0.114×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Cepharanthine (drug)]] 5 µM in 1 line (H4 0.271×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.815× | -3.2 | 0.67 | 16/47 (A-172, NCI-H460, …) | two highest doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15508. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 19.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.186× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 28.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.14× (z +8.5) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.236× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 25.3 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.271× (z -8.5) |
| [[HOP62 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +10.1) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +9.3) | — |
| [[SW48 (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 33.9 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +9.9) | — |
| [[A-172 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15508), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RINT1]] | +0.74 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[PARL]] | +0.72 | +0.76 / +0.60 | both halves | 7e-06 |  |
| [[DRG1]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[CDK5RAP1]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[SMN2]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CBY1]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[MPHOSPH10]] | +0.62 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[PSMD5]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[NDUFV3]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[DHX57]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[PPIL2]] | +0.62 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[ANKS3]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE1]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[LINC02035]] | -0.54 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[YWHAZ]] | -0.52 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[RFX3]] | -0.52 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.453). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-35.9, -7.8); signed map (-13.9, -13.3). **Vector** length 84.4, 17.8% of its response variance represented; |z| ≥ 3 in 840 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.7 | +11.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +1.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.9 | +2.2 |
|  | [[EX229 (drug)]] 0.5 µM |  | +1.9 | +2.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | +0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -3.2 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | alanyl-tRNA synthetase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:42,950,526-42,964,498 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2744, AlaXp |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTE6](https://www.uniprot.org/uniprotkb/Q9BTE6) (Alanyl-tRNA editing protein Aarsd1):

> Functions in trans to edit the amino acid moiety from incorrectly charged tRNA(Ala).

**Summary**, from NCBI Gene [80755](https://www.ncbi.nlm.nih.gov/gene/80755):

> Predicted to enable Ser-tRNA(Ala) deacylase activity. Predicted to be involved in regulation of translational fidelity. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28417](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28417) · Entrez [80755](https://www.ncbi.nlm.nih.gov/gene/80755) · UniProt [Q9BTE6](https://www.uniprot.org/uniprotkb/Q9BTE6) · Ensembl [ENSG00000266967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000266967)

## Data

Gene col 15508: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15508); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15508, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15508]; `tensor/DDL_lfc|DDL_z.npy` [15508]; `embed/gene_vectors.npy` [15508]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15508 or target_col == 15508). Every well: [[AARSD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AARSD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

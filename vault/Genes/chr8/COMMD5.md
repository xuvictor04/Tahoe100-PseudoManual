---
symbol: "COMMD5"
type: "gene"
col: 9983
ensembl_id: "ENSG00000170619"
name: "COMM domain containing 5"
location: "8q24.3"
module: 7
arm: "+"
pooled_cpm: 6.98
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# COMMD5

*COMM domain containing 5* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +7.0, q 1e-09, up in 23 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.798× (z -4.5, q 0.004, down in 16 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSSC4]] (+0.73, fdr 7e-06), [[FLAD1]] (+0.68, fdr 7e-06), [[ZNF513]] (+0.66, fdr 7e-06); moves opposite to [[PPP1CC]] (-0.56, fdr 2e-05), [[CLSTN1]] (-0.55, fdr 1e-04), [[TMSB4X]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9983.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +7.0 | 1e-09 | 23/41 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +5.8 | 2e-06 | 17/44 (KATO III, PANC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +5.3 | 2e-05 | 13/47 (A498, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +5.0 | 6e-05 | 17/45 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.6 | 5e-04 | 10/33 (A498, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.005 | 8/45 (NCI-H23, AsPC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.012 | 11/44 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.015 | 12/43 (HT-29, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.027 | 11/41 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.055 | 5/41 (Panc 03.27, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.081 | 3/35 (PANC-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.17× | +3.1 | 0.091 | 7/45 (Panc 03.27, HCT15, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.093 | 3/41 (HT-29, SW 900, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9983.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.798×** | -4.5 | 0.004 | 16/46 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.741×** | -4.1 | 0.014 | 16/44 (NCI-H23, C-33 A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.771×** | -3.7 | 0.047 | 12/44 (NCI-H2347, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.791× | -3.3 | 0.13 | 16/31 (HOP62, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | 0.653× | -3.1 | 0.20 | 4/43 (SK-MEL-2, HepG2/C3A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9983. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 8.24 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0911× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 9.56 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.138× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 7.04 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.112× (z -9.6) |
| [[KATO III (line)]] | alt | 6.14 | 0 | 1 | — | [[Pemigatinib (drug)]] 0.05 µM 0.102× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 5.26 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0787× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[MIA PaCa-2 (line)]] | alt | 5.92 | 0 | 1 | — | [[Tofacitinib (drug)]] 0.05 µM 0.0667× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 4.54 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0640× (z -9.8) ⚠ cell-cycle shift, explains ~10% of this change |
| [[SW 900 (line)]] | alt | 6.94 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0867× (z -8.8) |
| [[A-172 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9983), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSSC4]] | +0.73 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[FLAD1]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ZNF513]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[SLC66A1]] | +0.64 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[POLR3F]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[TIMM22]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[PHF5A]] | +0.64 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[TMEM199]] | +0.63 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[ZNF581]] | +0.63 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ARL16]] | +0.63 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[ZNF746]] | +0.62 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[KTI12]] | +0.62 | +0.53 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1CC]] | -0.56 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[CLSTN1]] | -0.55 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[TMSB4X]] | -0.55 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[HNRNPC]] | -0.55 | -0.31 / -0.62 | both halves | 2e-04 |  |
| [[PSIP1]] | -0.54 | -0.26 / -0.53 | both halves | 4e-04 |  |
| [[H2AZ2]] | -0.53 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[LRP11]] | -0.53 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[CXADR]] | -0.53 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[HSDL2]] | -0.52 | -0.38 / -0.52 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.672). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-45.3, 1.6); signed map (-6.0, -25.7). **Vector** length 53.2, 6.98% of its response variance represented; |z| ≥ 3 in 717 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.1 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.0 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.7 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.6 | -3.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.1 | -0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -4.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | COMM domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,841,042-144,853,736 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HT002, FLJ13008, HCaRG |
| Gene groups (HGNC) | COMM domain containing |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZQ3](https://www.uniprot.org/uniprotkb/Q9GZQ3) (COMM domain-containing protein 5):

> Scaffold protein in the commander complex that is essential for endosomal recycling of transmembrane cargos; the commander complex is composed of the CCC subcomplex and the retriever subcomplex. May modulate activity of cullin-RING E3 ubiquitin ligase (CRL) complexes. Negatively regulates cell proliferation (By similarity). Negatively regulates cell cycle G2/M phase transition probably by transactivating p21/CDKN1A through the p53/TP53-independent signaling pathway (By similarity). Involved in …

**Summary**, from NCBI Gene [28991](https://www.ncbi.nlm.nih.gov/gene/28991):

> Predicted to be involved in proximal tubule morphogenesis. Located in cytosol and nucleoplasm. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17902](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17902) · Entrez [28991](https://www.ncbi.nlm.nih.gov/gene/28991) · UniProt [Q9GZQ3](https://www.uniprot.org/uniprotkb/Q9GZQ3) · Ensembl [ENSG00000170619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170619)

## Data

Gene col 9983: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9983); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9983, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9983]; `tensor/DDL_lfc|DDL_z.npy` [9983]; `embed/gene_vectors.npy` [9983]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9983 or target_col == 9983). Every well: [[COMMD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COMMD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

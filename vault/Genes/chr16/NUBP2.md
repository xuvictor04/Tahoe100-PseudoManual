---
symbol: "NUBP2"
type: "gene"
col: 1757
ensembl_id: "ENSG00000095906"
name: "NUBP iron-sulfur cluster assembly factor 2, cytosolic"
location: "16p13.3"
module: 3
arm: "+"
pooled_cpm: 8.02
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# NUBP2

*NUBP iron-sulfur cluster assembly factor 2, cytosolic* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.08× (z +9.4, q 3e-18, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.746× (z -3.8, q 0.082, down in 16 of 47 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (J82 0.280×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 0.296×; ⚠ cell-cycle shift, would explain all of this change); [[Cobimetinib (drug)]] 0.05 µM in 1 line (SNU-423 0.0871×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf174]] (+0.82, fdr 7e-06), [[SIVA1]] (+0.72, fdr 1e-05), [[SPSB3]] (+0.71, fdr 1e-05, ⚠ same locus), [[MRPL55]] (+0.71, fdr 1e-05); moves opposite to [[ZNF300]] (-0.57, fdr 6e-05), [[ARRDC3-AS1]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1757.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +9.4 | 3e-18 | 38/47 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +8.4 | 1e-14 | 35/47 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.82×** | +7.4 | 3e-11 | 8/13 (SW480, NCI-H2347, …) | rises with dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.71×** | +6.9 | 9e-10 | 27/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +6.6 | 6e-09 | 27/38 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.9 | 3e-07 | 23/43 (C32, HT-29, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.52×** | +5.4 | 6e-06 | 12/32 (SW480, SNU-423, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.3 | 6e-06 | 18/36 (SW480, A-172, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.36×** | +3.8 | 0.010 | 15/37 (A-172, SNU-423, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.072 | 9/44 (AsPC-1, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1757.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (J82 0.280×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 0.296×; ⚠ cell-cycle shift, would explain all of this change); [[Cobimetinib (drug)]] 0.05 µM in 1 line (SNU-423 0.0871×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.746×** | -3.8 | 0.082 | 16/47 (A498, SW 900, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.591× | -3.6 | 0.11 | 11/43 (A-427, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.776× | -3.3 | 0.15 | 15/47 (A498, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.777× | -3.3 | 0.15 | 13/45 (H4, HCT15, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1757. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 5.75 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0871× (z -8.6) |
| [[A-172 (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1757), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf174]] | +0.82 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[SIVA1]] | +0.72 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[SPSB3]] | +0.71 | +0.65 / +0.57 | both halves | 1e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[MRPL55]] | +0.71 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[LCMT1]] | +0.69 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[OXNAD1]] | +0.68 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[CCNQ]] | +0.67 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[NPRL2]] | +0.66 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ZNRD2]] | +0.65 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[ANKS3]] | +0.65 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[COX14]] | +0.65 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[YIPF2]] | +0.65 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[PUSL1]] | +0.64 | +0.45 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF300]] | -0.57 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[ARRDC3-AS1]] | -0.53 | -0.32 / -0.43 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (0.5, -16.5); signed map (-36.7, 3.7). **Vector** length 53.6, 7.25% of its response variance represented; |z| ≥ 3 in 765 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +8.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.7 | +9.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.4 | +6.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.9 | +6.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | +1.6 | +3.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.0 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +1.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +0.9 | +2.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +0.9 | +1.1 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -3.7 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -0.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.3 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | NUBP iron-sulfur cluster assembly factor 2, cytosolic |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,782,932-1,789,186 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CFD1, CIAO6 |
| Gene groups (HGNC) | Cytosolic iron-sulfur assembly components |
| Reactome | 1 pathways, smallest: Cytosolic iron-sulfur cluster assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5Y2](https://www.uniprot.org/uniprotkb/Q9Y5Y2) (Cytosolic Fe-S cluster assembly factor NUBP2):

> Component of the cytosolic iron-sulfur (Fe/S) protein assembly (CIA) machinery. Required for maturation of extramitochondrial Fe-S proteins. The NUBP1-NUBP2 heterotetramer forms a Fe-S scaffold complex, mediating the de novo assembly of an Fe-S cluster and its transfer to target apoproteins. Negatively regulates cilium formation and structure.

**Summary**, from NCBI Gene [10101](https://www.ncbi.nlm.nih.gov/gene/10101):

> This gene encodes an adenosine triphosphate (ATP) and metal-binding protein that is required for the assembly of cyotosolic iron-sulfur proteins. The encoded protein functions in a heterotetramer with nucleotide-binding protein 1 (NUBP1). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2013]

**Accessions** — [HGNC:8042](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8042) · Entrez [10101](https://www.ncbi.nlm.nih.gov/gene/10101) · UniProt [Q9Y5Y2](https://www.uniprot.org/uniprotkb/Q9Y5Y2) · Ensembl [ENSG00000095906](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095906)

## Data

Gene col 1757: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1757); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1757, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1757]; `tensor/DDL_lfc|DDL_z.npy` [1757]; `embed/gene_vectors.npy` [1757]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1757 or target_col == 1757). Every well: [[NUBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

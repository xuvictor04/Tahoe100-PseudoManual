---
symbol: "SCAND1"
type: "gene"
col: 10075
ensembl_id: "ENSG00000171222"
name: "SCAN domain containing 1"
location: "20q11.23"
module: 11
arm: "+"
pooled_cpm: 10.46
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# SCAND1

*SCAN domain containing 1* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.23× (z +7.4, q 7e-11, up in 34 of 36 measured lines) ⚠ toxic. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.71× (z +3.5, q 0.075, up in 21 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.145×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.178×; ⚠ cell-cycle shift, explains ~0% of this change); [[Clofarabine (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0635×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMIM26]] (+0.81, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[EMC6]] (+0.78, fdr 8e-06), [[ZNF593]] (+0.77, fdr 8e-06), [[OXLD1]] (+0.76, fdr 1e-05); moves opposite to [[IPO5]] (-0.72, fdr 1e-05), [[MAPK9]] (-0.68, fdr 1e-05), [[TXNDC5]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[UBE2I]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10075.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.23×** | +7.4 | 7e-11 | 34/36 (KATO III, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **2.08×** | +4.8 | 4e-04 | 27/42 (MIA PaCa-2, SW 900, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.71×** | +3.5 | 0.075 | 21/46 (LS 180, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.73×** | +3.5 | 0.076 | 25/45 (LS 180, HOP62, …) | rises with dose | composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.63× | +3.2 | 0.15 | 25/46 (Panc 03.27, J82, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.39× | +3.1 | 0.19 | 18/48 (SW1417, AsPC-1, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.38× | +3.0 | 0.20 | 18/45 (KATO III, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10075.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.145×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H23 0.178×; ⚠ cell-cycle shift, explains ~0% of this change); [[Clofarabine (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0635×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.608× | -3.0 | 0.50 | 15/47 (RKO, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10075. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.145× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 6.46 | 0 | 1 | — | [[Clofarabine (drug)]] 0.5 µM 0.0635× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 6.59 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10075), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 10 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM26]] ⚠ | +0.81 | +0.67 / +0.88 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[EMC6]] | +0.78 | +0.57 / +0.86 | both halves | 8e-06 |  |
| [[ZNF593]] | +0.77 | +0.58 / +0.82 | both halves | 8e-06 |  |
| [[OXLD1]] | +0.76 | +0.52 / +0.80 | both halves | 1e-05 |  |
| [[MED19]] | +0.75 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[FDX2]] | +0.74 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[RPP25L]] | +0.74 | +0.57 / +0.85 | both halves | 9e-06 |  |
| [[MRPS18C]] | +0.74 | +0.60 / +0.77 | both halves | 7e-06 |  |
| [[NCBP2AS2]] | +0.73 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[RPL36AL]] ⚠ | +0.72 | +0.44 / +0.84 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EID2]] | +0.72 | +0.60 / +0.81 | both halves | 7e-06 |  |
| [[MPLKIP]] | +0.72 | +0.47 / +0.78 | both halves | 2e-05 |  |
| [[MRPL32]] | +0.72 | +0.40 / +0.79 | both halves | 5e-05 |  |
| [[TBCC]] | +0.72 | +0.58 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO5]] | -0.72 | -0.56 / -0.77 | both halves | 1e-05 |  |
| [[MAPK9]] | -0.68 | -0.52 / -0.72 | both halves | 1e-05 |  |
| [[TXNDC5]] | -0.68 | -0.49 / -0.77 | both halves | 1e-05 |  |
| [[YWHAQ]] | -0.64 | -0.58 / -0.70 | both halves | 7e-06 |  |
| [[DHFR]] | -0.64 | -0.35 / -0.76 | both halves | 1e-04 |  |
| [[RPSA]] | -0.64 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[ARHGAP4]] | -0.64 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.63 | -0.46 / -0.68 | both halves | 3e-05 |  |
| [[MACROH2A1]] | -0.63 | -0.45 / -0.69 | both halves | 3e-05 |  |
| [[RBBP7]] | -0.62 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[TFDP1]] | -0.62 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[SMG1P3]] | -0.62 | -0.36 / -0.74 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBE2I]] | C | UBE2I's natural level strengthens SCAND1's drug response | UBE2I's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.04; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.7, -11.6); signed map (-11.8, -6.7). **Vector** length 72.0, 18.3% of its response variance represented; |z| ≥ 3 in 473 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.8 | +7.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +3.8 | +3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.7 | +3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +1.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +2.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.3 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.5 | +0.4 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.0 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | +0.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -3.0 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.2 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.5 µM |  | -1.2 | -2.3 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | SCAN domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:35,953,617-35,959,472 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SDP1, RAZ1 |
| Gene groups (HGNC) | SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P57086](https://www.uniprot.org/uniprotkb/P57086) (SCAN domain-containing protein 1):

> May regulate transcriptional activity.

**Summary**, from NCBI Gene [51282](https://www.ncbi.nlm.nih.gov/gene/51282):

> This gene encodes a SCAN box domain-containing protein. The SCAN domain is a highly conserved, leucine-rich motif of approximately 60 aa originally found within a subfamily of zinc finger proteins. This gene belongs to a family of genes that encode an isolated SCAN domain, but no zinc finger motif. This protein binds to and may regulate the function of the transcription factor myeloid zinc finger 1B. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:10566](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10566) · Entrez [51282](https://www.ncbi.nlm.nih.gov/gene/51282) · UniProt [P57086](https://www.uniprot.org/uniprotkb/P57086) · Ensembl [ENSG00000171222](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171222)

## Data

Gene col 10075: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10075); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10075, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10075]; `tensor/DDL_lfc|DDL_z.npy` [10075]; `embed/gene_vectors.npy` [10075]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10075 or target_col == 10075). Every well: [[SCAND1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCAND1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

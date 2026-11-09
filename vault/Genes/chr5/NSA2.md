---
symbol: "NSA2"
type: "gene"
col: 8936
ensembl_id: "ENSG00000164346"
name: "NSA2 ribosome biogenesis factor"
location: "5q13.3"
module: 43
arm: "+"
pooled_cpm: 74.45
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# NSA2

*NSA2 ribosome biogenesis factor* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.99× (z +7.6, q 2e-11, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.80× (z +4.8, q 2e-04, up in 37 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.291×; ⚠ cell-cycle shift, would explain all of this change); [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.190×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NACA]] (+0.81, fdr 7e-06, ⚠ NACA in the vector space only through flagged drug-doses), [[RPL37]] (+0.79, fdr 7e-06, ⚠ RPL37 in the vector space only through flagged drug-doses), [[RPL34]] (+0.78, fdr 7e-06), [[SNHG6]] (+0.77, fdr 7e-06), [[RPL35A]] (+0.74, fdr 7e-06); moves opposite to [[NUP188]] (-0.67, fdr 1e-05), [[SIGMAR1]] (-0.66, fdr 7e-06), [[PYGO2]] (-0.65, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8936.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.99×** | +7.6 | 2e-11 | 47/49 (MIA PaCa-2, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.25×** | +6.5 | 3e-08 | 41/44 (A549, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +5.9 | 6e-07 | 39/45 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +4.8 | 2e-04 | 37/48 (SW480, SK-MEL-2, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **1.74×** | +4.6 | 5e-04 | 41/48 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.0 | 0.006 | 42/47 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +3.8 | 0.013 | 40/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.069 | 35/48 (HOP62, SK-MEL-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | 1.48× | +3.1 | 0.11 | 29/47 (LoVo, H4, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 1.48× | +3.1 | 0.13 | 33/48 (A-172, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.291×; ⚠ cell-cycle shift, would explain all of this change); [[Methylthiouracil (drug)]] 5 µM in 1 line (NCI-H596 0.190×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8936. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 70.7 | 2 (2 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.37× (z +9.2) ⚠ toxic | — |
| [[NCI-H460 (line)]] | wt | 76.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.67× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 80.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 78.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.77× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[AN3 CA (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 65.1 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.42× (z +8.9) ⚠ toxic | — |
| [[NCI-H596 (line)]] | alt | 83.5 | 0 | 1 | — | [[Methylthiouracil (drug)]] 5 µM 0.190× (z -9.3) |
| [[A-172 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 85.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 88.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 68.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 70.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 49.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 94.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 104 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 83.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 91.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 72.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 96.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 62.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 88.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8936), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 22 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NACA]] ⚠ | +0.81 | +0.72 / +0.80 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL37]] ⚠ | +0.79 | +0.69 / +0.80 | both halves | 7e-06 | STRING 896; ⚠ in the vector space only through flagged drug-doses |
| [[RPL34]] | +0.78 | +0.61 / +0.84 | both halves | 7e-06 | STRING 986 |
| [[RPL30]] ⚠ | +0.78 | +0.69 / +0.78 | both halves | 7e-06 | STRING 996; ⚠ in the vector space only through flagged drug-doses |
| [[SNHG6]] | +0.77 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[RPS6]] ⚠ | +0.76 | +0.67 / +0.78 | both halves | 7e-06 | STRING 991; ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | +0.74 | +0.59 / +0.80 | both halves | 7e-06 | STRING 985 |
| [[RPL5]] | +0.74 | +0.62 / +0.78 | both halves | 7e-06 | STRING 991 |
| [[RPS27]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[RPL21]] ⚠ | +0.74 | +0.59 / +0.76 | both halves | 7e-06 | STRING 991; ⚠ in the vector space only through flagged drug-doses |
| [[EPB41L4A-AS1]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[RPL19]] | +0.73 | +0.59 / +0.77 | both halves | 7e-06 | STRING 989 |
| [[RPS8]] | +0.73 | +0.61 / +0.76 | both halves | 7e-06 | STRING 448 |
| [[RPL17]] | +0.73 | +0.58 / +0.76 | both halves | 7e-06 | STRING 971 |
| [[RPL31]] | +0.73 | +0.56 / +0.78 | both halves | 1e-05 | STRING 996 |
| [[PFDN5]] | +0.73 | +0.52 / +0.79 | both halves | 1e-05 |  |
| [[RPL26]] | +0.72 | +0.59 / +0.77 | both halves | 7e-06 | STRING 912 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP188]] | -0.67 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[SIGMAR1]] | -0.66 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[PYGO2]] | -0.65 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[PTBP1]] | -0.63 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[AKIRIN1]] | -0.62 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[TUBG1]] | -0.61 | -0.61 / -0.69 | both halves | 7e-06 |  |
| [[PSME3]] | -0.61 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[HASPIN]] | -0.59 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[GPAA1]] | -0.59 | -0.50 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.768). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-44.2, -28.2); signed map (-59.1, -5.1). **Vector** length 63.0, 24.0% of its response variance represented; |z| ≥ 3 in 504 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.65 to 55); *Peptide chain elongation* (reactome, mean cos +0.65 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.65 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +3.6 | +3.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.8 | +1.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.7 | +0.6 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.7 | -0.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | -3.7 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -3.4 | +7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -2.9 | +5.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | -2.3 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | +0.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | +0.4 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.4 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.2 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | NSA2 ribosome biogenesis factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:74,766,991-74,780,113 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HUSSY-29, HCLG1, FLJ94393, TINP1 |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Matched by | ensembl_id |

**Function**, from UniProt [O95478](https://www.uniprot.org/uniprotkb/O95478) (Ribosome biogenesis protein NSA2 homolog):

> Involved in the biogenesis of the 60S ribosomal subunit. May play a part in the quality control of pre-60S particles (By similarity).

**Summary**, from NCBI Gene [10412](https://www.ncbi.nlm.nih.gov/gene/10412):

> This gene encodes a nucleolar protein involved in cell cycle regulation and proliferation. This gene was identified based on sequence similarity to a highly conserved Saccharomyces cerevisiae gene encoding a pre-ribosomal protein, which is involved in large ribosomal subunit biogenesis. The encoded protein is found at elevated levels in diabetic nephropathy. Alternative splicing results in multiple transcript variants. Several related pseudogenes have been identified. [provided by RefSeq, Nov …

**Accessions** — [HGNC:30728](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30728) · Entrez [10412](https://www.ncbi.nlm.nih.gov/gene/10412) · UniProt [O95478](https://www.uniprot.org/uniprotkb/O95478) · Ensembl [ENSG00000164346](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164346)

## Data

Gene col 8936: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8936); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8936, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8936]; `tensor/DDL_lfc|DDL_z.npy` [8936]; `embed/gene_vectors.npy` [8936]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8936 or target_col == 8936). Every well: [[NSA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

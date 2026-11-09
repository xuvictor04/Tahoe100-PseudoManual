---
symbol: "SF3B2"
type: "gene"
col: 1503
ensembl_id: "ENSG00000087365"
name: "splicing factor 3b subunit 2"
location: "11q13.1"
module: 41
arm: "+"
pooled_cpm: 225.03
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# SF3B2

*splicing factor 3b subunit 2* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.81× (z +6.3, q 9e-08, up in 40 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.33× (z +4.9, q 1e-04, up in 45 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF20]] (+0.70, fdr 1e-05), [[PPIL4]] (+0.70, fdr 1e-05), [[SUPT5H]] (+0.69, fdr 7e-06); moves opposite to [[ZNF124]] (-0.54, fdr 1e-04), [[VMA21]] (-0.54, fdr 1e-05), [[REEP3]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1503.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.81×** | +6.3 | 9e-08 | 40/44 (NCI-H1573, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.31×** | +6.3 | 9e-08 | 47/49 (NCI-H460, LoVo, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.75×** | +5.7 | 2e-06 | 42/45 (SW480, A-172, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.33×** | +4.9 | 1e-04 | 45/49 (PANC-1, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.43×** | +3.9 | 0.009 | 37/48 (PANC-1, A-172, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.83×** | +3.5 | 0.044 | 30/48 (BT-474, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.044 | 38/48 (PANC-1, A549, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~77% of this change | **1.35×** | +3.4 | 0.056 | 33/48 (SHP-77, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | 1.33× | +3.1 | 0.10 | 33/48 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.32× | +3.1 | 0.10 | 30/48 (LOX-IMVI, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1503. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 232 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +15.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.95× (z +10.0) | — |
| [[A-172 (line)]] | wt | 194 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A549 (line)]] | wt | 217 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +13.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 212 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 184 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 204 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.58× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[A-427 (line)]] | wt | 251 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 273 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 226 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 221 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 199 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 207 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 187 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 162 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 299 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 273 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 238 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 366 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 256 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 175 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 191 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 185 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 144 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 321 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 239 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 191 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 205 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 301 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 253 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1503), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF20]] | +0.70 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[PPIL4]] | +0.70 | +0.80 / +0.56 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 481 |
| [[SUPT5H]] | +0.69 | +0.73 / +0.58 | both halves | 7e-06 | STRING 454 |
| [[SRRM1]] | +0.64 | +0.67 / +0.59 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions; STRING 917 |
| [[VIRMA]] | +0.63 | +0.74 / +0.45 | both halves | 3e-05 | same gene group |
| [[ACBD3]] | +0.62 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[PRPF6]] | +0.61 | +0.68 / +0.41 | both halves | 4e-05 | pathway: Dengue Virus-Host Interactions; STRING 999 |
| [[TMF1]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[IK]] | +0.59 | +0.72 / +0.36 | both halves | 1e-04 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 924 |
| [[CFAP36]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[GOLGA4]] | +0.57 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[THAP8]] | +0.57 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF124]] | -0.54 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[VMA21]] | -0.54 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[REEP3]] | -0.53 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[TOR1A]] | -0.50 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[SLC25A13]] | -0.49 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[B3GLCT]] | -0.49 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[ARSB]] | -0.49 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[ATE1]] | -0.48 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[E2F3]] | -0.48 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[TTL]] | -0.48 | -0.58 / -0.37 | both halves | 9e-05 |  |
| [[GNG12]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.598). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-3.3, -49.5); signed map (-14.2, -10.1). **Vector** length 79.4, 35.3% of its response variance represented; |z| ≥ 3 in 571 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +0.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | -1.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +0.4 |
|  | [[Ciclopirox (drug)]] 5 µM |  | +1.8 | +0.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -0.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.1 | +1.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~99% of this change | -3.6 | +2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -1.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.0 | -0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | +0.8 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.7 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | splicing factor 3b subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:66,050,729-66,069,308 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SAP145, SF3b1, Cus1, SF3b145 |
| Gene groups (HGNC) | Armadillo like helical domain containing; SF3b complex |
| Reactome | 14 pathways, smallest: mRNA Splicing - Minor Pathway; CHD1 and CHD2 subfamily; CHD chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13435](https://www.uniprot.org/uniprotkb/Q13435) (Splicing factor 3B subunit 2):

> Component of the 17S U2 SnRNP complex of the spliceosome, a large ribonucleoprotein complex that removes introns from transcribed pre-mRNAs. The 17S U2 SnRNP complex (1) directly participates in early spliceosome assembly and (2) mediates recognition of the intron branch site during pre-mRNA splicing by promoting the selection of the pre-mRNA branch-site adenosine, the nucleophile for the first step of splicing. Within the 17S U2 SnRNP complex, SF3B2 is part of the SF3B subcomplex, which is …

**Summary**, from NCBI Gene [10992](https://www.ncbi.nlm.nih.gov/gene/10992):

> This gene encodes subunit 2 of the splicing factor 3b protein complex. Splicing factor 3b, together with splicing factor 3a and a 12S RNA unit, forms the U2 small nuclear ribonucleoproteins complex (U2 snRNP). The splicing factor 3b/3a complex binds pre-mRNA upstream of the intron's branch site in a sequence-independent manner and may anchor the U2 snRNP to the pre-mRNA. Splicing factor 3b is also a component of the minor U12-type spliceosome. Subunit 2 associates with pre-mRNA upstream of the …

**Accessions** — [HGNC:10769](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10769) · Entrez [10992](https://www.ncbi.nlm.nih.gov/gene/10992) · UniProt [Q13435](https://www.uniprot.org/uniprotkb/Q13435) · Ensembl [ENSG00000087365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087365)

## Data

Gene col 1503: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1503); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1503, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1503]; `tensor/DDL_lfc|DDL_z.npy` [1503]; `embed/gene_vectors.npy` [1503]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1503 or target_col == 1503). Every well: [[SF3B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SF3B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "SF3B5"
type: "gene"
col: 9886
ensembl_id: "ENSG00000169976"
name: "splicing factor 3b subunit 5"
location: "6q24.2"
module: 54
arm: "+"
pooled_cpm: 15.07
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/054", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# SF3B5

*splicing factor 3b subunit 5* — 6q24.2

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.73× (z +6.9, q 2e-09, up in 40 of 41 measured lines) ⚠ toxic. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL41]] (+0.81, fdr 8e-06, ⚠ MRPL41 in the vector space only through flagged drug-doses), [[RPL36AL]] (+0.80, fdr 1e-05, ⚠ RPL36AL in the vector space only through flagged drug-doses), [[EMC6]] (+0.79, fdr 2e-05), [[POP7]] (+0.78, fdr 3e-05), [[LAGE3]] (+0.76, fdr 1e-05); moves opposite to [[HNRNPA2B1]] (-0.63, fdr 4e-05), [[EWSR1]] (-0.63, fdr 3e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9886.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.73×** | +6.9 | 2e-09 | 40/41 (PANC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.23×** | +5.8 | 1e-06 | 40/48 (PANC-1, HT-29, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **2.19×** | +5.7 | 2e-06 | 41/47 (J82, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **2.17×** | +5.6 | 2e-06 | 34/43 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | **2.10×** | +5.1 | 4e-05 | 32/40 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.62×** | +5.0 | 6e-05 | 28/46 (NCI-H1792, A549, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.91×** | +4.7 | 2e-04 | 38/48 (J82, AsPC-1, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.65×** | +3.4 | 0.042 | 16/27 (Hs 766T, SW 900, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Arbutin (drug)]] 5 µM |  | 1.57× | +3.1 | 0.11 | 20/46 (SW480, A498, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.52× | +3.0 | 0.12 | 20/46 (J82, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.55× | +3.0 | 0.12 | 21/46 (SK-MEL-2, A-172, …) | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9886. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 18.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9886), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 18 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL41]] ⚠ | +0.81 | +0.58 / +0.86 | both halves | 8e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36AL]] ⚠ | +0.80 | +0.54 / +0.86 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EMC6]] | +0.79 | +0.48 / +0.86 | both halves | 2e-05 |  |
| [[POP7]] | +0.78 | +0.45 / +0.84 | both halves | 3e-05 |  |
| [[LAGE3]] | +0.76 | +0.56 / +0.78 | both halves | 1e-05 |  |
| [[C1orf122]] | +0.75 | +0.67 / +0.80 | both halves | 7e-06 |  |
| [[ROMO1]] | +0.75 | +0.56 / +0.78 | both halves | 1e-05 |  |
| [[C19orf53]] | +0.75 | +0.55 / +0.77 | both halves | 1e-05 |  |
| [[COMMD6]] | +0.74 | +0.47 / +0.77 | both halves | 2e-05 |  |
| [[MICOS13]] | +0.74 | +0.47 / +0.77 | both halves | 2e-05 |  |
| [[UQCR11]] | +0.74 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[NCBP2AS2]] | +0.74 | +0.52 / +0.78 | both halves | 1e-05 |  |
| [[DDT]] | +0.73 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[CHCHD1]] | +0.73 | +0.45 / +0.78 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPA2B1]] | -0.63 | -0.41 / -0.58 | both halves | 4e-05 | pathway: Dengue Virus-Host Interactions; STRING 538 |
| [[EWSR1]] | -0.63 | -0.27 / -0.67 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SF3B5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.791). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-44.5, -19.8); signed map (-32.6, 8.9). **Vector** length 57.0, 13.1% of its response variance represented; |z| ≥ 3 in 523 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial ribosome-associated quality control* (reactome, mean cos +0.61 to 9); *Mitochondrial translation* (reactome, mean cos +0.61 to 9); *Mitochondrial translation elongation* (reactome, mean cos +0.61 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +1.7 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.6 | +6.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +1.6 | +5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.1 | +3.1 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | +1.0 | +1.2 |
|  | [[Resveratrol (drug)]] 5 µM |  | +0.8 | +0.4 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM |  | +0.8 | +0.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -5.9 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.7 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | -5.6 | +5.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | +1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | -1.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | splicing factor 3b subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q24.2 — chr6:144,094,884-144,095,573 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SF3b10, MGC3133, Ysf3 |
| Gene groups (HGNC) | SF3b complex |
| Reactome | 14 pathways, smallest: mRNA Splicing - Minor Pathway; CHD1 and CHD2 subfamily; CHD chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWJ5](https://www.uniprot.org/uniprotkb/Q9BWJ5) (Splicing factor 3B subunit 5):

> Component of the 17S U2 SnRNP complex of the spliceosome, a large ribonucleoprotein complex that removes introns from transcribed pre-mRNAs. The 17S U2 SnRNP complex (1) directly participates in early spliceosome assembly and (2) mediates recognition of the intron branch site during pre-mRNA splicing by promoting the selection of the pre-mRNA branch-site adenosine, the nucleophile for the first step of splicing. Within the 17S U2 SnRNP complex, SF3B4 is part of the SF3B subcomplex, which is …

**Summary**, from NCBI Gene [83443](https://www.ncbi.nlm.nih.gov/gene/83443):

> Enables RNA binding activity and splicing factor binding activity. Involved in mRNA splicing, via spliceosome. Located in nucleoplasm. Part of U12-type spliceosomal complex and U2-type precatalytic spliceosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21083](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21083) · Entrez [83443](https://www.ncbi.nlm.nih.gov/gene/83443) · UniProt [Q9BWJ5](https://www.uniprot.org/uniprotkb/Q9BWJ5) · Ensembl [ENSG00000169976](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169976)

## Data

Gene col 9886: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9886); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9886, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9886]; `tensor/DDL_lfc|DDL_z.npy` [9886]; `embed/gene_vectors.npy` [9886]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9886 or target_col == 9886). Every well: [[SF3B5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SF3B5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

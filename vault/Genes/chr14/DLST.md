---
symbol: "DLST"
type: "gene"
col: 4101
ensembl_id: "ENSG00000119689"
name: "dihydrolipoamide S-succinyltransferase"
location: "14q24.3"
module: 25
arm: "+"
pooled_cpm: 39.85
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# DLST

*dihydrolipoamide S-succinyltransferase* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.52× (z +5.1, q 2e-04, up in 36 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.221×, Panc 03.27 0.312×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.276×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCTN1]] (+0.67, fdr 7e-06), [[VAMP3]] (+0.66, fdr 7e-06), [[CAPN1]] (+0.65, fdr 9e-06); moves opposite to [[SUMO4]] (-0.62, fdr 3e-05), [[ANKHD1]] (-0.62, fdr 1e-05), [[ZNF503]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4101.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.52×** | +5.1 | 2e-04 | 36/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +4.4 | 0.003 | 27/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.022 | 28/48 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +3.7 | 0.029 | 21/48 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4101.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 0.221×, Panc 03.27 0.312×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.276×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.749× | -3.4 | 0.29 | 19/39 (NCI-H1573, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.829× | -3.3 | 0.29 | 22/48 (C-33 A, SW480, …) | rises with dose | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.837× | -3.1 | 0.29 | 19/48 (NCI-H1792, NCI-H460, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.838× | -3.1 | 0.29 | 21/48 (BT-474, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4101. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 30.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 31.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -11.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 51.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 26.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +10.1) | — |
| [[A-427 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 42.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4101), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN1]] | +0.67 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[VAMP3]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[CAPN1]] | +0.65 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[ZDHHC6]] | +0.63 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[NRBP2]] | +0.63 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[ABHD17A]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[EIF4H]] | +0.62 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[EIF2B1]] | +0.62 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[MMGT1]] | +0.61 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[INTS11]] | +0.61 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[C1orf198]] | +0.61 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[TAF6]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUMO4]] | -0.62 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[ANKHD1]] | -0.62 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[ZNF503]] | -0.59 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[FOXA2]] | -0.57 | -0.39 / -0.64 | both halves | 5e-05 |  |
| [[ASH1L]] | -0.56 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.55 | -0.46 / -0.55 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL33]] | -0.54 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[ANKRD12]] | -0.54 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[SELENOH]] | -0.53 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[SPATC1]] | -0.53 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[KLHL4]] | -0.52 | -0.55 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers DLST's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.604). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.1, -26.2); signed map (-34.9, -31.4). **Vector** length 72.3, 16.0% of its response variance represented; |z| ≥ 3 in 628 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.1 | -0.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | +0.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.6 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.8 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | -0.3 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.5 | +1.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +0.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +2.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.5 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -1.4 | -3.3 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | dihydrolipoamide S-succinyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:74,881,891-74,903,743 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OGDC-E2, KGD2; previously DLTS |
| Gene groups (HGNC) | Oxoglutarate dehydrogenase complex subunits; Oxoadipate dehydrogenase complex subunits; Acyltransferases |
| Hallmark sets | FATTY_ACID_METABOLISM, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: OADH complex synthesizes glutaryl-CoA from 2-OA; OGDH complex synthesizes succinyl-CoA from 2-OG; Glycine degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [P36957](https://www.uniprot.org/uniprotkb/P36957) (Dihydrolipoyllysine-residue succinyltransferase component of 2-oxoglutarate dehydrogenase complex, mitochondrial):

> Dihydrolipoamide succinyltransferase (E2) component of the 2-oxoglutarate dehydrogenase complex. The 2-oxoglutarate dehydrogenase complex catalyzes the overall conversion of 2-oxoglutarate to succinyl-CoA and CO(2). The 2-oxoglutarate dehydrogenase complex is mainly active in the mitochondrion. A fraction of the 2-oxoglutarate dehydrogenase complex also localizes in the nucleus and is required for lysine succinylation of histones: associates with KAT2A on chromatin and provides succinyl-CoA to …

**Summary**, from NCBI Gene [1743](https://www.ncbi.nlm.nih.gov/gene/1743):

> This gene encodes a mitochondrial protein that belongs to the 2-oxoacid dehydrogenase family. This protein is one of the three components (the E2 component) of the 2-oxoglutarate dehydrogenase complex that catalyzes the overall conversion of 2-oxoglutarate to succinyl-CoA and CO(2). Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:2911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2911) · Entrez [1743](https://www.ncbi.nlm.nih.gov/gene/1743) · UniProt [P36957](https://www.uniprot.org/uniprotkb/P36957) · Ensembl [ENSG00000119689](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119689)

## Data

Gene col 4101: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4101); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4101, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4101]; `tensor/DDL_lfc|DDL_z.npy` [4101]; `embed/gene_vectors.npy` [4101]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4101 or target_col == 4101). Every well: [[DLST — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLST.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "FIS1"
type: "gene"
col: 13189
ensembl_id: "ENSG00000214253"
name: "fission, mitochondrial 1"
location: "7q22.1"
module: 24
arm: "+"
pooled_cpm: 18.47
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# FIS1

*fission, mitochondrial 1* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.69× (z +10.6, q 2e-23, up in 37 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.47× (z +4.1, q 0.003, up in 24 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 4.25×, SW480 3.32×, C32 3.66×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 4.01×, LoVo 3.41×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.172×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (J82 0.357×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COQ4]] (+0.62, fdr 2e-05), [[ALYREF]] (+0.58, fdr 1e-05), [[ZNF707]] (+0.56, fdr 2e-05); moves opposite to [[AKAP11]] (-0.48, fdr 2e-05), [[PDAP1]] (-0.48, fdr 4e-05), [[THNSL1]] (-0.48, fdr 8e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13189.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 4.25×, SW480 3.32×, C32 3.66×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 4.01×, LoVo 3.41×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.69×** | +10.6 | 2e-23 | 37/39 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +7.9 | 9e-13 | 26/30 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +7.3 | 5e-11 | 30/34 (LOX-IMVI, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +6.6 | 7e-09 | 36/43 (CFPAC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.63×** | +5.2 | 2e-05 | 34/46 (KATO III, NCI-H460, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.51×** | +4.4 | 9e-04 | 23/43 (HS-578T, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.003 | 24/48 (SW480, LoVo, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +3.5 | 0.029 | 20/45 (HCT15, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.35×** | +3.2 | 0.076 | 20/48 (KATO III, NCI-H460, …) | rises with dose | composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.49× | +3.0 | 0.13 | 11/45 (A549, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.48× | +3.0 | 0.13 | 16/46 (NCI-H1573, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.172×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (J82 0.357×; ⚠ cell-cycle shift, explains ~0% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13189. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 21.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 17.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 32.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +9.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.357× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 20.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 13.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13189), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 7 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COQ4]] | +0.62 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[ALYREF]] | +0.58 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ZNF707]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[RENO1]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SEM1]] | +0.55 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[COX16]] | +0.54 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[HINFP]] | +0.54 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[ZNF358]] | +0.53 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[MZT2B]] | +0.53 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[NDUFB11]] ⚠ | +0.53 | +0.45 / +0.56 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BRI3]] | +0.53 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[NDUFA13]] ⚠ | +0.53 | +0.44 / +0.51 | both halves | 3e-05 | STRING 401; ⚠ in the vector space only through flagged drug-doses |
| [[IP6K1]] | +0.53 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[SNHG19]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP11]] | -0.48 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[PDAP1]] | -0.48 | -0.43 / -0.48 | both halves | 4e-05 |  |
| [[THNSL1]] | -0.48 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[CCT5]] | -0.46 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[HASPIN]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[IPO7]] | -0.45 | -0.36 / -0.49 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.456). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.4, -35.7); signed map (-45.0, -25.5). **Vector** length 50.4, 8.06% of its response variance represented; |z| ≥ 3 in 593 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +6.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.5 | +3.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | +2.1 | +5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.0 | +1.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +1.7 | +3.2 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.5 | +1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +4.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.9 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.4 | +0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -0.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | +0.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.1 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | fission, mitochondrial 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:101,239,458-101,252,316 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-135, H_NH0132A01.6; previously TTC11 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing |
| Hallmark sets | PEROXISOME |
| Reactome | 2 pathways, smallest: Class I peroxisomal membrane protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3D6](https://www.uniprot.org/uniprotkb/Q9Y3D6) (Mitochondrial fission 1 protein):

> Involved in the fragmentation of the mitochondrial network and its perinuclear clustering. Plays a minor role in the recruitment and association of the fission mediator dynamin-related protein 1 (DNM1L) to the mitochondrial surface and mitochondrial fission. May not be essential for the assembly of functional fission complexes and the subsequent membrane scission event. Also mediates peroxisomal fission. May act when the products of fission are directed toward mitochondrial homeostasis, …

**Summary**, from NCBI Gene [51024](https://www.ncbi.nlm.nih.gov/gene/51024):

> Enables identical protein binding activity; lipid binding activity; and molecular adaptor activity. Involved in several processes, including negative regulation of ATP metabolic process; obsolete protein targeting to mitochondrion; and organelle fission. Acts upstream of or within mitochondrion organization. Located in mitochondrial outer membrane and peroxisomal membrane. Part of protein-containing complex. Biomarker of Alzheimer's disease. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21689](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21689) · Entrez [51024](https://www.ncbi.nlm.nih.gov/gene/51024) · UniProt [Q9Y3D6](https://www.uniprot.org/uniprotkb/Q9Y3D6) · Ensembl [ENSG00000214253](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214253)

## Data

Gene col 13189: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13189); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13189, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13189]; `tensor/DDL_lfc|DDL_z.npy` [13189]; `embed/gene_vectors.npy` [13189]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13189 or target_col == 13189). Every well: [[FIS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FIS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

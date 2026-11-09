---
symbol: "TOMM22"
type: "gene"
col: 1892
ensembl_id: "ENSG00000100216"
name: "translocase of outer mitochondrial membrane 22"
location: "22q13.1"
module: 54
arm: "+"
pooled_cpm: 24.22
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# TOMM22

*translocase of outer mitochondrial membrane 22* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.16× (z +9.1, q 6e-17, up in 42 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.65× (z +4.0, q 0.008, up in 26 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.694× (z -4.2, q 0.017, down in 31 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.212×, RKO 0.372×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMM13]] (+0.69, fdr 1e-05), [[INVS]] (+0.69, fdr 1e-05), [[AURKAIP1]] (+0.66, fdr 1e-05); moves opposite to [[CDC42BPG]] (-0.49, fdr 5e-05).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1892.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **3.16×** | +9.1 | 6e-17 | 42/44 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.65×** | +7.1 | 3e-10 | 27/34 (A498, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.10×** | +5.5 | 8e-06 | 30/39 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.83×** | +4.8 | 2e-04 | 36/46 (NCI-H2347, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.65×** | +4.0 | 0.008 | 26/47 (SK-MEL-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +3.6 | 0.028 | 24/47 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +3.6 | 0.028 | 28/48 (HOP62, CFPAC-1, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.57×** | +3.3 | 0.068 | 27/46 (C32, LOX-IMVI, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.34×** | +3.3 | 0.068 | 25/48 (HS-578T, A-427, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.56×** | +3.2 | 0.068 | 26/46 (KATO III, BT-474, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | **1.50×** | +3.2 | 0.068 | 27/46 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.31× | +3.1 | 0.10 | 20/48 (A-427, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1892.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SNU-1 0.212×, RKO 0.372×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.694×** | -4.2 | 0.017 | 31/47 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1892. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 28.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H460 (line)]] | wt | 13.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.57× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[PANC-1 (line)]] | alt | 32.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[RKO (line)]] | wt | 41.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -8.6) |
| [[SNU-1 (line)]] | wt | 34.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -10.5) |
| [[SW480 (line)]] | alt | 28.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.68× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1892), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM13]] | +0.69 | +0.50 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 861 |
| [[INVS]] | +0.69 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[AURKAIP1]] | +0.66 | +0.53 / +0.66 | both halves | 1e-05 | STRING 615 |
| [[TIMM10]] | +0.65 | +0.47 / +0.70 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 869 |
| [[MRPL12]] | +0.65 | +0.53 / +0.69 | both halves | 1e-05 | STRING 648 |
| [[MRPS12]] | +0.65 | +0.48 / +0.65 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[LARS2]] | +0.64 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[CDC123]] | +0.62 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[TMEM147]] | +0.61 | +0.45 / +0.64 | both halves | 3e-05 | pathway: Protein localization |
| [[MRPL36]] | +0.61 | +0.35 / +0.67 | both halves | 1e-04 |  |
| [[GEMIN6]] | +0.60 | +0.39 / +0.59 | both halves | 6e-05 |  |
| [[TYW1]] | +0.60 | +0.49 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC42BPG]] | -0.49 | -0.41 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.481). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-45.2, -11.6); signed map (-37.1, -26.6). **Vector** length 44.0, 9.29% of its response variance represented; |z| ≥ 3 in 524 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.6 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.2 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | +0.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -2.2 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -1.4 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | +0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -2.8 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.8 | -2.4 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.7 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.7 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -0.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | translocase of outer mitochondrial membrane 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,681,957-38,685,421 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TOM22 |
| Gene groups (HGNC) | Translocase of outer mitochondrial membrane complex |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 7 pathways, smallest: PINK1-PRKN Mediated Mitophagy; Mitophagy; Mitochondrial protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS69](https://www.uniprot.org/uniprotkb/Q9NS69) (Mitochondrial import receptor subunit TOM22 homolog):

> Central receptor component of the translocase of the outer membrane of mitochondria (TOM) complex essential for the recognition and translocation of cytosolically synthesized mitochondrial preproteins. Together with the peripheral receptor TOMM20, functions as the transit peptide receptor and facilitates the movement of preproteins into the translocation pore. The TOM complex associates with the ion channel VDAC2 and PINK1 kinase at depolarized mitochondria, this interaction stabilizes PINK1 at …

**Summary**, from NCBI Gene [56993](https://www.ncbi.nlm.nih.gov/gene/56993):

> The protein encoded by this gene is an integral membrane protein of the mitochondrial outer membrane. The encoded protein interacts with TOMM20 and TOMM40, and forms a complex with several other proteins to import cytosolic preproteins into the mitochondrion. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18002](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18002) · Entrez [56993](https://www.ncbi.nlm.nih.gov/gene/56993) · UniProt [Q9NS69](https://www.uniprot.org/uniprotkb/Q9NS69) · Ensembl [ENSG00000100216](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100216)

## Data

Gene col 1892: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1892); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1892, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1892]; `tensor/DDL_lfc|DDL_z.npy` [1892]; `embed/gene_vectors.npy` [1892]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1892 or target_col == 1892). Every well: [[TOMM22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOMM22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

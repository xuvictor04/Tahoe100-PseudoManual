---
symbol: "TIMM13"
type: "gene"
col: 1812
ensembl_id: "ENSG00000099800"
name: "translocase of inner mitochondrial membrane 13"
location: "19p13.3"
module: 54
arm: "+"
pooled_cpm: 11.42
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# TIMM13

*translocase of inner mitochondrial membrane 13* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.81× (z +7.9, q 2e-12, up in 34 of 35 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.67× (z +3.2, q 0.089, up in 21 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.252×).
> Its strongest partners by |cos| (77 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 31 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL12]] (+0.74, fdr 1e-05), [[TOMM22]] (+0.69, fdr 1e-05), [[GADD45GIP1]] (+0.69, fdr 7e-05); moves opposite to [[TLN1]] (-0.56, fdr 7e-05), [[PRKAR1A]] (-0.56, fdr 2e-04), [[STYX]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1812.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.81×** | +7.9 | 2e-12 | 34/35 (SW480, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **2.47×** | +5.5 | 1e-05 | 16/21 (SW480, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.34×** | +4.9 | 1e-04 | 23/28 (A-172, HOP62, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.26×** | +4.9 | 1e-04 | 29/37 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **2.08×** | +4.6 | 5e-04 | 26/41 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.82×** | +3.6 | 0.028 | 25/41 (A-172, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.73×** | +3.2 | 0.089 | 23/46 (A-172, LS 180, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +3.2 | 0.089 | 21/46 (MIA PaCa-2, Panc 03.27, …) | top dose only | position effect removed |
| [[Sulfatinib (drug)]] 5 µM |  | 1.66× | +3.1 | 0.14 | 21/46 (AsPC-1, A-172, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1812.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.252×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.337× | -3.5 | 0.23 | 30/46 (SNU-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.698× | -3.2 | 0.35 | 24/45 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.591× | -3.1 | 0.39 | 20/47 (A-172, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, +0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1812. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 22.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -9.1) |
| [[A-172 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1812), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 29 of them with an alert (⚠; 21 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL12]] | +0.74 | +0.54 / +0.81 | both halves | 1e-05 |  |
| [[TOMM22]] | +0.69 | +0.50 / +0.69 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 861 |
| [[GADD45GIP1]] | +0.69 | +0.38 / +0.74 | both halves | 7e-05 |  |
| [[MRPS12]] | +0.67 | +0.51 / +0.70 | both halves | 1e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[MICOS13]] | +0.65 | +0.24 / +0.80 | both halves | 4e-04 |  |
| [[TIMM10]] | +0.64 | +0.40 / +0.75 | both halves | 5e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[MRPS26]] | +0.63 | +0.46 / +0.68 | both halves | 3e-05 |  |
| [[CHCHD1]] | +0.63 | +0.25 / +0.70 | both halves | 4e-04 |  |
| [[ZNF593]] | +0.63 | +0.32 / +0.72 | both halves | 2e-04 |  |
| [[MRPL36]] | +0.63 | +0.21 / +0.73 | both halves | 6e-04 |  |
| [[MRPL46]] | +0.63 | +0.22 / +0.69 | both halves | 6e-04 |  |
| [[POP7]] | +0.62 | +0.31 / +0.64 | both halves | 2e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLN1]] | -0.56 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[PRKAR1A]] | -0.56 | -0.29 / -0.57 | both halves | 2e-04 |  |
| [[STYX]] | -0.53 | -0.32 / -0.56 | both halves | 2e-04 |  |
| [[ARF1]] | -0.52 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[CDC42]] | -0.50 | -0.17 / -0.59 | ⚠ one half (not replicated) | 0.001 |  |
| [[BAG6]] | -0.50 | -0.20 / -0.54 | both halves | 7e-04 | pathway: Protein localization |
| [[HAPSTR1]] | -0.50 | -0.17 / -0.59 | ⚠ one half (not replicated) | 0.001 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-44.9, -11.6); signed map (-37.4, -26.4). **Vector** length 46.4, 9.01% of its response variance represented; |z| ≥ 3 in 527 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial ribosome-associated quality control* (reactome, mean cos +0.59 to 9); *Mitochondrial translation* (reactome, mean cos +0.59 to 9); *Mitochondrial translation elongation* (reactome, mean cos +0.61 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +1.7 | +3.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.3 | +1.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +1.8 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.0 | +1.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | -3.5 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -2.7 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | -2.7 | +4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.3 | -3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -3.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -3.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.7 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | translocase of inner mitochondrial membrane 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:2,425,625-2,427,586 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Tim13; previously TIMM13B |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5L4](https://www.uniprot.org/uniprotkb/Q9Y5L4) (Mitochondrial import inner membrane translocase subunit Tim13):

> Mitochondrial intermembrane chaperone that participates in the import and insertion of some multi-pass transmembrane proteins into the mitochondrial inner membrane. Also required for the transfer of beta-barrel precursors from the TOM complex to the sorting and assembly machinery (SAM complex) of the outer membrane. Acts as a chaperone-like protein that protects the hydrophobic precursors from aggregation and guide them through the mitochondrial intermembrane space. The TIMM8-TIMM13 complex …

**Summary**, from NCBI Gene [26517](https://www.ncbi.nlm.nih.gov/gene/26517):

> This gene encodes a member of the evolutionarily conserved TIMM (translocase of inner mitochondrial membrane) family of proteins that function as chaperones in the import of proteins from the cytoplasm into the mitochondrial inner membrane. Proteins of this family play a role in collecting substrate proteins from the translocase of the outer mitochondrial membrane (TOM) complex and delivering them to either the sorting and assembly machinery in the outer mitochondrial membrane (SAM) complex or …

**Accessions** — [HGNC:11816](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11816) · Entrez [26517](https://www.ncbi.nlm.nih.gov/gene/26517) · UniProt [Q9Y5L4](https://www.uniprot.org/uniprotkb/Q9Y5L4) · Ensembl [ENSG00000099800](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099800)

## Data

Gene col 1812: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1812); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1812, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1812]; `tensor/DDL_lfc|DDL_z.npy` [1812]; `embed/gene_vectors.npy` [1812]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1812 or target_col == 1812). Every well: [[TIMM13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMM13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

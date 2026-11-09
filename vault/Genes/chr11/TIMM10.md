---
symbol: "TIMM10"
type: "gene"
col: 5607
ensembl_id: "ENSG00000134809"
name: "translocase of inner mitochondrial membrane 10"
location: "11q12.1"
module: 54
arm: "+"
pooled_cpm: 5.31
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/054"]
generated_by: "tahoemap"
---

# TIMM10

*translocase of inner mitochondrial membrane 10* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.60× (z +10.0, q 1e-20, up in 23 of 25 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +4.2, q 0.003, up in 21 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 7.56×, PANC-1 5.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 7.72×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EIF5AL1]] (+0.67, fdr 1e-05), [[NR2C2AP]] (+0.66, fdr 1e-05), [[EXOSC4]] (+0.66, fdr 3e-05); moves opposite to [[DYNC1LI2]] (-0.50, fdr 3e-05), [[RCAN3]] (-0.50, fdr 3e-05), [[HDLBP]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 054]] (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5607.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H460 7.56×, PANC-1 5.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 7.72×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **4.60×** | +10.0 | 1e-20 | 23/25 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **4.04×** | +8.8 | 5e-16 | 7/7 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.26×** | +6.9 | 1e-09 | 8/10 (SW480, A498, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **2.59×** | +6.2 | 7e-08 | 21/26 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.38×** | +5.7 | 2e-06 | 29/39 (PANC-1, NCI-H1573, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.2 | 0.003 | 21/40 (CFPAC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.83×** | +3.8 | 0.013 | 16/31 (HCT15, NCI-H2030, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.6 | 0.021 | 12/24 (J82, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.068 | 14/47 (NCI-H2347, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.61× | +3.1 | 0.10 | 11/46 (NCI-H2030, NCI-H1573, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.40× | +3.1 | 0.10 | 13/45 (HT-29, NCI-H460, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.63× | +3.1 | 0.10 | 14/43 (NCI-H1573, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5607.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.706× | -3.3 | 0.62 | 19/38 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.631× | -3.1 | 0.64 | 8/47 (A498, NCI-H1792, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5607. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.76 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.56× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[PANC-1 (line)]] | alt | 12.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5607), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 23 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF5AL1]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[NR2C2AP]] | +0.66 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[EXOSC4]] | +0.66 | +0.44 / +0.71 | both halves | 3e-05 |  |
| [[TOMM22]] | +0.65 | +0.47 / +0.70 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 869 |
| [[MRPS12]] | +0.65 | +0.28 / +0.76 | both halves | 3e-04 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[TIMM13]] | +0.64 | +0.40 / +0.75 | both halves | 5e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[HMGB1P5]] ⚠ | +0.63 | +0.51 / +0.66 | both halves | 1e-05 | **novel candidate**; ⚠ in the vector space only through flagged drug-doses |
| [[EMC6]] | +0.63 | +0.37 / +0.69 | both halves | 7e-05 | pathway: Protein localization; STRING 418 |
| [[MICOS13]] | +0.62 | +0.45 / +0.74 | both halves | 3e-05 | STRING 424 |
| [[OXLD1]] | +0.61 | +0.25 / +0.69 | both halves | 4e-04 |  |
| [[ZNF232-AS1]] | +0.59 | +0.23 / +0.64 | both halves | 5e-04 |  |
| [[APRT]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[LBHD1]] | +0.59 | +0.20 / +0.75 | both halves | 7e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC1LI2]] | -0.50 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[RCAN3]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[HDLBP]] | -0.45 | -0.32 / -0.47 | both halves | 1e-04 |  |
| [[SPDYA]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 054]] — Mitochondrial ribosome-associated quality control; 88 genes; this gene is in the **+** arm (projection on the module's main direction 0.458). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-45.0, -11.4); signed map (-37.2, -26.5). **Vector** length 43.5, 6.12% of its response variance represented; |z| ≥ 3 in 662 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +3.3 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.2 | +1.6 |
| fall | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | translocase of inner mitochondrial membrane 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:57,528,464-57,530,803 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIM10, TIM10A, TIMM10A |
| Gene groups (HGNC) | TIM22 complex |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Mitochondrial protein import; Mitochondrial protein degradation; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [P62072](https://www.uniprot.org/uniprotkb/P62072) (Mitochondrial import inner membrane translocase subunit Tim10):

> Mitochondrial intermembrane chaperone that participates in the import and insertion of multi-pass transmembrane proteins into the mitochondrial inner membrane. May also be required for the transfer of beta-barrel precursors from the TOM complex to the sorting and assembly machinery (SAM complex) of the outer membrane. Acts as a chaperone-like protein that protects the hydrophobic precursors from aggregation and guide them through the mitochondrial intermembrane space.

**Summary**, from NCBI Gene [26519](https://www.ncbi.nlm.nih.gov/gene/26519):

> The mitochondrial protein encoded by this gene belongs to a family of evolutionarily conserved proteins that are organized in heterooligomeric complexes in the mitochondrial intermembrane space. These proteins mediate the import and insertion of hydrophobic membrane proteins into the mitochondrial inner membrane, functioning as intermembrane space chaperones for the highly insoluble carrier proteins. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:11814](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11814) · Entrez [26519](https://www.ncbi.nlm.nih.gov/gene/26519) · UniProt [P62072](https://www.uniprot.org/uniprotkb/P62072) · Ensembl [ENSG00000134809](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134809)

## Data

Gene col 5607: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5607); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5607, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5607]; `tensor/DDL_lfc|DDL_z.npy` [5607]; `embed/gene_vectors.npy` [5607]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5607 or target_col == 5607). Every well: [[TIMM10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMM10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "ZNRD2"
type: "gene"
col: 10389
ensembl_id: "ENSG00000173465"
name: "zinc ribbon domain containing 2"
location: "11q13.1"
module: 3
arm: "+"
pooled_cpm: 9.78
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# ZNRD2

*zinc ribbon domain containing 2* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.31× (z +6.2, q 2e-07, up in 38 of 47 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +5.4, q 9e-06, up in 28 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2030 0.123×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL55]] (+0.78, fdr 7e-06), [[TMEM208]] (+0.70, fdr 7e-06), [[ATG101]] (+0.69, fdr 1e-05); moves opposite to [[ENOSF1]] (-0.61, fdr 1e-04), [[FUBP1]] (-0.60, fdr 5e-04), [[ACADM]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10389.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.31×** | +6.2 | 2e-07 | 38/47 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.28×** | +6.1 | 2e-07 | 37/47 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.10×** | +5.5 | 5e-06 | 29/47 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.4 | 9e-06 | 28/44 (NCI-H460, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.00×** | +5.2 | 3e-05 | 28/42 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +4.6 | 4e-04 | 28/45 (SW480, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.76×** | +4.2 | 0.002 | 23/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.74×** | +4.1 | 0.003 | 27/47 (PANC-1, A-427, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.13×** | +4.0 | 0.004 | 22/44 (A-427, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.66×** | +3.6 | 0.016 | 19/38 (SK-MEL-2, NCI-H460, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +3.6 | 0.019 | 21/44 (PANC-1, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.5 | 0.024 | 19/38 (SNU-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.3 | 0.042 | 16/43 (SK-MEL-2, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.57×** | +3.1 | 0.073 | 10/26 (MIA PaCa-2, LS 180, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10389.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2030 0.123×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.633× | -3.2 | 0.79 | 13/47 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10389. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 7.45 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.58 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10389), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL55]] | +0.78 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[TMEM208]] | +0.70 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[ATG101]] | +0.69 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[CIB1]] | +0.68 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[MPG]] | +0.68 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[NAT9]] | +0.67 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[TRPT1]] | +0.67 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[NUBP2]] | +0.65 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[BET1L]] | +0.65 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[MED8]] | +0.65 | +0.68 / +0.46 | both halves | 2e-05 |  |
| [[LCMT1]] | +0.65 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[SPSB3]] | +0.65 | +0.51 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOSF1]] | -0.61 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[FUBP1]] | -0.60 | -0.24 / -0.58 | both halves | 5e-04 |  |
| [[ACADM]] | -0.60 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[HACD2]] | -0.59 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[RHOBTB3]] | -0.59 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[AGL]] | -0.58 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[HMGN2]] | -0.58 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[RCN1]] | -0.57 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[HMGN1]] | -0.57 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[HNRNPU]] | -0.56 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[DDX6]] | -0.56 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[HNRNPK]] | -0.56 | -0.28 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.676). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (11.9, -26.3); signed map (-41.8, 6.8). **Vector** length 74.8, 16.6% of its response variance represented; |z| ≥ 3 in 675 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.2 | +6.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.1 | +6.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +2.8 | +5.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.5 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +4.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.9 | +2.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.9 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +1.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.0 | +2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -3.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Afatinib (drug)]] 5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc ribbon domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,570,460-65,573,942 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p27; previously SSSCA1 |
| Matched by | ensembl_id |

**Function**, from UniProt [O60232](https://www.uniprot.org/uniprotkb/O60232) (Ubiquitin ligase substrate adapter ZNRD2):

> Ubiquitin ligase substrate adapter that functions in the protein complex assembly quality control pathway that promotes the proteasomal elimination of unassembled protein complex subunits and incomplete sub-assemblies. As part of the protein complex assembly quality control pathway, links the E3 ubiquitin ligase HERC2 to unassembled chaperonin-containing TCP-1 complex (CCT) subunits.; (Microbial infection) Restricts replication of human respiratory syncytial virus (HRSV) by promoting …

**Summary**, from NCBI Gene [10534](https://www.ncbi.nlm.nih.gov/gene/10534):

> This antigen is recognized by a subset of anti-centromere antibodies from patients with scleroderma and/or Sjogren's syndrome. Subcellular localization has not yet been established. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11328) · Entrez [10534](https://www.ncbi.nlm.nih.gov/gene/10534) · UniProt [O60232](https://www.uniprot.org/uniprotkb/O60232) · Ensembl [ENSG00000173465](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173465)

## Data

Gene col 10389: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10389); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10389, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10389]; `tensor/DDL_lfc|DDL_z.npy` [10389]; `embed/gene_vectors.npy` [10389]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10389 or target_col == 10389). Every well: [[ZNRD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNRD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

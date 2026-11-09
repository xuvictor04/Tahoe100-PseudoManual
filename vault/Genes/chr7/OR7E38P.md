---
symbol: "OR7E38P"
type: "gene"
col: 11403
ensembl_id: "ENSG00000183444"
name: "olfactory receptor family 7 subfamily E member 38 pseudogene"
location: "7q21.3"
module: 11
arm: "+"
pooled_cpm: 2.6
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# OR7E38P

*olfactory receptor family 7 subfamily E member 38 pseudogene* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.34× (z +9.8, q 5e-20, up in 12 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.83× (z +3.5, q 0.035, up in 13 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ivermectin (drug)]] 0.5 µM in 1 line (SW1417 0.0470×).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FDX2]] (+0.69, fdr 1e-05), [[ZNF593]] (+0.63, fdr 2e-05), [[EIF4EBP3]] (+0.62, fdr 7e-06); moves opposite to [[PHTF2]] (-0.51, fdr 1e-04), [[RPSA]] (-0.51, fdr 3e-04), [[PRPF8]] (-0.50, fdr 6e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11403.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.34×** | +9.8 | 5e-20 | 12/12 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.46×** | +8.4 | 1e-14 | 2/3 (PANC-1, AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.55×** | +6.5 | 2e-08 | 4/5 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.43×** | +5.2 | 3e-05 | 16/23 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **2.18×** | +4.6 | 6e-04 | 10/15 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +4.2 | 0.003 | 9/17 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +3.5 | 0.035 | 13/31 (NCI-H1573, A-172, …) | two highest doses | cell-cycle shift (explains ~23% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.85×** | +3.4 | 0.040 | 5/18 (NCI-H2030, A-427, …) | top dose only | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ivermectin (drug)]] 0.5 µM in 1 line (SW1417 0.0470×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11403. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 4.63 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0470× (z -10.1) |
| [[A-172 (line)]] | wt | 0.995 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.793 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11403), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 16 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FDX2]] | +0.69 | +0.53 / +0.76 | both halves | 1e-05 |  |
| [[ZNF593]] | +0.63 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[EIF4EBP3]] | +0.62 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[OXLD1]] | +0.62 | +0.34 / +0.72 | both halves | 1e-04 |  |
| [[MRPL46]] | +0.62 | +0.35 / +0.66 | both halves | 1e-04 |  |
| [[MRPS18C]] | +0.61 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[ERVK3-1]] | +0.60 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[SCAND1]] | +0.60 | +0.39 / +0.67 | both halves | 5e-05 |  |
| [[C11orf1]] | +0.59 | +0.39 / +0.70 | both halves | 5e-05 |  |
| [[EMC6]] | +0.59 | +0.19 / +0.71 | ⚠ one half (not replicated) | 9e-04 |  |
| [[RPP25L]] | +0.58 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[TIMM10]] | +0.57 | +0.21 / +0.71 | both halves | 7e-04 |  |
| [[LSM10]] | +0.56 | +0.26 / +0.70 | both halves | 4e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHTF2]] | -0.51 | -0.33 / -0.60 | both halves | 1e-04 |  |
| [[RPSA]] | -0.51 | -0.29 / -0.55 | both halves | 3e-04 |  |
| [[PRPF8]] | -0.50 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[TXNDC5]] | -0.50 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[MAPK9]] | -0.49 | -0.28 / -0.59 | both halves | 3e-04 |  |
| [[ARF3]] | -0.49 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[SNRNP200]] | -0.49 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[YWHAQ]] | -0.48 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[RBM14-RBM4]] | -0.48 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[PARP1]] | -0.48 | -0.29 / -0.54 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-42.9, -11.3); signed map (-11.7, -6.7). **Vector** length 34.5, 3.91% of its response variance represented; |z| ≥ 3 in 655 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +1.6 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.2 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.6 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | olfactory receptor family 7 subfamily E member 38 pseudogene |
| Locus type | pseudogene |
| Location | 7q21.3 — chr7:97,966,090-97,967,074 (-) |
| Ensembl biotype | unprocessed_pseudogene |
| Also known as | OST127; previously OR7E76 |
| Gene groups (HGNC) | Olfactory receptors, family 7 |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [389537](https://www.ncbi.nlm.nih.gov/gene/389537):

> Olfactory receptors interact with odorant molecules in the nose, to initiate a neuronal response that triggers the perception of a smell. The olfactory receptor proteins are members of a large family of G-protein-coupled receptors (GPCR) arising from single coding-exon genes. Olfactory receptors share a 7-transmembrane domain structure with many neurotransmitter and hormone receptors and are responsible for the recognition and G protein-mediated transduction of odorant signals. The olfactory …

**Accessions** — [HGNC:8411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8411) · Entrez [389537](https://www.ncbi.nlm.nih.gov/gene/389537) · Ensembl [ENSG00000183444](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183444)

## Data

Gene col 11403: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11403); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11403, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11403]; `tensor/DDL_lfc|DDL_z.npy` [11403]; `embed/gene_vectors.npy` [11403]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11403 or target_col == 11403). Every well: [[OR7E38P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OR7E38P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "RAPSN"
type: "gene"
col: 9208
ensembl_id: "ENSG00000165917"
name: "receptor associated protein of the synapse"
location: "11p11.2"
module: 39
arm: "+"
pooled_cpm: 2.99
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# RAPSN

*receptor associated protein of the synapse* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.12× (z +6.2, q 4e-07, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 1.83× (z +5.2, q 7e-05, up in 13 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.402× (z -7.5, q 5e-11, down in 25 of 39 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Erlotinib (drug)]] 5 µM: 0.636× (z -3.7, q 0.020, down in 14 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC22A14]] (+0.80, fdr 7e-06), [[MSANTD1]] (+0.79, fdr 7e-06), [[OIT3]] (+0.79, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9208.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +6.2 | 4e-07 | 1/5 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.83×** | +5.2 | 7e-05 | 13/46 (SW480, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.48×** | +4.7 | 4e-04 | 11/44 (SW480, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +4.7 | 4e-04 | 1/8 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +4.6 | 5e-04 | 9/27 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.011 | 13/39 (LoVo, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.59×** | +3.7 | 0.015 | 6/40 (PANC-1, HS-578T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9208.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.402×** | -7.5 | 5e-11 | 25/39 (SNU-423, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.538×** | -5.3 | 4e-05 | 17/39 (PANC-1, BT-474, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.557×** | -5.0 | 1e-04 | 22/46 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.611×** | -4.2 | 0.004 | 14/39 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.614×** | -4.1 | 0.004 | 16/26 (SW480, PANC-1, …) | two highest doses |  |
| [[Erlotinib (drug)]] 5 µM |  | **0.636×** | -3.7 | 0.020 | 14/37 (NCI-H1573, A-172, …) | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **0.655×** | -3.6 | 0.027 | 13/44 (MIA PaCa-2, A-172, …) | rises with dose | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.666×** | -3.3 | 0.063 | 12/43 (H4, A-172, …) | top dose only | plate-row cell shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.771× | -3.1 | 0.11 | 16/32 (C32, PANC-1, …) | top dose only | composition shift |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.687× | -3.0 | 0.15 | 12/36 (NCI-H1573, C32, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9208. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.36 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -10.9) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SW480 (line)]] | alt | 3.18 | 0 | 2 (1 ⚠) | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0772× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 6.29 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0759× (z -10.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 3.22 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0719× (z -8.6) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SNU-423 (line)]] | alt | 3.93 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0505× (z -9.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.990 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9208), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC22A14]] | +0.80 | +0.75 / +0.81 | both halves | 7e-06 |  |
| [[MSANTD1]] | +0.79 | +0.78 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[OIT3]] | +0.79 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.77 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[TMEM236]] | +0.76 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[SLC22A13]] | +0.76 | +0.70 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[IMPA1P1]] | +0.75 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[ARL9]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.73 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[IDI2-AS1]] | +0.73 | +0.72 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.780). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.7, -15.0); signed map (16.4, 8.8). **Vector** length 66.1, 9.77% of its response variance represented; |z| ≥ 3 in 1,255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 0.05 µM |  | +3.7 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +6.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +3.2 | +4.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +5.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.6 | -7.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.5 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.2 | -5.0 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.2 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | receptor associated protein of the synapse |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:47,437,764-47,449,143 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF205, CMS1D, CMS1E |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13702](https://www.uniprot.org/uniprotkb/Q13702) (43 kDa receptor-associated protein of the synapse):

> Postsynaptic protein required for clustering of nicotinic acetylcholine receptors (nAChRs) at the neuromuscular junction. It may link the receptor to the underlying postsynaptic cytoskeleton, possibly by direct association with actin or spectrin.

**Summary**, from NCBI Gene [5913](https://www.ncbi.nlm.nih.gov/gene/5913):

> This gene encodes a member of a family of proteins that are receptor associated proteins of the synapse. The encoded protein contains a conserved cAMP-dependent protein kinase phosphorylation site, and plays a critical role in clustering and anchoring nicotinic acetylcholine receptors at synaptic sites by linking the receptors to the underlying postsynaptic cytoskeleton, possibly by direct association with actin or spectrin. Mutations in this gene may play a role in postsynaptic congenital …

**Accessions** — [HGNC:9863](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9863) · Entrez [5913](https://www.ncbi.nlm.nih.gov/gene/5913) · UniProt [Q13702](https://www.uniprot.org/uniprotkb/Q13702) · Ensembl [ENSG00000165917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165917)

## Data

Gene col 9208: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9208); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9208, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9208]; `tensor/DDL_lfc|DDL_z.npy` [9208]; `embed/gene_vectors.npy` [9208]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9208 or target_col == 9208). Every well: [[RAPSN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAPSN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "ATP5PO"
type: "gene"
col: 14287
ensembl_id: "ENSG00000241837"
name: "ATP synthase peripheral stalk subunit OSCP"
location: "21q22.11"
module: 24
arm: "+"
pooled_cpm: 33.56
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# ATP5PO

*ATP synthase peripheral stalk subunit OSCP* — 21q22.11

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.78× (z +8.2, q 1e-13, up in 41 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SNU-423 4.63×, A549 5.88×, A498 3.99×, MIA PaCa-2 4.63×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Sulfisoxazole (drug)]] 5 µM in 1 line (CHP-212 0.166×).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC5]] (+0.73, fdr 2e-05), [[UQCR10]] (+0.73, fdr 3e-05, ⚠ UQCR10 in the vector space only through flagged drug-doses), [[NDUFA8]] (+0.69, fdr 3e-05), [[POLR2I]] (+0.69, fdr 2e-04); moves opposite to [[SMG1P6]] (-0.64, fdr 7e-05), [[CERS2]] (-0.64, fdr 1e-05), [[LENG8-AS1]] (-0.63, fdr 5e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14287.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SNU-423 4.63×, A549 5.88×, A498 3.99×, MIA PaCa-2 4.63×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.78×** | +8.2 | 1e-13 | 41/45 (SNU-423, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.32×** | +6.5 | 2e-08 | 35/39 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.76×** | +4.2 | 0.005 | 33/43 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.67×** | +4.1 | 0.006 | 36/46 (CFPAC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Sulfisoxazole (drug)]] 5 µM in 1 line (CHP-212 0.166×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14287. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 37.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A549 (line)]] | wt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[CHP-212 (line)]] | wt | 29.6 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 5 µM 0.166× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 43.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SNU-423 (line)]] | alt | 28.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SW480 (line)]] | alt | 42.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 48.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14287), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 19 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC5]] | +0.73 | +0.48 / +0.70 | both halves | 2e-05 |  |
| [[UQCR10]] ⚠ | +0.73 | +0.44 / +0.82 | both halves | 3e-05 | pathway: HALLMARK_ADIPOGENESIS; STRING 761; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA8]] | +0.69 | +0.44 / +0.73 | both halves | 3e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 852 |
| [[POLR2I]] | +0.69 | +0.30 / +0.73 | both halves | 2e-04 |  |
| [[NDUFB10]] | +0.69 | +0.42 / +0.72 | both halves | 4e-05 | pathway: Aerobic respiration and respiratory electron transport; STRING 860 |
| [[MTLN]] ⚠ | +0.68 | +0.45 / +0.70 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNAPIN]] | +0.67 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[HPF1]] | +0.66 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[PITPNA-AS1]] | +0.65 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[ISCA2]] | +0.65 | +0.38 / +0.65 | both halves | 7e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[GPATCH11]] | +0.65 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[KRTCAP2]] | +0.64 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[GADD45GIP1]] | +0.64 | +0.30 / +0.73 | both halves | 2e-04 |  |
| [[IFI27L2]] | +0.64 | +0.38 / +0.69 | both halves | 6e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P6]] | -0.64 | -0.38 / -0.65 | both halves | 7e-05 |  |
| [[CERS2]] | -0.64 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[LENG8-AS1]] | -0.63 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[HCFC1]] | -0.62 | -0.41 / -0.60 | both halves | 4e-05 | pathway: Mitochondrial biogenesis |
| [[LY6G5B]] | -0.62 | -0.43 / -0.57 | both halves | 4e-05 |  |
| [[RCC2]] | -0.60 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[ERVK13-1]] | -0.60 | -0.15 / -0.57 | ⚠ one half (not replicated) | 0.001 |  |
| [[DDX5]] | -0.57 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[IL18BP]] | -0.57 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[HNRNPAB]] | -0.57 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[QRICH2]] | -0.56 | -0.16 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[GTF3C2-AS2]] | -0.56 | -0.20 / -0.37 | both halves | 7e-04 |  |
| [[CAPN15]] | -0.55 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[U2AF2]] | -0.55 | -0.23 / -0.58 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.3, -14.1); signed map (-18.3, -7.6). **Vector** length 49.2, 11.8% of its response variance represented; |z| ≥ 3 in 395 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +1.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.3 | +0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.2 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | -0.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | -3.4 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -3.3 | +6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | +0.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | -2.6 | +8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.9 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ATP synthase peripheral stalk subunit OSCP |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.11 — chr21:33,903,453-33,915,814 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OSCP, ATPO; previously ATP5O |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits |
| Hallmark sets | ADIPOGENESIS, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 6 pathways, smallest: Formation of ATP by chemiosmotic coupling; Cristae formation; Mitochondrial biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P48047](https://www.uniprot.org/uniprotkb/P48047) (ATP synthase peripheral stalk subunit OSCP, mitochondrial):

> Subunit OSCP, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain. ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel. These two domains are linked by a central stalk rotating inside the F(1) region and a stationary …

**Summary**, from NCBI Gene [539](https://www.ncbi.nlm.nih.gov/gene/539):

> The protein encoded by this gene is a component of the F-type ATPase found in the mitochondrial matrix. F-type ATPases are composed of a catalytic core and a membrane proton channel. The encoded protein appears to be part of the connector linking these two components and may be involved in transmission of conformational changes or proton conductance. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:850) · Entrez [539](https://www.ncbi.nlm.nih.gov/gene/539) · UniProt [P48047](https://www.uniprot.org/uniprotkb/P48047) · Ensembl [ENSG00000241837](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241837)

## Data

Gene col 14287: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14287); `tables/drug_effects.parquet` (4 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14287, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14287]; `tensor/DDL_lfc|DDL_z.npy` [14287]; `embed/gene_vectors.npy` [14287]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14287 or target_col == 14287). Every well: [[ATP5PO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP5PO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

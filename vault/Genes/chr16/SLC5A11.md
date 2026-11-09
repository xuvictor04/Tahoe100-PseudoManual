---
symbol: "SLC5A11"
type: "gene"
col: 8202
ensembl_id: "ENSG00000158865"
name: "solute carrier family 5 member 11"
location: "16p12.1"
module: 39
arm: "+"
pooled_cpm: 2.94
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# SLC5A11

*solute carrier family 5 member 11* — 16p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.92× (z +13.1, q 2e-36, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 2.06× (z +7.8, q 8e-13, up in 22 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM: 0.586× (z -4.1, q 0.022, down in 12 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vitamin K4 (drug)]] 0.5 µM in 1 line (HS-578T 0.0430×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OIT3]] (+0.80, fdr 7e-06), [[USP50]] (+0.75, fdr 7e-06), [[AXDND1]] (+0.73, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8202.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.92×** | +13.1 | 2e-36 | 3/4 (A498, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.78×** | +12.4 | 5e-33 | 4/6 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.18×** | +11.0 | 1e-25 | 10/14 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.06×** | +7.8 | 8e-13 | 22/45 (NCI-H460, SW 900, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +7.2 | 9e-11 | 18/36 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +6.7 | 2e-09 | 21/36 (PANC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.40×** | +6.7 | 2e-09 | 28/47 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.19×** | +6.0 | 1e-07 | 20/41 (SW480, COLO 205, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.16×** | +5.9 | 2e-07 | 21/46 (HepG2/C3A, COLO 205, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.20×** | +5.7 | 7e-07 | 18/42 (A498, LoVo, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.08×** | +5.6 | 1e-06 | 18/42 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.88×** | +4.8 | 7e-05 | 17/47 (J82, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +4.6 | 2e-04 | 15/34 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.79×** | +4.2 | 0.001 | 12/40 (HepG2/C3A, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.1 | 0.002 | 7/45 (A498, SW 900, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.42×** | +3.8 | 0.005 | 13/44 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.63×** | +3.7 | 0.006 | 12/42 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.51×** | +3.0 | 0.066 | 3/34 (COLO 205, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8202.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vitamin K4 (drug)]] 0.5 µM in 1 line (HS-578T 0.0430×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.586×** | -4.1 | 0.022 | 12/44 (C-33 A, A498, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | 0.645× | -3.4 | 0.21 | 7/44 (COLO 205, A498, …) | top dose only | position effect removed |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.646× | -3.2 | 0.28 | 9/38 (SW480, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8202. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 3.00 | 0 | 1 | — | [[Vitamin K4 (drug)]] 0.5 µM 0.0430× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 3.35 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.0× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.967 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8202), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OIT3]] | +0.80 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[USP50]] | +0.75 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[AXDND1]] | +0.73 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[SGSM3-AS1]] | +0.72 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[ARL9]] | +0.72 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[MPP4]] | +0.71 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[LINC02133]] | +0.71 | +0.64 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[SCUBE2]] | +0.71 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.71 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[TMEM236]] | +0.71 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[SLC6A13]] | +0.71 | +0.73 / +0.69 | both halves | 7e-06 | pathway: SLC-mediated transmembrane transport |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.767). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.1, -13.5); signed map (18.4, 9.6). **Vector** length 63.2, 8.79% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +12.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +6.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +13.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.7 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +5.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.5 | +5.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.8 |
| fall | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.6 | -3.2 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.9 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -2.6 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.9 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 5 member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.1 — chr16:24,845,841-24,911,628 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KST1, SMIT2, SGLT6 |
| Gene groups (HGNC) | Solute carrier family 5 |
| Reactome | 3 pathways, smallest: Inositol transporters; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WWX8](https://www.uniprot.org/uniprotkb/Q8WWX8) (Sodium/myo-inositol cotransporter 2):

> Involved in the sodium-dependent cotransport of myo-inositol (MI) with a Na(+):MI stoichiometry of 2:1. Exclusively responsible for apical MI transport and absorption in intestine (By similarity). Can also transport D-chiro-inositol (DCI) but not L-fucose. Exhibits stereospecific cotransport of both D-glucose and D-xylose (By similarity). May induce apoptosis through the TNF, PDCD1 pathway. May play a role in the regulation of MI concentration in serum, involving reabsorption in at least the …

**Summary**, from NCBI Gene [115584](https://www.ncbi.nlm.nih.gov/gene/115584):

> Cotransporters, such as SLC5A11, represent a major class of proteins that make use of ion gradients to drive active transport for the cellular accumulation of nutrients, neurotransmitters, osmolytes, and ions Roll et al. (2002) [PubMed 12039040].[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:23091](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23091) · Entrez [115584](https://www.ncbi.nlm.nih.gov/gene/115584) · UniProt [Q8WWX8](https://www.uniprot.org/uniprotkb/Q8WWX8) · Ensembl [ENSG00000158865](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158865)

## Data

Gene col 8202: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8202); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8202, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8202]; `tensor/DDL_lfc|DDL_z.npy` [8202]; `embed/gene_vectors.npy` [8202]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8202 or target_col == 8202). Every well: [[SLC5A11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC5A11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

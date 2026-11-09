---
symbol: "FANCG"
type: "gene"
col: 13307
ensembl_id: "ENSG00000221829"
name: "FA complementation group G"
location: "9p13.3"
module: 6
arm: "+"
pooled_cpm: 4.82
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# FANCG

*FA complementation group G* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.79× (z +5.8, q 4e-06, up in 13 of 22 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Trifluridine (drug)]] 0.5 µM: 1.50× (z +4.1, q 0.007, up in 11 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 5.46×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.615× (z -4.8, q 8e-04, down in 21 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Tucidinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.0687×; ⚠ cell-cycle shift, explains ~31% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.0506×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (A-172 0.0692×); [[Saquinavir (drug)]] 0.5 µM in 1 line (RKO 0.0956×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRM1]] (+0.81, fdr 7e-06), [[MYBL2]] (+0.80, fdr 7e-06), [[DDX12P]] (+0.79, fdr 7e-06); moves opposite to [[MRPL33]] (-0.68, fdr 9e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 7 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13307.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 5.46×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.79×** | +5.8 | 4e-06 | 13/22 (MIA PaCa-2, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.78×** | +5.3 | 4e-05 | 4/10 (NCI-H2347, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.66×** | +4.8 | 3e-04 | 5/7 (SW480, HOP62, …) | all doses, flat | composition shift |
| [[Trifluridine (drug)]] 0.5 µM |  | **1.50×** | +4.1 | 0.007 | 11/44 (A498, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +3.7 | 0.024 | 5/27 (SNU-1, A549, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 1.39× | +3.2 | 0.11 | 10/46 (J82, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.37× | +3.2 | 0.13 | 6/39 (A498, SW1417, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.36× | +3.1 | 0.14 | 9/46 (AsPC-1, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13307.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Tucidinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.0687×; ⚠ cell-cycle shift, explains ~31% of this change); [[Auranofin (drug)]] 5 µM in 1 line (SHP-77 0.0506×); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (A-172 0.0692×); [[Saquinavir (drug)]] 0.5 µM in 1 line (RKO 0.0956×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.615×** | -4.8 | 8e-04 | 21/45 (SHP-77, A-172, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.715× | -3.3 | 0.25 | 13/39 (SW480, H4, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.800× | -3.1 | 0.31 | 12/38 (J82, LS 180, …) | rises with dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.805× | -3.0 | 0.34 | 8/44 (SNU-423, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.55 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13307. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 5.43 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0692× (z -9.8) |
| [[A549 (line)]] | wt | 4.63 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0912× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 3.25 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0687× (z -11.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 6.38 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0956× (z -8.8) |
| [[SHP-77 (line)]] | alt | 6.08 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0506× (z -9.9) |
| [[SW480 (line)]] | alt | 7.38 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.46× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[A-427 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13307), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRM1]] | +0.81 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.80 | +0.76 / +0.80 | both halves | 7e-06 |  |
| [[DDX12P]] | +0.79 | +0.68 / +0.83 | both halves | 7e-06 |  |
| [[TIMELESS]] | +0.79 | +0.70 / +0.81 | both halves | 7e-06 |  |
| [[RFC5]] | +0.78 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[MCM4]] | +0.78 | +0.70 / +0.78 | both halves | 7e-06 |  |
| [[POLE]] | +0.77 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[TRIP13]] | +0.75 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[ORC1]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[KNTC1]] | +0.75 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[TONSL]] | +0.75 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[MCM2]] | +0.74 | +0.65 / +0.79 | both halves | 7e-06 | STRING 537 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL33]] | -0.68 | -0.57 / -0.69 | both halves | 9e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.803). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.2, -42.4); signed map (-35.9, -46.4). **Vector** length 64.5, 9.59% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.62 to 65); *DNA strand elongation* (reactome, mean cos +0.63 to 28); *DNA Replication* (reactome, mean cos +0.61 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +2.8 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +2.4 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +2.3 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +2.1 | +3.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.1 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | +2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +1.4 |
|  | [[Folic acid (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +1.1 | +1.7 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.1 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.9 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.5 | -2.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -1.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | FA complementation group G |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,073,835-35,080,004 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FAG; previously XRCC9 |
| Gene groups (HGNC) | FA complementation groups; FA core complex |
| Reactome | 6 pathways, smallest: Fanconi Anemia Pathway; PKR-mediated signaling; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O15287](https://www.uniprot.org/uniprotkb/O15287) (Fanconi anemia group G protein):

> DNA repair protein that may operate in a postreplication repair or a cell cycle checkpoint function. May be implicated in interstrand DNA cross-link repair and in the maintenance of normal chromosome stability. Candidate tumor suppressor gene.

**Summary**, from NCBI Gene [2189](https://www.ncbi.nlm.nih.gov/gene/2189):

> The Fanconi anemia complementation group (FANC) currently includes FANCA, FANCB, FANCC, FANCD1 (also called BRCA2), FANCD2, FANCE, FANCF, FANCG, FANCI, FANCJ (also called BRIP1), FANCL, FANCM and FANCN (also called PALB2). The previously defined group FANCH is the same as FANCA. Fanconi anemia is a genetically heterogeneous recessive disorder characterized by cytogenetic instability, hypersensitivity to DNA crosslinking agents, increased chromosomal breakage, and defective DNA repair. The …

**Accessions** — [HGNC:3588](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3588) · Entrez [2189](https://www.ncbi.nlm.nih.gov/gene/2189) · UniProt [O15287](https://www.uniprot.org/uniprotkb/O15287) · Ensembl [ENSG00000221829](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221829)

## Data

Gene col 13307: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13307); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13307, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13307]; `tensor/DDL_lfc|DDL_z.npy` [13307]; `embed/gene_vectors.npy` [13307]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13307 or target_col == 13307). Every well: [[FANCG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FANCG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

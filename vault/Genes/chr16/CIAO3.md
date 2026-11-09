---
symbol: "CIAO3"
type: "gene"
col: 2340
ensembl_id: "ENSG00000103245"
name: "cytosolic iron-sulfur assembly component 3"
location: "16p13.3"
module: 64
arm: "+"
pooled_cpm: 6.37
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# CIAO3

*cytosolic iron-sulfur assembly component 3* — 16p13.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.700× (z -7.3, q 1e-10, down in 22 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAB1]] (+0.72, fdr 7e-06), [[RBSN]] (+0.64, fdr 1e-05), [[METTL22]] (+0.63, fdr 7e-06); moves opposite to [[EPB41L2]] (-0.72, fdr 7e-06), [[KLF12]] (-0.54, fdr 2e-05), [[SLC12A2]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2340.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.26× | +3.4 | 0.36 | 7/44 (PANC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.24× | +3.2 | 0.36 | 3/46 (LoVo, A-427, …) | rises with dose |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.24× | +3.1 | 0.36 | 3/47 (hTERT-HPNE, A498, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2340.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -7.3 | 1e-10 | 22/41 (LoVo, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Crizotinib (hydrochloride) (drug)]] 0.5 µM |  | **0.763×** | -3.9 | 0.018 | 9/43 (NCI-H1792, NCI-H23, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.765×** | -3.9 | 0.018 | 14/27 (LoVo, SNU-423, …) | inconsistent across doses | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.771×** | -3.8 | 0.022 | 12/44 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Valdecoxib (drug)]] 0.5 µM |  | **0.784×** | -3.5 | 0.044 | 11/43 (NCI-H2030, RKO, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.851× | -3.3 | 0.090 | 12/47 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 0.855× | -3.2 | 0.099 | 9/47 (CFPAC-1, NCI-H661, …) | top dose only |  |
| [[Silodosin (drug)]] 5 µM |  | **0.796×** | -3.2 | 0.099 | 14/42 (COLO 205, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2340. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 5.30 | 0 | 2 | — | [[Infigratinib (drug)]] 0.05 µM 0.0785× (z -9.4) |
| [[BT-474 (line)]] | alt | 8.05 | 0 | 1 | — | [[Thymopentin (drug)]] 0.05 µM 0.0626× (z -10.3) |
| [[Hs 766T (line)]] | wt | 5.81 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.05 µM 0.0630× (z -9.9) |
| [[SNU-423 (line)]] | alt | 6.18 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0916× (z -8.9) |
| [[A-172 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2340), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAB1]] | +0.72 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[RBSN]] | +0.64 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[METTL22]] | +0.63 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[C19orf44]] | +0.63 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[AP3S2]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[KLHL12]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[GNPAT]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[RUFY1]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[CDC16]] | +0.57 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[TSC2]] | +0.56 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[EIF2B4]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[CBY1]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L2]] | -0.72 | -0.73 / -0.66 | both halves | 7e-06 |  |
| [[KLF12]] | -0.54 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[SLC12A2]] | -0.53 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[EXTL2]] | -0.53 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[ADGRE3]] | -0.52 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[ARL5B]] | -0.52 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[TLL2]] | -0.52 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[HNRNPA2B1]] | -0.52 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[MYADM-AS1]] | -0.51 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[CHD4]] | -0.50 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[CFL1]] | -0.50 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[SLIT2]] | -0.49 | -0.36 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.369). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-35.1, -8.0); signed map (-15.1, -16.1). **Vector** length 49.5, 5.63% of its response variance represented; |z| ≥ 3 in 854 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.8 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +3.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.4 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.3 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.2 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +3.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.5 | -3.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.3 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.1 | -0.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | cytosolic iron-sulfur assembly component 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:729,760-741,329 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21988, PRN, HPRN, IOP1, NAR1; previously NARFL |
| Gene groups (HGNC) | Cytosolic iron-sulfur assembly components |
| Reactome | 1 pathways, smallest: Cytosolic iron-sulfur cluster assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6Q4](https://www.uniprot.org/uniprotkb/Q9H6Q4) (Cytosolic iron-sulfur assembly component 3):

> Component of the cytosolic iron-sulfur protein assembly (CIA) complex, a multiprotein complex that mediates the incorporation of iron-sulfur cluster into extramitochondrial Fe/S proteins. Seems to negatively regulate the level of HIF1A expression, although this effect could be indirect.

**Summary**, from NCBI Gene [64428](https://www.ncbi.nlm.nih.gov/gene/64428):

> Predicted to enable 4 iron, 4 sulfur cluster binding activity and metal ion binding activity. Involved in several processes, including intracellular oxygen homeostasis; iron-sulfur cluster assembly; and response to hypoxia. Part of cytosolic [4Fe-4S] assembly targeting complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14179](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14179) · Entrez [64428](https://www.ncbi.nlm.nih.gov/gene/64428) · UniProt [Q9H6Q4](https://www.uniprot.org/uniprotkb/Q9H6Q4) · Ensembl [ENSG00000103245](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103245)

## Data

Gene col 2340: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2340); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2340, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2340]; `tensor/DDL_lfc|DDL_z.npy` [2340]; `embed/gene_vectors.npy` [2340]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2340 or target_col == 2340). Every well: [[CIAO3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIAO3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "FANCE"
type: "gene"
col: 3315
ensembl_id: "ENSG00000112039"
name: "FA complementation group E"
location: "6p21.31"
module: 85
arm: "+"
pooled_cpm: 3.42
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# FANCE

*FA complementation group E* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 3.63× (z +13.6, q 2e-39, up in 41 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Tadalafil (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0469×); [[Pemetrexed (drug)]] 5 µM in 1 line (J82 0.0883×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBX4]] (+0.66, fdr 3e-05), [[CCNQ]] (+0.66, fdr 1e-05), [[ZMYND19]] (+0.65, fdr 1e-05); moves opposite to [[CAPS2]] (-0.62, fdr 3e-05), [[MR1]] (-0.62, fdr 3e-04), [[PNISR-AS1]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 085]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3315.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **3.63×** | +13.6 | 2e-39 | 41/44 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.39×** | +12.9 | 1e-35 | 40/46 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.32×** | +12.7 | 2e-34 | 38/42 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.96×** | +11.0 | 4e-26 | 2/7 (SNU-423, CFPAC-1) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.09×** | +7.8 | 7e-13 | 31/46 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.06×** | +7.6 | 3e-12 | 20/30 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.93×** | +6.7 | 2e-09 | 7/19 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.72×** | +5.7 | 8e-07 | 5/18 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.70×** | +5.4 | 5e-06 | 8/26 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.63×** | +4.4 | 6e-04 | 1/9 (J82) | all doses, stronger at high dose | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +4.1 | 0.002 | 5/26 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.69×** | +4.0 | 0.003 | 3/24 (PANC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.8 | 0.005 | 7/27 (Panc 03.27, NCI-H2030, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.025 | 5/32 (A-427, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.57×** | +3.4 | 0.025 | 3/30 (CFPAC-1, SW480, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Talc (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.037 | 3/40 (C-33 A, A-427, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.84×** | +3.2 | 0.044 | 0/37 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.049 | 4/29 (SW480, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Tadalafil (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0469×); [[Pemetrexed (drug)]] 5 µM in 1 line (J82 0.0883×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3315. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 4.54 | 0 | 1 | — | [[Tadalafil (drug)]] 0.05 µM 0.0469× (z -11.2) |
| [[J82 (line)]] | alt | 4.25 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0883× (z -9.1) |
| [[A-172 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.869 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3315), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBX4]] | +0.66 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[CCNQ]] | +0.66 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[ZMYND19]] | +0.65 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[CABLES2]] | +0.64 | +0.52 / +0.35 | both halves | 1e-04 |  |
| [[PAQR4]] | +0.63 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CKLF]] | +0.62 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[TSEN54]] | +0.62 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[BMP8B]] | +0.61 | +0.47 / +0.35 | both halves | 1e-04 |  |
| [[MPST]] | +0.61 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[KANK2]] | +0.61 | +0.53 / +0.34 | both halves | 1e-04 |  |
| [[DHTKD1]] | +0.61 | +0.34 / +0.39 | both halves | 1e-04 |  |
| [[GAS2L1]] | +0.60 | +0.52 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPS2]] | -0.62 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[MR1]] | -0.62 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[PNISR-AS1]] | -0.62 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[CFAP418-AS1]] | -0.61 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[CCDC90B-AS1]] | -0.60 | -0.38 / -0.26 | both halves | 3e-04 |  |
| [[ZSCAN30]] | -0.60 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[PAPOLA]] | -0.60 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[VPS52]] | -0.60 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[HFE]] | -0.59 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[LINC02542]] | -0.59 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[NQO1-DT]] | -0.59 | -0.41 / -0.26 | both halves | 4e-04 |  |
| [[PBLD]] | -0.59 | -0.37 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[ARRDC3-AS1]] | -0.58 | -0.32 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (2.9, -0.3); signed map (-40.2, -2.7). **Vector** length 52.8, 7.38% of its response variance represented; |z| ≥ 3 in 893 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.7 | +13.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.5 | +12.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +12.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.3 | +7.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +1.8 | +7.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.2 | +0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.1 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.0 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +4.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -0.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.6 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | FA complementation group E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:35,452,338-35,467,104 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FAE; previously FACE |
| Gene groups (HGNC) | FA complementation groups; FA core complex |
| Reactome | 6 pathways, smallest: Fanconi Anemia Pathway; PKR-mediated signaling; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HB96](https://www.uniprot.org/uniprotkb/Q9HB96) (Fanconi anemia group E protein):

> As part of the Fanconi anemia (FA) complex functions in DNA cross-links repair. Required for the nuclear accumulation of FANCC and provides a critical bridge between the FA complex and FANCD2.

**Summary**, from NCBI Gene [2178](https://www.ncbi.nlm.nih.gov/gene/2178):

> The Fanconi anemia complementation group (FANC) currently includes FANCA, FANCB, FANCC, FANCD1 (also called BRCA2), FANCD2, FANCE, FANCF, FANCG, FANCI, FANCJ (also called BRIP1), FANCL, FANCM and FANCN (also called PALB2). The previously defined group FANCH is the same as FANCA. Fanconi anemia is a genetically heterogeneous recessive disorder characterized by cytogenetic instability, hypersensitivity to DNA crosslinking agents, increased chromosomal breakage, and defective DNA repair. The …

**Accessions** — [HGNC:3586](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3586) · Entrez [2178](https://www.ncbi.nlm.nih.gov/gene/2178) · UniProt [Q9HB96](https://www.uniprot.org/uniprotkb/Q9HB96) · Ensembl [ENSG00000112039](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112039)

## Data

Gene col 3315: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3315); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3315, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3315]; `tensor/DDL_lfc|DDL_z.npy` [3315]; `embed/gene_vectors.npy` [3315]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3315 or target_col == 3315). Every well: [[FANCE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FANCE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

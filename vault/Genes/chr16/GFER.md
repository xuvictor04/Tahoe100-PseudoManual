---
symbol: "GFER"
type: "gene"
col: 4821
ensembl_id: "ENSG00000127554"
name: "growth factor, augmenter of liver regeneration"
location: "16p13.3"
module: 12
arm: "+"
pooled_cpm: 7.4
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# GFER

*growth factor, augmenter of liver regeneration* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.85× (z +9.2, q 3e-17, up in 25 of 40 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.01× (z +7.3, q 7e-11, up in 25 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0528×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.0981×); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0873×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF579]] (+0.72, fdr 7e-06), [[CASKIN2]] (+0.71, fdr 7e-06), [[SNHG11]] (+0.71, fdr 7e-06); moves opposite to [[TMBIM6]] (-0.58, fdr 1e-05), [[FKBP1A]] (-0.57, fdr 1e-05), [[ITGB1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4821.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.85×** | +9.2 | 3e-17 | 25/40 (HEC-1-A, A549, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +7.3 | 7e-11 | 25/40 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.05×** | +7.3 | 7e-11 | 32/44 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.91×** | +6.8 | 2e-09 | 33/46 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.90×** | +6.7 | 2e-09 | 25/38 (A-172, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +5.6 | 2e-06 | 22/32 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.6 | 2e-06 | 7/12 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +4.1 | 0.003 | 14/35 (KATO III, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.7 | 0.015 | 15/46 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.6 | 0.015 | 10/38 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.041 | 9/47 (A498, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +3.1 | 0.085 | 10/43 (HCT15, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Saquinavir (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0528×); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 1 line (Hs 766T 0.0981×); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0873×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4821. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.30 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -9.3) ⚠ cell-cycle shift, explains ~4% of this change |
| [[CFPAC-1 (line)]] | alt | 5.41 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0528× (z -11.9) |
| [[Hs 766T (line)]] | wt | 6.87 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0981× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 4.54 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0873× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 5.55 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0928× (z -9.1) |
| [[A-427 (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4821), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF579]] | +0.72 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[CASKIN2]] | +0.71 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[WASHC1]] | +0.70 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[DPF2]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[PDRG1]] | +0.67 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[ZNF205]] | +0.66 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[GORASP1]] | +0.65 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[HEIH]] | +0.65 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[THAP3]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[AUP1]] | +0.64 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[NSMCE3]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMBIM6]] | -0.58 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[FKBP1A]] | -0.57 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[ITGB1]] | -0.57 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.54 | -0.47 / -0.61 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.687). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.6, -1.8); signed map (0.5, -12.0). **Vector** length 53.7, 8.04% of its response variance represented; |z| ≥ 3 in 653 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.9 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.4 | +7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.3 | +6.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.1 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.9 | +0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.0 | -0.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.0 | -1.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.8 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | growth factor, augmenter of liver regeneration |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,984,193-1,987,749 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSS, ERV1, ALR, HERV1, HPO1, HPO2 |
| Gene groups (HGNC) | Flavoproteins |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [P55789](https://www.uniprot.org/uniprotkb/P55789) (FAD-linked sulfhydryl oxidase ALR):

> [Isoform 1]: FAD-dependent sulfhydryl oxidase that regenerates the redox-active disulfide bonds in CHCHD4/MIA40, a chaperone essential for disulfide bond formation and protein folding in the mitochondrial intermembrane space. The reduced form of CHCHD4/MIA40 forms a transient intermolecular disulfide bridge with GFER/ERV1, resulting in regeneration of the essential disulfide bonds in CHCHD4/MIA40, while GFER/ERV1 becomes re-oxidized by donating electrons to cytochrome c or molecular oxygen.; …

**Summary**, from NCBI Gene [2671](https://www.ncbi.nlm.nih.gov/gene/2671):

> The hepatotrophic factor designated augmenter of liver regeneration (ALR) is thought to be one of the factors responsible for the extraordinary regenerative capacity of mammalian liver. It has also been called hepatic regenerative stimulation substance (HSS). The gene resides on chromosome 16 in the interval containing the locus for polycystic kidney disease (PKD1). The putative gene product is 42% similar to the scERV1 protein of yeast. The yeast scERV1 gene had been found to be essential for …

**Accessions** — [HGNC:4236](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4236) · Entrez [2671](https://www.ncbi.nlm.nih.gov/gene/2671) · UniProt [P55789](https://www.uniprot.org/uniprotkb/P55789) · Ensembl [ENSG00000127554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127554)

## Data

Gene col 4821: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4821); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4821, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4821]; `tensor/DDL_lfc|DDL_z.npy` [4821]; `embed/gene_vectors.npy` [4821]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4821 or target_col == 4821). Every well: [[GFER — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GFER.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

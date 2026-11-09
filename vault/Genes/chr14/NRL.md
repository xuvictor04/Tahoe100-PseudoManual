---
symbol: "NRL"
type: "gene"
col: 4986
ensembl_id: "ENSG00000129535"
name: "neural retina leucine zipper"
location: "14q11.2-q12"
module: 35
arm: "+"
pooled_cpm: 2.71
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# NRL

*neural retina leucine zipper* — 14q11.2-q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.68× (z +16.4, q 0e+00, up in 32 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.723× (z -5.4, q 4e-05, down in 12 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNPY2-AS1]] (+0.68, fdr 1e-05), [[DDX19A-DT]] (+0.68, fdr 1e-05), [[ATXN7L3-AS1]] (+0.68, fdr 6e-05); moves opposite to [[PHF6]] (-0.55, fdr 2e-04).
> It sits in the **+** arm of [[Module 035]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4986.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.68×** | +16.4 | 0e+00 | 32/34 (NCI-H23, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +10.5 | 4e-23 | 16/35 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +8.2 | 5e-14 | 5/14 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +7.6 | 4e-12 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +6.3 | 4e-08 | 1/4 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.8 | 0.012 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +3.8 | 0.012 | 4/16 (NCI-H23, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.012 | 12/42 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.020 | 4/28 (LoVo, CFPAC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.020 | 4/44 (HOP62, SW1417, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.51×** | +3.5 | 0.029 | 0/26 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.034 | 5/31 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.034 | 2/42 (AsPC-1, NCI-H23) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4986.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.723×** | -5.4 | 4e-05 | 12/44 (RKO, PANC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.648×** | -5.1 | 1e-04 | 8/41 (MIA PaCa-2, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.634×** | -5.0 | 1e-04 | 10/29 (NCI-H23, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.691×** | -4.3 | 0.002 | 6/42 (NCI-H2347, HCT15, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.717×** | -3.9 | 0.011 | 13/44 (PANC-1, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.722×** | -3.8 | 0.012 | 4/44 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.761× | -3.2 | 0.11 | 12/45 (COLO 205, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.769× | -3.1 | 0.13 | 6/46 (RKO, SW480, …) | top dose only | composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.831× | -3.1 | 0.13 | 6/44 (Hs 766T, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4986. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 2.92 | 0 | 1 | — | [[Afatinib (drug)]] 0.05 µM 0.142× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 2.09 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM 0.0514× (z -11.2) |
| [[SW480 (line)]] | alt | 3.48 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.143× (z -8.9) |
| [[A-172 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4986), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNPY2-AS1]] | +0.68 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[DDX19A-DT]] | +0.68 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ATXN7L3-AS1]] | +0.68 | +0.39 / +0.71 | both halves | 6e-05 |  |
| [[RBM15-AS1]] | +0.66 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[MED28-DT]] | +0.66 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[MYLK4]] | +0.65 | +0.37 / +0.66 | both halves | 7e-05 |  |
| [[GPAT4-AS1]] | +0.65 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[SPATA1]] | +0.64 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[C1orf54]] | +0.63 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[PTOV1-AS1]] | +0.63 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[USP34-DT]] | +0.63 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[ALG1L9P]] | +0.62 | +0.49 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF6]] | -0.55 | -0.31 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.663). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (11.7, 20.9); signed map (26.9, -2.6). **Vector** length 43.7, 4.67% of its response variance represented; |z| ≥ 3 in 928 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +16.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +10.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.8 | +2.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +0.8 | +1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +0.8 | +0.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.6 | -3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.6 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.2 | -5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -4.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | neural retina leucine zipper |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2-q12 — chr14:24,078,662-24,115,010 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D14S46E, RP27, NRL-MAF |
| Gene groups (HGNC) | Large MAF bZIP transcription factor family |
| Matched by | ensembl_id |

**Function**, from UniProt [P54845](https://www.uniprot.org/uniprotkb/P54845) (Neural retina-specific leucine zipper protein):

> Acts as a transcriptional activator which regulates the expression of several rod-specific genes, including RHO and PDE6B. Also functions as a transcriptional coactivator, stimulating transcription mediated by the transcription factor CRX and NR2E3. Binds to the rhodopsin promoter in a sequence-specific manner.

**Summary**, from NCBI Gene [4901](https://www.ncbi.nlm.nih.gov/gene/4901):

> This gene encodes a basic motif-leucine zipper transcription factor of the Maf subfamily. The encoded protein is conserved among vertebrates and is a critical intrinsic regulator of photoceptor development and function. Mutations in this gene have been associated with retinitis pigmentosa and retinal degenerative diseases. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8002](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8002) · Entrez [4901](https://www.ncbi.nlm.nih.gov/gene/4901) · UniProt [P54845](https://www.uniprot.org/uniprotkb/P54845) · Ensembl [ENSG00000129535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129535)

## Data

Gene col 4986: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4986); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4986, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4986]; `tensor/DDL_lfc|DDL_z.npy` [4986]; `embed/gene_vectors.npy` [4986]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4986 or target_col == 4986). Every well: [[NRL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

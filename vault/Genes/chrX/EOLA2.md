---
symbol: "EOLA2"
type: "gene"
col: 12324
ensembl_id: "ENSG00000197021"
name: "endothelium and lymphocyte associated ASCH domain 2"
location: "Xq28"
module: 20
arm: "+"
pooled_cpm: 7.19
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# EOLA2

*endothelium and lymphocyte associated ASCH domain 2* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.55× (z +8.6, q 5e-15, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Gallic acid (hydrate) (drug)]] 0.05 µM: 0.511× (z -4.6, q 0.002, down in 29 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (SW1417 0.0876×); [[ULK-101 (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0690×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EOLA1]] (+0.79, fdr 7e-06), [[CRYBB2P1]] (+0.75, fdr 7e-06), [[RPL10]] (+0.69, fdr 7e-06); moves opposite to [[RPL7L1]] (-0.59, fdr 7e-06), [[GPATCH8]] (-0.56, fdr 1e-05), [[LYRM2]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12324.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.55×** | +8.6 | 5e-15 | 41/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.15×** | +6.5 | 3e-08 | 39/44 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.49×** | +6.2 | 1e-07 | 34/46 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.24×** | +5.4 | 7e-06 | 30/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.50×** | +5.3 | 1e-05 | 28/40 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +4.8 | 1e-04 | 23/43 (AsPC-1, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.01×** | +4.7 | 2e-04 | 22/42 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.96×** | +4.6 | 4e-04 | 25/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.78×** | +3.9 | 0.007 | 13/46 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.76×** | +3.8 | 0.007 | 18/47 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +3.2 | 0.061 | 14/46 (LS 180, HEC-1-A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12324.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (SW1417 0.0876×); [[ULK-101 (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0690×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.511×** | -4.6 | 0.002 | 29/46 (Hs 766T, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.551×** | -4.1 | 0.012 | 22/47 (CHP-212, SHP-77, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.564×** | -3.9 | 0.016 | 19/47 (NCI-H661, NCI-H460, …) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | 0.643× | -3.0 | 0.33 | 11/47 (LoVo, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12324. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.8 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 9.76× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 7.16 | 0 | 1 | — | [[ULK-101 (drug)]] 0.05 µM 0.0690× (z -9.0) |
| [[PANC-1 (line)]] | alt | 8.05 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.48× (z +8.5) | — |
| [[SW1417 (line)]] | alt | 9.52 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0876× (z -9.4) |
| [[A-172 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12324), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EOLA1]] | +0.79 | +0.77 / +0.76 | both halves | 7e-06 | STRING 877 |
| [[CRYBB2P1]] | +0.75 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[RPL10]] | +0.69 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[USF1]] | +0.67 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[HFM1]] | +0.67 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | +0.67 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[ANKRD30BL]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[RPL18A]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[TIMM10B]] | +0.65 | +0.72 / +0.58 | both halves | 8e-06 |  |
| [[BCL2L2]] | +0.65 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[ABHD17A]] | +0.64 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[RPS18]] | +0.64 | +0.69 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL7L1]] | -0.59 | -0.64 / -0.60 | both halves | 7e-06 |  |
| [[GPATCH8]] | -0.56 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[LYRM2]] | -0.56 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[ZNF75A]] | -0.55 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[GSPT2]] | -0.55 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[GLRX2]] | -0.54 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[CEBPZ]] | -0.54 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[LARP7]] | -0.52 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[RBMXL1]] | -0.52 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[TMEM70]] | -0.52 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[DHRSX]] | -0.51 | -0.38 / -0.55 | both halves | 7e-05 |  |
| [[BPTF]] | -0.51 | -0.61 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.515). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (8.8, -23.3); signed map (-20.4, -33.4). **Vector** length 62.8, 10.3% of its response variance represented; |z| ≥ 3 in 983 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.55 to 10); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.52 to 10); *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.50 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | -1.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.4 | -2.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.2 | +0.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.5 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.4 | -0.2 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +1.4 | +1.4 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.3 | +1.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +0.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.5 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -2.0 | -4.6 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.7 | -2.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.6 | -2.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | endothelium and lymphocyte associated ASCH domain 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:149,929,527-149,938,700 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CXorf40B |
| Matched by | ensembl_id |

UniProt [Q96DE9](https://www.uniprot.org/uniprotkb/Q96DE9) carries no function annotation.

**Summary**, from NCBI Gene [541578](https://www.ncbi.nlm.nih.gov/gene/541578):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17402](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17402) · Entrez [541578](https://www.ncbi.nlm.nih.gov/gene/541578) · UniProt [Q96DE9](https://www.uniprot.org/uniprotkb/Q96DE9) · Ensembl [ENSG00000197021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197021)

## Data

Gene col 12324: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12324); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12324, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12324]; `tensor/DDL_lfc|DDL_z.npy` [12324]; `embed/gene_vectors.npy` [12324]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12324 or target_col == 12324). Every well: [[EOLA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EOLA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

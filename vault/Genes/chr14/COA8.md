---
symbol: "COA8"
type: "gene"
col: 14971
ensembl_id: "ENSG00000256053"
name: "cytochrome c oxidase assembly factor 8"
location: "14q32.33"
module: 12
arm: "+"
pooled_cpm: 14.43
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# COA8

*cytochrome c oxidase assembly factor 8* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +9.8, q 1e-19, up in 34 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.71× (z +4.8, q 2e-04, up in 36 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 4.34×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.628× (z -4.1, q 0.021, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS35]] (+0.60, fdr 1e-05), [[NOL7]] (+0.58, fdr 1e-05, ⚠ NOL7 in the vector space only through flagged drug-doses), [[MYG1]] (+0.58, fdr 2e-05), [[ZFAND2A]] (+0.56, fdr 2e-05); moves opposite to [[TRIM28]] (-0.57, fdr 8e-05), [[SRSF1]] (-0.50, fdr 2e-04), [[VMA21]] (-0.49, fdr 6e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14971.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 4.34×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.98×** | +9.8 | 1e-19 | 34/38 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +7.9 | 6e-13 | 23/27 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +4.9 | 2e-04 | 25/32 (LS 180, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +4.8 | 2e-04 | 36/47 (BT-474, SW 900, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | 1.42× | +3.2 | 0.17 | 17/42 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.28× | +3.1 | 0.17 | 17/48 (KATO III, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14971.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -4.1 | 0.021 | 29/47 (SW 900, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.733×** | -3.8 | 0.038 | 24/47 (J82, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.885× | -3.5 | 0.073 | 10/48 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.684×** | -3.4 | 0.096 | 21/47 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.487×** | -3.3 | 0.096 | 17/43 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.693× | -3.2 | 0.11 | 17/48 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14971. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.142× (z -9.0) |
| [[J82 (line)]] | alt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.164× (z -9.3) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW480 (line)]] | alt | 17.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.34× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14971), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS35]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[NOL7]] ⚠ | +0.58 | +0.56 / +0.53 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MYG1]] | +0.58 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[ZFAND2A]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[CINP]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[GOLGA7]] | +0.55 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[TSR3]] | +0.55 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[PFDN4]] | +0.53 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[ADGRL3-AS1]] | +0.53 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[SSNA1]] | +0.53 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[ACAP2]] | +0.53 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[NACA4P]] ⚠ | +0.52 | +0.44 / +0.58 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RWDD1]] | +0.52 | +0.53 / +0.37 | both halves | 8e-05 |  |
| [[CAMLG]] | +0.51 | +0.43 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM28]] | -0.57 | -0.37 / -0.60 | both halves | 8e-05 |  |
| [[SRSF1]] | -0.50 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[VMA21]] | -0.49 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[HELLS]] | -0.49 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[H2AZ2]] | -0.47 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[SKA2]] | -0.47 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[ARGLU1]] | -0.46 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[SNRPG]] | -0.45 | -0.40 / -0.52 | both halves | 4e-05 |  |
| [[FANCL]] | -0.45 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[TYMS]] | -0.45 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[EIF5A]] | -0.44 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[B4GAT1-DT]] | -0.44 | -0.27 / -0.46 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.420). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-5.1, -50.4); signed map (-17.3, -6.1). **Vector** length 49.4, 8.27% of its response variance represented; |z| ≥ 3 in 533 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.1 | +4.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.5 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.3 | +2.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.3 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | +0.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -4.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.0 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.7 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -3.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.2 | +0.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.1 | +0.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.1 | +0.7 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase assembly factor 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:103,562,960-103,607,523 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2562, APOP-1; previously C14orf153, APOPT1 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IL0](https://www.uniprot.org/uniprotkb/Q96IL0) (Cytochrome c oxidase assembly factor 8):

> Required for cytochrome c complex (COX) IV assembly and function Protects COX assembly from oxidation-induced degradation, COX being the terminal component of the mitochondrial respiratory chain.

**Summary**, from NCBI Gene [84334](https://www.ncbi.nlm.nih.gov/gene/84334):

> This gene encodes a protein that localizes to the mitochondria, where it stimulates the release of cytochrome c, thereby promoting programmed cell death. Mutations in this gene have been found in individuals with mitochondrial complex IV deficiency. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2014]

**Accessions** — [HGNC:20492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20492) · Entrez [84334](https://www.ncbi.nlm.nih.gov/gene/84334) · UniProt [Q96IL0](https://www.uniprot.org/uniprotkb/Q96IL0) · Ensembl [ENSG00000256053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256053)

## Data

Gene col 14971: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14971); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14971, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14971]; `tensor/DDL_lfc|DDL_z.npy` [14971]; `embed/gene_vectors.npy` [14971]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14971 or target_col == 14971). Every well: [[COA8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COA8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

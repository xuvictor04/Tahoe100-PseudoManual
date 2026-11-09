---
symbol: "C6orf47"
type: "gene"
col: 12874
ensembl_id: "ENSG00000204439"
name: "chromosome 6 open reading frame 47"
location: "6p21.33"
module: 7
arm: "+"
pooled_cpm: 6.56
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# C6orf47

*chromosome 6 open reading frame 47* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.32× (z +10.6, q 2e-23, up in 35 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.52× (z +4.3, q 0.003, up in 18 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.487× (z -7.9, q 2e-12, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INTS5]] (+0.72, fdr 7e-06), [[THAP7]] (+0.68, fdr 7e-06), [[TMEM115]] (+0.68, fdr 7e-06); moves opposite to [[USP45]] (-0.58, fdr 2e-04), [[FAM81A]] (-0.55, fdr 7e-04), [[FUT10]] (-0.55, fdr 0.002, ⚠ one half only (not replicated)), [[ME2]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12874.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.32×** | +10.6 | 2e-23 | 35/48 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.5 | 0.002 | 14/37 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.52×** | +4.3 | 0.003 | 18/45 (LoVo, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.45×** | +4.0 | 0.008 | 13/47 (J82, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.40×** | +3.7 | 0.029 | 14/46 (J82, CFPAC-1, …) | two highest doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.59×** | +3.6 | 0.032 | 7/44 (J82, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.40×** | +3.5 | 0.033 | 1/12 (SW1417) | top dose only | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.044 | 6/44 (Panc 03.27, hTERT-HPNE, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.072 | 6/41 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Larotrectinib (drug)]] 0.05 µM |  | **1.34×** | +3.2 | 0.079 | 2/47 (KATO III, C32) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.33× | +3.1 | 0.11 | 7/44 (Panc 03.27, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.32× | +3.0 | 0.12 | 13/47 (J82, SNU-423, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12874.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.487×** | -7.9 | 2e-12 | 35/46 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.536×** | -6.8 | 3e-09 | 32/47 (SW48, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.588×** | -5.8 | 1e-06 | 24/42 (SNU-423, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.636×** | -4.9 | 1e-04 | 21/46 (hTERT-HPNE, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.668×** | -4.4 | 0.001 | 19/46 (LOX-IMVI, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.692×** | -4.0 | 0.005 | 14/47 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.696×** | -4.0 | 0.006 | 16/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Baicalin (drug)]] 5 µM |  | **0.780×** | -3.9 | 0.008 | 8/48 (HEC-1-A, SW480, …) | top dose only | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.729×** | -3.3 | 0.054 | 18/42 (SK-MEL-2, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12874. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 8.25 | 0 | 1 | — | [[Dorzolamide (hydrochloride) (drug)]] 0.05 µM 0.0945× (z -8.6) |
| [[C-33 A (line)]] | alt | 7.78 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0778× (z -8.5) |
| [[HS-578T (line)]] | alt | 6.47 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.115× (z -8.7) |
| [[HT-29 (line)]] | alt | 7.87 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 3.57 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0718× (z -8.9) |
| [[PANC-1 (line)]] | alt | 6.27 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[RKO (line)]] | wt | 7.66 | 0 | 1 | — | [[Rifaximin (drug)]] 5 µM 0.0559× (z -11.1) |
| [[SNU-423 (line)]] | alt | 7.48 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0739× (z -9.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 5.02 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0699× (z -8.7) |
| [[A-172 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12874), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS5]] | +0.72 | +0.69 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[THAP7]] | +0.68 | +0.58 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[TMEM115]] | +0.68 | +0.60 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[TBCC]] | +0.65 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[HPS6]] | +0.64 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[ZNF513]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[MGAT2]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[GCC1]] | +0.61 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[KTI12]] | +0.61 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[OXLD1]] | +0.59 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[ZNF646]] | +0.59 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[VPS18]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP45]] | -0.58 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[FAM81A]] | -0.55 | -0.21 / -0.62 | both halves | 7e-04 |  |
| [[FUT10]] | -0.55 | -0.14 / -0.64 | ⚠ one half (not replicated) | 0.002 |  |
| [[ME2]] | -0.53 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[VPS36]] | -0.49 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[RCAN3]] | -0.49 | -0.31 / -0.56 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-46.0, -0.4); signed map (-5.0, -25.4). **Vector** length 49.9, 6.25% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -0.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.1 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | -1.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +1.6 | +10.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +4.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.0 | +0.9 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.3 | -1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -4.2 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.9 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -0.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 6 open reading frame 47 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,658,298-31,660,778 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D6S53E, G4 |
| Matched by | ensembl_id |

UniProt [O95873](https://www.uniprot.org/uniprotkb/O95873) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:19076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19076) · Entrez [57827](https://www.ncbi.nlm.nih.gov/gene/57827) · UniProt [O95873](https://www.uniprot.org/uniprotkb/O95873) · Ensembl [ENSG00000204439](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204439)

## Data

Gene col 12874: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12874); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12874, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12874]; `tensor/DDL_lfc|DDL_z.npy` [12874]; `embed/gene_vectors.npy` [12874]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12874 or target_col == 12874). Every well: [[C6orf47 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C6orf47.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

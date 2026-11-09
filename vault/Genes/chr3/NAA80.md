---
symbol: "NAA80"
type: "gene"
col: 14361
ensembl_id: "ENSG00000243477"
name: "N-alpha-acetyltransferase 80, NatH catalytic subunit"
location: "3p21.31"
module: 88
arm: "-"
pooled_cpm: 2.88
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# NAA80

*N-alpha-acetyltransferase 80, NatH catalytic subunit* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.77× (z +4.7, q 0.002, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.480× (z -6.3, q 1e-07, down in 23 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPOR]] (+0.64, fdr 1e-05), [[OCEL1]] (+0.62, fdr 1e-04), [[ANKRD9]] (+0.60, fdr 2e-05); moves opposite to [[RGS5]] (-0.60, fdr 3e-05), [[ARMCX4]] (-0.54, fdr 2e-04), [[TRIM44]] (-0.54, fdr 3e-05).
> It sits in the **-** arm of [[Module 088]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14361.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +4.7 | 0.002 | 0/5 | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +4.0 | 0.016 | 5/17 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.65× | +3.0 | 0.45 | 3/14 (SW1417, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14361.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.480×** | -6.3 | 1e-07 | 23/44 (NCI-H2347, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.638×** | -5.5 | 1e-05 | 22/34 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.543×** | -5.3 | 2e-05 | 21/39 (PANC-1, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.531×** | -5.2 | 2e-05 | 17/39 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.334×** | -4.9 | 9e-05 | 18/35 (J82, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.580×** | -4.7 | 2e-04 | 14/32 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.606×** | -4.1 | 0.004 | 17/41 (A-172, SW1417, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.639×** | -3.9 | 0.008 | 13/44 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.441×** | -3.7 | 0.014 | 14/32 (NCI-H460, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.692×** | -3.2 | 0.082 | 9/41 (NCI-H2030, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14361. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.80 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0539× (z -12.7) |
| [[A-172 (line)]] | wt | 4.96 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0649× (z -10.9) |
| [[NCI-H661 (line)]] | alt | 1.66 | 0 | 1 | — | [[Uridine (drug)]] 5 µM 0.618× (z -12.2) |
| [[A-427 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.968 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14361), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPOR]] | +0.64 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[OCEL1]] | +0.62 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[ANKRD9]] | +0.60 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[EFNA3]] | +0.58 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[HYAL3]] | +0.58 | +0.58 / +0.61 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TRPT1]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[RRAS]] | +0.57 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[AGPAT2]] | +0.55 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[B3GAT3]] | +0.55 | +0.29 / +0.50 | both halves | 3e-04 |  |
| [[CIB1]] | +0.55 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[PI4KAP2]] | +0.55 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[SH3D21]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[IGSF8]] | +0.54 | +0.47 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS5]] | -0.60 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[ARMCX4]] | -0.54 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[TRIM44]] | -0.54 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[DPP8]] | -0.53 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[KRR1]] | -0.51 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[MATR3-1]] | -0.51 | -0.36 / -0.58 | both halves | 9e-05 |  |
| [[GTF2H1]] | -0.51 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[CLHC1]] | -0.51 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[ECHDC1]] | -0.50 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[DNAJC7]] | -0.50 | -0.14 / -0.55 | ⚠ one half (not replicated) | 0.002 |  |
| [[PAWR]] | -0.50 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[SEMA6A-AS1]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[ZMYM4]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **-** arm (projection on the module's main direction -0.557). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (3.5, -4.1); signed map (-30.6, 14.5). **Vector** length 47.5, 6.07% of its response variance represented; |z| ≥ 3 in 836 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.4 | +4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.9 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +1.7 | +2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.1 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +2.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.5 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.9 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.2 | -5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -3.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.8 | -4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -4.1 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.3 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | N-alpha-acetyltransferase 80, NatH catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:50,296,402-50,299,416 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FUS2; previously NAT6 |
| Gene groups (HGNC) | N-alpha-acetyltransferase subunits; GCN5 related N-acetyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93015](https://www.uniprot.org/uniprotkb/Q93015) (N-alpha-acetyltransferase 80):

> N-alpha-acetyltransferase that specifically mediates the acetylation of the acidic amino terminus of processed forms of beta- and gamma-actin (ACTB and ACTG, respectively). N-terminal acetylation of processed beta- and gamma-actin regulates actin filament depolymerization and elongation. In vivo, preferentially displays N-terminal acetyltransferase activity towards acid N-terminal sequences starting with Asp-Asp-Asp and Glu-Glu-Glu. In vitro, shows high activity towards Met-Asp-Glu-Leu and …

**Summary**, from NCBI Gene [24142](https://www.ncbi.nlm.nih.gov/gene/24142):

> This gene encodes a member of the N-acetyltransferase family. N-acetyltransferases modify proteins by transferring acetyl groups from acetyl CoA to the N-termini of protein substrates. The encoded protein is a cytoplasmic N-acetyltransferase with a substrate specificity for proteins with an N-terminal methionine. This gene is located in the tumor suppressor gene region on chromosome 3p21.3 and the encoded protein may play a role in cancer. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:30252](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30252) · Entrez [24142](https://www.ncbi.nlm.nih.gov/gene/24142) · UniProt [Q93015](https://www.uniprot.org/uniprotkb/Q93015) · Ensembl [ENSG00000243477](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243477)

## Data

Gene col 14361: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14361); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14361, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14361]; `tensor/DDL_lfc|DDL_z.npy` [14361]; `embed/gene_vectors.npy` [14361]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14361 or target_col == 14361). Every well: [[NAA80 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAA80.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

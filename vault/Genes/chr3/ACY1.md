---
symbol: "ACY1"
type: "gene"
col: 14384
ensembl_id: "ENSG00000243989"
name: "aminoacylase 1"
location: "3p21.2"
module: 92
arm: "+"
pooled_cpm: 5.24
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# ACY1

*aminoacylase 1* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.49× (z +10.6, q 2e-23, up in 21 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.36× (z +3.7, q 0.032, up in 13 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.428× (z -7.2, q 4e-10, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPRED1]] (+0.60, fdr 1e-05), [[SPRY4-AS1]] (+0.59, fdr 1e-05), [[AGMAT]] (+0.58, fdr 1e-05); moves opposite to [[TMEM167B]] (-0.52, fdr 3e-05), [[DYNC1LI2]] (-0.44, fdr 1e-04), [[CD47]] (-0.43, fdr 7e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14384.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.49×** | +10.6 | 2e-23 | 21/24 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +8.1 | 2e-13 | 9/11 (NCI-H2030, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +5.6 | 4e-06 | 10/15 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.032 | 13/44 (A-427, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.46× | +3.2 | 0.14 | 6/43 (SW1417, A-427, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, none with an alert; shown: the 15 strongest. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14384.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.428×** | -7.2 | 4e-10 | 32/46 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.583×** | -6.5 | 3e-08 | 25/38 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.481×** | -6.2 | 1e-07 | 27/46 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.554×** | -5.0 | 9e-05 | 20/44 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.560×** | -4.9 | 1e-04 | 19/43 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.566×** | -4.8 | 1e-04 | 23/45 (LS 180, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.588×** | -4.5 | 6e-04 | 20/44 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.612×** | -4.2 | 0.002 | 18/45 (SW48, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.621×** | -4.0 | 0.003 | 16/43 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.639×** | -4.0 | 0.003 | 14/46 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.637×** | -3.7 | 0.013 | 16/43 (HT-29, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.633×** | -3.6 | 0.016 | 16/45 (MIA PaCa-2, LS 180, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.655×** | -3.6 | 0.016 | 8/45 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.642×** | -3.5 | 0.017 | 13/42 (A498, J82, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.461×** | -3.4 | 0.023 | 11/40 (A-427, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14384. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.34 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.3) |
| [[A498 (line)]] | wt | 3.66 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0840× (z -10.1) |
| [[HOP62 (line)]] | alt | 3.23 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0709× (z -9.5) |
| [[J82 (line)]] | alt | 4.61 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0622× (z -9.5) |
| [[LoVo (line)]] | wt | 5.44 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0742× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 9.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 4.29 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0544× (z -9.1) |
| [[SNU-1 (line)]] | wt | 7.66 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0384× (z -9.3) |
| [[A-172 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14384), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRED1]] | +0.60 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SPRY4-AS1]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[AGMAT]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[LINC00467]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[PALD1]] | +0.57 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[SPRY2]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[LINC00941]] | +0.55 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[SHH]] | +0.55 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[SLC25A45]] | +0.55 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[CASC19]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SPRY4]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[DMAC1]] | +0.53 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM167B]] | -0.52 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[DYNC1LI2]] | -0.44 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[CD47]] | -0.43 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[TOM1]] | -0.43 | -0.50 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.580). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.5, 4.3); signed map (10.2, 48.1). **Vector** length 55.2, 9.01% of its response variance represented; |z| ≥ 3 in 723 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.2 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +2.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +0.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +5.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.6 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +0.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.1 | +1.6 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.0 | +2.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -7.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -3.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | aminoacylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:51,983,340-51,989,197 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | M20 metallopeptidases |
| Reactome | 6 pathways, smallest: Aflatoxin activation and detoxification; Paracetamol ADME; Metabolic disorders of biological oxidation enzymes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03154](https://www.uniprot.org/uniprotkb/Q03154) (Aminoacylase-1):

> Aminoacylase involved in the hydrolysis of N-acetylated and N-formylated amino acids. May act sequentially with APEH in the degradation of N-acylated peptides: APEH first cleaves N-acylaminoacids from N-acylated peptides, then ACY1 further hydrolyzes the N-acylaminoacid into free aminoacid and a carboxylate.

**Summary**, from NCBI Gene [95](https://www.ncbi.nlm.nih.gov/gene/95):

> This gene encodes a cytosolic, homodimeric, zinc-binding enzyme that catalyzes the hydrolysis of acylated L-amino acids to L-amino acids and an acyl group, and has been postulated to function in the catabolism and salvage of acylated amino acids. This gene is located on chromosome 3p21.1, a region reduced to homozygosity in small-cell lung cancer (SCLC), and its expression has been reported to be reduced or undetectable in SCLC cell lines and tumors. The amino acid sequence of human …

**Accessions** — [HGNC:177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:177) · Entrez [95](https://www.ncbi.nlm.nih.gov/gene/95) · UniProt [Q03154](https://www.uniprot.org/uniprotkb/Q03154) · Ensembl [ENSG00000243989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243989)

## Data

Gene col 14384: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14384); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14384, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14384]; `tensor/DDL_lfc|DDL_z.npy` [14384]; `embed/gene_vectors.npy` [14384]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14384 or target_col == 14384). Every well: [[ACY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

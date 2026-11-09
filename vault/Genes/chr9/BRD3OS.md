---
symbol: "BRD3OS"
type: "gene"
col: 13999
ensembl_id: "ENSG00000235106"
name: "BRD3 opposite strand"
location: "9q34.2"
module: 50
arm: "+"
pooled_cpm: 6.56
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# BRD3OS

*BRD3 opposite strand* — 9q34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.36× (z +9.7, q 1e-19, up in 23 of 29 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.47× (z +6.2, q 1e-07, up in 18 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.571× (z -8.9, q 3e-16, down in 27 of 42 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM210B]] (+0.66, fdr 1e-05), [[BAIAP2-DT]] (+0.62, fdr 2e-05), [[PCYOX1]] (+0.57, fdr 2e-05); moves opposite to [[IL34]] (-0.44, fdr 2e-04), [[BTN2A3P]] (-0.42, fdr 4e-04), [[ZNF547]] (-0.42, fdr 8e-04, ⚠ not reproduced).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13999.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.36×** | +9.7 | 1e-19 | 23/29 (SW1417, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +9.7 | 1e-19 | 7/13 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +6.2 | 1e-07 | 18/48 (A498, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +5.9 | 5e-07 | 23/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.60×** | +5.3 | 1e-05 | 19/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +5.0 | 6e-05 | 12/20 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.0 | 0.005 | 13/35 (HOP62, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.31× | +3.0 | 0.15 | 8/47 (PANC-1, RPMI-7951, …) | rises with dose | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.31× | +3.0 | 0.15 | 8/41 (A-427, LS 180, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13999.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.571×** | -8.9 | 3e-16 | 27/42 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.462×** | -8.3 | 3e-14 | 28/45 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.502×** | -7.7 | 2e-12 | 31/47 (LOX-IMVI, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.520×** | -7.3 | 3e-11 | 27/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.558×** | -6.5 | 7e-09 | 24/43 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.620×** | -5.4 | 8e-06 | 24/44 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.629×** | -5.2 | 2e-05 | 21/46 (A549, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.631×** | -5.2 | 2e-05 | 19/46 (MIA PaCa-2, LoVo, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.691×** | -4.1 | 0.002 | 15/46 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.731×** | -3.5 | 0.025 | 15/47 (SW 1271, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.751×** | -3.2 | 0.067 | 13/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.755×** | -3.2 | 0.076 | 10/47 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.763× | -3.0 | 0.11 | 12/47 (NCI-H460, LoVo, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13999. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 12.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0963× (z -12.8) |
| [[A-172 (line)]] | wt | 10.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.172× (z -8.8) |
| [[BT-474 (line)]] | alt | 7.66 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0637× (z -10.9) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 9.55 | 0 | 1 | — | [[Macitentan (drug)]] 5 µM 0.177× (z -9.3) |
| [[Hs 766T (line)]] | wt | 7.37 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0632× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 7.38 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.109× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 6.55 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -8.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 5.15 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.05 µM 0.0620× (z -8.9) |
| [[SW 900 (line)]] | alt | 5.28 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0738× (z -8.9) |
| [[A-427 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13999), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM210B]] | +0.66 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[BAIAP2-DT]] | +0.62 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[PCYOX1]] | +0.57 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[ABRAXAS1]] | +0.56 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[COMMD9]] | +0.56 | +0.43 / +0.55 | both halves | 4e-05 |  |
| [[NAGA]] | +0.55 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[BCKDK]] | +0.54 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[ARSA]] | +0.54 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[VAMP3]] | +0.53 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[EXT2]] | +0.53 | +0.47 / +0.31 | both halves | 2e-04 |  |
| [[C2orf68]] | +0.53 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[GRN]] | +0.52 | +0.46 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL34]] | -0.44 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[BTN2A3P]] | -0.42 | -0.35 / -0.24 | both halves | 4e-04 |  |
| [[ZNF547]] | -0.42 | -0.41 / -0.19 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.506). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.7, -17.5); signed map (-52.3, -10.1). **Vector** length 48.5, 5.78% of its response variance represented; |z| ≥ 3 in 892 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.4 | +6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.2 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.1 | +5.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | -1.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +3.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.3 | +1.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.2 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -8.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -6.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.5 | -8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +0.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -0.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.4 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | BRD3 opposite strand |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.2 — chr9:134,025,481-134,034,666 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35348, bA374P20.3, SERLOC; previously NCRNA00094, LINC00094 |
| Matched by | ensembl_id |

UniProt [A0A1B0GUI7](https://www.uniprot.org/uniprotkb/A0A1B0GUI7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:24742](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24742) · Entrez [266655](https://www.ncbi.nlm.nih.gov/gene/266655) · UniProt [A0A1B0GUI7](https://www.uniprot.org/uniprotkb/A0A1B0GUI7) · Ensembl [ENSG00000235106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235106)

## Data

Gene col 13999: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13999); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13999, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13999]; `tensor/DDL_lfc|DDL_z.npy` [13999]; `embed/gene_vectors.npy` [13999]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13999 or target_col == 13999). Every well: [[BRD3OS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRD3OS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

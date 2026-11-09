---
symbol: "MFSD3"
type: "gene"
col: 9522
ensembl_id: "ENSG00000167700"
name: "solute carrier family 33 member 2"
location: "8q24.3"
module: 58
arm: "+"
pooled_cpm: 2.02
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# MFSD3

*solute carrier family 33 member 2* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.13× (z +9.0, q 1e-16, up in 8 of 12 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.303× (z -7.7, q 1e-11, down in 29 of 35 measured lines).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDDC3]] (+0.66, fdr 1e-05), [[ANTKMT]] (+0.64, fdr 6e-05), [[CDK5]] (+0.63, fdr 4e-05); moves opposite to [[DVL3]] (-0.51, fdr 5e-04), [[SNHG22]] (-0.50, fdr 6e-04), [[UNKL]] (-0.47, fdr 1e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9522.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **4.13×** | +9.0 | 1e-16 | 8/12 (A498, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.11×** | +7.6 | 6e-12 | 1/2 (A498) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.34×** | +5.0 | 1e-04 | 2/3 (A498, NCI-H2030) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **2.04×** | +4.5 | 9e-04 | 5/12 (LS 180, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +4.4 | 1e-03 | 6/12 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.5 | 0.038 | 6/23 (PANC-1, HT-29, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.87×** | +3.4 | 0.060 | 5/17 (HEC-1-A, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.63× | +3.1 | 0.15 | 7/37 (CFPAC-1, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9522.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.303×** | -7.7 | 1e-11 | 29/35 (NCI-H2030, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.312×** | -7.5 | 2e-11 | 28/42 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.394×** | -6.0 | 4e-07 | 22/32 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.359×** | -3.4 | 0.082 | 8/32 (BT-474, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.613× | -3.2 | 0.17 | 11/44 (A549, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.617× | -3.1 | 0.17 | 15/36 (J82, BT-474, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.626× | -3.0 | 0.20 | 7/28 (LoVo, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.39 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9522. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 4.41 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0449× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 6.31 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0707× (z -9.8) |
| [[SW1417 (line)]] | alt | 3.23 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0434× (z -9.7) |
| [[A-172 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.732 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.697 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.910 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.567 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.747 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.945 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.600 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.570 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.818 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.899 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.923 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.881 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.626 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.909 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.921 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9522), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 19 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDDC3]] | +0.66 | +0.51 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[ANTKMT]] | +0.64 | +0.38 / +0.73 | both halves | 6e-05 |  |
| [[CDK5]] | +0.63 | +0.40 / +0.65 | both halves | 4e-05 |  |
| [[NTHL1]] | +0.62 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[NDUFA7]] | +0.61 | +0.30 / +0.71 | both halves | 2e-04 |  |
| [[FAM104B]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SLC37A4]] | +0.61 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[DMAC1]] | +0.61 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[MTLN]] ⚠ | +0.60 | +0.32 / +0.68 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[NUDT8]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[MRPL57]] | +0.59 | +0.30 / +0.65 | both halves | 2e-04 |  |
| [[NDUFAF3]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[HMBS]] | +0.59 | +0.45 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DVL3]] | -0.51 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[SNHG22]] | -0.50 | -0.22 / -0.53 | both halves | 6e-04 |  |
| [[UNKL]] | -0.47 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[CROCC]] | -0.46 | -0.01 / -0.50 | ⚠ one half (not replicated) | 0.008 |  |
| [[UBE2A]] | -0.45 | -0.04 / -0.52 | ⚠ one half (not replicated) | 0.005 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-48.5, -13.2); signed map (-21.4, -4.9). **Vector** length 36.4, 4.63% of its response variance represented; |z| ≥ 3 in 712 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | +1.6 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.2 | +2.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.1 | +1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +1.1 | +3.1 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.2 |
|  | [[Omeprazole (drug)]] 0.5 µM |  | +0.8 | +3.0 |
|  | [[Flutamide (drug)]] 5 µM |  | +0.8 | +2.1 |
|  | [[Bendamustine (drug)]] 5 µM |  | +0.8 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -7.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -6.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 33 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,509,070-144,511,213 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MFSD3 |
| Gene groups (HGNC) | Solute carrier family 33 |
| Matched by | ensembl_id |

UniProt [Q96ES6](https://www.uniprot.org/uniprotkb/Q96ES6) carries no function annotation.

**Summary**, from NCBI Gene [113655](https://www.ncbi.nlm.nih.gov/gene/113655):

> Predicted to enable transmembrane transporter activity. Predicted to be involved in transmembrane transport. Predicted to be located in plasma membrane. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25157) · Entrez [113655](https://www.ncbi.nlm.nih.gov/gene/113655) · UniProt [Q96ES6](https://www.uniprot.org/uniprotkb/Q96ES6) · Ensembl [ENSG00000167700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167700)

## Data

Gene col 9522: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9522); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9522, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9522]; `tensor/DDL_lfc|DDL_z.npy` [9522]; `embed/gene_vectors.npy` [9522]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9522 or target_col == 9522). Every well: [[MFSD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFSD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

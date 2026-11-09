---
symbol: "ZBTB3"
type: "gene"
col: 11715
ensembl_id: "ENSG00000185670"
name: "zinc finger and BTB domain containing 3"
location: "11q12.3"
module: 119
arm: "+"
pooled_cpm: 4.11
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# ZBTB3

*zinc finger and BTB domain containing 3* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 1.43× (z +4.0, q 0.044, up in 5 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.551× (z -6.5, q 4e-08, down in 20 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KAT5]] (+0.61, fdr 1e-05), [[TIMM29]] (+0.61, fdr 1e-05), [[TAF6L]] (+0.58, fdr 1e-05, ⚠ same locus), [[CWC25]] (+0.57, fdr 2e-05); moves opposite to [[GLS]] (-0.54, fdr 4e-05), [[EPB41L2]] (-0.52, fdr 2e-05), [[HPRT1]] (-0.48, fdr 4e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11715.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.044 | 5/47 (HS-578T, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11715.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.551×** | -6.5 | 4e-08 | 20/44 (LOX-IMVI, LoVo, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.552×** | -6.2 | 1e-07 | 17/37 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.612×** | -5.4 | 2e-05 | 16/47 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.642×** | -4.8 | 2e-04 | 16/36 (LoVo, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.643×** | -4.8 | 2e-04 | 11/38 (A-172, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.665×** | -4.4 | 8e-04 | 13/46 (A-172, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.670×** | -4.4 | 1e-03 | 13/47 (HS-578T, J82, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.679×** | -4.2 | 0.002 | 11/44 (SNU-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.693×** | -4.0 | 0.004 | 14/38 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.714×** | -3.5 | 0.024 | 13/31 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.806×** | -3.3 | 0.045 | 10/46 (SW480, H4, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.740×** | -3.3 | 0.047 | 13/45 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.743×** | -3.1 | 0.080 | 8/45 (SW 1271, hTERT-HPNE, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.818×** | -3.1 | 0.080 | 14/38 (PANC-1, J82, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11715. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.55 | 0 | 2 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0850× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 2.59 | 0 | 1 | — | [[Cinacalcet (drug)]] 0.5 µM 0.0662× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 2.88 | 0 | 1 | — | [[5-Fluorouracil (drug)]] 0.05 µM 0.0506× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 4.56 | 0 | 1 (1 ⚠) | — | [[Trifluridine (drug)]] 0.5 µM 0.0607× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 5.37 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0778× (z -9.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[PANC-1 (line)]] | alt | 5.91 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -10.1) |
| [[SW480 (line)]] | alt | 6.63 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11715), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KAT5]] | +0.61 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[TIMM29]] | +0.61 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[TAF6L]] | +0.58 | +0.56 / +0.52 | both halves | 1e-05 | ⚠ same locus (17.2 kb: neighbours can correlate without regulation) |
| [[CWC25]] | +0.57 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[SMIM7]] | +0.56 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[PRPF6]] | +0.55 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[KBTBD4]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[DCTN4]] | +0.55 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[RNF40]] | +0.55 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[ZSWIM1]] | +0.54 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[MCRS1]] | +0.54 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[NRDE2]] | +0.54 | +0.58 / +0.41 | both halves | 4e-05 |  |
| [[ALKBH4]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLS]] | -0.54 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[EPB41L2]] | -0.52 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[HPRT1]] | -0.48 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[STK26]] | -0.48 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[AP1S2]] | -0.47 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[OSBPL10]] | -0.47 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[IPO7]] | -0.46 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[SRPK1]] | -0.46 | -0.39 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.7, -5.7); signed map (-8.9, -11.4). **Vector** length 43.8, 4.56% of its response variance represented; |z| ≥ 3 in 896 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +4.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +0.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.0 | -0.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.5 | -4.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.2 | -2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.0 | -4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,748,319-62,754,184 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23392 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5J0](https://www.uniprot.org/uniprotkb/Q9H5J0) (Zinc finger and BTB domain-containing protein 3):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [79842](https://www.ncbi.nlm.nih.gov/gene/79842):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22918](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22918) · Entrez [79842](https://www.ncbi.nlm.nih.gov/gene/79842) · UniProt [Q9H5J0](https://www.uniprot.org/uniprotkb/Q9H5J0) · Ensembl [ENSG00000185670](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185670)

## Data

Gene col 11715: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11715); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11715, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11715]; `tensor/DDL_lfc|DDL_z.npy` [11715]; `embed/gene_vectors.npy` [11715]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11715 or target_col == 11715). Every well: [[ZBTB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "CCDC157"
type: "gene"
col: 11957
ensembl_id: "ENSG00000187860"
name: "coiled-coil domain containing 157"
location: "22q12.2"
module: 205
arm: "+"
pooled_cpm: 3.64
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/205"]
generated_by: "tahoemap"
---

# CCDC157

*coiled-coil domain containing 157* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.42× (z +12.3, q 4e-32, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.699× (z -5.1, q 2e-04, down in 24 of 44 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP210]] (+0.74, fdr 7e-06), [[DRC3]] (+0.74, fdr 7e-06), [[KIF9]] (+0.71, fdr 7e-06); moves opposite to [[TNPO1]] (-0.47, fdr 2e-04), [[ACSL4]] (-0.43, fdr 8e-04, ⚠ one half only (not replicated)), [[CCND2]] (-0.41, fdr 7e-04), [[HSPA4]] (-0.41, fdr 2e-04).
> It is in [[Module 205]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11957.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.42×** | +12.3 | 4e-32 | 43/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.16×** | +10.9 | 2e-25 | 27/36 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.43×** | +8.9 | 1e-16 | 33/44 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.36×** | +8.6 | 1e-15 | 30/45 (COLO 205, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +6.2 | 8e-08 | 5/18 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.92×** | +5.9 | 3e-07 | 0/7 | inconsistent across doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.9 | 3e-07 | 14/36 (NCI-H1792, LS 180, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +5.3 | 1e-05 | 19/41 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.61×** | +4.4 | 7e-04 | 15/45 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.48×** | +3.9 | 0.005 | 15/43 (HOP62, NCI-H1792, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.46×** | +3.8 | 0.009 | 7/41 (HOP62, PANC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.021 | 7/34 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.40×** | +3.4 | 0.033 | 9/29 (PANC-1, J82, …) | two highest doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.066 | 4/42 (LoVo, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.40×** | +3.1 | 0.075 | 1/10 (HOP62) | inconsistent across doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11957.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.699×** | -5.1 | 2e-04 | 24/44 (Panc 03.27, hTERT-HPNE, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | **0.670×** | -4.0 | 0.017 | 11/45 (CFPAC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.683×** | -3.8 | 0.021 | 14/44 (A-172, BT-474, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.766×** | -3.8 | 0.021 | 11/42 (LOX-IMVI, A498, …) | rises with dose |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | 0.718× | -3.3 | 0.10 | 10/45 (C-33 A, SW 900, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.722× | -3.3 | 0.10 | 13/45 (Panc 03.27, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.739× | -3.0 | 0.19 | 10/40 (SW480, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11957. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 8.09 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.102× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11957), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP210]] | +0.74 | +0.71 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[DRC3]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[KIF9]] | +0.71 | +0.75 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[RNF213-AS1]] | +0.70 | +0.69 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[TMEM67]] | +0.69 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ZNF487]] | +0.61 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[CFAP69]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[MOK]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 | **novel candidate** |
| [[RFX1]] | +0.59 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[ANKRD42]] | +0.57 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[FOSB]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[C16orf46]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNPO1]] | -0.47 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[ACSL4]] | -0.43 | -0.20 / -0.53 | ⚠ one half (not replicated) | 8e-04 |  |
| [[CCND2]] | -0.41 | -0.20 / -0.39 | both halves | 7e-04 |  |
| [[HSPA4]] | -0.41 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[GSR]] | -0.41 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[ABHD13]] | -0.41 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[PAQR3]] | -0.41 | -0.31 / -0.34 | both halves | 2e-04 |  |
| [[TSEN15]] | -0.40 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[NAPB]] | -0.40 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[USP46]] | -0.40 | -0.29 / -0.32 | both halves | 2e-04 |  |
| [[CCNY-AS1]] | -0.40 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[GAB3]] | -0.40 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[NAE1]] | -0.40 | -0.37 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 205]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.842). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-42.1, 20.8); signed map (-1.6, 7.5). **Vector** length 56.4, 8.04% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +12.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.2 | +10.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.0 | +8.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | +1.9 | +4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +2.5 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.1 | +0.5 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +1.1 | +2.3 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +1.1 | +2.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.6 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -3.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.9 | -2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 157 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:30,356,635-30,378,673 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q569K6](https://www.uniprot.org/uniprotkb/Q569K6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:33854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33854) · Entrez [550631](https://www.ncbi.nlm.nih.gov/gene/550631) · UniProt [Q569K6](https://www.uniprot.org/uniprotkb/Q569K6) · Ensembl [ENSG00000187860](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187860)

## Data

Gene col 11957: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11957); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11957, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11957]; `tensor/DDL_lfc|DDL_z.npy` [11957]; `embed/gene_vectors.npy` [11957]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11957 or target_col == 11957). Every well: [[CCDC157 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC157.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

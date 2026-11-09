---
symbol: "PYCR3"
type: "gene"
col: 2471
ensembl_id: "ENSG00000104524"
name: "pyrroline-5-carboxylate reductase 3"
location: "8q24.3"
module: 36
arm: "+"
pooled_cpm: 2.51
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# PYCR3

*pyrroline-5-carboxylate reductase 3* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.79× (z +11.9, q 4e-30, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +9.5, q 8e-19, up in 22 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (PANC-1 0.0716×); [[Lactate (calcium) (drug)]] 0.05 µM in 1 line (A549 0.0567×); [[Tirabrutinib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0457×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC35C1]] (+0.69, fdr 7e-06), [[FLAD1]] (+0.65, fdr 1e-05), [[TOMM40]] (+0.63, fdr 7e-06); moves opposite to [[PHF21A]] (-0.60, fdr 1e-05), [[ANAPC16]] (-0.59, fdr 3e-05), [[MATCAP2]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2471.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.79×** | +11.9 | 4e-30 | 2/5 (NCI-H2347, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +9.5 | 8e-19 | 22/32 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.35×** | +8.0 | 3e-13 | 33/45 (A-172, Hs 766T, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.44×** | +7.7 | 2e-12 | 4/7 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.10×** | +6.9 | 6e-10 | 5/12 (J82, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.92×** | +6.1 | 1e-07 | 21/40 (A-427, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.77×** | +5.3 | 8e-06 | 16/40 (A-427, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.81×** | +5.3 | 8e-06 | 5/14 (J82, NCI-H2347, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.3 | 8e-06 | 10/43 (HOP62, HEC-1-A, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.54×** | +4.0 | 0.003 | 3/23 (PANC-1, BT-474, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.035 | 6/34 (LS 180, NCI-H460, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.3 | 0.052 | 3/23 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.096 | 3/43 (Panc 03.27, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2471.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (PANC-1 0.0716×); [[Lactate (calcium) (drug)]] 0.05 µM in 1 line (A549 0.0567×); [[Tirabrutinib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0457×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM |  | 0.709× | -3.2 | 0.67 | 3/37 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 2.61 | 0 | 1 | — | [[Lactate (calcium) (drug)]] 0.05 µM 0.0567× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 2.11 | 0 | 1 | — | [[Tirabrutinib (drug)]] 0.5 µM 0.0457× (z -8.6) |
| [[PANC-1 (line)]] | alt | 2.76 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0716× (z -11.0) |
| [[A-172 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.803 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35C1]] | +0.69 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[FLAD1]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[TOMM40]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[DPH2]] | +0.63 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[ARMC6]] | +0.62 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[ATAD3A]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[PUS1]] | +0.61 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[TWNK]] | +0.60 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[IL9RP3]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TBL3]] | +0.60 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[WDR4]] | +0.59 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[TIMM23B-AGAP6]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF21A]] | -0.60 | -0.67 / -0.52 | both halves | 1e-05 |  |
| [[ANAPC16]] | -0.59 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[MATCAP2]] | -0.55 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[SNX2]] | -0.54 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[HADHB]] | -0.52 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[KAT2B]] | -0.51 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[KPNA5]] | -0.50 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[SNX16]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[ABCA5]] | -0.49 | -0.40 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-15.1, -34.2); signed map (-3.8, -46.0). **Vector** length 40.9, 4.35% of its response variance represented; |z| ≥ 3 in 972 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +2.6 | +6.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.3 | +8.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +5.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +2.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[vincristine (drug)]] 5 µM |  | +1.1 | +2.3 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -1.8 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | pyrroline-5-carboxylate reductase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,603,210-143,609,773 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13852; previously PYCRL |
| Gene groups (HGNC) | Pyrroline-5-carboxylate reductase family |
| Reactome | 2 pathways, smallest: Glutamate and glutamine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53H96](https://www.uniprot.org/uniprotkb/Q53H96) (Pyrroline-5-carboxylate reductase 3):

> Oxidoreductase that catalyzes the last step in proline biosynthesis, which corresponds to the reduction of pyrroline-5-carboxylate (P5C) to L-proline using NAD(P)H. Proline is synthesized from either glutamate or ornithine; both are converted to P5C, and then to proline via pyrroline-5-carboxylate reductases (PYCRs). PYCR3 is exclusively linked to the biosynthesis of proline from ornithine.

**Summary**, from NCBI Gene [65263](https://www.ncbi.nlm.nih.gov/gene/65263):

> This gene encodes a protein that belongs to the pyrroline-5-carboxylate reductase family of enzymes. Members of this family catalyze the final step in proline biosynthesis, converting pyrroline-5-carboxylate to proline. Glutamate and ornithine are precursors in the synthesis of proline. The protein encoded by this gene is a cytoplasmic enzyme involved in the biosynthesis of proline from ornithine. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:25846](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25846) · Entrez [65263](https://www.ncbi.nlm.nih.gov/gene/65263) · UniProt [Q53H96](https://www.uniprot.org/uniprotkb/Q53H96) · Ensembl [ENSG00000104524](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104524)

## Data

Gene col 2471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2471); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2471]; `tensor/DDL_lfc|DDL_z.npy` [2471]; `embed/gene_vectors.npy` [2471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2471 or target_col == 2471). Every well: [[PYCR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PYCR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

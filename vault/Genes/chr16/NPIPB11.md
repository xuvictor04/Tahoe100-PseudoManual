---
symbol: "NPIPB11"
type: "gene"
col: 14861
ensembl_id: "ENSG00000254206"
name: "nuclear pore complex interacting protein family member B11"
location: "16p11.2"
module: 5
arm: "+"
pooled_cpm: 4.4
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 6
n_dd_up_clean: 3
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NPIPB11

*nuclear pore complex interacting protein family member B11* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.63× (z +7.4, q 8e-11, up in 20 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.525× (z -6.7, q 8e-09, down in 21 of 41 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.646× (z -4.8, q 5e-04, down in 14 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMG1P6]] (+0.76, fdr 7e-06, ⚠ same locus), [[TIMM23B-AGAP6]] (+0.71, fdr 7e-06), [[DNHD1]] (+0.69, fdr 7e-06), [[DRD4]] (+0.66, fdr 7e-06); moves opposite to [[HPF1]] (-0.63, fdr 1e-05), [[COMMD8]] (-0.62, fdr 4e-05), [[RAB30]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14861.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +7.4 | 8e-11 | 20/37 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +5.9 | 1e-06 | 15/33 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +5.6 | 5e-06 | 12/46 (PANC-1, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.010 | 10/44 (AsPC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.36× | +3.3 | 0.13 | 8/44 (AsPC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.36× | +3.2 | 0.14 | 6/37 (A-172, SW1417, …) | top dose only | cell-cycle shift (explains ~9% here); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.35× | +3.1 | 0.14 | 5/33 (A498, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | 1.73× | +3.1 | 0.14 | 1/13 (AsPC-1) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.22× | +3.0 | 0.15 | 6/45 (HEC-1-A, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14861.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.525×** | -6.7 | 8e-09 | 21/41 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.646×** | -4.8 | 5e-04 | 14/43 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.691×** | -4.0 | 0.010 | 11/33 (hTERT-HPNE, PANC-1, …) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.613×** | -3.8 | 0.019 | 9/21 (NCI-H460, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -3.3 | 0.098 | 11/42 (A-172, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.657×** | -3.3 | 0.098 | 11/36 (A-427, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.759× | -3.0 | 0.20 | 4/44 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14861. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.72 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0857× (z -12.1) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HEC-1-A (line)]] | alt | 3.41 | 0 | 2 | — | [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0664× (z -10.0) |
| [[A-172 (line)]] | wt | 4.14 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0734× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -10.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 7.78 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0972× (z -13.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14861), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG1P6]] | +0.76 | +0.68 / +0.77 | both halves | 7e-06 | ⚠ same locus (19.1 kb, same strand: neighbours can correlate without regulation) |
| [[TIMM23B-AGAP6]] | +0.71 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[DNHD1]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[DRD4]] | +0.66 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[NPIPB12]] | +0.64 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[GHRLOS]] | +0.63 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[CAPN15]] | +0.61 | +0.42 / +0.66 | both halves | 4e-05 |  |
| [[UBAP1L]] | +0.61 | +0.47 / +0.66 | both halves | 2e-05 |  |
| [[PDCD6]] | +0.60 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[KCNIP2]] | +0.60 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[AGAP5]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[MAD1L1]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[RSKR]] | +0.59 | +0.54 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HPF1]] | -0.63 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[COMMD8]] | -0.62 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[RAB30]] | -0.62 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[PRKAA1]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[MIER1]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[ELAPOR2]] | -0.57 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[HCFC2]] | -0.57 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[MRPL40]] | -0.57 | -0.36 / -0.65 | both halves | 9e-05 |  |
| [[ZDHHC17]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[CDC73]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[SNAPIN]] | -0.55 | -0.37 / -0.67 | both halves | 8e-05 |  |
| [[GTPBP8]] | -0.54 | -0.40 / -0.48 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.491). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (21.6, -14.9); signed map (2.8, -54.0). **Vector** length 47.7, 5.50% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.3 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +3.0 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +0.9 | +2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.8 | +0.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +0.7 | +1.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.5 | -6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -0.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | nuclear pore complex interacting protein family member B11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,381,310-29,406,711 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [E5RHQ5](https://www.uniprot.org/uniprotkb/E5RHQ5) carries no function annotation.

**Summary**, from NCBI Gene [728888](https://www.ncbi.nlm.nih.gov/gene/728888):

> Predicted to act upstream of or within prevention of polyspermy. Predicted to be located in external side of plasma membrane and sperm head plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:37453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37453) · Entrez [728888](https://www.ncbi.nlm.nih.gov/gene/728888) · UniProt [E5RHQ5](https://www.uniprot.org/uniprotkb/E5RHQ5) · Ensembl [ENSG00000254206](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254206)

## Data

Gene col 14861: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14861); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14861, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14861]; `tensor/DDL_lfc|DDL_z.npy` [14861]; `embed/gene_vectors.npy` [14861]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14861 or target_col == 14861). Every well: [[NPIPB11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NPIPB11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

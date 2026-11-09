---
symbol: "HSP90AB3P"
type: "gene"
col: 11379
ensembl_id: "ENSG00000183199"
name: "heat shock protein 90 alpha family class B member 3, pseudogene"
location: "4q22.1"
module: 60
arm: "+"
pooled_cpm: 3.92
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# HSP90AB3P

*heat shock protein 90 alpha family class B member 3, pseudogene* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 4.44× (z +12.7, q 3e-34, up in 43 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (LS 180 0.0734×; ⚠ transcription drop); [[Vortioxetine (drug)]] 5 µM in 1 line (SW1417 0.0692×; ⚠ toxic); [[Roxadustat (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0674×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSP90AB2P]] (+0.95, fdr 7e-06), [[HSP90AB1]] (+0.86, fdr 7e-06), [[HSP90AA2P]] (+0.85, fdr 7e-06); moves opposite to [[SKA2]] (-0.52, fdr 4e-05), [[YY1AP1]] (-0.51, fdr 3e-05), [[HARBI1]] (-0.51, fdr 4e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11379.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.44×** | +12.7 | 3e-34 | 43/46 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.00×** | +11.8 | 8e-30 | 42/44 (SW480, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.62×** | +11.0 | 1e-25 | 42/44 (SW480, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.50×** | +10.7 | 2e-24 | 19/21 (HT-29, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.34×** | +9.9 | 5e-21 | 6/6 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.22×** | +9.4 | 4e-19 | 40/43 (HT-29, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +8.6 | 7e-16 | 6/9 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **5.57×** | +7.7 | 1e-12 | 16/20 (NCI-H2347, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.54×** | +5.7 | 1e-06 | 25/45 (SW480, NCI-H2347, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **3.17×** | +5.1 | 2e-05 | 16/31 (A-427, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.39×** | +3.9 | 0.005 | 3/11 (SNU-423, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.60×** | +3.9 | 0.005 | 9/30 (SK-MEL-2, NCI-H1573, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.54×** | +3.7 | 0.011 | 11/46 (Panc 03.27, NCI-H1792, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.54×** | +3.6 | 0.011 | 10/45 (NCI-H23, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 0.05 µM |  | **1.57×** | +3.6 | 0.011 | 10/42 (HOP62, A498, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.04×** | +3.2 | 0.046 | 3/41 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.057 | 8/44 (SW480, SW 900, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11379.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 1 line (LS 180 0.0734×; ⚠ transcription drop); [[Vortioxetine (drug)]] 5 µM in 1 line (SW1417 0.0692×; ⚠ toxic); [[Roxadustat (drug)]] 0.05 µM in 1 line (CFPAC-1 0.0674×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.887× | -3.7 | 0.10 | 15/47 (CFPAC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.764× | -3.3 | 0.32 | 10/45 (MIA PaCa-2, H4, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11379. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 3.80 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0674× (z -8.5) |
| [[LS 180 (line)]] | wt | 3.85 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0734× (z -8.9) ⚠ transcription drop |
| [[SW1417 (line)]] | alt | 3.40 | 0 | 1 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0692× (z -8.8) ⚠ toxic |
| [[A-172 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11379), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90AB2P]] | +0.95 | +0.94 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[HSP90AB1]] | +0.86 | +0.88 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[HSP90AA2P]] | +0.85 | +0.82 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[HSPD1]] | +0.79 | +0.79 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CCT4]] | +0.74 | +0.73 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CACYBP]] | +0.74 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[HSP90AA1]] | +0.74 | +0.69 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[HSPA8]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[PWWP3A]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[CCT3]] | +0.70 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[ATP2C1]] | +0.67 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PTGES3]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKA2]] | -0.52 | -0.51 / -0.43 | both halves | 4e-05 |  |
| [[YY1AP1]] | -0.51 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[HARBI1]] | -0.51 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ZC3H7B]] | -0.50 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.859). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.3, -11.4); signed map (-26.3, -28.6). **Vector** length 58.5, 8.44% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *heat shock* (control, mean cos +0.58 to 13); *Attenuation phase* (reactome, mean cos +0.61 to 13); *HSF1-dependent transactivation* (reactome, mean cos +0.60 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.6 | +11.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.0 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.9 | +12.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.5 | +11.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.5 | +7.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.2 | +2.4 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -1.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.0 | +0.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +0.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.3 | -0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.0 | -0.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein 90 alpha family class B member 3, pseudogene |
| Locus type | pseudogene |
| Location | 4q22.1 — chr4:87,891,843-87,894,015 (+) |
| Ensembl biotype | processed_pseudogene |
| Also known as | ; previously HSPCP1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q58FF7](https://www.uniprot.org/uniprotkb/Q58FF7) (Putative heat shock protein HSP 90-beta-3):

> Putative molecular chaperone that may promote the maturation, structural maintenance and proper regulation of specific target proteins.

**Summary**, from NCBI Gene [3327](https://www.ncbi.nlm.nih.gov/gene/3327):

> Predicted to enable ATP binding activity; ATP hydrolysis activity; and unfolded protein binding activity. Predicted to be involved in cellular response to heat; protein folding; and protein stabilization. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:5259](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5259) · Entrez [3327](https://www.ncbi.nlm.nih.gov/gene/3327) · UniProt [Q58FF7](https://www.uniprot.org/uniprotkb/Q58FF7) · Ensembl [ENSG00000183199](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183199)

## Data

Gene col 11379: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11379); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11379, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11379]; `tensor/DDL_lfc|DDL_z.npy` [11379]; `embed/gene_vectors.npy` [11379]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11379 or target_col == 11379). Every well: [[HSP90AB3P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSP90AB3P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

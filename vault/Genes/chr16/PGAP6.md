---
symbol: "PGAP6"
type: "gene"
col: 5006
ensembl_id: "ENSG00000129925"
name: "post-GPI attachment to proteins 6"
location: "16p13.3"
module: 2
arm: "+"
pooled_cpm: 11.51
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PGAP6

*post-GPI attachment to proteins 6* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.29× (z +11.3, q 1e-26, up in 30 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.79× (z +7.9, q 5e-13, up in 30 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.739× (z -4.1, q 0.021, down in 19 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIP5K1C]] (+0.62, fdr 1e-05), [[CORO7]] (+0.61, fdr 3e-05), [[GPR153]] (+0.60, fdr 1e-05); moves opposite to [[MTREX]] (-0.56, fdr 3e-05), [[NSUN3]] (-0.54, fdr 1e-04), [[COX15]] (-0.49, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 12 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5006.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.29×** | +11.3 | 1e-26 | 30/39 (NCI-H1573, NCI-H1792, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.22×** | +10.0 | 7e-21 | 25/32 (PANC-1, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.03×** | +9.2 | 4e-18 | 18/22 (KATO III, HS-578T, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.79×** | +7.9 | 5e-13 | 30/45 (LoVo, A498, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.61×** | +6.5 | 1e-08 | 28/47 (LoVo, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.52×** | +5.7 | 1e-06 | 26/47 (SW480, LoVo, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +5.6 | 2e-06 | 24/42 (AsPC-1, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.48×** | +5.3 | 7e-06 | 26/47 (RKO, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.45×** | +5.0 | 4e-05 | 20/44 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.9 | 4e-05 | 21/46 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +4.6 | 2e-04 | 15/43 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.3 | 7e-04 | 14/41 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.32×** | +3.8 | 0.007 | 15/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **1.32×** | +3.6 | 0.014 | 15/40 (KATO III, NCI-H2030, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.035 | 10/44 (NCI-H460, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5006.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.739×** | -4.1 | 0.021 | 19/43 (NCI-H1573, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.933× | -3.6 | 0.056 | 5/48 (NCI-H23, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.753×** | -3.6 | 0.056 | 9/47 (CHP-212, BT-474, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.759×** | -3.5 | 0.056 | 6/48 (HEC-1-A, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.758×** | -3.5 | 0.056 | 11/47 (CHP-212, SK-MEL-2, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 0.615× | -3.2 | 0.11 | 8/42 (SW48, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 5 µM |  | 0.854× | -3.1 | 0.17 | 10/48 (SW 1088, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5006. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 23.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.108× (z -9.1) |
| [[A-172 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.31 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5006), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIP5K1C]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[CORO7]] | +0.61 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[GPR153]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[KIFC2]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[FAAP20]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[PACS2]] | +0.58 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[GNA11]] | +0.58 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[FGFR3]] | +0.58 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[PITPNA]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[CSNK1G2]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ATG2A]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PRKCD]] | +0.55 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTREX]] | -0.56 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[NSUN3]] | -0.54 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[COX15]] | -0.49 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[AIMP1]] | -0.49 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[COPS2]] | -0.47 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[BCLAF1]] | -0.47 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[ZXDA]] | -0.46 | -0.36 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.594). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (12.2, -4.6); signed map (-26.1, 18.0). **Vector** length 65.5, 11.0% of its response variance represented; |z| ≥ 3 in 798 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.5 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.4 | +11.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +2.5 | +5.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.9 | +0.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.6 | +3.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -4.1 |
|  | [[NG25 (drug)]] 5 µM |  | -2.9 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -0.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | post-GPI attachment to proteins 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:370,788-387,113 (-) |
| Ensembl biotype | protein_coding |
| Also known as | M83; previously TMEM6, TMEM8, TMEM8A |
| Gene groups (HGNC) | TMEM8 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCN3](https://www.uniprot.org/uniprotkb/Q9HCN3) (Post-GPI attachment to proteins factor 6):

> Involved in the lipid remodeling steps of GPI-anchor maturation. Lipid remodeling steps consist in the generation of 2 saturated fatty chains at the sn-2 position of GPI-anchor proteins (GPI-AP). Has phospholipase A2 activity that removes an acyl-chain at the sn-2 position of GPI-anchors during the remodeling of GPI. Required for the shedding of the GPI-AP CRIPTO, but not CFC1, at the cell surface. Shedding of CRIPTO modulates Nodal signaling by allowing soluble CRIPTO to act as a Nodal …

**Summary**, from NCBI Gene [58986](https://www.ncbi.nlm.nih.gov/gene/58986):

> Predicted to enable A2-type glycerophospholipase activity. Predicted to be involved in lipid metabolic process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17205) · Entrez [58986](https://www.ncbi.nlm.nih.gov/gene/58986) · UniProt [Q9HCN3](https://www.uniprot.org/uniprotkb/Q9HCN3) · Ensembl [ENSG00000129925](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129925)

## Data

Gene col 5006: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5006); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5006, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5006]; `tensor/DDL_lfc|DDL_z.npy` [5006]; `embed/gene_vectors.npy` [5006]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5006 or target_col == 5006). Every well: [[PGAP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGAP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "ADAM20P1"
type: "gene"
col: 15176
ensembl_id: "ENSG00000259158"
name: "ADAM metallopeptidase domain 20 pseudogene 1"
location: "14q24.2"
module: 37
arm: "+"
pooled_cpm: 2.75
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# ADAM20P1

*ADAM metallopeptidase domain 20 pseudogene 1* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.09× (z +10.5, q 4e-23, up in 29 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.731× (z -10.1, q 3e-21, down in 34 of 46 measured lines) ⚠ position not correctable. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.646× (z -4.1, q 0.006, down in 12 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM20]] (+0.86, fdr 7e-06), [[ECT2L]] (+0.70, fdr 7e-06), [[LINC00640]] (+0.70, fdr 7e-06); moves opposite to [[MICAL3]] (-0.54, fdr 1e-05), [[ALDH1B1]] (-0.50, fdr 6e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC28A2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15176.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.09×** | +10.5 | 4e-23 | 29/42 (SW480, SW 900, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.19×** | +5.6 | 5e-06 | 15/38 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.62×** | +4.7 | 5e-04 | 5/39 (SW480, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.36×** | +4.2 | 0.004 | 1/5 (NCI-H1573) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.062 | 10/34 (NCI-H2030, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.062 | 8/45 (HT-29, NCI-H1792, …) | rises with dose | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.28×** | +3.3 | 0.081 | 6/45 (SW480, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15176.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.731×** | -10.1 | 3e-21 | 34/46 (SW480, SNU-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.569×** | -5.2 | 5e-05 | 15/45 (A-427, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.577×** | -4.9 | 2e-04 | 16/40 (HOP62, SW 900, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.626×** | -4.2 | 0.004 | 11/16 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.646×** | -4.1 | 0.006 | 12/45 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **0.701×** | -3.3 | 0.089 | 11/15 (PANC-1, SW480, …) | inconsistent across doses | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.704×** | -3.3 | 0.089 | 7/34 (MIA PaCa-2, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.687×** | -3.2 | 0.089 | 8/42 (SNU-1, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Atazanavir (sulfate) (drug)]] 0.5 µM |  | 0.723× | -3.0 | 0.16 | 10/40 (A498, BT-474, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15176. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 6.74 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.05 µM 0.0531× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 3.94 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0765× (z -9.4) |
| [[HOP62 (line)]] | alt | 3.37 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0813× (z -8.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.985 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.969 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.01 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15176), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM20]] | +0.86 | +0.89 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[ECT2L]] | +0.70 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[LINC00640]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[LINC00159]] | +0.69 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ZNF814]] | +0.69 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[WDR49]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[LVRN]] | +0.67 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[TMEM225B]] | +0.66 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[CD200R1]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CLEC4A]] | +0.64 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[MED6]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TMEM269]] | +0.63 | +0.52 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MICAL3]] | -0.54 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ALDH1B1]] | -0.50 | -0.39 / -0.54 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC28A2-AS1]] | B | SLC28A2-AS1 activity raises ADAM20P1's level | lines that do not express SLC28A2-AS1 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without SLC28A2-AS1 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.7, -19.5); signed map (8.7, 4.8). **Vector** length 53.2, 6.60% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.4 | +10.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | +4.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +1.5 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.5 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +2.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.1 | +1.4 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +1.1 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.8 | -4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.4 | -4.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.3 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.5 | -1.8 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.3 | -2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase domain 20 pseudogene 1 |
| Locus type | pseudogene |
| Location | 14q24.2 — chr14:70,468,881-70,471,206 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | ; previously C14orf55 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:20102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20102) · Entrez [317760](https://www.ncbi.nlm.nih.gov/gene/317760) · Ensembl [ENSG00000259158](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259158)

## Data

Gene col 15176: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15176); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15176, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15176]; `tensor/DDL_lfc|DDL_z.npy` [15176]; `embed/gene_vectors.npy` [15176]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15176 or target_col == 15176). Every well: [[ADAM20P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAM20P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

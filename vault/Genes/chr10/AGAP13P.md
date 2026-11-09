---
symbol: "AGAP13P"
type: "gene"
col: 14349
ensembl_id: "ENSG00000243289"
name: "ArfGAP with GTPase domain, ankyrin repeat and PH domain 13, pseudogene"
location: "10q11.22"
module: 28
arm: "+"
pooled_cpm: 2.39
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 7
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# AGAP13P

*ArfGAP with GTPase domain, ankyrin repeat and PH domain 13, pseudogene* — 10q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.43× (z +8.1, q 3e-13, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Anethole trithione (drug)]] 5 µM: 1.34× (z +3.9, q 0.017, up in 1 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.483× (z -6.9, q 2e-09, down in 20 of 45 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMS1P1-1]] (+0.72, fdr 7e-06, ⚠ same locus), [[AGAP9]] (+0.70, fdr 7e-06), [[BMS1P1]] (+0.57, fdr 4e-05, ⚠ same locus), [[ASAH2B]] (+0.54, fdr 4e-05), [[BMS1P2]] (+0.52, fdr 4e-05); moves opposite to [[NBEAL1]] (-0.52, fdr 4e-05), [[NEAT1]] (-0.51, fdr 1e-04), [[MEX3D]] (-0.50, fdr 2e-04).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ECHDC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14349.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.43×** | +8.1 | 3e-13 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +6.1 | 3e-07 | 1/4 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.017 | 1/44 (Hs 766T) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.46×** | +3.6 | 0.052 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | 1.40× | +3.2 | 0.17 | 3/33 (NCI-H2030, J82, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.39× | +3.1 | 0.17 | 4/41 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14349.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.483×** | -6.9 | 2e-09 | 20/45 (PANC-1, RKO, …) | top dose only | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.514×** | -6.3 | 7e-08 | 11/23 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.664×** | -3.9 | 0.018 | 12/38 (CFPAC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | **0.666×** | -3.7 | 0.028 | 9/36 (NCI-H1792, SW48, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.686×** | -3.6 | 0.038 | 13/40 (NCI-H2030, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.694×** | -3.5 | 0.048 | 8/45 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.778×** | -3.4 | 0.054 | 13/31 (NCI-H460, LoVo, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.717× | -3.2 | 0.10 | 8/41 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14349. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 2.98 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0521× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 3.17 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0605× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 5.22 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0813× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 2.24 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0858× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 3.50 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -9.0) |
| [[SW480 (line)]] | alt | 5.63 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -10.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.907 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.603 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.207 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14349), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMS1P1-1]] | +0.72 | +0.72 / +0.62 | both halves | 7e-06 | ⚠ same locus (4.5 kb, same strand: neighbours can correlate without regulation) |
| [[AGAP9]] | +0.70 | +0.60 / +0.71 | both halves | 7e-06 | same gene group |
| [[BMS1P1]] | +0.57 | +0.70 / +0.41 | both halves | 4e-05 | ⚠ same locus (16.7 kb, same strand: neighbours can correlate without regulation) |
| [[ASAH2B]] | +0.54 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[BMS1P2]] | +0.52 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[TAS2R30]] | +0.52 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[C5orf63]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[NLRX1]] | +0.51 | +0.48 / +0.31 | both halves | 2e-04 |  |
| [[RMDN2]] | +0.50 | +0.50 / +0.30 | both halves | 2e-04 |  |
| [[MTHFS]] | +0.48 | +0.33 / +0.31 | both halves | 2e-04 |  |
| [[ZNF485]] | +0.47 | +0.42 / +0.38 | both halves | 6e-05 |  |
| [[AGAP5]] | +0.46 | +0.39 / +0.37 | both halves | 8e-05 | same gene group |
| [[ERMARD]] | +0.46 | +0.29 / +0.40 | both halves | 2e-04 |  |
| [[ECHDC1]] | +0.46 | +0.40 / +0.32 | both halves | 1e-04 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBEAL1]] | -0.52 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[NEAT1]] | -0.51 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[MEX3D]] | -0.50 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[NR6A1]] | -0.48 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[TGFB1]] | -0.47 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[ERC1]] | -0.47 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[SH3PXD2B]] | -0.46 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[BBS9]] | -0.46 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[SMG6]] | -0.46 | -0.32 / -0.45 | both halves | 2e-04 |  |
| [[TUBA1A]] | -0.46 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[PTPRN]] | -0.46 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[TMEM120A]] | -0.45 | -0.37 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ECHDC2]] | B | ECHDC2 activity raises AGAP13P's level | lines that do not express ECHDC2 (12) vs lines expressing it (38) | 1.38× lower at baseline in the lines without ECHDC2 | 0.030 | ⚠ within organs, on part of the lines; also absent: STXBP2, C10orf88B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.261). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-46.4, 21.3); signed map (18.2, -44.8). **Vector** length 33.4, 2.94% of its response variance represented; |z| ≥ 3 in 1,029 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.6 | +0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.2 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | -0.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.0 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.8 | +0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.7 | +0.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.6 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.6 | +1.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | -6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.3 | -6.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.2 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -3.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.8 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | +0.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.7 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with GTPase domain, ankyrin repeat and PH domain 13, pseudogene |
| Locus type | pseudogene |
| Location | 10q11.22 — chr10:46,816,516-46,837,947 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Also known as | bA548K23.1; previously CTGLF9P |
| Gene groups (HGNC) | ArfGAPs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23499](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23499) · Entrez [728005](https://www.ncbi.nlm.nih.gov/gene/728005) · Ensembl [ENSG00000243289](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243289)

## Data

Gene col 14349: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14349); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14349, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14349]; `tensor/DDL_lfc|DDL_z.npy` [14349]; `embed/gene_vectors.npy` [14349]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14349 or target_col == 14349). Every well: [[AGAP13P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGAP13P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

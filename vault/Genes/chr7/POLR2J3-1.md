---
symbol: "POLR2J3-1"
type: "gene"
col: 16110
ensembl_id: "ENSG00000285437"
name: ""
location: ""
module: 24
arm: "+"
pooled_cpm: 5.75
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# POLR2J3-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.06× (z +7.7, q 1e-11, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.503× (z -7.2, q 3e-10, down in 29 of 45 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM: 0.606× (z -5.3, q 3e-05, down in 22 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2J4]] (+0.63, fdr 1e-05), [[ZNF611]] (+0.60, fdr 1e-05), [[MEF2B]] (+0.55, fdr 1e-05); moves opposite to [[GTF3A]] (-0.54, fdr 4e-05, ⚠ GTF3A in the vector space only through flagged drug-doses), [[COX11]] (-0.53, fdr 4e-05), [[CPNE1]] (-0.53, fdr 9e-05), [[CFAP97]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16110.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +7.7 | 1e-11 | 34/46 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +5.8 | 1e-06 | 24/45 (LoVo, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +4.9 | 1e-04 | 21/44 (LoVo, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | 1.38× | +3.3 | 0.16 | 5/36 (J82, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Benproperine (phosphate) (drug)]] 5 µM |  | 1.37× | +3.2 | 0.17 | 9/44 (C-33 A, J82, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16110.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.503×** | -7.2 | 3e-10 | 29/45 (A498, A549, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.572×** | -5.9 | 1e-06 | 28/45 (hTERT-HPNE, Panc 03.27, …) | inconsistent across doses |  |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **0.606×** | -5.3 | 3e-05 | 22/39 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.409×** | -4.9 | 1e-04 | 17/39 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.447×** | -4.4 | 0.001 | 21/43 (Panc 03.27, COLO 205, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | **0.692×** | -3.9 | 0.010 | 16/43 (RPMI-7951, SW 900, …) | inconsistent across doses | position effect removed |
| [[Berbamine (drug)]] 0.5 µM |  | **0.715×** | -3.5 | 0.033 | 11/43 (SNU-1, HCT15, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.729×** | -3.3 | 0.062 | 10/45 (NCI-H460, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[TAK-901 (drug)]] 0.5 µM |  | **0.645×** | -3.3 | 0.062 | 8/42 (NCI-H23, HEC-1-A, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Simotinib (drug)]] 0.05 µM |  | **0.716×** | -3.2 | 0.066 | 14/42 (A498, A549, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.736×** | -3.2 | 0.066 | 7/46 (Panc 03.27, RKO, …) | inconsistent across doses | position effect removed |
| [[Brimonidine (drug)]] 0.5 µM |  | **0.738×** | -3.2 | 0.066 | 19/43 (A-427, SNU-423, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16110. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 9.65 | 0 | 3 (1 ⚠) | — | [[Penfluridol (drug)]] 5 µM 0.0990× (z -9.6) |
| [[A498 (line)]] | wt | 8.07 | 0 | 2 | — | [[XRK3F2 (drug)]] 0.5 µM 0.107× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 7.60 | 0 | 2 | — | [[Harringtonine (drug)]] 0.05 µM 0.0647× (z -9.4) |
| [[SW1417 (line)]] | alt | 6.92 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0959× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~84% of this change |
| [[A-172 (line)]] | wt | 6.41 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0873× (z -9.5) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 6.49 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 9.67 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 4.83 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 4.38 | 0 | 1 | — | [[Balsalazide (sodium hydrate) (drug)]] 0.05 µM 0.0605× (z -8.5) |
| [[SW 900 (line)]] | alt | 6.24 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.0732× (z -9.0) |
| [[A-427 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16110), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*44 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2J4]] | +0.63 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[ZNF611]] | +0.60 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[MEF2B]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | +0.53 | +0.53 / +0.48 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[C19orf25]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ROMO1]] | +0.51 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[COX17]] | +0.51 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[ATP5MK]] | +0.48 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[GABARAPL2]] | +0.48 | +0.44 / +0.46 | both halves | 3e-05 |  |
| [[GON4L]] | +0.48 | +0.49 / +0.31 | both halves | 2e-04 |  |
| [[SMG6]] | +0.48 | +0.40 / +0.33 | both halves | 1e-04 |  |
| [[ENDOV]] | +0.48 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[ADGRL1-AS1]] | +0.47 | +0.47 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*56 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF3A]] ⚠ | -0.54 | -0.46 / -0.40 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COX11]] | -0.53 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[CPNE1]] | -0.53 | -0.37 / -0.60 | both halves | 9e-05 |  |
| [[CFAP97]] | -0.53 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[FLOT2]] | -0.52 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[LRRC58]] | -0.51 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[NELFCD]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[MANEA]] | -0.51 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[SNX17]] | -0.51 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[RBBP9]] | -0.51 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[PFN2]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[XK]] | -0.50 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[TMEM123]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers POLR2J3-1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.284). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-50.9, -5.9); signed map (-19.7, 0.5). **Vector** length 44.5, 4.38% of its response variance represented; |z| ≥ 3 in 1,068 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.7 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.3 | +1.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.2 | +7.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.0 | +4.9 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.0 | +1.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.8 | +1.4 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +0.8 | +1.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +0.8 | +1.5 |
|  | [[Resveratrol (drug)]] 5 µM |  | +0.8 | +0.5 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.1 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -4.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | +0.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Lopinavir (drug)]] 5 µM |  | -1.1 | -0.9 |

## What is on record

> [!warning] No registry record
> POLR2J3-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16110: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16110); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16110, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16110]; `tensor/DDL_lfc|DDL_z.npy` [16110]; `embed/gene_vectors.npy` [16110]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16110 or target_col == 16110). Every well: [[POLR2J3-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2J3-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

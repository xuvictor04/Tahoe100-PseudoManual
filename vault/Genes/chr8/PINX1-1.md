---
symbol: "PINX1-1"
type: "gene"
col: 15133
ensembl_id: "ENSG00000258724"
name: ""
location: ""
module: 5
arm: "+"
pooled_cpm: 2.12
n_lines_expressing: 48
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PINX1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.41× (z +11.7, q 1e-28, up in 32 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.594× (z -5.0, q 4e-04, down in 18 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0946×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 0.0676×); [[Triclosan (drug)]] 0.5 µM in 1 line (SHP-77 0.0752×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PINX1]] (+0.74, fdr 7e-06, ⚠ read-through risk), [[PDCD11]] (+0.73, fdr 7e-06), [[LYAR]] (+0.70, fdr 1e-05), [[WDR3]] (+0.66, fdr 2e-05); moves opposite to [[ATOSA]] (-0.56, fdr 2e-05), [[TXNDC16]] (-0.55, fdr 1e-04), [[CEP57]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MTHFD1L]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15133.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.41×** | +11.7 | 1e-28 | 32/42 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.33×** | +11.4 | 7e-28 | 32/41 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.96×** | +10.3 | 9e-23 | 27/39 (SHP-77, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.08×** | +7.0 | 4e-10 | 22/42 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +6.8 | 1e-09 | 0/0 | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.51×** | +5.6 | 2e-06 | 7/29 (A498, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +4.2 | 0.002 | 8/27 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **1.56×** | +4.1 | 0.004 | 1/10 (PANC-1) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.52×** | +4.0 | 0.005 | 4/41 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **2.16×** | +3.8 | 0.007 | 1/16 (NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +3.8 | 0.008 | 11/43 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.13×** | +3.7 | 0.008 | 2/20 (NCI-H23, MIA PaCa-2) | inconsistent across doses | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.2 | 0.051 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.44×** | +3.2 | 0.051 | 0/0 | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.2 | 0.051 | 1/11 (SHP-77) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.066 | 7/32 (RKO, LOX-IMVI, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.86×** | +3.1 | 0.066 | 0/22 | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.066 | 3/19 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Resveratrol (drug)]] 5 µM |  | **1.25×** | +3.0 | 0.081 | 1/43 (NCI-H460) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15133.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0946×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (KATO III 0.0676×); [[Triclosan (drug)]] 0.5 µM in 1 line (SHP-77 0.0752×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.594×** | -5.0 | 4e-04 | 18/43 (KATO III, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.665×** | -3.7 | 0.053 | 12/40 (SW48, NCI-H460, …) | top dose only | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -3.4 | 0.15 | 8/45 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.793× | -3.1 | 0.26 | 8/43 (COLO 205, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15133. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 3.67 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0676× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 5.41 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0946× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 5.84 | 0 | 1 | — | [[Triclosan (drug)]] 0.5 µM 0.0752× (z -8.6) |
| [[A-172 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.902 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.814 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.488 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.753 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.892 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.940 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.908 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.906 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15133), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PINX1]] | +0.74 | +0.73 / +0.72 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of PINX1 on the same strand (can correlate by spillover, not regulation) |
| [[PDCD11]] | +0.73 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[LYAR]] | +0.70 | +0.57 / +0.70 | both halves | 1e-05 |  |
| [[WDR3]] | +0.66 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[CHCHD6]] | +0.65 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[DKC1]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[CTU1]] | +0.64 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[POLR1B]] | +0.63 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[URB1]] | +0.63 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[TWNK]] | +0.62 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[NOP16]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[NOL10]] | +0.62 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[RRP1]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATOSA]] | -0.56 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[TXNDC16]] | -0.55 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[CEP57]] | -0.55 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[ABCA5]] | -0.55 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[SNX16]] | -0.54 | -0.39 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTHFD1L]] | C | MTHFD1L activity raises PINX1-1's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.01× lower at baseline in the lines without MTHFD1L | 0.063 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; co-absent with the target |
| [[GARNL3]] | C | GARNL3 activity raises PINX1-1's level | lines that do not express GARNL3 (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without GARNL3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WHRN, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.555). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.6, -38.2); signed map (-3.6, -48.6). **Vector** length 40.6, 4.62% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +7.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.1 | +11.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.9 | +11.4 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.4 | +3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | +1.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.1 | -3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.0 | -0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -0.9 | -5.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -0.8 | -0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.6 |
|  | [[Vandetanib (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.7 | +1.4 |

## What is on record

> [!warning] No registry record
> PINX1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 15133: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15133); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15133, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15133]; `tensor/DDL_lfc|DDL_z.npy` [15133]; `embed/gene_vectors.npy` [15133]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15133 or target_col == 15133). Every well: [[PINX1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PINX1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

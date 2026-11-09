---
symbol: "ZSCAN20"
type: "gene"
col: 4305
ensembl_id: "ENSG00000121903"
name: "zinc finger and SCAN domain containing 20"
location: "1p35.1"
module: 16
arm: "+"
pooled_cpm: 7.77
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# ZSCAN20

*zinc finger and SCAN domain containing 20* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.52× (z +6.2, q 2e-07, up in 24 of 48 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.42× (z +3.7, q 0.071, up in 13 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.503× (z -7.2, q 3e-10, down in 20 of 29 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.627× (z -6.9, q 1e-09, down in 29 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZSCAN22]] (+0.75, fdr 7e-06), [[ZFP37]] (+0.67, fdr 7e-06), [[ZNF780A]] (+0.67, fdr 7e-06); moves opposite to [[RPS6KA5]] (-0.57, fdr 1e-05), [[PHLPP1]] (-0.55, fdr 6e-05), [[TMEM50B]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4305.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.52×** | +6.2 | 2e-07 | 24/48 (LOX-IMVI, HT-29, …) | rises with dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.071 | 13/45 (A-427, NCI-H23, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.39×** | +3.5 | 0.098 | 14/45 (SW480, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.33× | +3.0 | 0.38 | 11/45 (HOP62, A549, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4305.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.503×** | -7.2 | 3e-10 | 20/29 (A498, J82, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.627×** | -6.9 | 1e-09 | 29/42 (SNU-423, LS 180, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.546×** | -6.3 | 4e-08 | 29/48 (SW 900, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.552×** | -6.2 | 6e-08 | 28/42 (PANC-1, SHP-77, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.507×** | -6.2 | 6e-08 | 23/38 (SK-MEL-2, PANC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.578×** | -5.0 | 5e-05 | 21/44 (C32, SNU-423, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.596×** | -4.7 | 2e-04 | 21/43 (SNU-423, C32, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.670×** | -4.2 | 0.002 | 20/45 (NCI-H1792, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.675×** | -4.1 | 0.002 | 20/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Atazanavir (sulfate) (drug)]] 0.5 µM |  | **0.734×** | -3.3 | 0.061 | 16/45 (J82, C-33 A, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.734×** | -3.2 | 0.061 | 18/46 (COLO 205, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.747× | -3.1 | 0.10 | 13/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4305. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -11.1) |
| [[COLO 205 (line)]] | alt | 26.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 5.84 | 0 | 2 (1 ⚠) | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0658× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 7.38 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.112× (z -9.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[PANC-1 (line)]] | alt | 9.15 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SHP-77 (line)]] | alt | 8.80 | 0 | 2 (1 ⚠) | — | [[Tofacitinib (drug)]] 0.5 µM 0.0788× (z -10.5) |
| [[SW 900 (line)]] | alt | 7.52 | 0 | 2 (1 ⚠) | — | [[Orlistat (drug)]] 0.05 µM 0.0805× (z -9.1) |
| [[A-172 (line)]] | wt | 7.98 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -8.6) |
| [[A498 (line)]] | wt | 3.65 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0671× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[AsPC-1 (line)]] | alt | 5.35 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0659× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 6.55 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0768× (z -8.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 6.09 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.0603× (z -12.2) |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0982× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change |
| [[LOX-IMVI (line)]] | wt | 6.37 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0985× (z -8.6) |
| [[LS 180 (line)]] | wt | 4.85 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 5.74 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 5.95 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0646× (z -14.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.102× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4305), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN22]] | +0.75 | +0.64 / +0.75 | both halves | 7e-06 | same gene group; STRING 797 |
| [[ZFP37]] | +0.67 | +0.58 / +0.69 | both halves | 7e-06 | same gene group |
| [[ZNF780A]] | +0.67 | +0.59 / +0.71 | both halves | 7e-06 | same gene group |
| [[CBLL1]] | +0.67 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[MSANTD4]] | +0.67 | +0.60 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZBTB6]] | +0.67 | +0.69 / +0.58 | both halves | 7e-06 | same gene group |
| [[ZNF691]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZNF268]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 | same gene group |
| [[ZNF221]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 | same gene group |
| [[ZNF484]] | +0.65 | +0.56 / +0.66 | both halves | 1e-05 | same gene group |
| [[ZNF284]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 | same gene group |
| [[ZNF317]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS6KA5]] | -0.57 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[PHLPP1]] | -0.55 | -0.38 / -0.59 | both halves | 6e-05 |  |
| [[TMEM50B]] | -0.54 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[PPM1B]] | -0.54 | -0.38 / -0.60 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZSCAN20's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZNF256]] | B | ZNF256 activity raises ZSCAN20's level | lines that do not express ZNF256 (14) vs lines expressing it (36) | 1.29× lower at baseline in the lines without ZNF256 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ZNF331, GAMT, ZNF625 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.650). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.0, 9.9); signed map (0.9, -26.9). **Vector** length 59.6, 8.40% of its response variance represented; |z| ≥ 3 in 1,026 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +5.5 | +6.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +3.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +2.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +2.9 | +3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +1.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.9 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | -1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -6.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.9 | -5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -4.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | -3.4 | -6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -2.6 | -6.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.0 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | +0.3 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:33,472,645-33,501,643 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KOX29; previously ZNF360, ZNF31 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing; Myb/SANT domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17040](https://www.uniprot.org/uniprotkb/P17040) (Zinc finger and SCAN domain-containing protein 20):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7579](https://www.ncbi.nlm.nih.gov/gene/7579):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13093](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13093) · Entrez [7579](https://www.ncbi.nlm.nih.gov/gene/7579) · UniProt [P17040](https://www.uniprot.org/uniprotkb/P17040) · Ensembl [ENSG00000121903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121903)

## Data

Gene col 4305: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4305); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4305, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4305]; `tensor/DDL_lfc|DDL_z.npy` [4305]; `embed/gene_vectors.npy` [4305]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4305 or target_col == 4305). Every well: [[ZSCAN20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

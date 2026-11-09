---
symbol: "MNS1"
type: "gene"
col: 6186
ensembl_id: "ENSG00000138587"
name: "meiosis specific nuclear structural 1"
location: "15q21.3"
module: 6
arm: "+"
pooled_cpm: 11.13
n_lines_expressing: 45
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MNS1

*meiosis specific nuclear structural 1* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.86× (z +13.1, q 3e-36, up in 30 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.05 µM: 1.41× (z +3.1, q 0.099, up in 12 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 5 lines (PANC-1 3.90×, J82 4.18×, HT-29 5.18×, A498 4.92×, …; ⚠ cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 6.49×, NCI-H1792 10.4×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 5.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.582× (z -5.2, q 1e-04, down in 21 of 42 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRCC1]] (+0.72, fdr 7e-06), [[ALDH7A1]] (+0.70, fdr 1e-05), [[PRIM1]] (+0.66, fdr 1e-05); moves opposite to [[SMIM12]] (-0.57, fdr 2e-04), [[LTO1]] (-0.57, fdr 2e-04), [[SPON1-AS1]] (-0.57, fdr 3e-04).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6186.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 5 lines (PANC-1 3.90×, J82 4.18×, HT-29 5.18×, A498 4.92×, …; ⚠ cell-cycle shift, explains ~50% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 6.49×, NCI-H1792 10.4×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 5.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **3.86×** | +13.1 | 3e-36 | 30/32 (SW480, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.56×** | +11.8 | 1e-29 | 19/19 (LoVo, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **3.25×** | +11.4 | 9e-28 | 40/43 (PANC-1, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **3.09×** | +10.9 | 1e-25 | 37/43 (J82, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.66×** | +8.7 | 3e-16 | 20/24 (LoVo, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **2.41×** | +8.5 | 2e-15 | 33/43 (J82, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.85×** | +6.0 | 2e-07 | 24/43 (J82, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.57×** | +4.2 | 0.002 | 15/41 (C32, LoVo, …) | top dose only | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **1.52×** | +3.9 | 0.005 | 17/35 (CFPAC-1, NCI-H2030, …) | all doses, flat |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.49×** | +3.7 | 0.010 | 12/42 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.26×** | +3.2 | 0.076 | 14/43 (HT-29, PANC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.099 | 12/37 (Panc 03.27, J82, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.39× | +3.0 | 0.10 | 13/43 (NCI-H1573, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6186.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.582×** | -5.2 | 1e-04 | 21/42 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.609×** | -4.8 | 5e-04 | 22/43 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -4.1 | 0.008 | 18/39 (NCI-H23, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.661×** | -4.0 | 0.010 | 17/41 (A-172, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.668×** | -3.9 | 0.012 | 19/43 (NCI-H23, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.674×** | -3.8 | 0.014 | 22/42 (RKO, NCI-H661, …) | two highest doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.678×** | -3.7 | 0.015 | 19/43 (COLO 205, CFPAC-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.901× | -3.6 | 0.027 | 10/43 (H4, Panc 03.27, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.787×** | -3.2 | 0.076 | 18/43 (LS 180, SHP-77, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.707×** | -3.2 | 0.079 | 16/42 (NCI-H2030, LOX-IMVI, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.535×** | -3.1 | 0.084 | 13/38 (SW1417, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.89 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6186. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.33 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.92× (z +8.5) ⚠ cell-cycle shift, explains ~50% of this change | [[Belzutifan (drug)]] 5 µM 0.0448× (z -8.7) |
| [[J82 (line)]] | alt | 21.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.46× (z +9.3) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[A-427 (line)]] | wt | 3.49 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0648× (z -8.6) |
| [[A549 (line)]] | wt | 13.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.10× (z +8.5) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[AN3 CA (line)]] | alt | 23.7 | 0 | 1 | — | [[5-Fluorouracil (drug)]] 0.5 µM 0.0640× (z -8.6) |
| [[C32 (line)]] | wt | 8.02 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0978× (z -8.6) |
| [[Hs 766T (line)]] | wt | 7.17 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.05 µM 0.0827× (z -8.8) |
| [[HT-29 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.18× (z +8.7) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[LoVo (line)]] | wt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.84× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H1792 (line)]] | alt | 9.22 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.4× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[NCI-H23 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -9.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 15.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.90× (z +8.9) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SW480 (line)]] | alt | 4.63 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[A-172 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.40 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.42 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6186), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRCC1]] | +0.72 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[ALDH7A1]] | +0.70 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[PRIM1]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[ACACB]] | +0.66 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[HAUS4]] | +0.64 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[CENPU]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[SPATA6]] | +0.62 | +0.30 / +0.59 | both halves | 2e-04 |  |
| [[NUP62CL]] | +0.62 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[CCDC34]] | +0.61 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[POT1]] | +0.60 | +0.27 / +0.53 | both halves | 3e-04 |  |
| [[HAUS1]] | +0.59 | +0.33 / +0.69 | both halves | 1e-04 |  |
| [[HLTF]] | +0.59 | +0.46 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM12]] | -0.57 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[LTO1]] | -0.57 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[SPON1-AS1]] | -0.57 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[ZNF778]] | -0.54 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[BANP]] | -0.52 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[SMUG1]] | -0.51 | -0.25 / -0.32 | both halves | 4e-04 |  |
| [[LINC00862]] | -0.51 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[MIATNB]] | -0.51 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[DENND6A-AS1]] | -0.50 | -0.11 / -0.34 | ⚠ not reproduced | 0.002 |  |
| [[EXOSC3]] | -0.50 | -0.28 / -0.37 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers MNS1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.499). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-26.4, -50.1); signed map (-35.3, -35.7). **Vector** length 74.9, 15.5% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +5.9 | +13.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +5.4 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +4.5 | +8.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +4.0 | +11.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.3 | +10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | -0.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.7 | -3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | -3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | -5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -2.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | meiosis specific nuclear structural 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:56,421,544-56,465,137 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CFAP127, FLJ11222, SPATA40 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEH6](https://www.uniprot.org/uniprotkb/Q8NEH6) (Meiosis-specific nuclear structural protein 1):

> Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating. May play a role in the control of meiotic division and germ cell differentiation through regulation of pairing and recombination during meiosis. Required for sperm flagella assembly (By similarity). May play a role in the assembly and function of the outer dynein arm-docking complex (ODA-DC). ODA-DC mediates outer dynein arms (ODA) binding onto …

**Summary**, from NCBI Gene [55329](https://www.ncbi.nlm.nih.gov/gene/55329):

> This gene encodes a protein highly similar to the mouse meiosis-specific nuclear structural 1 protein. The mouse protein was shown to be expressed at the pachytene stage during spermatogenesis and may function as a nuclear skeletal protein to regulate nuclear morphology during meiosis. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:29636](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29636) · Entrez [55329](https://www.ncbi.nlm.nih.gov/gene/55329) · UniProt [Q8NEH6](https://www.uniprot.org/uniprotkb/Q8NEH6) · Ensembl [ENSG00000138587](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138587)

## Data

Gene col 6186: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6186); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6186, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6186]; `tensor/DDL_lfc|DDL_z.npy` [6186]; `embed/gene_vectors.npy` [6186]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6186 or target_col == 6186). Every well: [[MNS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MNS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

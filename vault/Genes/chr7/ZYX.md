---
symbol: "ZYX"
type: "gene"
col: 8278
ensembl_id: "ENSG00000159840"
name: "zyxin"
location: "7q34"
module: 96
arm: "+"
pooled_cpm: 55.06
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/096"]
generated_by: "tahoemap"
---

# ZYX

*zyxin* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.27× (z +9.6, q 3e-19, up in 41 of 49 measured lines) ⚠ position not correctable. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.48× (z +6.5, q 2e-08, up in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-172 2.55×, AsPC-1 2.60×, A498 2.05×, SNU-1 2.61×, …); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 2.58×, A-427 3.46×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 2.71×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.401× (z -10.8, q 1e-24, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR1]] (+0.73, fdr 7e-06), [[FAAP100]] (+0.68, fdr 7e-06), [[MYO1C]] (+0.66, fdr 7e-06); moves opposite to [[FNTB]] (-0.64, fdr 1e-05), [[ASB7]] (-0.61, fdr 1e-05), [[PPP1R12B]] (-0.61, fdr 1e-05).
> It is in [[Module 096]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SLC4A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8278.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A-172 2.55×, AsPC-1 2.60×, A498 2.05×, SNU-1 2.61×, …); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 2.58×, A-427 3.46×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 2.71×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.27×** | +9.6 | 3e-19 | 41/49 (A498, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +6.5 | 2e-08 | 29/48 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +4.7 | 6e-04 | 25/47 (A498, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.009 | 28/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +3.4 | 0.081 | 21/45 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.47× | +3.3 | 0.11 | 23/48 (SNU-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Erythromycin (drug)]] 5 µM |  | 1.30× | +3.1 | 0.17 | 20/48 (CFPAC-1, RKO, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8278.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.401×** | -10.8 | 1e-24 | 43/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.450×** | -9.5 | 8e-19 | 39/48 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.525×** | -7.6 | 4e-12 | 38/48 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.626×** | -5.3 | 1e-05 | 38/48 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.671×** | -4.7 | 3e-04 | 33/48 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.787×** | -4.0 | 0.006 | 24/48 (J82, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.714×** | -3.8 | 0.009 | 26/47 (SW48, SNU-1, …) | rises with dose | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.715×** | -3.8 | 0.009 | 23/48 (A498, BT-474, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -3.5 | 0.032 | 25/48 (NCI-H2347, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.741×** | -3.3 | 0.046 | 25/48 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.759×** | -3.3 | 0.055 | 18/48 (SW 900, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.753×** | -3.1 | 0.091 | 21/48 (BT-474, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.834× | -3.0 | 0.11 | 18/48 (A549, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8278. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 84.9 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.287× (z -11.8) |
| [[BT-474 (line)]] | alt | 60.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -10.8) |
| [[A498 (line)]] | wt | 90.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 114 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -13.9) |
| [[A-427 (line)]] | wt | 37.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -9.9) |
| [[A549 (line)]] | wt | 54.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.343× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 41.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.385× (z -8.5) |
| [[J82 (line)]] | alt | 50.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.328× (z -10.0) |
| [[A-172 (line)]] | wt | 39.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 61.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.5) | — |
| [[C-33 A (line)]] | alt | 54.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 31.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 75.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -9.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[HS-578T (line)]] | alt | 59.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -8.6) |
| [[HT-29 (line)]] | alt | 52.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -10.5) ⚠ cell-cycle shift, explains ~51% of this change |
| [[LOX-IMVI (line)]] | wt | 60.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.322× (z -9.4) |
| [[LS 180 (line)]] | wt | 57.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -8.7) ⚠ cell-cycle shift, explains ~51% of this change |
| [[NCI-H1573 (line)]] | alt | 21.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 53.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.228× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 67.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 187 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 103 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 83.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 37.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8278), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR1]] | +0.73 | +0.75 / +0.70 | both halves | 7e-06 | same gene group |
| [[FAAP100]] | +0.68 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[MYO1C]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[THOC6]] | +0.64 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[FAM83G]] | +0.63 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[MUS81]] | +0.63 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[WIZ]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[PLEC]] | +0.61 | +0.62 / +0.61 | both halves | 7e-06 | same gene group |
| [[CSRP1]] | +0.60 | +0.67 / +0.51 | both halves | 1e-05 | STRING 694 |
| [[CELSR3]] | +0.60 | +0.53 / +0.47 | both halves | 2e-05 | same gene group |
| [[NCDN]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[UBA1]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FNTB]] | -0.64 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[ASB7]] | -0.61 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[PPP1R12B]] | -0.61 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[CRYZL1]] | -0.60 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[RELCH]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[ZNF148]] | -0.56 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[COX7C]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 | same gene group |
| [[NENF]] | -0.54 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[SEC24B]] | -0.54 | -0.48 / -0.42 | both halves | 4e-05 | same gene group |
| [[UBE4B]] | -0.53 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[RNF149]] | -0.52 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[ATP5PD]] | -0.52 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC4A3]] | B | SLC4A3 activity raises ZYX's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.36× lower at baseline in the lines without SLC4A3 | 0.088 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 096]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-11.2, -25.3); signed map (-6.6, 31.6). **Vector** length 116, 31.8% of its response variance represented; |z| ≥ 3 in 903 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.3 | +6.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +1.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.2 | +3.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.1 | +1.2 |
| fall | [[Verteporfin (drug)]] 5 µM |  | -4.8 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.7 | -2.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.1 | -3.8 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | zyxin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:143,381,295-143,391,111 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zyxin family; MicroRNA protein coding host genes |
| Hallmark sets | APICAL_JUNCTION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15942](https://www.uniprot.org/uniprotkb/Q15942) (Zyxin):

> Adhesion plaque protein. Binds alpha-actinin and the CRP protein. Important for targeting TES and ENA/VASP family members to focal adhesions and for the formation of actin-rich structures. May be a component of a signal transduction pathway that mediates adhesion-stimulated changes in gene expression (By similarity).

**Summary**, from NCBI Gene [7791](https://www.ncbi.nlm.nih.gov/gene/7791):

> Focal adhesions are actin-rich structures that enable cells to adhere to the extracellular matrix and at which protein complexes involved in signal transduction assemble. Zyxin is a zinc-binding phosphoprotein that concentrates at focal adhesions and along the actin cytoskeleton. Zyxin has an N-terminal proline-rich domain and three LIM domains in its C-terminal half. The proline-rich domain may interact with SH3 domains of proteins involved in signal transduction pathways while the LIM domains …

**Accessions** — [HGNC:13200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13200) · Entrez [7791](https://www.ncbi.nlm.nih.gov/gene/7791) · UniProt [Q15942](https://www.uniprot.org/uniprotkb/Q15942) · Ensembl [ENSG00000159840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159840)

## Data

Gene col 8278: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8278); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8278, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8278]; `tensor/DDL_lfc|DDL_z.npy` [8278]; `embed/gene_vectors.npy` [8278]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8278 or target_col == 8278). Every well: [[ZYX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZYX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

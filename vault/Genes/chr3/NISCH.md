---
symbol: "NISCH"
type: "gene"
col: 208
ensembl_id: "ENSG00000010322"
name: "nischarin"
location: "3p21.1"
module: 209
arm: "+"
pooled_cpm: 33.06
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/209"]
generated_by: "tahoemap"
---

# NISCH

*nischarin* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.47× (z +6.0, q 1e-06, up in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 2.19×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 2.40×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.585× (z -11.6, q 2e-28, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF594-DT]] (+0.66, fdr 1e-05), [[CROCCP2]] (+0.65, fdr 7e-06), [[NELFA]] (+0.65, fdr 1e-05); moves opposite to [[EHBP1]] (-0.57, fdr 1e-05), [[ARPC5]] (-0.55, fdr 2e-05), [[SCHIP1]] (-0.53, fdr 3e-05).
> It is in [[Module 209]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 208.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 2.19×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 2.40×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +6.0 | 1e-06 | 33/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 0.004 | 23/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.0 | 0.014 | 21/47 (RKO, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.020 | 19/48 (A-427, SW480, …) | rises with dose | composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | 1.15× | +3.1 | 0.24 | 6/48 (NCI-H23, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 208.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.585×** | -11.6 | 2e-28 | 41/48 (LOX-IMVI, LS 180, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.629×** | -7.2 | 1e-10 | 32/46 (LOX-IMVI, KATO III, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.623×** | -6.8 | 2e-09 | 27/44 (A-427, SW48, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.654×** | -6.4 | 3e-08 | 27/40 (C-33 A, HS-578T, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.706×** | -5.2 | 2e-05 | 28/48 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.816×** | -4.4 | 0.001 | 21/48 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **0.828×** | -4.1 | 0.004 | 21/48 (LS 180, SW480, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.788×** | -3.7 | 0.014 | 21/48 (SW 1088, C32, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.790×** | -3.5 | 0.025 | 18/48 (NCI-H1573, HepG2/C3A, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.799×** | -3.5 | 0.027 | 17/48 (LoVo, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.813×** | -3.2 | 0.064 | 15/48 (NCI-H1792, LS 180, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.817× | -3.0 | 0.11 | 19/47 (hTERT-HPNE, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 0.824× | -3.0 | 0.11 | 17/48 (HS-578T, SW 1088, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 208. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 50.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.309× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -9.1) |
| [[A-427 (line)]] | wt | 36.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HOP62 (line)]] | alt | 43.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -8.6) |
| [[HS-578T (line)]] | alt | 38.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[hTERT-HPNE (line)]] | wt | 41.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 36.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -13.5) |
| [[LS 180 (line)]] | wt | 33.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -12.6) |
| [[A498 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.326× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[AN3 CA (line)]] | alt | 54.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[C-33 A (line)]] | alt | 58.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[HT-29 (line)]] | alt | 23.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -10.2) |
| [[KATO III (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.279× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H23 (line)]] | alt | 41.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 24.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.250× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 46.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -9.8) |
| [[SHP-77 (line)]] | alt | 30.8 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.301× (z -8.5) |
| [[SNU-423 (line)]] | alt | 35.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -11.3) |
| [[SW 900 (line)]] | alt | 34.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.5) |
| [[SW1417 (line)]] | alt | 23.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -10.7) |
| [[SW48 (line)]] | wt | 51.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 37.8 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +9.8) | — |
| [[A-172 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 208), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF594-DT]] | +0.66 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CROCCP2]] | +0.65 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[NELFA]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[MORN4]] | +0.63 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[KLHL26]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[USP30]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[OSBPL7]] | +0.60 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ACVR1B]] | +0.60 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[TTC38]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[CDAN1]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[SAT2]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ZSWIM9]] | +0.58 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHBP1]] | -0.57 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[ARPC5]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[SCHIP1]] | -0.53 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[PRDX1]] | -0.53 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[YWHAZ]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[ZSWIM6]] | -0.52 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[PTPRK]] | -0.51 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[ATP11C]] | -0.51 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[FER]] | -0.50 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SLIT2]] | -0.50 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[GLS]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NISCH's level | compounds that target TOP2A: 3 of 5 lower it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 209]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-22.3, -4.9); signed map (-25.5, -11.7). **Vector** length 77.1, 15.5% of its response variance represented; |z| ≥ 3 in 736 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +1.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.7 | -2.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.5 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.1 | +0.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -11.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.3 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -1.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Thymol (drug)]] 5 µM |  | -2.0 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | nischarin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:52,455,118-52,493,068 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0975, I-1, IRAS |
| Reactome | 6 pathways, smallest: RND2 GTPase cycle; RND3 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2I1](https://www.uniprot.org/uniprotkb/Q9Y2I1) (Nischarin):

> Acts either as the functional imidazoline-1 receptor (I1R) candidate or as a membrane-associated mediator of the I1R signaling. Binds numerous imidazoline ligands that induces initiation of cell-signaling cascades triggering to cell survival, growth and migration. Its activation by the agonist rilmenidine induces an increase in phosphorylation of mitogen-activated protein kinases MAPK1 and MAPK3 in rostral ventrolateral medulla (RVLM) neurons that exhibited rilmenidine-evoked hypotension (By …

**Summary**, from NCBI Gene [11188](https://www.ncbi.nlm.nih.gov/gene/11188):

> This gene encodes a nonadrenergic imidazoline-1 receptor protein that localizes to the cytosol and anchors to the inner layer of the plasma membrane. The orthologous mouse protein has been shown to influence cytoskeletal organization and cell migration by binding to alpha-5-beta-1 integrin. In humans, this protein has been shown to bind to the adapter insulin receptor substrate 4 (IRS4) to mediate translocation of alpha-5 integrin from the cell membrane to endosomes. Expression of this protein …

**Accessions** — [HGNC:18006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18006) · Entrez [11188](https://www.ncbi.nlm.nih.gov/gene/11188) · UniProt [Q9Y2I1](https://www.uniprot.org/uniprotkb/Q9Y2I1) · Ensembl [ENSG00000010322](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010322)

## Data

Gene col 208: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 208); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 208, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 208]; `tensor/DDL_lfc|DDL_z.npy` [208]; `embed/gene_vectors.npy` [208]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 208 or target_col == 208). Every well: [[NISCH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NISCH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

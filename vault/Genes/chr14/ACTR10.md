---
symbol: "ACTR10"
type: "gene"
col: 5261
ensembl_id: "ENSG00000131966"
name: "actin related protein 10"
location: "14q23.1"
module: 17
arm: "+"
pooled_cpm: 43.36
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 17
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ACTR10

*actin related protein 10* — 14q23.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 2.73×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.603× (z -14.2, q 4e-43, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD17]] (+0.69, fdr 8e-06), [[RUFY2]] (+0.66, fdr 7e-06), [[ZYG11B]] (+0.66, fdr 1e-05); moves opposite to [[SNRPB]] (-0.60, fdr 1e-05), [[DNAH1]] (-0.56, fdr 1e-05), [[ZNF407]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5261.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 2.73×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.20× | +3.5 | 0.16 | 15/47 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | 1.19× | +3.4 | 0.16 | 14/49 (MIA PaCa-2, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.12× | +3.3 | 0.18 | 10/48 (J82, HEC-1-A, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.18× | +3.2 | 0.18 | 4/48 (A498, NCI-H460, …) | rises with dose | plate-row cell shift |
| [[Retinoic acid (drug)]] 5 µM |  | 1.12× | +3.2 | 0.18 | 2/49 (SNU-423, KATO III) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 22 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5261.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.603×** | -14.2 | 4e-43 | 44/48 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.665×** | -8.1 | 2e-13 | 33/48 (LS 180, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.667×** | -8.0 | 2e-13 | 34/48 (A-172, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.721×** | -6.5 | 1e-08 | 29/48 (hTERT-HPNE, LS 180, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.718×** | -6.3 | 3e-08 | 30/48 (A-172, BT-474, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.720×** | -6.3 | 4e-08 | 27/47 (SK-MEL-2, SHP-77, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.736×** | -6.1 | 1e-07 | 23/48 (LS 180, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **0.741×** | -5.9 | 2e-07 | 31/48 (LS 180, HS-578T, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.736×** | -5.8 | 3e-07 | 29/48 (SNU-423, RKO, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.740×** | -5.5 | 2e-06 | 25/43 (Panc 03.27, NCI-H23, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.781×** | -4.9 | 5e-05 | 23/46 (NCI-H1573, Panc 03.27, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.843× | -4.8 | 8e-05 | 18/48 (BT-474, SW1417, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.791×** | -4.5 | 4e-04 | 21/48 (A498, NCI-H1573, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.655×** | -4.4 | 5e-04 | 23/49 (NCI-H1792, J82, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.858× | -4.3 | 7e-04 | 19/48 (HS-578T, CFPAC-1, …) | rises with dose |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.836× | -3.5 | 0.012 | 13/48 (NCI-H460, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.737×** | -3.2 | 0.036 | 13/48 (LOX-IMVI, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.860× | -3.0 | 0.065 | 13/48 (H4, A549, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.861× | -2.9 | 0.069 | 6/48 (NCI-H1573, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5261. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 48.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -8.9) |
| [[HS-578T (line)]] | alt | 35.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -13.1) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 37.9 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.203× (z -12.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H1792 (line)]] | alt | 54.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -19.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 73.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.0) |
| [[A-172 (line)]] | wt | 39.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -9.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 46.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 34.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 49.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 39.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 70.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -11.2) |
| [[HOP62 (line)]] | alt | 37.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -10.2) |
| [[Hs 766T (line)]] | wt | 43.0 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.365× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.253× (z -9.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 54.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 69.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 41.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 65.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[SK-MEL-2 (line)]] | alt | 35.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.222× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[SW48 (line)]] | wt | 44.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 42.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5261), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD17]] | +0.69 | +0.68 / +0.57 | both halves | 8e-06 |  |
| [[RUFY2]] | +0.66 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[ZYG11B]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[WDR11]] | +0.64 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MORN4]] | +0.64 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[ARNT]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[FRA10AC1]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[TRAPPC11]] | +0.63 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[STAM2]] | +0.62 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[IFT52]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[CGRRF1]] | +0.62 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[KLHL12]] | +0.62 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPB]] | -0.60 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[DNAH1]] | -0.56 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[ZNF407]] | -0.53 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[DDX5]] | -0.53 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[HNRNPA2B1]] | -0.53 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[SEMA4A]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[HDAC4]] | -0.53 | -0.48 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ACTR10's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.4, -3.0); signed map (-21.3, -13.4). **Vector** length 100, 24.2% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.8 | +1.6 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.6 | +2.3 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +2.4 | +3.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -14.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -4.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | -4.2 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -4.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.7 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -8.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:58,200,080-58,235,636 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HARP11, ACTR11, Arp11, Arp10 |
| Gene groups (HGNC) | Dynactin subunits; Actin related proteins |
| Reactome | 19 pathways, smallest: COPI-independent Golgi-to-ER retrograde traffic; HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand; Processing of antigen in germinal center B cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZ32](https://www.uniprot.org/uniprotkb/Q9NZ32) (Actin-related protein 10):

> Part of the dynactin complex that activates the molecular motor dynein for ultra-processive transport along microtubules.

**Summary**, from NCBI Gene [55860](https://www.ncbi.nlm.nih.gov/gene/55860):

> Predicted to be a structural constituent of cytoskeleton. Predicted to be involved in retrograde axonal transport of mitochondrion. Predicted to act upstream of or within microtubule-based movement. Predicted to be located in cytosol; extracellular region; and secretory granule. Predicted to be part of dynactin complex. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17372](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17372) · Entrez [55860](https://www.ncbi.nlm.nih.gov/gene/55860) · UniProt [Q9NZ32](https://www.uniprot.org/uniprotkb/Q9NZ32) · Ensembl [ENSG00000131966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131966)

## Data

Gene col 5261: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5261); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5261, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5261]; `tensor/DDL_lfc|DDL_z.npy` [5261]; `embed/gene_vectors.npy` [5261]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5261 or target_col == 5261). Every well: [[ACTR10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTR10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

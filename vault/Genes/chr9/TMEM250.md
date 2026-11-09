---
symbol: "TMEM250"
type: "gene"
col: 14177
ensembl_id: "ENSG00000238227"
name: "transmembrane protein 250"
location: "9q34.3"
module: 7
arm: "+"
pooled_cpm: 6.61
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 19
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TMEM250

*transmembrane protein 250* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.26× (z +8.4, q 2e-14, up in 16 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.60× (z +4.7, q 3e-04, up in 21 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 5.54×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.438× (z -11.4, q 2e-27, down in 32 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL20-AS1]] (+0.67, fdr 7e-06), [[B3GALT6]] (+0.66, fdr 7e-06), [[PLPP6]] (+0.61, fdr 1e-05); moves opposite to [[TALAM1]] (-0.49, fdr 5e-05), [[SNAP23]] (-0.49, fdr 5e-05), [[SELENOW]] (-0.48, fdr 3e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14177.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 5.54×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.26×** | +8.4 | 2e-14 | 16/26 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +7.1 | 3e-10 | 8/11 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.00×** | +5.9 | 6e-07 | 10/19 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.75×** | +5.8 | 1e-06 | 19/33 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.60×** | +4.7 | 3e-04 | 21/43 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.9 | 0.009 | 14/31 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | 1.80× | +3.2 | 0.11 | 4/30 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.35× | +3.1 | 0.12 | 4/44 (HCT15, RKO, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 1.34× | +3.0 | 0.14 | 7/44 (SW1417, HOP62, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 1.24× | +3.0 | 0.14 | 6/45 (HCT15, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14177.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.438×** | -11.4 | 2e-27 | 32/40 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.366×** | -10.4 | 1e-22 | 34/47 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.478×** | -7.2 | 1e-10 | 30/43 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.545×** | -6.3 | 6e-08 | 28/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.318×** | -6.2 | 7e-08 | 28/43 (J82, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.550×** | -6.2 | 7e-08 | 26/47 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.568×** | -5.8 | 5e-07 | 24/41 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.348×** | -5.7 | 9e-07 | 23/41 (MIA PaCa-2, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.579×** | -5.6 | 1e-06 | 22/47 (RKO, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.626×** | -4.8 | 7e-05 | 19/44 (J82, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.626×** | -4.8 | 7e-05 | 23/47 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.443×** | -4.4 | 5e-04 | 15/25 (J82, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.676×** | -4.0 | 0.002 | 16/45 (LoVo, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.672×** | -3.9 | 0.003 | 19/45 (A-172, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.696×** | -3.7 | 0.007 | 17/46 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.714×** | -3.5 | 0.019 | 20/45 (RKO, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.735×** | -3.2 | 0.051 | 4/48 (A498, A-172, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14177. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 10.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -13.2) |
| [[J82 (line)]] | alt | 15.3 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.240× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 7.23 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0924× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.278× (z -9.1) |
| [[RKO (line)]] | wt | 7.45 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0727× (z -9.8) |
| [[SW480 (line)]] | alt | 8.07 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.217× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.217× (z -9.5) |
| [[A-172 (line)]] | wt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -10.0) |
| [[A498 (line)]] | wt | 9.57 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +10.6) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 5.42 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0735× (z -8.9) |
| [[KATO III (line)]] | alt | 9.99 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -9.7) |
| [[SW1417 (line)]] | alt | 6.04 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0802× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14177), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL20-AS1]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[B3GALT6]] | +0.66 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[PLPP6]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[OXLD1]] | +0.61 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[RPP25]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[RRS1]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[HPS6]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ALDH1B1]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ZNF623]] | +0.58 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[CIAPIN1]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ZNF768]] | +0.56 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[TMEM129]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TALAM1]] | -0.49 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[SNAP23]] | -0.49 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[SELENOW]] | -0.48 | -0.53 / -0.26 | both halves | 3e-04 |  |
| [[HSPB11]] | -0.47 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[CD99]] | -0.47 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[RASA4B]] | -0.47 | -0.42 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | TMEM250's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | TMEM250's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.481 over the table, 0.076 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.420). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-48.4, -0.1); signed map (-4.6, -28.0). **Vector** length 49.1, 6.53% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.2 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.4 | +0.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.5 | -7.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.3 | -6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -2.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -2.0 | -4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 250 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:136,114,581-136,118,875 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA83N9.1; previously C9orf69 |
| Matched by | ensembl_id |

**Function**, from UniProt [H0YL14](https://www.uniprot.org/uniprotkb/H0YL14) (Transmembrane protein 250):

> May play a role in cell proliferation by promoting progression into S phase.; (Microbial infection) Promotes human herpes simplex virus 1/HHV-1 proliferation.

**Summary**, from NCBI Gene [90120](https://www.ncbi.nlm.nih.gov/gene/90120):

> Involved in positive regulation of cell population proliferation and positive regulation of viral process. Located in cytoplasm and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31009) · Entrez [90120](https://www.ncbi.nlm.nih.gov/gene/90120) · UniProt [H0YL14](https://www.uniprot.org/uniprotkb/H0YL14) · Ensembl [ENSG00000238227](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000238227)

## Data

Gene col 14177: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14177); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14177, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14177]; `tensor/DDL_lfc|DDL_z.npy` [14177]; `embed/gene_vectors.npy` [14177]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14177 or target_col == 14177). Every well: [[TMEM250 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM250.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

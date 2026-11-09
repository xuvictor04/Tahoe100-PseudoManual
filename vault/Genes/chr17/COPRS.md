---
symbol: "COPRS"
type: "gene"
col: 10237
ensembl_id: "ENSG00000172301"
name: "coordinator of PRMT5 and differentiation stimulator"
location: "17q11.2"
module: 24
arm: "+"
pooled_cpm: 14.13
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# COPRS

*coordinator of PRMT5 and differentiation stimulator* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.52× (z +11.1, q 6e-26, up in 34 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[9-ING-41 (drug)]] 0.5 µM: 2.06× (z +3.3, q 0.055, up in 12 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 4.60×, SW480 4.86×, A549 6.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 5.71×, PANC-1 4.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 3.33×; ⚠ cell-cycle shift, would explain all of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.152×; ⚠ cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SHP-77 0.0841×); [[Bentamapimod (drug)]] 0.05 µM in 1 line (SHP-77 0.0746×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAMP3]] (+0.59, fdr 4e-05), [[RANGRF]] (+0.58, fdr 3e-05), [[ORAI1]] (+0.53, fdr 2e-05); moves opposite to [[EIF2AK1]] (-0.52, fdr 3e-05), [[ANXA2]] (-0.48, fdr 2e-05), [[ANXA1]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LRFN4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 12 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10237.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 4.60×, SW480 4.86×, A549 6.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 5.71×, PANC-1 4.51×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 3.33×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.52×** | +11.1 | 6e-26 | 34/37 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.85×** | +8.9 | 2e-16 | 21/23 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.55×** | +7.9 | 4e-13 | 36/41 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.36×** | +7.6 | 5e-12 | 38/45 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.91×** | +5.7 | 1e-06 | 30/39 (HOP62, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.77×** | +4.8 | 1e-04 | 28/40 (LoVo, SNU-423, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.95×** | +4.7 | 2e-04 | 24/30 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.44×** | +4.5 | 4e-04 | 21/44 (NCI-H460, SK-MEL-2, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.58×** | +3.9 | 0.006 | 21/45 (NCI-H460, NCI-H2030, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.53×** | +3.8 | 0.010 | 23/47 (HT-29, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.06×** | +3.3 | 0.055 | 12/43 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.44×** | +3.2 | 0.057 | 12/46 (SW480, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.43×** | +3.1 | 0.076 | 18/45 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10237.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.152×; ⚠ cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SHP-77 0.0841×); [[Bentamapimod (drug)]] 0.05 µM in 1 line (SHP-77 0.0746×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | 0.503× | -3.2 | 0.77 | 13/45 (PANC-1, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10237. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 21.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.60× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[SHP-77 (line)]] | alt | 10.5 | 0 | 2 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0841× (z -10.9) |
| [[SW480 (line)]] | alt | 14.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.71× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H460 (line)]] | wt | 12.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -10.6) ⚠ cell-cycle shift, explains ~68% of this change |
| [[A-172 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10237), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 6 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAMP3]] | +0.59 | +0.43 / +0.58 | both halves | 4e-05 |  |
| [[RANGRF]] | +0.58 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[ORAI1]] | +0.53 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[RNF166]] | +0.52 | +0.37 / +0.60 | both halves | 9e-05 |  |
| [[GUSBP11]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[C22orf39]] | +0.50 | +0.32 / +0.56 | both halves | 2e-04 |  |
| [[LAMTOR4]] | +0.50 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[HRAS]] | +0.49 | +0.24 / +0.60 | both halves | 4e-04 |  |
| [[DNLZ]] | +0.49 | +0.25 / +0.61 | both halves | 4e-04 |  |
| [[TOLLIP]] | +0.48 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[LSM7]] | +0.48 | +0.25 / +0.52 | both halves | 4e-04 |  |
| [[SURF2]] | +0.48 | +0.26 / +0.66 | both halves | 4e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2AK1]] | -0.52 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[ANXA2]] | -0.48 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[ANXA1]] | -0.48 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[PDAP1]] | -0.47 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[SMU1]] | -0.46 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[CSNK1A1]] | -0.46 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[TCP1]] | -0.46 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[PAPOLA]] | -0.46 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[TPM3]] | -0.45 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[COPB2]] | -0.45 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[ARF1]] | -0.45 | -0.37 / -0.46 | both halves | 9e-05 |  |
| [[PTGES3]] | -0.44 | -0.47 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRFN4]] | B | LRFN4 activity raises COPRS's level | lines that do not express LRFN4 (8) vs lines expressing it (42) | 1.14× lower at baseline in the lines without LRFN4 | 0.032 | ⚠ within organs, on part of the lines; also absent: OTULINL, TCEAL3 |
| [[HES6]] | B | HES6 activity raises COPRS's level | lines that do not express HES6 (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without HES6 | 0.085 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.436). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.9, -20.1); signed map (-29.0, 8.8). **Vector** length 49.5, 8.92% of its response variance represented; |z| ≥ 3 in 561 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +7.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +2.6 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.2 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.1 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.3 | +2.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.4 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -3.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | coordinator of PRMT5 and differentiation stimulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:31,851,871-31,859,291 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TTP1, HSA272196, COPR5; previously C17orf79 |
| Reactome | 3 pathways, smallest: RMTs methylate histone arginines; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ92](https://www.uniprot.org/uniprotkb/Q9NQ92) (Coordinator of PRMT5 and differentiation stimulator):

> Histone-binding protein required for histone H4 methyltransferase activity of PRMT5. Specifically required for histone H4 'Arg-3' methylation mediated by PRMT5, but not histone H3 'Arg-8' methylation, suggesting that it modulates the substrate specificity of PRMT5. Specifically interacts with the N-terminus of histone H4 but not with histone H3, suggesting that it acts by promoting the association between histone H4 and PRMT5. Involved in CCNE1 promoter repression. Plays a role in muscle cell …

**Summary**, from NCBI Gene [55352](https://www.ncbi.nlm.nih.gov/gene/55352):

> Enables histone binding activity. Involved in chromatin remodeling. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28848](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28848) · Entrez [55352](https://www.ncbi.nlm.nih.gov/gene/55352) · UniProt [Q9NQ92](https://www.uniprot.org/uniprotkb/Q9NQ92) · Ensembl [ENSG00000172301](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172301)

## Data

Gene col 10237: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10237); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10237, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10237]; `tensor/DDL_lfc|DDL_z.npy` [10237]; `embed/gene_vectors.npy` [10237]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10237 or target_col == 10237). Every well: [[COPRS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COPRS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

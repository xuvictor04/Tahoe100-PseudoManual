---
symbol: "ESD"
type: "gene"
col: 6334
ensembl_id: "ENSG00000139684"
name: "esterase D"
location: "13q14.2"
module: 17
arm: "+"
pooled_cpm: 36.99
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ESD

*esterase D* — 13q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.89× (z +7.9, q 2e-12, up in 37 of 47 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-423 3.15×, HT-29 3.80×, NCI-H460 2.82×, A549 2.85×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 3.30×, SW480 2.93×, PANC-1 2.64×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.587× (z -9.3, q 8e-18, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLK]] (+0.72, fdr 7e-06), [[METTL5]] (+0.68, fdr 3e-05), [[SLC25A12]] (+0.67, fdr 1e-05); moves opposite to [[DDX5]] (-0.64, fdr 1e-05), [[FSCN2]] (-0.60, fdr 9e-06), [[TRPV1]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[KATNAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6334.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (SNU-423 3.15×, HT-29 3.80×, NCI-H460 2.82×, A549 2.85×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 3.30×, SW480 2.93×, PANC-1 2.64×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +7.9 | 2e-12 | 37/47 (SNU-423, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +7.7 | 4e-12 | 26/37 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +4.2 | 0.006 | 24/42 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | 1.20× | +3.1 | 0.23 | 15/47 (LS 180, AsPC-1, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 1.63× | +3.1 | 0.23 | 18/46 (A-172, H4, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6334.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.587×** | -9.3 | 8e-18 | 40/47 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.599×** | -9.0 | 9e-17 | 38/47 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.630×** | -5.7 | 2e-06 | 34/47 (HEC-1-A, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.645×** | -5.2 | 2e-05 | 30/47 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.657×** | -5.2 | 2e-05 | 33/47 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.659×** | -5.2 | 2e-05 | 30/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.780×** | -4.4 | 0.001 | 23/47 (SNU-1, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.713×** | -4.2 | 0.002 | 26/47 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.571×** | -3.6 | 0.023 | 23/47 (LOX-IMVI, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.758×** | -3.4 | 0.034 | 23/47 (Hs 766T, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.776×** | -3.1 | 0.088 | 24/47 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6334. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 41.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 37.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +8.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.9) |
| [[SNU-1 (line)]] | wt | 63.8 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.273× (z -12.1) |
| [[SW480 (line)]] | alt | 40.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.93× (z +9.4) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.389× (z -8.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -11.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 51.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -9.7) |
| [[AN3 CA (line)]] | alt | 60.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.119× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.139× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~3% of this change |
| [[HEC-1-A (line)]] | alt | 56.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -9.3) |
| [[HOP62 (line)]] | alt | 32.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -12.7) |
| [[Hs 766T (line)]] | wt | 59.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -13.3) |
| [[HT-29 (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +9.0) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 50.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -11.1) |
| [[LOX-IMVI (line)]] | wt | 51.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 47.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 38.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +8.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 40.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 28.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -10.4) |
| [[SNU-423 (line)]] | alt | 64.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6334), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLK]] | +0.72 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[METTL5]] | +0.68 | +0.46 / +0.71 | both halves | 3e-05 |  |
| [[SLC25A12]] | +0.67 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[NIPSNAP2]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[IRAK1BP1]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[NUDT12]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MRPS31P4]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[SAAL1]] | +0.64 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[SKIC3]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[TRAPPC11]] | +0.64 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[UBXN2B]] | +0.63 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[TBC1D19]] | +0.63 | +0.48 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX5]] | -0.64 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[FSCN2]] | -0.60 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[TRPV1]] | -0.58 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[SLC25A44]] | -0.57 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[COL20A1]] | -0.56 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[NXF1]] | -0.54 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[PIPOX]] | -0.54 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[HCFC1]] | -0.54 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[SEPTIN9-DT]] | -0.53 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[CFL1]] | -0.53 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[TNRC18]] | -0.53 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[SLC9A5]] | -0.53 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity raises ESD's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 2.15× lower at baseline in the lines without KATNAL1 | 0.013 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[KATNAL1]] | B | KATNAL1 activity strengthens ESD's drug response | lines that do not express KATNAL1 (6) vs lines expressing it (41) | the lines without KATNAL1 respond 0.80× as strongly (z diff +0.83); strongest at Belinostat 5 µM: 1.06x vs 0.69x (z diff +3.2) | 0.037 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises ESD's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.772). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.9, -2.5); signed map (-22.6, -13.8). **Vector** length 78.9, 20.4% of its response variance represented; |z| ≥ 3 in 667 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.2 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | -1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.9 | +0.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.7 | -5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.4 | -0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | esterase D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.2 — chr13:46,771,256-46,797,420 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Thioester hydrolases |
| Reactome | 3 pathways, smallest: Glutathione conjugation; Phase II - Conjugation of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [P10768](https://www.uniprot.org/uniprotkb/P10768) (S-formylglutathione hydrolase):

> Serine hydrolase involved in the detoxification of formaldehyde.

**Summary**, from NCBI Gene [2098](https://www.ncbi.nlm.nih.gov/gene/2098):

> This gene encodes a serine hydrolase that belongs to the esterase D family. The encoded enzyme is active toward numerous substrates including O-acetylated sialic acids, and it may be involved in the recycling of sialic acids. This gene is used as a genetic marker for retinoblastoma and Wilson's disease. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:3465](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3465) · Entrez [2098](https://www.ncbi.nlm.nih.gov/gene/2098) · UniProt [P10768](https://www.uniprot.org/uniprotkb/P10768) · Ensembl [ENSG00000139684](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139684)

## Data

Gene col 6334: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6334); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6334, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6334]; `tensor/DDL_lfc|DDL_z.npy` [6334]; `embed/gene_vectors.npy` [6334]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6334 or target_col == 6334). Every well: [[ESD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

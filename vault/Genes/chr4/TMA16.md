---
symbol: "TMA16"
type: "gene"
col: 12603
ensembl_id: "ENSG00000198498"
name: "translation machinery associated 16 homolog"
location: "4q32.2"
module: 1
arm: "+"
pooled_cpm: 32.81
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TMA16

*translation machinery associated 16 homolog* — 4q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.26× (z +11.3, q 4e-27, up in 40 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.77× (z +7.9, q 7e-13, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.676× (z -5.4, q 3e-05, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF485]] (+0.70, fdr 7e-06), [[IMPACT]] (+0.69, fdr 1e-05), [[GPATCH4]] (+0.69, fdr 7e-06); moves opposite to [[GNB2]] (-0.66, fdr 3e-05), [[GRN]] (-0.63, fdr 1e-05), [[PSAP]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAM169A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12603.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.26×** | +11.3 | 4e-27 | 40/45 (MIA PaCa-2, A498, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +7.9 | 7e-13 | 35/47 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.95×** | +7.9 | 7e-13 | 32/40 (HOP62, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +7.7 | 3e-12 | 32/45 (HT-29, HOP62, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +7.1 | 2e-10 | 38/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.50×** | +4.8 | 2e-04 | 30/48 (NCI-H1792, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.4 | 0.001 | 26/48 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.009 | 21/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.32×** | +3.8 | 0.009 | 24/46 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.59×** | +3.3 | 0.054 | 15/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.089 | 15/48 (HOP62, Hs 766T, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.1 | 0.092 | 17/48 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.092 | 17/48 (C32, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.54×** | +3.1 | 0.092 | 12/47 (AsPC-1, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12603.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.676×** | -5.4 | 3e-05 | 25/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.682×** | -5.3 | 3e-05 | 28/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.735×** | -4.3 | 0.004 | 22/48 (RKO, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.761×** | -3.8 | 0.021 | 18/48 (RKO, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.788× | -3.1 | 0.17 | 14/47 (SW480, Panc 03.27, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.645× | -3.1 | 0.17 | 20/48 (NCI-H23, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12603. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 43.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 0.5 µM 0.409× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 24.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.52× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 28.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.45× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 22.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.93× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.71× (z +8.6) | — |
| [[A498 (line)]] | wt | 50.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A549 (line)]] | wt | 28.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HEC-1-A (line)]] | alt | 48.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[HT-29 (line)]] | alt | 15.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 39.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 39.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.2) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H460 (line)]] | wt | 29.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +12.0) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[RKO (line)]] | wt | 47.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.363× (z -8.9) |
| [[SHP-77 (line)]] | alt | 55.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -9.6) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SNU-1 (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 18.1 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.144× (z -10.6) |
| [[SW480 (line)]] | alt | 41.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.38× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-172 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12603), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF485]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[IMPACT]] | +0.69 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[GPATCH4]] | +0.69 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[RIOX2]] | +0.69 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[ZC3H8]] | +0.69 | +0.74 / +0.52 | both halves | 1e-05 |  |
| [[DCAF17]] | +0.69 | +0.78 / +0.51 | both halves | 1e-05 |  |
| [[GCFC2]] | +0.68 | +0.69 / +0.57 | both halves | 8e-06 |  |
| [[ZNF239]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[METTL8]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[UTP15]] | +0.66 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.65 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[SCO1]] | +0.64 | +0.68 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB2]] | -0.66 | -0.71 / -0.46 | both halves | 3e-05 |  |
| [[GRN]] | -0.63 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[PSAP]] | -0.60 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[ADIPOR1]] | -0.58 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[GNAI2]] | -0.57 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[PHF1]] | -0.57 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[NLGN2]] | -0.57 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[CTSD]] | -0.56 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[FKBP8]] | -0.56 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[PBXIP1]] | -0.56 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[CLPTM1]] | -0.56 | -0.62 / -0.37 | both halves | 9e-05 |  |
| [[SEMA6C]] | -0.56 | -0.53 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM169A]] | B | FAM169A activity raises TMA16's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 1.26× lower at baseline in the lines without FAM169A | 0.070 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.735). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-19.9, -37.0); signed map (-0.8, -39.3). **Vector** length 81.0, 19.6% of its response variance represented; |z| ≥ 3 in 713 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +7.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.3 | +4.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.1 | +4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | -0.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.9 | +3.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.5 | -4.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.3 | -3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -5.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -3.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.8 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.7 | -3.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | translation machinery associated 16 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.2 — chr4:163,494,442-163,520,539 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11184; previously C4orf43 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EY4](https://www.uniprot.org/uniprotkb/Q96EY4) (Translation machinery-associated protein 16):

> Involved in the biogenesis of the 60S ribosomal subunit in the nucleus.

**Summary**, from NCBI Gene [55319](https://www.ncbi.nlm.nih.gov/gene/55319):

> Enables preribosome binding activity and protein-macromolecule adaptor activity. Involved in ribosomal large subunit biogenesis. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25638](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25638) · Entrez [55319](https://www.ncbi.nlm.nih.gov/gene/55319) · UniProt [Q96EY4](https://www.uniprot.org/uniprotkb/Q96EY4) · Ensembl [ENSG00000198498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198498)

## Data

Gene col 12603: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12603); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12603, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12603]; `tensor/DDL_lfc|DDL_z.npy` [12603]; `embed/gene_vectors.npy` [12603]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12603 or target_col == 12603). Every well: [[TMA16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMA16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.

---
symbol: "UMPS"
type: "gene"
col: 3559
ensembl_id: "ENSG00000114491"
name: "uridine monophosphate synthetase"
location: "3q21.2"
module: 1
arm: "+"
pooled_cpm: 25.58
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# UMPS

*uridine monophosphate synthetase* — 3q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.92× (z +12.7, q 6e-34, up in 41 of 46 measured lines) ⚠ toxic. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.61× (z +9.6, q 2e-19, up in 31 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.147×, HEC-1-A 0.385×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.146×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[olaparib (drug)]] 5 µM in 1 line (SW48 0.0468×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0986×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMT61B]] (+0.76, fdr 7e-06), [[PALB2]] (+0.73, fdr 7e-06), [[NOL11]] (+0.72, fdr 7e-06); moves opposite to [[PHF1]] (-0.68, fdr 7e-06), [[CHP1]] (-0.59, fdr 1e-05), [[MXD4]] (-0.59, fdr 8e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SMARCA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3559.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +12.7 | 6e-34 | 41/46 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +9.6 | 2e-19 | 31/47 (J82, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +9.1 | 1e-17 | 31/47 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +8.9 | 1e-16 | 32/48 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +7.2 | 7e-11 | 23/47 (J82, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +6.6 | 5e-09 | 24/48 (PANC-1, LOX-IMVI, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +6.4 | 1e-08 | 23/48 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.75×** | +5.9 | 2e-07 | 24/45 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +5.7 | 8e-07 | 19/48 (J82, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +5.6 | 9e-07 | 18/47 (SW480, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.31×** | +5.2 | 1e-05 | 21/46 (HS-578T, J82, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.29×** | +5.2 | 1e-05 | 17/47 (J82, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.8 | 6e-05 | 17/47 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.56×** | +4.7 | 1e-04 | 14/46 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.24×** | +4.4 | 4e-04 | 19/48 (HT-29, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.2 | 0.001 | 12/48 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.031 | 7/47 (J82, SW480, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.044 | 6/45 (MIA PaCa-2, J82, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.11× | +2.9 | 0.094 | 4/48 (J82, HCT15, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3559.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (A549 0.147×, HEC-1-A 0.385×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 0.146×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.125×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[olaparib (drug)]] 5 µM in 1 line (SW48 0.0468×); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0986×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Gefitinib (drug)]] 5 µM |  | 0.841× | -3.5 | 0.14 | 9/48 (NCI-H460, C-33 A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.836× | -3.5 | 0.14 | 9/35 (A549, HEC-1-A, …) | rises with dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.846× | -3.4 | 0.14 | 11/47 (LS 180, BT-474, …) | all doses, flat |  |
| [[Malotilate (drug)]] 0.05 µM |  | 0.855× | -3.2 | 0.21 | 6/47 (NCI-H2347, HT-29, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 0.859× | -3.1 | 0.23 | 14/46 (A-172, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3559. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 22.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 43.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +12.3) | — |
| [[SW48 (line)]] | wt | 29.0 | 0 | 2 (1 ⚠) | — | [[olaparib (drug)]] 5 µM 0.0468× (z -8.9) |
| [[A-427 (line)]] | wt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[C-33 A (line)]] | alt | 31.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 25.3 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0986× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 45.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.385× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 19.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.04× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.355× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 35.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3559), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT61B]] | +0.76 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[PALB2]] | +0.73 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[NOL11]] | +0.72 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[EXOSC2]] | +0.72 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[SCO1]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[PPIL1]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[TRMT5]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[COA4]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[UTP15]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ZNF239]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[SF3B3]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF1]] | -0.68 | -0.69 / -0.61 | both halves | 7e-06 |  |
| [[CHP1]] | -0.59 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[MXD4]] | -0.59 | -0.64 / -0.58 | both halves | 8e-06 | same gene group |
| [[EPB41L5]] | -0.59 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[CARD19]] | -0.56 | -0.54 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMARCA2]] | B | SMARCA2 activity lowers UMPS's level | lines that do not express SMARCA2 (6) vs lines expressing it (44) | 1.31× higher at baseline in the lines without SMARCA2 | 0.086 | ⚠ within organs, on part of the lines; also absent: CEMIP2, S100A13, PYROXD2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.744). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-52.3, 0.1); signed map (1.7, -40.2). **Vector** length 92.8, 19.5% of its response variance represented; |z| ≥ 3 in 849 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitochondrial mRNA modification* (reactome, mean cos +0.54 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.9 | +12.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.8 | +5.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.5 | +5.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.6 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +5.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +4.7 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -0.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -2.6 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.3 | -3.4 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.0 | -3.5 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.9 | -2.7 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | uridine monophosphate synthetase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.2 — chr3:124,730,433-124,749,273 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OPRT, ODC |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Decarboxylases; Phosphoribosyltransferases |
| Hallmark sets | DNA_REPAIR, IL2_STAT5_SIGNALING |
| Reactome | 3 pathways, smallest: Pyrimidine biosynthesis; Nucleotide biosynthesis; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P11172](https://www.uniprot.org/uniprotkb/P11172) (Uridine 5'-monophosphate synthase):

> Bifunctional enzyme catalyzing the last two steps of de novo pyrimidine biosynthesis, orotate phosphoribosyltransferase (OPRT), which converts orotate to orotidine-5'-monophosphate (OMP), and orotidine-5'-monophosphate decarboxylase (ODC), the terminal enzymatic reaction that decarboxylates OMP to uridine monophosphate (UMP).

**Summary**, from NCBI Gene [7372](https://www.ncbi.nlm.nih.gov/gene/7372):

> This gene encodes a uridine 5'-monophosphate synthase. The encoded protein is a bifunctional enzyme that catalyzes the final two steps of the de novo pyrimidine biosynthetic pathway. The first reaction is carried out by the N-terminal enzyme orotate phosphoribosyltransferase which converts orotic acid to orotidine-5'-monophosphate. The terminal reaction is carried out by the C-terminal enzyme OMP decarboxylase which converts orotidine-5'-monophosphate to uridine monophosphate. Defects in this …

**Accessions** — [HGNC:12563](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12563) · Entrez [7372](https://www.ncbi.nlm.nih.gov/gene/7372) · UniProt [P11172](https://www.uniprot.org/uniprotkb/P11172) · Ensembl [ENSG00000114491](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114491)

## Data

Gene col 3559: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3559); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3559, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3559]; `tensor/DDL_lfc|DDL_z.npy` [3559]; `embed/gene_vectors.npy` [3559]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3559 or target_col == 3559). Every well: [[UMPS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UMPS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
